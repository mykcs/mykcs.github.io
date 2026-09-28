#!/usr/bin/env python3
"""Validate the public gateway's redirect contract without external services."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "https://wangrui92.pages.dev"
EXPECTED_ROUTES = {
    "index.html": "/",
    "en/index.html": "/en/",
    "zh/index.html": "/zh/",
    "en/cv/index.html": "/en/cv/",
    "zh/cv/index.html": "/zh/cv/",
    "404.html": "/",
}


def tracked_html_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.html"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return {path.decode() for path in result.stdout.split(b"\0") if path}


def validate() -> list[str]:
    errors: list[str] = []
    tracked = tracked_html_files()
    expected = set(EXPECTED_ROUTES)
    for path in sorted(expected - tracked):
        errors.append(f"missing required redirect file: {path}")
    for path in sorted(tracked - expected):
        errors.append(f"unreviewed HTML route added to gateway: {path}")

    for relative, route in EXPECTED_ROUTES.items():
        file_path = ROOT / relative
        if not file_path.is_file():
            continue
        html = file_path.read_text(encoding="utf-8")
        meta_target = f"url={CANONICAL}{route}"
        canonical_link = f'<link rel="canonical" href="{CANONICAL}{route}">'
        if "mykcs.github.io" in html:
            errors.append(f"{relative}: redirect must go directly to the canonical host")
        if meta_target not in html:
            errors.append(f"{relative}: meta refresh must target {CANONICAL}{route}")
        if canonical_link not in html:
            errors.append(f"{relative}: canonical link must target {CANONICAL}{route}")
        if "location.replace(target.href)" not in html:
            errors.append(f"{relative}: JavaScript redirect must use location.replace")
        if "target.search = location.search" not in html or "target.hash = location.hash" not in html:
            errors.append(f"{relative}: redirect must preserve query and hash")
        if relative == "index.html":
            if "target.pathname = location.pathname" not in html:
                errors.append("index.html: root gateway must preserve known paths")
        else:
            script_target = f"new URL('{CANONICAL}{route}')"
            if script_target not in html:
                errors.append(f"{relative}: script target must be {CANONICAL}{route}")
        if "<meta name=\"robots\" content=\"noindex,follow\">" not in html:
            errors.append(f"{relative}: compatibility gateway must stay non-indexable")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(EXPECTED_ROUTES)} gateway routes match the canonical redirect contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
