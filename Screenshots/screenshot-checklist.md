# Screenshot Checklist

**Status:** 0 / 40 screenshots on disk (as of 2026-06-05)

**Capture system:** Portfolio Demo Mode + Portfolio Screenshot Mode → save with exact filename → place in folder → website auto-updates.

**Full instructions:** [HOW_TO_CAPTURE.md](HOW_TO_CAPTURE.md)  
**All tables:** [SCREENSHOT_CAPTURE_REGISTRY.md](SCREENSHOT_CAPTURE_REGISTRY.md)  
**Website manifest:** [screenshot-manifest.json](screenshot-manifest.json)

---

## Before every Streamlit capture

- [ ] Enable **Portfolio Demo Mode** (sidebar)
- [ ] Enable **Portfolio Screenshot Mode** (sidebar)
- [ ] Open the hero page listed below
- [ ] Wait for data/charts to load
- [ ] Save PNG with **exact filename** into the listed folder

**Recommended size:** 1920×1080 desktop · optional `-mobile` variant at 390×844

---

## P0 — Hero captures (11) — do first

### Investment → `Screenshots/Investment/`

- [ ] `investment-overview-demo.png` — Overview: allocation, Sharpe, growth, summary (Demo auto-opens)
- [ ] `investment-portfolio-analytics-demo.png` — Portfolio Analytics: risk & correlation

### Baseball → `Screenshots/Baseball/`

- [ ] `baseball-draft-assistant-demo.png` — Draft Assistant: board + elite recommendation
- [ ] `baseball-ml-projections-demo.png` — ML Predictions: stars + feature importance chart
- [ ] `baseball-career-totals-demo.png` — Career Totals: HR leaders + bar chart

### Applied Math → `Screenshots/Applied-Math/`

- [ ] `applied-math-betting-ev-demo.png` — Analyze a Bet: EV + decision tree
- [ ] `applied-math-ai-training-demo.png` — Train an AI: overfit train/val chart
- [ ] `applied-math-disease-spread-demo.png` — Model a Disease: SIR graph

### NBA → `Screenshots/NBA/`

- [ ] `nba-home-dashboard-demo.png` — Home Dashboard: Finals hero + win probability
- [ ] `nba-legacy-tracker-demo.png` — Legacy Tracker: Brunson comparison chart

### Music → `Screenshots/Music/`

- [ ] `music-practice-demo.png` — Practice: Across the Universe full song card

---

## P1 — Strong support (17)

### Investment

- [ ] `investment-portfolio-health.png`
- [ ] `investment-monte-carlo.png`
- [ ] `investment-efficient-frontier.png`

### Baseball

- [ ] `baseball-player-comparison.png`
- [ ] `baseball-trend-analysis.png`

### Applied Math

- [ ] `applied-math-home-actions.png`
- [ ] `applied-math-sports-prediction.png`

### NBA

- [ ] `nba-playoff-bracket.png`
- [ ] `nba-live-game-center.png`

### Music

- [ ] `music-song-catalog.png`
- [ ] `music-backing-tracks.png`

### SQL & Excel → `Screenshots/SQL-Excel/`

- [ ] `sql-excel-ai-evaluator-dashboard.png`
- [ ] `sql-excel-ai-evaluator-sql.png`
- [ ] `sql-excel-investment-workbook-dashboard.png`
- [ ] `sql-excel-investment-pivot-practice.png`

### Portfolio Website → `Screenshots/Portfolio-Website/`

- [ ] `portfolio-website-home.png`

---

## P2 — Depth (12)

### Investment

- [ ] `investment-correlation-heatmap.png`
- [ ] `investment-optimizer.png`

### Baseball

- [ ] `baseball-draft-room.png`
- [ ] `baseball-sleepers-busts.png`

### Applied Math

- [ ] `applied-math-optimization.png`

### NBA

- [ ] `nba-matchup-intelligence.png`
- [ ] `nba-player-tracker.png`

### Music

- [ ] `music-adaptive-sheet.png`
- [ ] `music-tuner.png`

### SQL & Excel

- [ ] `sql-excel-quant-claims.png`
- [ ] `sql-excel-real-world-credit-risk.png`

### Portfolio Website

- [ ] `portfolio-website-analytics.png`
- [ ] `portfolio-website-sql-excel.png`

---

## Folder map

```
Screenshots/
├── HOW_TO_CAPTURE.md
├── screenshot-manifest.json
├── screenshot-checklist.md          ← this file
├── SCREENSHOT_CAPTURE_REGISTRY.md
├── Investment/                      ← 7 images
├── Baseball/                        ← 7 images
├── Applied-Math/                  ← 6 images
├── NBA/                           ← 6 images
├── Music/                         ← 5 images
├── SQL-Excel/                     ← 6 images
└── Portfolio-Website/             ← 3 images
```

---

## Progress tracker

| Folder | P0 | P1 | P2 | Total | Done |
|--------|----|----|-----|-------|------|
| Investment | 2 | 3 | 2 | 7 | 0 |
| Baseball | 3 | 2 | 2 | 7 | 0 |
| Applied-Math | 3 | 2 | 1 | 6 | 0 |
| NBA | 2 | 2 | 2 | 6 | 0 |
| Music | 1 | 2 | 2 | 5 | 0 |
| SQL-Excel | 0 | 4 | 2 | 6 | 0 |
| Portfolio-Website | 0 | 1 | 2 | 3 | 0 |
| **Total** | **11** | **16** | **13** | **40** | **0** |

---

## Legacy note

The previous 54-screenshot plan included Future Lens and Command Center repos (not in the demo-mode pass). Those remain optional Tier 3 captures outside this folder structure. Revisit after P0–P1 complete.
