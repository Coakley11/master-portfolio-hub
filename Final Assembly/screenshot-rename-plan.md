# Screenshot Rename Plan

**Generated:** 2026-06-05  
**Executed by:** `scripts/integrate-screenshots.py`

Legacy captures used a pre-manifest naming scheme (`.png.jpg` extension, no `-demo` suffix). This plan maps each staging file to the canonical manifest filename under `Portfolio Website/assets/screenshots/`.

## Investment (`Screenshots/Investment/`)

| Legacy file | Canonical target | Rationale |
|-------------|------------------|-----------|
| `investment-portfolio-summary-mobile.png.jpg` | `investment-overview-demo.png` | Only overview capture available; used as P0 hero |
| `investment-portfolio-summary-mobile.png.jpg` | `investment-overview-demo-mobile.png` | Duplicate for mobile manifest slot |
| `investment-portfolio-health.png.jpg` | `investment-portfolio-health.png` | Exact match |
| `investment-allocation-optimizer.png.jpg` | `investment-optimizer.png` | Optimizer page |

**Still need fresh capture:** `investment-portfolio-analytics-demo.png`, `investment-monte-carlo.png`, `investment-efficient-frontier.png`, `investment-correlation-heatmap.png`

## Baseball (`Screenshots/Baseball/`)

| Legacy file | Canonical target | Rationale |
|-------------|------------------|-----------|
| `baseball-draft-recommendation-engine.png.jpg` | `baseball-draft-assistant-demo.png` | Draft Assistant P0 hero |
| `baseball-ml-projections.png.jpg` | `baseball-ml-projections-demo.png` | ML Predictions P0 |
| `baseball-roster-heatmap.png.jpg` | `baseball-career-totals-demo.png` | Best available for Career Totals P0 |
| `baseball-player-insight.png.jpg` | `baseball-player-comparison.png` | Player comparison P1 |
| `baseball-statistical-testing.png.jpg` | `baseball-trend-analysis.png` | Statistical testing → trend gallery |

**Still need fresh capture:** `baseball-draft-room.png`, `baseball-sleepers-busts.png`

## Applied Math (`Screenshots/Applied-Math/`)

| Legacy file | Canonical target | Rationale |
|-------------|------------------|-----------|
| `applied-math-betting-ev.png.jpg` | `applied-math-betting-ev-demo.png` | P0 hero |
| `applied-math-ai-overfitting.png.jpg` | `applied-math-ai-training-demo.png` | Train an AI P0 |
| `applied-math-disease-simulation.png.jpg` | `applied-math-disease-spread-demo.png` | SIR epidemic P0 |

**Still need fresh capture:** `applied-math-home-actions.png`, `applied-math-sports-prediction.png`, `applied-math-optimization.png`

## NBA (`Screenshots/NBA/`)

| Legacy file | Canonical target | Rationale |
|-------------|------------------|-----------|
| `nba-home-dashboard.png.jpg` | `nba-home-dashboard-demo.png` | P0 hero |
| `nba-legacy-tracker.png.jpg` | `nba-legacy-tracker-demo.png` | P0 legacy chart |

**Still need fresh capture:** `nba-playoff-bracket.png`, `nba-live-game-center.png`, `nba-matchup-intelligence.png`, `nba-player-tracker.png`

## Music (`Screenshots/Music/`)

| Legacy file | Canonical target | Rationale |
|-------------|------------------|-----------|
| `music-practice-coach-main.png.jpg` | `music-practice-demo.png` | P0 hero |
| `music-backing-traci-studio.png.jpg` | `music-backing-tracks.png` | Backing Track Studio |
| `music-custom-progression-builder.png.jpg` | `music-adaptive-sheet.png` | Closest gallery slot for progression builder |

**Still need fresh capture:** `music-song-catalog.png`, `music-tuner.png`

## SQL & Excel

No legacy files on disk. Capture from `SQL Portfolio/*.xlsx` per `Screenshots/SQL-Excel/CAPTURE_TABLE.md`.

## Re-run integration

After adding new captures to `Screenshots/<Folder>/` (as `.png` or `.png.jpg`):

```powershell
python scripts/integrate-screenshots.py
powershell -File scripts/verify-screenshots.ps1
```
