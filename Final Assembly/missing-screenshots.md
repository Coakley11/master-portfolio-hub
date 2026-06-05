# Missing Screenshots

**Generated:** 2026-06-05  
**Status:** 0 of 35 referenced files present on disk  
**Verification:** `scripts/verify-screenshots.ps1` (exit code 1)

All filenames in `projects.json` match `screenshot-manifest.json`. Paths updated to `assets/screenshots/<Folder>/` for GitHub Pages.

## P0 — Hero captures (show on home cards & detail pages)

| App | Filename | Page |
|-----|----------|------|
| Investment | `investment-overview-demo.png` | Overview (Demo Mode) |
| Investment | `investment-portfolio-analytics-demo.png` | Portfolio Analytics |
| Baseball | `baseball-draft-assistant-demo.png` | Draft Assistant |
| Baseball | `baseball-ml-projections-demo.png` | ML Predictions |
| Baseball | `baseball-career-totals-demo.png` | Career Totals |
| Applied Math | `applied-math-betting-ev-demo.png` | Analyze a Bet |
| Applied Math | `applied-math-ai-training-demo.png` | Train an AI |
| Applied Math | `applied-math-disease-spread-demo.png` | Disease Spread |
| NBA | `nba-home-dashboard-demo.png` | Home Dashboard |
| NBA | `nba-legacy-tracker-demo.png` | Legacy Tracker |
| Music | `music-practice-demo.png` | Practice studio |

## P1 — Secondary gallery

| App | Filename |
|-----|----------|
| Investment | `investment-portfolio-health.png`, `investment-monte-carlo.png`, `investment-efficient-frontier.png` |
| Baseball | `baseball-player-comparison.png`, `baseball-trend-analysis.png` |
| Applied Math | `applied-math-home-actions.png`, `applied-math-sports-prediction.png` |
| NBA | `nba-playoff-bracket.png`, `nba-live-game-center.png` |
| Music | `music-song-catalog.png`, `music-backing-tracks.png` |
| SQL-Excel | `sql-excel-ai-evaluator-dashboard.png`, `sql-excel-investment-workbook-dashboard.png` |

## P2 — Extended gallery

| App | Filename |
|-----|----------|
| Investment | `investment-correlation-heatmap.png`, `investment-optimizer.png` |
| Baseball | `baseball-draft-room.png`, `baseball-sleepers-busts.png` |
| Applied Math | `applied-math-optimization.png` |
| NBA | `nba-matchup-intelligence.png`, `nba-player-tracker.png` |
| Music | `music-adaptive-sheet.png`, `music-tuner.png` |
| SQL-Excel | `sql-excel-quant-claims.png`, `sql-excel-real-world-credit-risk.png` |

## Drop location

```
Portfolio Website/assets/screenshots/<Folder>/<filename>.png
```

Capture workflow: `Screenshots/HOW_TO_CAPTURE.md` at repo root.

## UI behavior until captures land

Missing images show a dashed placeholder with the expected filename. No broken-image icons; `onerror` handler applies `.screenshot-img--missing` styling.
