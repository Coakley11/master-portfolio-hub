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

Set in `data/projects.json` → `site.linkedin`.

Current: https://www.linkedin.com/in/daniel-cohen-355319340/

## Resume PDF

Regenerate after resume edits:

```powershell
python scripts/refresh-resume-content.py
python scripts/generate-resume-pdf.py
```
