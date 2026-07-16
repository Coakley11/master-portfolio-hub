# GitHub Pages Deployment

## Live URL

**https://coakley11.github.io/master-portfolio-hub/**

Repo: https://github.com/Coakley11/master-portfolio-hub

## How it deploys

GitHub Actions workflow `.github/workflows/deploy-portfolio.yml` publishes the `Portfolio Website/` folder on every push to `master`.

Classic Pages folder source only supports `/` or `/docs`, so Actions is required for this nested folder name.

## Local preview

```powershell
cd "Portfolio Website"
python -m http.server 9890
```

## LinkedIn

Set in `data/projects.json` → `site.linkedin` to your permanent `https://www.linkedin.com/in/...` URL when ready. Leave empty until then (the site shows a placeholder; do not use Google Share / `linkedin.com/me` shortcuts — those are not public profile links).

## Resume PDF

Regenerate after resume edits:

```powershell
python scripts/refresh-resume-content.py
python scripts/generate-resume-pdf.py
```
