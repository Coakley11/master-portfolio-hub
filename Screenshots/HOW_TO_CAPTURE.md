# How to Capture Portfolio Screenshots

Mechanical workflow — go app by app, save files with exact names, and the portfolio website updates automatically.

---

## Before You Start

1. Run each app locally: `streamlit run streamlit_app.py` (or the app’s main entry file).
2. Open this folder in a second window so you can drag saves into the right subfolder.
3. Use **1920×1080** for desktop captures (1280×800 minimum). Optional mobile: **390×844** with `-mobile` suffix on the filename.

---

## Capture Workflow (Every Streamlit App)

| Step | Action |
|------|--------|
| 1 | Open the app in your browser |
| 2 | Enable **Portfolio Demo Mode** in the sidebar (required — auto-loads examples) |
| 3 | Enable **Portfolio Screenshot Mode** in the sidebar (recommended — cleaner layout) |
| 4 | Navigate to the **hero page** listed in that app’s `README.md` or `CAPTURE_TABLE.md` |
| 5 | Wait for charts and data to finish loading (no spinners) |
| 6 | **Desktop:** capture full browser window or crop to main content area |
| 7 | **Mobile (optional):** resize DevTools to 390×844, capture again |
| 8 | Save using the **exact filename** from the capture table (e.g. `investment-overview-demo.png`) |
| 9 | Place the file in the correct folder under `Screenshots/` (e.g. `Screenshots/Investment/`) |
| 10 | Refresh the portfolio website — the image appears when the file exists |

---

## Recommended Capture Order (P0 First)

Do these eleven captures first — they tell the full portfolio story in under an hour:

1. `Investment/investment-overview-demo.png`
2. `Baseball/baseball-draft-assistant-demo.png`
3. `Baseball/baseball-ml-projections-demo.png`
4. `Baseball/baseball-career-totals-demo.png`
5. `Applied-Math/applied-math-betting-ev-demo.png`
6. `Applied-Math/applied-math-ai-training-demo.png`
7. `Applied-Math/applied-math-disease-spread-demo.png`
8. `NBA/nba-home-dashboard-demo.png`
9. `NBA/nba-legacy-tracker-demo.png`
10. `Music/music-practice-demo.png`
11. `SQL-Excel/sql-excel-ai-evaluator-dashboard.png`

Then work through P1 and P2 items in each folder’s `CAPTURE_TABLE.md`.

---

## SQL & Excel Workbooks

No Streamlit toggles. Open the `.xlsx` from `SQL Portfolio/`, navigate to the sheet listed in the capture table, and screenshot Excel directly.

Save into `Screenshots/SQL-Excel/` using the filenames in that folder’s README.

---

## Portfolio Website Check

After adding P0 screenshots:

1. Open `Portfolio Website/index.html` in a browser (local file or simple HTTP server).
2. Tier 1 project cards should show images instead of gray placeholders.
3. Missing files still show a placeholder — add the PNG and refresh.

**Path rule:** Images live in `Master Portfolio Hub/Screenshots/<Folder>/`. The website references them as `../Screenshots/<Folder>/<filename>.png` relative to `Portfolio Website/`.

---

## File Naming Rules

- Lowercase, hyphen-separated: `app-feature-demo.png`
- Hero demo shots use `-demo` suffix: `baseball-draft-assistant-demo.png`
- Mobile variants add `-mobile` before `.png`: `nba-home-dashboard-demo-mobile.png`
- **Never rename** after the website is wired — use manifest filenames exactly.

---

## Reference Files

| File | Purpose |
|------|---------|
| `screenshot-manifest.json` | Machine-readable list for the website |
| `screenshot-checklist.md` | Master checklist with checkboxes |
| `SCREENSHOT_CAPTURE_REGISTRY.md` | All capture tables in one document |
| `<Folder>/CAPTURE_TABLE.md` | Per-app capture instructions |
| `<Folder>/README.md` | What images belong in that folder |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Empty page in demo mode | Toggle Demo Mode off/on; click the app’s “Load Demo” button if shown |
| Chart not visible | Ensure Screenshot/Demo Mode is on; scroll to above-the-fold hero content |
| Website still shows placeholder | Confirm filename spelling and folder name (case-sensitive on some hosts) |
| Image broken on GitHub Pages | Deploy the whole `Master Portfolio Hub` or copy PNGs into `Portfolio Website/assets/screenshots/` |
