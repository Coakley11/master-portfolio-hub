#!/usr/bin/env python3
"""Copy and rename legacy captures into Portfolio Website/assets/screenshots/."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

HUB = Path(__file__).resolve().parent.parent
STAGING = HUB / "Screenshots"
DEPLOY = HUB / "Portfolio Website" / "assets" / "screenshots"
MANIFEST_PATHS = [
    HUB / "Screenshots" / "screenshot-manifest.json",
    DEPLOY / "screenshot-manifest.json",
]

MAPPING: list[dict] = [
    {
        "source": "Investment/investment-portfolio-summary-mobile.png.jpg",
        "target": "Investment/investment-overview-demo.png",
        "note": "Mobile portfolio summary used as Overview hero until desktop capture",
    },
    {
        "source": "Investment/investment-portfolio-summary-mobile.png.jpg",
        "target": "Investment/investment-overview-demo-mobile.png",
        "note": "Same capture retained as mobile variant",
    },
    {
        "source": "Investment/investment-portfolio-health.png.jpg",
        "target": "Investment/investment-portfolio-health.png",
        "note": "Exact manifest match",
    },
    {
        "source": "Investment/investment-allocation-optimizer.png.jpg",
        "target": "Investment/investment-optimizer.png",
        "note": "Allocation optimizer → optimizer",
    },
    {
        "source": "Baseball/baseball-draft-recommendation-engine.png.jpg",
        "target": "Baseball/baseball-draft-assistant-demo.png",
        "note": "Draft recommendation engine → draft assistant demo",
    },
    {
        "source": "Baseball/baseball-ml-projections.png.jpg",
        "target": "Baseball/baseball-ml-projections-demo.png",
        "note": "ML projections",
    },
    {
        "source": "Baseball/baseball-roster-heatmap.png.jpg",
        "target": "Baseball/baseball-career-totals-demo.png",
        "note": "Roster heatmap used for career totals hero",
    },
    {
        "source": "Baseball/baseball-player-insight.png.jpg",
        "target": "Baseball/baseball-player-comparison.png",
        "note": "Player insight → comparison tool",
    },
    {
        "source": "Baseball/baseball-statistical-testing.png.jpg",
        "target": "Baseball/baseball-trend-analysis.png",
        "note": "Statistical testing → trend analysis gallery",
    },
    {
        "source": "Applied-Math/applied-math-betting-ev.png.jpg",
        "target": "Applied-Math/applied-math-betting-ev-demo.png",
        "note": "Betting EV demo",
    },
    {
        "source": "Applied-Math/applied-math-ai-overfitting.png.jpg",
        "target": "Applied-Math/applied-math-ai-training-demo.png",
        "note": "AI overfitting → training demo",
    },
    {
        "source": "Applied-Math/applied-math-disease-simulation.png.jpg",
        "target": "Applied-Math/applied-math-disease-spread-demo.png",
        "note": "Disease simulation → spread demo",
    },
    {
        "source": "NBA/nba-home-dashboard.png.jpg",
        "target": "NBA/nba-home-dashboard-demo.png",
        "note": "Home dashboard demo",
    },
    {
        "source": "NBA/nba-legacy-tracker.png.jpg",
        "target": "NBA/nba-legacy-tracker-demo.png",
        "note": "Legacy tracker demo",
    },
    {
        "source": "Music/music-practice-coach-main.png.jpg",
        "target": "Music/music-practice-demo.png",
        "note": "Practice coach main → practice demo",
    },
    {
        "source": "Music/music-backing-traci-studio.png.jpg",
        "target": "Music/music-backing-tracks.png",
        "note": "Backing track studio (typo in legacy filename)",
    },
    {
        "source": "Music/music-custom-progression-builder.png.jpg",
        "target": "Music/music-adaptive-sheet.png",
        "note": "Progression builder → adaptive sheet slot",
    },
]


def convert_to_png(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as img:
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        img.save(dest, format="PNG", optimize=True)


def scan_staging() -> dict[str, list[str]]:
    images: dict[str, list[str]] = {"legacy_png_jpg": [], "png": [], "jpg": [], "other": []}
    if not STAGING.exists():
        return images
    for p in STAGING.rglob("*"):
        if not p.is_file():
            continue
        name = p.name.lower()
        rel = str(p.relative_to(STAGING)).replace("\\", "/")
        if name.endswith(".png.jpg"):
            images["legacy_png_jpg"].append(rel)
        elif name.endswith(".png"):
            images["png"].append(rel)
        elif name.endswith((".jpg", ".jpeg")):
            images["jpg"].append(rel)
        elif name not in (".gitkeep",) and p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            images["other"].append(rel)
    return images


def load_expected_refs() -> set[str]:
    data = json.loads((HUB / "Portfolio Website" / "data" / "projects.json").read_text(encoding="utf-8"))
    refs: set[str] = set()
    for repo in data.get("repos", []):
        for s in repo.get("screenshots") or []:
            refs.add(s.replace("assets/screenshots/", ""))
        folder = repo.get("screenshotFolder")
        hero = repo.get("heroScreenshot")
        if folder and hero:
            refs.add(f"{folder}/{hero}")
    for extra in [
        "SQL-Excel/sql-excel-ai-evaluator-dashboard.png",
        "SQL-Excel/sql-excel-investment-workbook-dashboard.png",
        "SQL-Excel/sql-excel-quant-claims.png",
        "SQL-Excel/sql-excel-real-world-credit-risk.png",
    ]:
        refs.add(extra)
    return refs


def update_manifest(published: dict[str, str]) -> None:
    for manifest_path in MANIFEST_PATHS:
        if not manifest_path.exists():
            continue
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["version"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        manifest["integration"] = {
            "lastRun": datetime.now(timezone.utc).isoformat(),
            "publishedCount": len(published),
            "renamePlan": MAPPING,
        }
        for app in manifest.get("apps", []):
            folder = app.get("folder", "")
            for cap in app.get("captures", []):
                fn = cap.get("filename", "")
                key = f"{folder}/{fn}"
                cap["deployPath"] = f"assets/screenshots/{key}"
                if key in published:
                    cap["status"] = "published"
                    cap["legacySource"] = published[key]
                else:
                    cap["status"] = "missing"
                    cap.pop("legacySource", None)
                mfn = cap.get("mobileFilename")
                if mfn:
                    mkey = f"{folder}/{mfn}"
                    cap["mobileDeployPath"] = f"assets/screenshots/{mkey}"
                    if mkey in published:
                        cap["mobileStatus"] = "published"
                    elif (DEPLOY / mkey.replace("/", "\\")).exists():
                        cap["mobileStatus"] = "published"
                    else:
                        cap["mobileStatus"] = "missing"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    scan = scan_staging()
    expected = load_expected_refs()
    published: dict[str, str] = {}
    copied = 0

    print("=== Screenshot Integration ===")
    print(f"Legacy .png.jpg in staging: {len(scan['legacy_png_jpg'])}")
    print(f"Native .png in staging: {len(scan['png'])}")
    print(f"Expected deploy references: {len(expected)}")
    print()

    for entry in MAPPING:
        src = STAGING / entry["source"].replace("/", "\\")
        dest_rel = entry["target"]
        dest = DEPLOY / dest_rel.replace("/", "\\")
        if not src.exists():
            print(f"SKIP missing source: {entry['source']}")
            continue
        convert_to_png(src, dest)
        published[dest_rel] = entry["source"]
        copied += 1
        print(f"OK {entry['source']} -> {dest_rel}")

    # Also copy any native .png already in staging with matching names
    for rel in scan["png"]:
        dest = DEPLOY / rel.replace("/", "\\")
        src = STAGING / rel.replace("/", "\\")
        if not dest.exists() or src.stat().st_mtime > dest.stat().st_mtime:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            published[rel] = rel
            copied += 1
            print(f"OK native copy: {rel}")

    update_manifest(published)

    present = {r for r in expected if (DEPLOY / r.replace("/", "\\")).exists()}
    missing = sorted(expected - present)
    legacy_unmapped = sorted(set(scan["legacy_png_jpg"]) - {e["source"] for e in MAPPING})

    report_dir = HUB / "Final Assembly"
    report_dir.mkdir(exist_ok=True)
    lines = [
        "# Screenshot Coverage Report",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Legacy `.png.jpg` in staging | {len(scan['legacy_png_jpg'])} |",
        f"| Native `.png` in staging | {len(scan['png'])} |",
        f"| Files copied/converted this run | {copied} |",
        f"| Expected site references | {len(expected)} |",
        f"| **Published on site** | **{len(present)}** |",
        f"| Still missing | {len(missing)} |",
        "",
        "## Rename plan (executed)",
        "",
        "| Legacy source | Deploy target | Note |",
        "|---------------|---------------|------|",
    ]
    for entry in MAPPING:
        lines.append(f"| `{entry['source']}` | `{entry['target']}` | {entry['note']} |")

    lines.extend([
        "",
        "## Published files",
        "",
    ])
    for p in sorted(present):
        src = published.get(p, "native")
        lines.append(f"- `{p}` ← `{src}`")

    lines.extend(["", "## Missing captures", ""])
    if missing:
        for m in missing:
            lines.append(f"- `{m}`")
    else:
        lines.append("- None — full coverage.")

    if legacy_unmapped:
        lines.extend(["", "## Unmapped legacy files", ""])
        for u in legacy_unmapped:
            lines.append(f"- `{u}`")

    lines.extend([
        "",
        "## P0 hero status",
        "",
    ])
    p0 = [
        "Investment/investment-overview-demo.png",
        "Baseball/baseball-draft-assistant-demo.png",
        "Baseball/baseball-ml-projections-demo.png",
        "Baseball/baseball-career-totals-demo.png",
        "Applied-Math/applied-math-betting-ev-demo.png",
        "Applied-Math/applied-math-ai-training-demo.png",
        "Applied-Math/applied-math-disease-spread-demo.png",
        "NBA/nba-home-dashboard-demo.png",
        "NBA/nba-legacy-tracker-demo.png",
        "Music/music-practice-demo.png",
    ]
    for p in p0:
        ok = "✅" if p in present else "❌"
        lines.append(f"- {ok} `{p}`")

    report_path = report_dir / "screenshot-coverage-report.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print()
    print(f"Published: {len(present)}/{len(expected)}")
    print(f"Report: {report_path}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
