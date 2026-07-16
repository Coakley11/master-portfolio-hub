# Portfolio Screenshots (GitHub Pages)

Screenshots served by the portfolio site live here. Paths in `data/projects.json` use `assets/screenshots/<Folder>/<filename>.png`.

## Canonical set (2026-07-15)

Use the numbered captures in `Screenshots/` at the repo root:

- `Baseball/01-…` through `09-…`
- `Music/01-…` through `06-…`
- `Investment/01-…` through `06-…`
- `Applied-Math/01-…` through `05-…`
- `NBA/01-…` through `05-…`
- `Future-Lens/01-…` through `04-…`
- `Command-Center/*.png`

## Publish

```powershell
python scripts/sync-portfolio-screenshots.py
```

Optional full copy refresh after editing project metadata:

```powershell
python scripts/refresh-portfolio-website-data.py
python scripts/sync-portfolio-screenshots.py
```

**Current coverage:** 40 app screenshots published across all seven suite applications.

## Source of truth

- Staging / capture workspace: `Screenshots/`
- Deploy copies: `Portfolio Website/assets/screenshots/`
- Manifest: `screenshot-manifest.json` (synced to both locations)
