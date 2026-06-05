# README Improvement Report

Review of all README files across 7 GitHub repositories. Original repos remain untouched — recommendations for future updates.

---

## Cross-Repo Gaps (All 7 Repositories)

| Gap | Priority | Recommendation |
|-----|----------|----------------|
| No screenshots | P0 | Add 3–5 screenshots per repo showing key features |
| No live demo URLs | P1 | Add Streamlit Cloud URLs to each README |
| No portfolio badge/link | P2 | Link to Master Portfolio Hub website |

---

## Per-Repository Review

### investment-portfolio-analyzer — Score: 8/10

**Present:** Features list, quick start, project structure table, disclaimer, dev workflow (dev/main branches)

**Missing:**
- Screenshots of dashboard tabs
- Live Streamlit Cloud demo URL
- Test running instructions (`pytest`)
- Author/contact section
- Link to SQL/Excel companion workbook

**Recommended additions:**
```markdown
## Live demo
[Streamlit Cloud URL]

## Screenshots
![Portfolio Overview](docs/screenshots/overview.png)

## Testing
pytest tests/

## Related work
See Investment App Portfolio Analysis Workbook in Master Portfolio Hub SQL Portfolio.
```

---

### Applied-mathematical-intelligence — Score: 9/10

**Present:** Version table, 7 labs, navigation, install, disclaimer, author, QA commands

**Missing:**
- Screenshots of home page and 2–3 labs
- Live demo URL
- Architecture diagram (components/ structure)
- Test count / coverage note

**Recommended additions:**
```markdown
## Architecture
components/ → streamlit_app.py router → simulations/

## Screenshots
![Home](docs/screenshots/home.png)
![Betting Lab](docs/screenshots/betting-lab.png)
```

---

### baseball-stat-app — Score: 6/10

**Present:** Comprehensive feature list, fantasy tools description, trend intelligence, current status

**Missing:**
- Quick start / install instructions
- `pip install -r requirements.txt` and run command
- Deployment instructions
- Tech stack table
- Project structure
- Author section
- Screenshots
- Live demo URL

**Recommended additions:**
```markdown
## Quick start
pip install -r requirements.txt
streamlit run streamlit_app.py

## Tech stack
Python, Streamlit, pybaseball, scikit-learn, statsmodels, plotly

## Project structure
| File | Purpose |
| streamlit_app.py | Main dashboard |
| ml_training_build.py | ML pipeline |
```

---

### nba-playoff-companion-ai — Score: 8/10

**Present:** Features, tech, run locally, deployment, docs index, author, cursor-prompts reference

**Missing:**
- Screenshots (home, live game center, bracket)
- Live demo URL
- Systems status summary in README (exists in docs/)

**Recommended additions:**
```markdown
## Screenshots
![Home Dashboard](docs/screenshots/home.png)
![Live Game Center](docs/screenshots/live-games.png)

## Current status
See docs/SYSTEMS_STATUS.md — stability phase, systems 65–95% complete.
```

---

### ai-music-practice-coach — Score: 3/10

**Present:** Version number, dev workflow link, adaptive sheet description

**Missing:**
- Project summary / what the app does
- Install instructions
- Feature list (9 studio pages)
- Tech stack
- Architecture overview
- Screenshots
- Author
- Live demo URL
- Deployment instructions

**Recommended additions:**
```markdown
# AI Music Practice Coach
AI-powered music practice studio with adaptive sheets, live tuner,
backing tracks, MIDI/MusicXML analysis, and OpenAI coaching.

## Features
- 9 studio pages including practice sheets, song catalog, tuner, karaoke
- Adaptive practice sheet generation from MIDI/MusicXML or catalog songs
- OpenAI coaching integration
- librosa-based recording analysis

## Quick start
pip install -r requirements.txt
streamlit run streamlit_music_practice_app.py
```

---

### future-lens-ai-transition-simulator — Score: 4/10

**Present:** One-line description, run locally, Streamlit Cloud deploy steps, prototype status

**Missing:**
- Feature tour / what users can explore
- Domain taxonomy list (work, learning, sports, investing)
- Scenario types (Conservative/Balanced/Aggressive)
- Screenshots
- Architecture note
- Author

**Recommended additions:**
```markdown
## What you can explore
- Timeline eras from 1980 to today across 6 domains
- Future scenarios through 2050 with 3 impact profiles
- Domain taxonomy: work, learning, creativity, sports, investing, everyday life

## Screenshots
![Timeline](docs/screenshots/timeline.png)
```

---

### daniel-ai-command-center — Score: 5/10

**Present:** Ecosystem app list, run command, status note, roadmap link

**Missing:**
- Feature tour (activity feed, coach insights, resume)
- Architecture diagram
- Supabase setup summary
- Screenshots
- Author
- Link to SQL migrations

**Recommended additions:**
```markdown
## Features
- App directory with deep links to all 6 satellite apps
- Cross-app activity feed and weekly summaries
- Coach-driven insights and recommendations
- Resume/continue workflow across apps

## Supabase setup
See supabase/migrations/ — 4 migration files for activity, users, saved items.

## Screenshots
![Command Center](docs/screenshots/home.png)
```

---

## Priority Summary

| Priority | Repos needing work | Effort |
|----------|-------------------|--------|
| P0 | All 7 — screenshots | Medium (capture from Streamlit Cloud) |
| P1 | ai-music-practice-coach, baseball-stat-app, future-lens | Low–Medium (write missing sections) |
| P1 | All 7 — live demo URLs | Low |
| P2 | daniel-ai-command-center — architecture | Low |
| P2 | investment-portfolio-analyzer — test instructions | Low |
