# Final QA Report — Portfolio Hub

**Generated:** 2026-06-05  
**Scope:** Master Portfolio Hub only (`Portfolio Website/`)

## Page load verification

| Page | HTTP | Notes |
|------|------|-------|
| `index.html` | 200 | Hero, Featured Analytics, About, Skills, Projects, Case Studies, CTA render via `main.js` |
| `contact.html` | 200 | Mailto button; no email in static HTML |
| `resume.html` | 200 | Bullets + download link to `assets/docs/resume-project-descriptions.md` |
| `project.html?id=<id>` | 200 | Detail layout, `detailSections`, case studies, live/GitHub/README buttons |
| `sql-excel.html` | 200 | Workbook showcase cards |
| `analytics.html` | 200 | Category filter page |
| `data/projects.json` | 200 | 38 KB; 7 repos, 7 `liveUrl` values |

Local server: `python -m http.server 9876` from `Portfolio Website/`.

## Section checks (home)

| Section | Status |
|---------|--------|
| Home hero | Pass |
| Featured Analytics grid | Pass — 7 cards from `featuredAnalytics` |
| About Me + pillars | Pass — positioning updated |
| Skills dashboard | Pass — 10 meters |
| Flagship project cards (4) | Pass — placeholders until PNGs added |
| Case Studies | Pass — 4 flagship case studies |
| Resume / Contact CTA | Pass — GitHub + LinkedIn placeholder; **no email** |

## Contact privacy

| Check | Status |
|-------|--------|
| Email absent from `index.html` static shell | Pass |
| Email absent from homepage CTA (`renderCtaSection`) | Pass |
| Email only via mailto on contact page | Pass |
| GitHub `https://github.com/Coakley11` | Pass |
| LinkedIn placeholder (not fake URL) | Pass |

## Screenshot integration

| Check | Status |
|-------|--------|
| `projects.json` paths → `assets/screenshots/` | Pass (31 paths updated) |
| Filenames match `screenshot-manifest.json` | Pass |
| Hero filenames match `heroScreenshot` fields | Pass |
| Images on disk | **Pending** — 0/35 files (see `missing-screenshots.md`) |
| Broken-image handling | Pass — dashed placeholder + filename hint |

## Live app buttons

| Check | Status |
|-------|--------|
| 7 Streamlit apps have real `liveUrl` | Pass |
| SQL workbooks show disabled Live App | Pass |
| No fake placeholder URLs | Pass |

## Project detail polish

| Project | `detailSections` |
|---------|------------------|
| Investment | Portfolio Analytics, Risk Analysis, Allocation Modeling, Quantitative Decision Support |
| Baseball | Statistical Testing, ML Projections, Fantasy Baseball Analytics |
| NBA | Legacy Scoring, Playoff Forecasting, Matchup Analysis, Scenario Simulation |
| Music | Practice Intelligence, Backing Track Generation, Progression Builder, Interactive Learning Tools |

## Deployment readiness

| Check | Status |
|-------|--------|
| Relative paths within `Portfolio Website/` | Pass |
| `.nojekyll` present | Pass |
| Resume download path Pages-safe | Pass (`assets/docs/`) |
| `DEPLOYMENT.md` guide | Pass |
| `scripts/verify-screenshots.ps1` | Pass |

## Mobile responsiveness

| Check | Status |
|-------|--------|
| Breakpoints at 900px / 768px | Pass — grid stacks, nav wraps, hero CTA column |
| Detail sidebar unstacks on mobile | Pass |

## Console / data placeholders

| Check | Status |
|-------|--------|
| `fetch('data/projects.json')` resolves | Pass |
| Missing project id handled | Pass — friendly message |
| No `example.com` email | Pass — updated to real address (contact only) |
| Screenshot placeholders (not Lorem) | Pass — show expected filename |

## Known limitations (not blockers)

1. **Screenshots:** UI works; visual polish awaits PNG drop into `assets/screenshots/`.
2. **LinkedIn:** Placeholder text until URL provided.
3. **Console:** Lazy-load `onerror` on missing PNGs is expected until captures complete.

## Application repositories

**Confirmed:** No changes to NBA, Baseball, Investment, Music, or other app GitHub repos in this phase.
