from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from ..models import DecisionRequest, ModelDecision


@dataclass(frozen=True)
class JevProviderConfig:
    model: str = "jev-latest"


class JevProvider:
    """Official TypeSafe Jev provider adapter.

    The provider is intentionally thin and delegates HTTP/retry/auth behavior
    to the official `typesafe-sdk` package. It converts JoyLab bounded
    DecisionRequest objects into a Jev Choice question and returns only the
    selected bounded label plus confidence.

    No secret is accepted as a function argument by default. The official SDK
    reads TYPESAFE_API_KEY from the environment.
    """

    def __init__(
        self,
        *,
        client: Any | None = None,
        config: JevProviderConfig | None = None,
    ) -> None:
        self.config = config or JevProviderConfig()
        if client is None:
            try:
                from typesafe_sdk import TypeSafeClient
            except ImportError as exc:
                raise RuntimeError(
                    "Live Jev requires the official typesafe-sdk package. "
                    "Install it and set TYPESAFE_API_KEY."
                ) from exc
            client = TypeSafeClient()
        self._client = client

    def __call__(self, request: DecisionRequest) -> ModelDecision:
        if not request.allowed_outputs:
            raise ValueError("JevProvider requires a non-empty bounded output set")

        criteria = {
            label: self._criterion_for(label)
            for label in request.allowed_outputs
        }

        try:
            from typesafe_sdk import Choice
        except ImportError:
            # Unit tests can inject a fake client and fake Choice-compatible
            # shape without installing the optional live SDK.
            Choice = _FallbackChoice  # type: ignore[assignment]

        response = self._client.system_one(
            state=dict(request.state),
            questions={
                "route": Choice(
                    instructions=(
                        "Choose exactly one allowed label for this bounded "
                        "JoyLab decision. Do not invent a new label."
                    ),
                    criteria=criteria,
                )
            },
            model=self.config.model,
        )

        answer = response.answers["route"]
        return ModelDecision(
            choice=str(answer.choice),
            confidence=float(answer.confidence),
            provider="jev",
        )

    @staticmethod
    def _criterion_for(label: str) -> str:
        return f"Select when the state best matches the '{label}' category."


class _FallbackChoice:
    def __init__(self, *, instructions: str, criteria: Mapping[str, str]) -> None:
        self.instructions = instructions
        self.criteria = dict(criteria)
