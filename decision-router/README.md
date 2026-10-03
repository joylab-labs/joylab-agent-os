# decision-router

Repository-facing contract and policy files for JoyLab Decision Router V1.

Runtime implementation lives in:

`src/joylab_agent_os/decision_router/`

V1 mode: **SHADOW ONLY**.

Rules:
- deterministic checks run before model judgment;
- model output never overrides hard safety/data-integrity rules;
- shadow decisions never change the production route;
- False Autonomy must remain exactly zero;
- promotion is per decision type after GOLD evidence.
