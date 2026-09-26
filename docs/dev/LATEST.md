# Current development direction

This public repository maintains one small compatibility gateway: legacy `mykcs.github.io` links lead directly to the current canonical personal homepage. Keep its source public-safe and its redirect behavior easy to inspect.

GitHub owns source and PR history. GitHub Pages publishes the root static files from `main`. There is no GitHub Actions workflow in this repository today; no CI badge should be treated as redirect acceptance without an executed check. Cloudflare Pages serves the full canonical homepage from the separate private source repository. Vercel, CircleCI and Cloudflare Workers have no gateway build, runtime or scheduling role here.

The root redirect files and live GitHub Pages settings own current behavior. The [Wish](../wish/LATEST.md) owns the reason this stable entry exists; this folder explains its development and CI choices.
