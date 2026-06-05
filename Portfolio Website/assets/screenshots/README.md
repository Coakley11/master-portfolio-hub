# Portfolio Screenshots (GitHub Pages)

Screenshots served by the portfolio site live here. Paths in `data/projects.json` use `assets/screenshots/<Folder>/<filename>.png`.

## Adding captures

1. Capture PNGs per `Screenshots/HOW_TO_CAPTURE.md` (repo root).
2. Copy files into the matching subfolder here (e.g. `Investment/investment-overview-demo.png`).
3. Run `scripts/verify-screenshots.ps1` from the Master Portfolio Hub root to confirm all references resolve.

## Source of truth

- Filenames: `screenshot-manifest.json` in this folder (synced from `Screenshots/screenshot-manifest.json`).
- Staging area: `Screenshots/` at repo root remains the capture workspace; publish copies into `assets/screenshots/` for deployment.
