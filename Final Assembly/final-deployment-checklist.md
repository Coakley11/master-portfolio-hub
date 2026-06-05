# Final Deployment Checklist — GitHub Pages

**Generated:** 2026-06-05  
**Pre-deploy QA:** `scripts/qa-deployment.ps1` (local server required)  
**Commit at QA time:** `cda3c85`

---

## A. GitHub Pages setup

- [ ] Push `master` branch to GitHub remote
- [ ] Repo → **Settings** → **Pages**
- [ ] Source: **Deploy from a branch**
- [ ] Branch: `master` · Folder: **`/Portfolio Website`**
- [ ] Confirm `.nojekyll` exists in `Portfolio Website/`
- [ ] Wait 1–3 minutes for build; note live URL

---

## B. Post-deploy smoke test (live URL)

Replace `<pages-url>` with your GitHub Pages base URL.

| # | URL | Expected |
|---|-----|----------|
| 1 | `<pages-url>/` | Home loads; 4 flagship cards show screenshots |
| 2 | `<pages-url>/index.html#projects` | Jumps to Featured Project Showcase |
| 3 | `<pages-url>/career-profile.html` | Career sections populate |
| 4 | `<pages-url>/executive-summary.html` | Executive summary populates |
| 5 | `<pages-url>/resume.html` | Resume hub with education & bullets |
| 6 | `<pages-url>/resume-preview.html` | Formatted resume document |
| 7 | `<pages-url>/assets/docs/daniel-cohen-resume.pdf` | PDF downloads (4+ KB) |
| 8 | `<pages-url>/sql-excel.html` | Workbook cards render |
| 9 | `<pages-url>/contact.html` | Send Email button (no address in hero) |
| 10 | `<pages-url>/project.html?id=baseball-stat-app` | Detail page + Live App button |
| 11 | `<pages-url>/data/projects.json` | JSON loads (no 404) |

---

## C. Navigation (all pages)

- [ ] **Home** → `index.html`
- [ ] **Projects** → `index.html#projects`
- [ ] **Career** → `career-profile.html`
- [ ] **Summary** → `executive-summary.html`
- [ ] **Resume** → `resume.html`
- [ ] **SQL & Excel** → `sql-excel.html`
- [ ] **Contact** → `contact.html`
- [ ] Logo returns to home from every page

---

## D. Resume flow

- [ ] Homepage hero: **Resume Preview** → `resume-preview.html`
- [ ] Homepage hero: **Download PDF** → `daniel-cohen-resume.pdf`
- [ ] Bottom CTA: **View Resume** → `resume-preview.html`
- [ ] Bottom CTA: **Download PDF** → PDF file
- [ ] Resume preview: **Download PDF** + **Print** buttons work
- [ ] Resume hub: links to Career Profile + Executive Summary

Regenerate PDF after resume edits:
```powershell
python scripts/generate-resume-pdf.py
```

---

## E. Screenshots

- [x] **P0 heroes (10/10)** — all flagship + Applied Math cards display images
- [ ] **P1/P2 gallery (19 missing)** — secondary slots show dashed placeholders (non-blocking)
- [ ] **SQL & Excel (4 missing)** — workbook cards show placeholders until captured

Verify locally:
```powershell
python scripts/verify-project-heroes.py   # must show all OK
powershell -File scripts/verify-screenshots.ps1   # exit 1 expected until gallery complete
```

---

## F. Contact privacy

- [x] Email **not** in `index.html` static HTML
- [x] Email **not** in homepage `renderCtaSection` (GitHub + LinkedIn placeholder + contact link only)
- [x] Email **only** via mailto button on `contact.html` (not visible as plain text)
- [ ] Re-check live site after deploy — view page source on home

---

## G. Live app buttons

- [x] 7 Streamlit apps have real `liveUrl` in `projects.json`
- [ ] Click **Live App** on each flagship detail page after deploy
- [ ] SQL workbook cards correctly show disabled / no fake URLs

---

## H. Mobile check (phone or DevTools ≤ 768px)

- [ ] Navigation wraps cleanly
- [ ] Hero CTA buttons stack vertically
- [ ] Resume preview readable (no horizontal scroll)
- [ ] Project cards single-column
- [ ] Contact cards stack

---

## I. Optional polish (post-launch)

- [ ] Add final LinkedIn URL to `projects.json` → `site.linkedin`
- [ ] Capture 19 remaining gallery + SQL screenshots
- [ ] Add LinkedIn URL to resume PDF (regenerate)
- [ ] Custom domain (if desired)

---

## J. Application repositories

- [x] **Confirmed:** No app repos modified during portfolio work
- [ ] Do not edit app repos when updating portfolio — only Master Portfolio Hub

---

## Quick local QA command

```powershell
cd "Portfolio Website"
python -m http.server 9890
# New terminal:
powershell -File scripts/qa-deployment.ps1 -Port 9890
```

Expected: all checks pass (25+), zero failures.
