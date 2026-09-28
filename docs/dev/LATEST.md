# Current development direction

**CI mode: `STANDARD_CI` (required PR gate active).**

This public repository maintains one small compatibility gateway: legacy `mykcs.github.io` links lead directly to the current canonical personal homepage. Keep its source public-safe and its redirect behavior easy to inspect.

GitHub owns source, pull requests and the small redirect-integrity gate. The strict `main` ruleset requires GitHub Actions check `Repository validation` (integration ID `15368`). Its workflow checks out the exact PR head and runs only `python3 scripts/validate_redirects.py`; it does not build the Astro site or publish the canonical homepage. GitHub Pages publishes the root static files from `main`. Cloudflare Pages serves the full canonical homepage from the separate private source repository. Vercel, CircleCI and Cloudflare Workers have no gateway build, runtime or scheduling role here.

The root redirect files and live GitHub Pages settings own current behavior. The [Wish](../wish/LATEST.md) owns the reason this stable entry exists; this folder explains its development and CI choices.
