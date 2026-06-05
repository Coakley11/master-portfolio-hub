# Screenshot Coverage Report

**Generated:** 2026-06-05 19:41 UTC

## Summary

| Metric | Count |
|--------|-------|
| Legacy `.png.jpg` in staging | 16 |
| Native `.png` in staging | 0 |
| Files copied/converted this run | 17 |
| Expected site references | 35 |
| **Published on site** | **16** |
| Still missing | 19 |

## Rename plan (executed)

| Legacy source | Deploy target | Note |
|---------------|---------------|------|
| `Investment/investment-portfolio-summary-mobile.png.jpg` | `Investment/investment-overview-demo.png` | Mobile portfolio summary used as Overview hero until desktop capture |
| `Investment/investment-portfolio-summary-mobile.png.jpg` | `Investment/investment-overview-demo-mobile.png` | Same capture retained as mobile variant |
| `Investment/investment-portfolio-health.png.jpg` | `Investment/investment-portfolio-health.png` | Exact manifest match |
| `Investment/investment-allocation-optimizer.png.jpg` | `Investment/investment-optimizer.png` | Allocation optimizer → optimizer |
| `Baseball/baseball-draft-recommendation-engine.png.jpg` | `Baseball/baseball-draft-assistant-demo.png` | Draft recommendation engine → draft assistant demo |
| `Baseball/baseball-ml-projections.png.jpg` | `Baseball/baseball-ml-projections-demo.png` | ML projections |
| `Baseball/baseball-roster-heatmap.png.jpg` | `Baseball/baseball-career-totals-demo.png` | Roster heatmap used for career totals hero |
| `Baseball/baseball-player-insight.png.jpg` | `Baseball/baseball-player-comparison.png` | Player insight → comparison tool |
| `Baseball/baseball-statistical-testing.png.jpg` | `Baseball/baseball-trend-analysis.png` | Statistical testing → trend analysis gallery |
| `Applied-Math/applied-math-betting-ev.png.jpg` | `Applied-Math/applied-math-betting-ev-demo.png` | Betting EV demo |
| `Applied-Math/applied-math-ai-overfitting.png.jpg` | `Applied-Math/applied-math-ai-training-demo.png` | AI overfitting → training demo |
| `Applied-Math/applied-math-disease-simulation.png.jpg` | `Applied-Math/applied-math-disease-spread-demo.png` | Disease simulation → spread demo |
| `NBA/nba-home-dashboard.png.jpg` | `NBA/nba-home-dashboard-demo.png` | Home dashboard demo |
| `NBA/nba-legacy-tracker.png.jpg` | `NBA/nba-legacy-tracker-demo.png` | Legacy tracker demo |
| `Music/music-practice-coach-main.png.jpg` | `Music/music-practice-demo.png` | Practice coach main → practice demo |
| `Music/music-backing-traci-studio.png.jpg` | `Music/music-backing-tracks.png` | Backing track studio (typo in legacy filename) |
| `Music/music-custom-progression-builder.png.jpg` | `Music/music-adaptive-sheet.png` | Progression builder → adaptive sheet slot |

## Published files

- `Applied-Math/applied-math-ai-training-demo.png` ← `Applied-Math/applied-math-ai-overfitting.png.jpg`
- `Applied-Math/applied-math-betting-ev-demo.png` ← `Applied-Math/applied-math-betting-ev.png.jpg`
- `Applied-Math/applied-math-disease-spread-demo.png` ← `Applied-Math/applied-math-disease-simulation.png.jpg`
- `Baseball/baseball-career-totals-demo.png` ← `Baseball/baseball-roster-heatmap.png.jpg`
- `Baseball/baseball-draft-assistant-demo.png` ← `Baseball/baseball-draft-recommendation-engine.png.jpg`
- `Baseball/baseball-ml-projections-demo.png` ← `Baseball/baseball-ml-projections.png.jpg`
- `Baseball/baseball-player-comparison.png` ← `Baseball/baseball-player-insight.png.jpg`
- `Baseball/baseball-trend-analysis.png` ← `Baseball/baseball-statistical-testing.png.jpg`
- `Investment/investment-optimizer.png` ← `Investment/investment-allocation-optimizer.png.jpg`
- `Investment/investment-overview-demo.png` ← `Investment/investment-portfolio-summary-mobile.png.jpg`
- `Investment/investment-portfolio-health.png` ← `Investment/investment-portfolio-health.png.jpg`
- `Music/music-adaptive-sheet.png` ← `Music/music-custom-progression-builder.png.jpg`
- `Music/music-backing-tracks.png` ← `Music/music-backing-traci-studio.png.jpg`
- `Music/music-practice-demo.png` ← `Music/music-practice-coach-main.png.jpg`
- `NBA/nba-home-dashboard-demo.png` ← `NBA/nba-home-dashboard.png.jpg`
- `NBA/nba-legacy-tracker-demo.png` ← `NBA/nba-legacy-tracker.png.jpg`

## Missing captures

- `Applied-Math/applied-math-home-actions.png`
- `Applied-Math/applied-math-optimization.png`
- `Applied-Math/applied-math-sports-prediction.png`
- `Baseball/baseball-draft-room.png`
- `Baseball/baseball-sleepers-busts.png`
- `Investment/investment-correlation-heatmap.png`
- `Investment/investment-efficient-frontier.png`
- `Investment/investment-monte-carlo.png`
- `Investment/investment-portfolio-analytics-demo.png`
- `Music/music-song-catalog.png`
- `Music/music-tuner.png`
- `NBA/nba-live-game-center.png`
- `NBA/nba-matchup-intelligence.png`
- `NBA/nba-player-tracker.png`
- `NBA/nba-playoff-bracket.png`
- `SQL-Excel/sql-excel-ai-evaluator-dashboard.png`
- `SQL-Excel/sql-excel-investment-workbook-dashboard.png`
- `SQL-Excel/sql-excel-quant-claims.png`
- `SQL-Excel/sql-excel-real-world-credit-risk.png`

## UI verification

| Surface | Status | Notes |
|---------|--------|-------|
| Home flagship cards (4) | ✅ All heroes load | Investment, Baseball, NBA, Music |
| Tier 1 project card (Applied Math) | ✅ Hero loads | `applied-math-betting-ev-demo.png` |
| Project detail pages (5 apps) | ✅ Hero + partial galleries | Secondary slots show placeholder until re-captured |
| SQL & Excel cards | ⏳ Placeholders | 4 workbook screenshots not yet captured |
| HTTP PNG validation | ✅ Valid PNG headers | Tested via local server on port 9877 |

## P0 hero status

- ✅ `Investment/investment-overview-demo.png`
- ✅ `Baseball/baseball-draft-assistant-demo.png`
- ✅ `Baseball/baseball-ml-projections-demo.png`
- ✅ `Baseball/baseball-career-totals-demo.png`
- ✅ `Applied-Math/applied-math-betting-ev-demo.png`
- ✅ `Applied-Math/applied-math-ai-training-demo.png`
- ✅ `Applied-Math/applied-math-disease-spread-demo.png`
- ✅ `NBA/nba-home-dashboard-demo.png`
- ✅ `NBA/nba-legacy-tracker-demo.png`
- ✅ `Music/music-practice-demo.png`
