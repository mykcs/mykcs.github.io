# Gateway development and CI reasoning

## Small public surface

GitHub Pages already serves this public hostname from the root of `main`. The repository holds only static redirect files and governance, so it needs no framework build, container, Worker or second web host. The complete Astro application and Scholar runtime belong to private `mykcs/personal-homepage`; Cloudflare Pages serves that site's canonical Production. This separation keeps the old URL working while the serving provider can change.

## Validation and release

For a redirect edit, inspect every root route file, validate HTML and the direct target, then check known language/CV paths, unknown-path fallback, query and hash behavior. A public browser check after GitHub Pages publishes `main` establishes that the old URL reaches the intended host; source review alone does not. Test the gateway and the private site's canonical/SEO identity together for a serving-host migration. Root [AGENTS.md](../../AGENTS.md), redirect files and live Pages branch settings are the current owners.

There is currently no automated CI workflow in this repository. A proposed check becomes a gate only after its workflow actually runs and its required status is configured and verified; a plan document does not change that state. Documentation edits need link and boundary review, not an Astro build or a Cloudflare deployment. GitHub Pages may still publish a new branch snapshot when `main` changes; verify its actual build status rather than attributing that work to GitHub Actions jobs.

If publication or routing fails, inspect Pages build status and public redirect behavior separately. Restore the last known target in the root files and republish `main` if a target change must be rolled back. Cloudflare outages belong to the canonical site's provider investigation, while this gateway should continue to point to the owner-approved serving host.
