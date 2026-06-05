# Master Portfolio Screenshot Guide

**Updated for Portfolio Demo Mode** (2026-06-05)

---

## Quick start

1. Read **[HOW_TO_CAPTURE.md](HOW_TO_CAPTURE.md)** — mechanical 10-step workflow
2. Capture **P0** shots from **[screenshot-checklist.md](screenshot-checklist.md)**
3. Save into the folder named in each app's **CAPTURE_TABLE.md**

---

## Two sidebar toggles (every Streamlit app)

| Toggle | Required? | What it does |
|--------|-----------|--------------|
| **Portfolio Demo Mode** | **Yes** | Auto-loads curated examples, populates forms, expands key outputs |
| **Portfolio Screenshot Mode** | Recommended | Hides clutter, shows executive summaries and hero banners |

Use **both** for hero page captures.

---

## Folder structure

```
Screenshots/
├── HOW_TO_CAPTURE.md              ← start here
├── screenshot-manifest.json       ← website reads this
├── screenshot-checklist.md        ← master checkboxes
├── SCREENSHOT_CAPTURE_REGISTRY.md ← all capture tables
├── Investment/                    ← investment-*.png
├── Baseball/                      ← baseball-*.png
├── Applied-Math/                  ← applied-math-*.png
├── NBA/                           ← nba-*.png
├── Music/                         ← music-*.png
├── SQL-Excel/                     ← sql-excel-*.png
└── Portfolio-Website/             ← portfolio-website-*.png
```

---

## P0 hero pages (11 captures)

| App | Page | Filename |
|-----|------|----------|
| Investment | Overview | `investment-overview-demo.png` |
| Baseball | Draft Assistant | `baseball-draft-assistant-demo.png` |
| Baseball | ML Predictions | `baseball-ml-projections-demo.png` |
| Baseball | Career Totals | `baseball-career-totals-demo.png` |
| Applied Math | Analyze a Bet | `applied-math-betting-ev-demo.png` |
| Applied Math | Train an AI | `applied-math-ai-training-demo.png` |
| Applied Math | Model a Disease | `applied-math-disease-spread-demo.png` |
| NBA | Home Dashboard | `nba-home-dashboard-demo.png` |
| NBA | Legacy Tracker | `nba-legacy-tracker-demo.png` |
| Music | Practice | `music-practice-demo.png` |
| SQL Excel | AI Evaluator Dashboard | `sql-excel-ai-evaluator-dashboard.png` |

---

## Website integration

The portfolio website (`Portfolio Website/`) expects images at:

`../Screenshots/<Folder>/<filename>.png`

When a PNG exists, project cards show it automatically. Missing files show a placeholder with the expected filename.

**Verify:** Open `Portfolio Website/index.html` in a browser after adding P0 shots.

---

## Per-app detail

Each folder contains:

- **README.md** — list of expected filenames
- **CAPTURE_TABLE.md** — full capture table with toggles and priorities

Per-repo Streamlit guides (optional extra detail) remain in each GitHub repo under `docs/PORTFOLIO_SCREENSHOT_GUIDE.md`.
