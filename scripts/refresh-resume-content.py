#!/usr/bin/env python3
"""Refresh resume section in projects.json for PDF + website resume pages.

Preserves broader role positioning from projects.json; syncs markdown copies only
unless --force-resume-overwrite is passed (not implemented — edit projects.json directly).
"""

from __future__ import annotations

import json
from pathlib import Path

PROJECTS = Path(__file__).resolve().parent.parent / "Portfolio Website" / "data" / "projects.json"
DOCS_COPY = (
    Path(__file__).resolve().parent.parent
    / "Portfolio Website"
    / "assets"
    / "docs"
    / "resume-project-descriptions.md"
)
RESUME_MD = Path(__file__).resolve().parent.parent / "Resume" / "resume-project-descriptions.md"


def main() -> int:
    data = json.loads(PROJECTS.read_text(encoding="utf-8"))
    site = data["site"]
    linkedin = site.get("linkedin") or ""

    # Keep bundled docs copy in sync with Resume markdown if present
    if RESUME_MD.exists():
        DOCS_COPY.write_text(RESUME_MD.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Synced {DOCS_COPY}")

    data["site"]["linkedin"] = linkedin or site.get("linkedin")
    PROJECTS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    print(f"Synced resume markdown; resume fields in {PROJECTS} unchanged (edit JSON for copy updates).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
