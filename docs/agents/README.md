# Agent documentation router

This repository is the public, redirect-only compatibility gateway for the private `mykcs/personal-homepage` source.

## Read order

1. [`AGENTS.md`](../../AGENTS.md) — repository boundary and Agent rules.
2. [`../wish/LATEST.md`](../wish/LATEST.md) — current gateway intent; add `DESIGN.md` for route/product-direction changes.
3. [`../dev/LATEST.md`](../dev/LATEST.md) — current development direction; add `DESIGN.md` for hosting/provider changes.
4. Tracked redirect HTML plus live GitHub Pages state — executable/live truth.

## Truth boundaries

- `mykcs/personal-homepage` owns the full private homepage source.
- This repository owns only its public-safe redirect behavior and compatibility URL.
- Wish explains desired direction; Dev explains development/hosting rationale; neither overrides tracked redirects or live Pages state.
- Read Wish/Dev archives only for historical rationale.

## Validation

For redirect changes, inspect every tracked redirect file and verify canonical targets and route preservation against the current gateway contract. Refresh live GitHub Pages state before making provider-side claims.

Shared lifecycle owners: [`WISH_PROTOCOL.md`](https://github.com/mykcs/.agents/blob/main/docs/agents/WISH_PROTOCOL.md) and [`DEV_PROTOCOL.md`](https://github.com/mykcs/.agents/blob/main/docs/agents/DEV_PROTOCOL.md).
