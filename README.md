# Master Portfolio Hub

**Daniel Cohen — Quantitative Analytics & AI Portfolio**

Professional portfolio workspace for Data Analyst, Product Analyst, BI Analyst, Research Analyst, Quant Analyst, Financial Analyst, AI Evaluator, and AI Trainer applications.

> Decision-support applications · Statistics · Finance · SQL · AI-assisted product development

**Latest refresh (2026-07-15):** Portfolio Website uses the numbered canonical screenshot set for all seven apps. See `Final Assembly/portfolio-refresh-audit-2026-07-15.md`.

---

## Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Portfolio Website | `Portfolio Website/` |
| 2 | Portfolio Inventory | `Portfolio Inventory/portfolio-inventory.md` |
| 3 | SQL & Excel Analytics Inventory | `SQL Portfolio/sql-excel-analytics-inventory.md` |
| 4 | Professional Project Descriptions | `Professional Project Descriptions/` |
| 5 | LinkedIn Project Descriptions | `LinkedIn/linkedin-project-descriptions.md` |
| 5b | LinkedIn Profile Optimization | `LinkedIn/linkedin-profile-optimization.md` |
| 6 | Resume Project Descriptions | `Resume/resume-project-descriptions.md` |
| 7 | Screenshot Checklist | `Screenshots/screenshot-checklist.md` |
| 8 | README Improvement Report | `README Review/readme-improvement-report.md` |
| 9 | Portfolio Gap Analysis | `Gap Analysis/portfolio-gap-analysis.md` |
| 10 | Application Readiness Report | `Application Readiness/application-readiness-report.md` |

---

## Project Categories

| Category | Projects |
|----------|----------|
| Analytics & Data Science | investment-portfolio-analyzer, baseball-stat-app, Applied-mathematical-intelligence |
| AI & Decision Support | Applied-mathematical-intelligence, future-lens-ai-transition-simulator |
| Interactive Applications | nba-playoff-companion-ai, ai-music-practice-coach |
| Infrastructure / Platform | daniel-ai-command-center |
| SQL & Excel Portfolio | 5 workbooks in `SQL Portfolio/` |

---

## View the Website Locally

**Important:** Start the server from `Portfolio Website/` (not the Hub root).

```powershell
powershell -File scripts/start-portfolio-server.ps1
```

Or manually:

```powershell
cd "Portfolio Website"
python -m http.server 9890
```

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:9890/ |
| **Resume Preview** (primary) | http://127.0.0.1:9890/resume-preview.html |
| Resume Hub | http://127.0.0.1:9890/resume.html |
| Career Profile | http://127.0.0.1:9890/career-profile.html |
| Executive Summary | http://127.0.0.1:9890/executive-summary.html |
| Contact | http://127.0.0.1:9890/contact.html |
| Projects | http://127.0.0.1:9890/index.html#projects |

Short aliases: `career.html`, `summary.html`, `projects.html`

For GitHub Pages: set source to `/Portfolio Website` folder.

---

## Source Repositories (Read-Only References)

Original repos remain in `Documents\GitHub` — untouched.

- https://github.com/Coakley11/investment-portfolio-analyzer
- https://github.com/Coakley11/baseball-stat-app
- https://github.com/Coakley11/Applied-mathematical-intelligence
- https://github.com/Coakley11/nba-playoff-companion-ai
- https://github.com/Coakley11/ai-music-practice-coach
- https://github.com/Coakley11/future-lens-ai-transition-simulator
- https://github.com/Coakley11/daniel-ai-command-center

---

## Portfolio Website Highlights

The home page (`Portfolio Website/index.html`) now includes:

- **Featured Analytics Work** — statistical testing, ML, optimization, probability modeling, simulations, dashboards
- **About Me** — analytics-focused professional positioning
- **Skills Dashboard** — visual competency meters
- **Featured Project Showcase** — Baseball, Investment Explorer, AMI, Music Practice Coach with current screenshots
- **Full Project Suite** — Basketball Playoff Companion, Future Lens, AI Command Center
- **Analytics Case Studies** — problem → results for each flagship project
- **Project detail pages** — `project.html?id=<project-id>` with full galleries
- **Resume & Contact** — view/download resume, email, GitHub, LinkedIn

## Next Steps (Highest ROI)

1. Deploy portfolio website to GitHub Pages (`/Portfolio Website` folder) and put the public URL on LinkedIn / resume / applications
2. Prefer replacing `site.linkedin` with a permanent `https://www.linkedin.com/in/...` URL when available (Google Share link is wired for now)
3. Capture SQL/Excel workbook screenshots into `Screenshots/SQL-Excel/` (only remaining screenshot gap)
4. Refresh resume PDF to match `Resume/resume-project-descriptions.md`
5. Restore Actuarial Analytics `.xlsx` source file (optional)
