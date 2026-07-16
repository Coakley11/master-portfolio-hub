# Portfolio Refresh Audit & Recruiter Review

**Date:** 2026-07-15  
**Scope:** Master Portfolio Hub + verification against GitHub app repos  
**Screenshot source:** `Screenshots/` numbered canonical set (40 PNGs)  
**Priority 1 completed:** Portfolio Website wired to new screenshots + refreshed copy for all 7 apps

---

## Deliverable status

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | Portfolio Website refresh | **Done** — `projects.json`, homepage copy, captions, 40 screenshots published |
| 2 | Screenshot integration | **Done** — `scripts/sync-portfolio-screenshots.py` |
| 3 | Portfolio Hub refresh | **In progress** — website + professional descriptions + LinkedIn/Resume docs; empty category folders unchanged |
| 4 | Professional project descriptions | **Done** |
| 5 | LinkedIn recommendations | **Done** — `LinkedIn/` |
| 6 | Resume recommendations | **Done** — `Resume/` |
| 7 | Recruiter-impact review | **This document** |
| 8 | Prioritized improvement list | **This document** |

---

## 1. Weak areas of the portfolio

1. **SQL/Excel still has zero screenshots** — weakens Data Analyst / AI Evaluator proof for spreadsheet fluency.
2. **Empty hub folders** (`Interactive Applications`, `AI & Decision Support`, `Analytics & Data Science`) look unfinished if someone browses the repo.
3. ~~LinkedIn URL still null~~ — wired to Google Share link; prefer permanent `linkedin.com/in/...` when available.
4. **Future Lens is easy to oversell** — must stay labeled as Phase 1 prototype.
5. **Teaching-heavy resume history** can bury the product story if projects are not above the fold.
6. **Naming inconsistency** historically (Investment Analyzer vs Explorer; NBA vs Basketball Companion) — website now uses recruiter-friendly display names.
7. **Auth / “production accounts”** should not be claimed as fully closed across the suite.

---

## 2. Missing screenshots

| Area | Status |
|------|--------|
| Baseball, Music, Investment, AMI, NBA, Future Lens, Command Center | **Complete** (today’s set) |
| SQL-Excel workbooks | **Missing** (4 expected heroes) |
| Portfolio Website chrome captures | Optional / not required for applications |

No new screenshot plan needed for the seven apps.

---

## 3. Outdated content (found & addressed on website)

| Item | Before | After |
|------|--------|-------|
| Screenshot filenames | Legacy `*-demo.png` names | Numbered canonical set |
| AMI version framing | v2.5.0 | v3.6.1 capability framing |
| Baseball story | Mostly draft/ML heroes | Draft + live room + leagues + lineup/trade + AMI |
| Investment story | Overview-centric | Health, frontier, Monte Carlo, ETF overlap, beginner coach, AMI |
| Future Lens live URL | Old Streamlit URL | Current README URL |
| Command Center / Future Lens screenshots | Empty on site | Full galleries |
| Target roles | Missing Product Analyst | Added |

README rewrites deferred per instructions (only where clearly stale — not rewritten in app repos).

---

## 4. Broken / risky links

| Link | Note |
|------|------|
| Future Lens live URL | **Updated** to `…-m6n4kaku28ztzlxfts2xt6.streamlit.app` |
| Other Streamlit live URLs | Present in `projects.json`; spot-check before applications |
| Website `site.linkedin` | Still `null` — placeholder text shows |
| Empty hub category folders | Not links, but recruiter-confusing if exploring GitHub tree |

---

## 5. Redundant content

- Overlapping copy across website / LinkedIn / professional descriptions / resume (now intentionally aligned).
- Old screenshot filenames + orphan deploy copies (**removed** from `assets/screenshots/`).
- Multiple “tier” systems in older inventory docs (inventory still dated June 5 — lower priority to rewrite).

---

## 6. Areas confusing to recruiters

1. **Seven apps at once** without hierarchy → website now leads with 4 flagships, then full suite.
2. **Sports apps** can look like hobbies unless framed as decision systems (Decision Score, live ops, matchup intelligence).
3. **Command Center alone** looks like a launcher — needs “suite platform” framing (now in copy).
4. **Future Lens** without “prototype” label looks like unverifiable forecasting.
5. **Teacher → analytics transition** needs one crisp sentence (now in About / LinkedIn).

---

## 7. Strongest areas

1. **Baseball Analytics** — deepest product surface + strongest “owns a real app” signal.
2. **Investment Explorer** — clearest quant/finance proof for analyst roles.
3. **AMI** — best AI Evaluator / decision-lab narrative.
4. **Suite integration** (Command Center + AMI handoffs) — rare for portfolio candidates.
5. **Credential stack** (M.A. Stats + MBA Finance + SOA exams) backing the apps.
6. **New screenshots** — current, feature-specific, recruiter-readable.

