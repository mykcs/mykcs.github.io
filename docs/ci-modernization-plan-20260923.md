# CI modernization plan — 2026-09-23

Status: **plan accepted for implementation; implementation pending**

Repository: `mykcs/mykcs.github.io`  
Integration branch: `main`

## Objective

Align this public homepage repository's CI with its current role as a stable redirect/gateway rather than rebuilding a full website validation stack.

## Current state verified before this PR

- Main deploys the `github-pages-redirect/` shell to GitHub Pages.
- Cross-site consistency and dependency security workflows are manual by design.
- There is currently no branch ruleset or PR correctness gate.

## Implementation checklist

- [x] Open this plan-only PR before changing CI/provider behavior.
- [ ] 1. Define a tiny repository-owned redirect integrity check for the canonical target, redirect shell, and accidental old-site resurrection hazards.
- [ ] 2. Add a pinned GitHub Actions PR workflow that runs only deterministic redirect/gateway validation.
- [ ] 3. Keep multi-site consistency and dependency-security audits manual unless a demonstrated failure requires promotion.
- [ ] 4. Create a `main` ruleset requiring PRs plus the app-bound redirect `Repository validation`, deletion protection, and non-fast-forward protection.
- [ ] 5. Keep GitHub Pages deploy on `main`; do not add a second hosting provider.
- [ ] 6. Update this plan with exact redirect contract and merge-gate evidence.

## Acceptance criteria

- [ ] PRs cannot silently break the intended redirect/gateway role.
- [ ] Pages deployment remains main-only.
- [ ] No heavy Astro/site CI is reintroduced for a redirect-only repository.
- [ ] Cross-repository audits remain on-demand.

## Rollout discipline

- Implement this plan in **this same PR**, one phase at a time, and check items only after fresh evidence exists.
- Refresh the integration branch immediately before ruleset changes and again before merge.
- Bind required checks to the exact provider/app when GitHub supports it; do not trust a same-name status from an unrelated app.
- Keep deterministic correctness in repository-owned commands. Workflow/provider configuration should execute that authority rather than reimplement it.
- A local PASS is not hosted-CI proof. Exercise a clean hosted checkout before declaring the migration complete.
- Do not weaken existing scientific, product, deployment, privacy, or operational authority to make CI green.

## Non-goals

- No unrelated product/content/scientific changes.
- No provider migration merely for uniformity.
- No destructive cleanup or visibility change.
- No temporary provider/build state should become long-lived documentation except the durable architecture and acceptance evidence.
