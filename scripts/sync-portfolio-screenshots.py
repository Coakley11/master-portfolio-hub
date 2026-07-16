#!/usr/bin/env python3
"""Publish numbered Screenshots/ captures into Portfolio Website/assets/screenshots/."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
STAGING = HUB / "Screenshots"
DEPLOY = HUB / "Portfolio Website" / "assets" / "screenshots"
PROJECTS = HUB / "Portfolio Website" / "data" / "projects.json"

APP_FOLDERS = [
    "Applied-Math",
    "Baseball",
    "Command-Center",
    "Future-Lens",
    "Investment",
    "Music",
    "NBA",
]


def humanize(filename: str) -> str:
    stem = Path(filename).stem
    stem = stem.lstrip("0123456789-")
    return stem.replace("-", " ").replace("_", " ").title()


def copy_pngs() -> list[str]:
    published: list[str] = []
    DEPLOY.mkdir(parents=True, exist_ok=True)
    for folder in APP_FOLDERS:
        src_dir = STAGING / folder
        if not src_dir.exists():
            continue
        dest_dir = DEPLOY / folder
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(src_dir.glob("*.png")):
            dest = dest_dir / src.name
            shutil.copy2(src, dest)
            published.append(f"{folder}/{src.name}")
            print(f"OK {folder}/{src.name}")
    # Keep root manifest copy for site fetch
    root_manifest = STAGING / "screenshot-manifest.json"
    if root_manifest.exists():
        shutil.copy2(root_manifest, DEPLOY / "screenshot-manifest.json")
    return published


def build_manifest(published: list[str]) -> dict:
    by_folder: dict[str, list[str]] = {}
    for rel in published:
        folder, name = rel.split("/", 1)
        by_folder.setdefault(folder, []).append(name)

    folder_to_app = {
        "Investment": ("investment-portfolio-analyzer", "Investment Explorer"),
        "Baseball": ("baseball-stat-app", "Baseball Analytics"),
        "Applied-Math": ("applied-mathematical-intelligence", "Applied Mathematical Intelligence"),
        "NBA": ("nba-playoff-companion-ai", "Basketball Playoff Companion"),
        "Music": ("ai-music-practice-coach", "AI Music Practice Coach"),
        "Command-Center": ("daniel-ai-command-center", "AI Command Center"),
        "Future-Lens": ("future-lens-ai-transition-simulator", "Future Lens"),
    }

    apps = []
    for folder, names in by_folder.items():
        app_id, app_name = folder_to_app.get(folder, (folder.lower(), folder))
        captures = []
        for i, name in enumerate(names):
            captures.append(
                {
                    "filename": name,
                    "page": humanize(name),
                    "demonstrates": humanize(name),
                    "priority": "P0" if i == 0 else "P1",
                    "hero": i == 0,
                    "deployPath": f"assets/screenshots/{folder}/{name}",
                    "status": "published",
                }
            )
        apps.append(
            {
                "id": app_id,
                "name": app_name,
                "folder": folder,
                "captures": captures,
            }
        )

    return {
        "version": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "description": "Canonical numbered screenshot set captured 2026-07-15. Source: Screenshots/; deploy: Portfolio Website/assets/screenshots/.",
        "basePathFromWebsite": "../Screenshots",
        "recommendedSize": "1920×1080 desktop",
        "apps": apps,
        "integration": {
            "lastRun": datetime.now(timezone.utc).isoformat(),
            "publishedCount": len(published),
            "source": "numbered-canonical-set",
        },
    }


HERO_OVERRIDES = {
    "Investment": "01-portfolio-health.png",
    "Baseball": "01-draft-assistant-recommendations.png",
    "Applied-Math": "01-home-dashboard.png",
    "NBA": "01-home-dashboard.png",
    "Music": "02-practice-control-center.png",
    "Command-Center": "homepage-continue.png",
    "Future-Lens": "01-domain-wizard.png",
}


def ordered_files(folder: str) -> list[Path]:
    files = sorted((STAGING / folder).glob("*.png"), key=lambda p: p.name.lower())
    preferred = HERO_OVERRIDES.get(folder)
    if preferred:
        files = sorted(files, key=lambda p: (0 if p.name == preferred else 1, p.name.lower()))
    return files


def update_projects_screenshot_fields() -> None:
    data = json.loads(PROJECTS.read_text(encoding="utf-8"))
    folder_map = {
        "investment-portfolio-analyzer": "Investment",
        "baseball-stat-app": "Baseball",
        "applied-mathematical-intelligence": "Applied-Math",
        "nba-playoff-companion-ai": "NBA",
        "ai-music-practice-coach": "Music",
        "daniel-ai-command-center": "Command-Center",
        "future-lens-ai-transition-simulator": "Future-Lens",
    }
    for repo in data.get("repos", []):
        folder = folder_map.get(repo["id"])
        if not folder:
            continue
        files = ordered_files(folder)
        if not files:
            continue
        repo["screenshotFolder"] = folder
        repo["heroScreenshot"] = files[0].name
        repo["screenshots"] = [f"assets/screenshots/{folder}/{f.name}" for f in files]
        repo["screenshotChecklist"] = [f"{f.name} — {humanize(f.name)}" for f in files]
    PROJECTS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Updated screenshot paths in {PROJECTS}")


def main() -> int:
    published = copy_pngs()
    manifest = build_manifest(published)
    for path in (STAGING / "screenshot-manifest.json", DEPLOY / "screenshot-manifest.json"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {path}")
    update_projects_screenshot_fields()
    print(f"Published {len(published)} screenshots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
