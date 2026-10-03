# Jev Provider Adapter V1

This adapter wraps the official TypeSafe Python SDK and keeps JoyLab's
Decision Router provider-isolated.

## Live requirements

```bash
python -m pip install typesafe-sdk
export TYPESAFE_API_KEY="..."
```

Official SDK defaults used by this adapter:
- base URL: `https://api.typesafe.ai`
- model: `jev-latest`
- API key environment variable: `TYPESAFE_API_KEY`

## Safety boundary

The provider only returns:

```text
choice + confidence
```

It does not:
- execute a route;
- modify production state;
- approve GOLD;
- bypass deterministic gates;
- authorize destructive or Human-gated actions.

The caller remains responsible for Shadow Mode isolation and JoyLab safety
overrides.