---

## 8. Highest-impact improvements (prioritized)

| Priority | Action | Why |
|----------|--------|-----|
| P0 | Deploy Portfolio Website + put URL on resume/LinkedIn/applications | Public link is the conversion asset |
| P0 | Add LinkedIn URL to `projects.json` → `site.linkedin` | Removes “coming soon” dead end |
| P1 | Capture 2–4 SQL/Excel screenshots | Unlocks Data Analyst / AI Evaluator spreadsheet proof |
| P1 | Update LinkedIn Featured with website + 3 heroes | 30-second recruiter path |
| P1 | Put Analytics & AI Portfolio Developer role above teaching on resume PDF | Fixes above-the-fold story |
| P2 | Trim/redirect empty hub folders or add index READMEs | Cleaner GitHub browsing |
| P2 | Spot-check all Streamlit apps load in Demo Mode | Avoid live-demo embarrassment |
| P3 | Light README screenshot path updates in app repos | Only where still saying “TODO screenshots” |

---

## Recruiter 30-second review (by project)

### Baseball Analytics
- **Stands out:** Decision Score recommendation cards; huge feature surface in sidebar.
- **Impressive:** Full draft → league ops product, not a chart page.
- **Unclear:** Could look “just fantasy” without the scoring/ops framing.
- **Emphasize more:** Decision systems, shared leagues, AMI handoff, test-backed logic.
- **Interview value:** **Yes — top interview generator** for product/analytics roles.

### Investment Explorer
- **Stands out:** Portfolio Health Score + plain-language what’s working/not.
- **Impressive:** Monte Carlo + frontier + ETF overlap on one engine.
- **Unclear:** Health score magnitude may look odd without methodology note.
- **Emphasize more:** Quant methods + beginner/advanced product design.
- **Interview value:** **Yes — top for DA / quant / finance roles.**

### AMI
- **Stands out:** Action-lab hub; cross-domain decision framing.
- **Impressive:** Simulation breadth + suite insight routing.
- **Unclear:** “Intelligence” name can sound like a chatbot.
- **Emphasize more:** Structured labs, interpretation layers, evaluator relevance.
- **Interview value:** **Yes — especially AI Evaluator / quant reasoning.**

### AI Music Practice Coach
- **Stands out:** Real studio UX (catalog → practice → backing → log).
- **Impressive:** Complex state + AI-assisted creative product.
- **Unclear:** Relevance to analytics jobs unless framed as product/AI systems.
- **Emphasize more:** Product design, persistence, AI-assisted workflows.
- **Interview value:** **Yes for product/AI builder roles; selective for pure finance.**

### Basketball Playoff Companion
- **Stands out:** Live game center + matchup boards + legacy tracker.
- **Impressive:** Live-data resilience and narrative product craft.
- **Unclear:** Single-team companion vs league analytics platform.
- **Emphasize more:** Live ingestion, trust/safe modes, matchup intelligence.
- **Interview value:** **Yes as supporting proof of live-data product skill.**

### Future Lens
- **Stands out:** Clean Domain→Skill IA and 2050 scenario framing.
- **Impressive:** Turns vague AI-future talk into a navigable tool.
- **Unclear:** Whether forecasts are rigorous (they are curated Phase 1).
- **Emphasize more:** Taxonomy design + prototype honesty.
- **Interview value:** **Yes for AI narrative / evaluator conversations; not a lead technical project.**

### AI Command Center
- **Stands out:** Continue-where-you-left-off across apps.
- **Impressive:** Platform/ecosystem thinking.
- **Unclear:** Looks like a homepage without suite context.
- **Emphasize more:** Activity schema, deep links, multi-app ownership.
- **Interview value:** **Yes as proof you build systems, not isolated demos.**

---

## NBA + Future Lens placement decision

| Project | Website placement | Lead in applications? |
|---------|-------------------|------------------------|
| Basketball Playoff Companion | Full suite + category Applications/Analytics; featured=true; tier 2 | Support — lead only for sports/product storytelling |
| Future Lens | Full suite + AI category; tier 2; prototype status explicit | Support — lead for AI Evaluator / strategy narrative |

Both are now first-class on the portfolio website with galleries and accurate copy.

---

## How to preview Priority 1 locally

```powershell
cd "Portfolio Website"
python -m http.server 9890
```

Open http://127.0.0.1:9890/

Confirm heroes load for Baseball, Investment, AMI, Music, and that Full Suite shows Basketball Companion, Future Lens, and Command Center.
