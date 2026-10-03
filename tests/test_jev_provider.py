from __future__ import annotations

from dataclasses import dataclass

from joylab_agent_os.decision_router.models import DecisionRequest
from joylab_agent_os.decision_router.providers.jev import JevProvider, JevProviderConfig


@dataclass
class FakeAnswer:
    choice: str
    confidence: float


class FakeResponse:
    def __init__(self, choice: str, confidence: float) -> None:
        self.answers = {"route": FakeAnswer(choice, confidence)}


class FakeClient:
    def __init__(self) -> None:
        self.calls = []

    def system_one(self, **kwargs):
        self.calls.append(kwargs)
        return FakeResponse("major", 0.93)


def test_jev_provider_maps_bounded_choice_without_changing_authority():
    client = FakeClient()
    provider = JevProvider(client=client, config=JevProviderConfig(model="jev-latest"))
    result = provider(
        DecisionRequest(
            decision_id="ld-001",
            decision_type="defect_type",
            allowed_outputs=("blocker", "critical", "major", "minor"),
            state={"summary": "interview log does not save"},
            risk=frozenset(),
        )
    )

    assert result.choice == "major"
    assert result.confidence == 0.93
    assert result.provider == "jev"
    assert client.calls[0]["model"] == "jev-latest"
    assert client.calls[0]["state"]["summary"] == "interview log does not save"


def test_jev_provider_rejects_unbounded_request():
    provider = JevProvider(client=FakeClient())
    request = DecisionRequest(
        decision_id="empty",
        decision_type="unknown",
        allowed_outputs=(),
        state={},
        risk=frozenset(),
    )

    try:
        provider(request)
    except ValueError as exc:
        assert "non-empty bounded output" in str(exc)
    else:
        raise AssertionError("expected ValueError")
