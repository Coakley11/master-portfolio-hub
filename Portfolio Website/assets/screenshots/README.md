# Portfolio Screenshots (GitHub Pages)

Screenshots served by the portfolio site live here. Paths in `data/projects.json` use `assets/screenshots/<Folder>/<filename>.png`.

## Adding captures

1. Capture PNGs per `Screenshots/HOW_TO_CAPTURE.md` (repo root).
2. Drop into `Screenshots/<Folder>/` (legacy `.png.jpg` or native `.png` both work).
3. Run `python scripts/integrate-screenshots.py` to convert, rename, and publish into this folder.
4. Run `scripts/verify-screenshots.ps1` to confirm all `projects.json` references resolve.

**Current coverage:** 16/35 references published · all P0 heroes present. See `Final Assembly/screenshot-coverage-report.md`.

## Source of truth

- Filenames: `screenshot-manifest.json` in this folder (synced from `Screenshots/screenshot-manifest.json`).
- Staging area: `Screenshots/` at repo root remains the capture workspace; publish copies into `assets/screenshots/` for deployment.
