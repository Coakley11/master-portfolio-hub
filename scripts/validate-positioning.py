#!/usr/bin/env python3
"""Validate site positioning, links, and screenshots; fail if old PM/TPM positioning reappears.

Run from anywhere: python scripts/validate-positioning.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "Portfolio Website"
HEADLINE = "Daniel Cohen — Quantitative Analytics, AI & Data Portfolio"
AVAILABILITY = "Open to remote part-time, contract, project-based, and flexible analytical opportunities."
TAGLINE = "Statistics • Excel • Python • SQL • AI Evaluation • Data Analysis • Quantitative Modeling"

# Phrases that signal the retired Product Manager / Technical Manager positioning.
BANNED = [
    r"product manager", r"technical manager", r"technical product", r"ai product",
    r"product owner", r"product strategy", r"product management", r"product ownership",
    r"product direction", r"release readiness", r"acceptance criteria", r"\bTPM\b",
    r"fully remote u\.s", r"role targets", r"flagship product",
]
SCAN = ["index.html", "resume.html", "career-profile.html", "executive-summary.html", "contact.html",
        "data/projects.json", "js/main.js", "js/resume-pages.js", "js/project-detail.js"]
ALLOW_IN_FILES: dict[str, list[str]] = {}  # file -> patterns allowed there


def main() -> int:
    errors: list[str] = []
    data = json.loads((SITE / "data/projects.json").read_text(encoding="utf-8"))
    site = data["site"]

    if site["title"] != HEADLINE:
        errors.append(f"site.title != approved headline: {site['title']!r}")
    if site["tagline"] != TAGLINE:
        errors.append(f"site.tagline != approved supporting line: {site['tagline']!r}")
    if site.get("availability") != AVAILABILITY:
        errors.append("site.availability missing or changed")
    if "Quantitative Analytics, AI &amp; Data" not in (SITE / "index.html").read_text(encoding="utf-8"):
        errors.append("index.html <h1> does not carry the approved headline")

    for rel in SCAN:
        text = (SITE / rel).read_text(encoding="utf-8")
        for pat in BANNED:
            if pat in ALLOW_IN_FILES.get(rel, []):
                continue
            for m in re.finditer(pat, text, flags=re.I):
                line = text.count("\n", 0, m.start()) + 1
                errors.append(f"{rel}:{line}: banned positioning phrase /{pat}/")

    # Resume button label and link
    if not (SITE / site["resumePdf"]).exists():
        errors.append(f"resume PDF missing: {site['resumePdf']}")
    js = (SITE / "js/main.js").read_text(encoding="utf-8")
    if "Resume (PDF)" not in js:
        errors.append("main.js lacks neutral 'Resume (PDF)' label")

    # Every screenshot referenced by a project must exist
    for repo in data["repos"]:
        for rel in repo.get("screenshots", []):
            if not (SITE / rel).exists():
                errors.append(f"{repo['id']}: missing screenshot {rel}")
        hero = repo.get("heroScreenshot")
        if hero and repo.get("screenshots") and not any(s.endswith("/" + hero) for s in repo["screenshots"]):
            errors.append(f"{repo['id']}: hero {hero} not in screenshots list")
    music = next(r for r in data["repos"] if r["id"] == "ai-music-practice-coach")
    if not 4 <= len(music["screenshots"]) <= 6:
        errors.append(f"Music Coach should show 4-6 screenshots, has {len(music['screenshots'])}")
    if re.search(r"\b\d[\d,]*\+?\s+(automated\s+)?tests\b", json.dumps(music), flags=re.I):
        errors.append("Music Coach copy states a specific test count; describe the suite without a number")

    # Live/GitHub links preserved
    for repo in data["repos"]:
        if repo.get("github") and not repo["github"].startswith("https://github.com/Coakley11/"):
            errors.append(f"{repo['id']}: unexpected github link")

    print("title:", site["title"])
    print("music screenshots:", len(music["screenshots"]), "hero:", music["heroScreenshot"])
    if errors:
        print(f"FAILED ({len(errors)}):")
        for e in errors:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
