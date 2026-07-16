# GitHub Pages Deployment

## Recommended setup

| Setting | Value |
|---------|--------|
| Source | Deploy from a branch |
| Branch | `main` |
| Folder | `/Portfolio Website` |

The site is self-contained under `Portfolio Website/`. All asset paths are relative (`css/`, `js/`, `data/`, `assets/`).

## Pre-deploy checklist

1. Copy captured PNGs from `Screenshots/<Folder>/` into `Portfolio Website/assets/screenshots/<Folder>/`.
2. Run `scripts/verify-screenshots.ps1` from the Master Portfolio Hub root (exit 0 = all images present).
3. Open `index.html` locally via `python -m http.server` inside `Portfolio Website/` and spot-check project cards and detail pages.
4. Confirm `.nojekyll` is present (allows `_` paths and static JSON).

## Path notes

- Screenshot URLs in `data/projects.json` use `assets/screenshots/...` (GitHub Pages safe).
- Resume download uses `assets/docs/resume-project-descriptions.md` (bundled copy for Pages).
- LinkedIn is set in `projects.json` → `site.linkedin` (currently a Google Share redirect). Prefer a permanent `https://www.linkedin.com/in/...` URL when available.

## Professional pages

| Page | URL |
|------|-----|
| Resume Hub | `resume.html` |
| Resume Preview | `resume-preview.html` |
| Resume PDF | `assets/docs/daniel-cohen-resume.pdf` |
| Career Profile | `career-profile.html` |
| Executive Summary | `executive-summary.html` |

Regenerate PDF after resume edits: `python scripts/generate-resume-pdf.py`

## Contact privacy

- Email is **not** rendered on the homepage CTA.
- Contact page uses a **Send Email** mailto button only (`contact.html`).

## Live app buttons

- Enabled when `liveUrl` is set in `projects.json`.
- Disabled (grey) when `liveUrl` is null — no fake placeholder URLs.
