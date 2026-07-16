#!/usr/bin/env python3
"""Refresh Portfolio Website projects.json copy for recruiter impact (2026-07-15)."""

from __future__ import annotations

import json
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
PROJECTS = HUB / "Portfolio Website" / "data" / "projects.json"
STAGING = HUB / "Screenshots"


HERO_OVERRIDES = {
    "Investment": "01-portfolio-health.png",
    "Baseball": "01-draft-assistant-recommendations.png",
    "Applied-Math": "01-home-dashboard.png",
    "NBA": "01-home-dashboard.png",
    "Music": "02-practice-control-center.png",
    "Command-Center": "homepage-continue.png",
    "Future-Lens": "01-domain-wizard.png",
}


def shots(folder: str) -> tuple[str, list[str], list[str]]:
    files = sorted((STAGING / folder).glob("*.png"), key=lambda p: p.name.lower())
    if not files:
        return "", [], []
    preferred = HERO_OVERRIDES.get(folder)
    if preferred:
        files = sorted(files, key=lambda p: (0 if p.name == preferred else 1, p.name.lower()))
    paths = [f"assets/screenshots/{folder}/{f.name}" for f in files]
    checklist = [
        f"{f.name} — {f.stem.lstrip('0123456789-').replace('-', ' ').title()}" for f in files
    ]
    return files[0].name, paths, checklist


def main() -> int:
    data = json.loads(PROJECTS.read_text(encoding="utf-8"))

    data["site"]["title"] = "Daniel Cohen — Analytics, Quantitative Modeling & AI Portfolio"
    data["site"]["tagline"] = "Decision-support applications · Statistics · Finance · SQL · AI-assisted product development"

    data["summary"] = {
        "headline": "Mathematics & Statistics Professional — Analytics, Quant Modeling & AI Applications",
        "paragraphs": [
            "M.A. Statistics & Applied Mathematics (Hunter, 3.93 GPA) · MBA Finance & Investments (Baruch, Finance GPA 4.00) · SOA Exams P, FM, MFE · B.A. Mathematics & Economics, Magna Cum Laude.",
            "I design and ship end-to-end analytics products — seven interconnected Streamlit applications plus SQL/Excel workbooks — that turn probability, risk, and modeling into decision-ready tools recruiters can click through in minutes.",
            "Target roles: Data Analyst · Product Analyst · Quantitative Analyst · Financial Analyst · AI Evaluator · AI Trainer · BI / Research Analyst.",
        ],
        "skills": [
            "Python", "SQL", "Excel", "Pandas", "Streamlit", "Statistics",
            "Monte Carlo", "Portfolio Optimization", "Machine Learning",
            "Data Visualization", "AI Evaluation", "Decision Support",
            "Product Analytics", "Git / GitHub", "AI-Assisted Development",
        ],
    }

    data["aboutMe"] = {
        "headline": "Mathematics & Statistics Professional · Quantitative Analytics · AI-Assisted Product Development",
        "subheadline": "M.A. Statistics · MBA Finance · SOA Exams (P, FM, MFE) · Python · SQL · Excel · Streamlit · End-to-End Ownership",
        "paragraphs": [
            "I am a Mathematics and Statistics professional who builds production analytics applications — not notebook demos. Graduate training in statistics and finance, actuarial exam foundation, and a seven-app product suite demonstrate how I turn quantitative methods into usable decision-support systems.",
            "The Daniel AI Suite spans investment risk analytics, fantasy baseball decision engines, applied math labs, NBA playoff intelligence, music practice tooling, AI transition scenario modeling, and a cross-app Command Center. Each app is designed for real workflows: explore → analyze → decide → continue.",
            "I use AI-assisted development to move faster while owning architecture, analytics design, UX, testing, and deployment end to end.",
        ],
        "pillars": [
            {
                "title": "Analytical Thinking",
                "text": "Hypothesis testing, probability, Monte Carlo, optimization, and model interpretation across finance and sports products.",
            },
            {
                "title": "Product & Decision Support",
                "text": "Workflow-first apps with scoring engines, health diagnostics, draft rooms, and plain-language coaching — not chart galleries.",
            },
            {
                "title": "AI-Assisted Development",
                "text": "Shipped a multi-app suite with shared persistence, insight handoffs, and evaluator-style workflows using modern AI tooling.",
            },
            {
                "title": "End-to-End Ownership",
                "text": "From data ingestion and modeling through Streamlit UX, Supabase schemas, pytest coverage, and live deployment.",
            },
        ],
    }

    data["featuredAnalytics"] = [
        {
            "icon": "📈",
            "title": "Portfolio Risk & Optimization",
            "text": "Sharpe/Sortino health scoring, efficient frontier, Monte Carlo paths, and ETF overlap diagnostics.",
        },
        {
            "icon": "⚾",
            "title": "Decision Scoring Systems",
            "text": "Fantasy draft Decision Score combining market rank, roster fit, scarcity, and model projections.",
        },
        {
            "icon": "🤖",
            "title": "AI & Model Interpretation",
            "text": "AMI labs for EV, overfitting, simulation, plus AI evaluator workbook workflows.",
        },
        {
            "icon": "🎲",
            "title": "Probability & Forecasting",
            "text": "Series win probability, playoff forecasting, and scenario timelines through 2050.",
        },
        {
            "icon": "🔗",
            "title": "Cross-App Product Design",
            "text": "Command Center resume flows and AMI insight handoffs across the suite.",
        },
        {
            "icon": "🖥️",
            "title": "Interactive Dashboards",
            "text": "Seven live Streamlit apps with demo modes, galleries, and recruiter-ready walkthroughs.",
        },
        {
            "icon": "📊",
            "title": "SQL · Excel · Reporting",
            "text": "KPI dashboards, pivot practice, and 42+ SQL queries spanning AI eval, finance, and risk.",
        },
    ]

    data["flagshipIds"] = [
        "baseball-stat-app",
        "investment-portfolio-analyzer",
        "applied-mathematical-intelligence",
        "ai-music-practice-coach",
    ]

    # Career / executive / resume targeting updates
    data["resume"]["targetRoles"] = [
        "Data Analyst",
        "Product Analyst",
        "AI Evaluator",
        "AI Trainer",
        "Business Intelligence Analyst",
        "Research Analyst",
        "Junior Data Scientist",
        "Quantitative Analyst",
        "Financial Analyst",
    ]
    data["careerProfile"]["sections"]["targetRoles"]["roles"] = [
        {
            "role": "Data Analyst",
            "fit": "M.A. Statistics, SQL/Excel workbooks, and live Python dashboards for reporting and interpretation.",
        },
        {
            "role": "Product Analyst",
            "fit": "Shipped multi-page products with workflow metrics, user-facing decision scores, and suite-level activity design.",
        },
        {
            "role": "AI Evaluator",
            "fit": "AI evaluator workbook, AMI training/overfitting labs, and structured evidence-based analysis workflows.",
        },
        {
            "role": "AI Trainer",
            "fit": "Years of quantitative instruction plus UX designed to explain → simulate → interpret complex methods.",
        },
        {
            "role": "Quantitative Analyst",
            "fit": "Actuarial exam foundation, MBA finance, Monte Carlo, portfolio optimization, and risk analytics.",
        },
        {
            "role": "Financial Analyst",
            "fit": "MBA Finance (4.00), investment health scoring, efficient frontier, and ETF holdings diagnostics.",
        },
        {
            "role": "Business Intelligence Analyst",
            "fit": "KPI dashboards, Excel pivot fluency, executive case studies, and demo-ready Streamlit walkthroughs.",
        },
        {
            "role": "Junior Data Scientist",
            "fit": "ML projections, feature importance, optimization, and model validation-oriented portfolio evidence.",
        },
    ]
    data["careerProfile"]["sections"]["portfolioHighlights"]["items"] = [
        {
            "title": "Baseball Analytics",
            "text": "Full-season fantasy platform — Decision Score drafts, shared leagues, lineup/trade ops, AMI insight handoff.",
        },
        {
            "title": "Investment Explorer",
            "text": "Live portfolio health, Monte Carlo, efficient frontier, ETF overlap, beginner/advanced modes.",
        },
        {
            "title": "Applied Mathematical Intelligence",
            "text": "Multi-lab decision engine for EV, prediction, disease models, AI training, and cross-app insight routing.",
        },
        {
            "title": "AI Music Practice Coach",
            "text": "Song-aware practice studio with backing tracks, progression builder, and practice intelligence.",
        },
        {
            "title": "Basketball Playoff Companion",
            "text": "Live games, bracket, matchup intelligence, and legacy tracking for a fan-first playoff product.",
        },
        {
            "title": "Future Lens + Command Center",
            "text": "AI transition scenarios through 2050 and suite-level resume/activity orchestration.",
        },
    ]

    data["executiveSummaryDoc"]["keyStrengths"] = [
        "M.A. Statistics & Applied Mathematics (Hunter, GPA 3.93) and MBA Finance & Investments (Baruch, Finance GPA 4.00)",
        "Society of Actuaries exams P/1, FM/2, and MFE — probability and financial mathematics foundation",
        "Seven live Streamlit applications forming an interconnected analytics product suite",
        "End-to-end ownership: data, modeling, UX, persistence, testing, and deployment",
        "AI-assisted development used to ship substantial applications with decision-support design",
        "SQL & Excel workbooks with KPI dashboards and 42+ structured queries including AI evaluation",
    ]
    data["executiveSummaryDoc"]["analyticsProjects"]["items"] = [
        "Portfolio health scoring, efficient frontier, Monte Carlo, ETF overlap (Investment Explorer)",
        "Decision Score draft engine, shared leagues, lineup/trade workflows (Baseball Analytics)",
        "EV, sports prediction, disease modeling, AI training labs (Applied Mathematical Intelligence)",
        "Live playoff command center with matchup and legacy analytics (Basketball Playoff Companion)",
        "SQL & Excel workbooks with KPI dashboards, pivot exercises, and AI evaluator practice",
    ]
    data["executiveSummaryDoc"]["aiRelatedWork"]["items"] = [
        "AI Evaluator & Analytics workbook — prompt rating, pairwise comparison, hallucination KPIs",
        "AMI Train-an-AI / overfitting visualization and cross-app analytical insight handoffs",
        "AI Music Practice Coach — adaptive practice tooling and optional OpenAI coaching hub",
        "Future Lens — taxonomy-driven AI transition scenarios through 2050",
        "Command Center — suite activity, coach insights, and resume/continue orchestration",
    ]
    data["executiveSummaryDoc"]["careerDirection"][
        "text"
    ] = "Daniel is targeting Data Analyst, Product Analyst, AI Evaluator, AI Trainer, BI Analyst, Research Analyst, Junior Data Scientist, Quantitative Analyst, and Financial Analyst roles. He offers credentialed statistics and finance training plus a deployed multi-app portfolio that proves independent product execution."

    # Per-repo refresh
    inv_hero, inv_shots, inv_check = shots("Investment")
    bb_hero, bb_shots, bb_check = shots("Baseball")
    ami_hero, ami_shots, ami_check = shots("Applied-Math")
    nba_hero, nba_shots, nba_check = shots("NBA")
    mus_hero, mus_shots, mus_check = shots("Music")
    cc_hero, cc_shots, cc_check = shots("Command-Center")
    fl_hero, fl_shots, fl_check = shots("Future-Lens")

    updates = {
        "investment-portfolio-analyzer": {
            "name": "Investment Portfolio Analyzer",
            "displayName": "Investment Explorer",
            "oneLiner": "Live-market portfolio analytics with health scoring, Monte Carlo, efficient frontier, and ETF overlap.",
            "liveUrl": "https://investment-portfolio-analyzer-ty2sbzumvxsqwbqhkvf6rz.streamlit.app",
            "featured": True,
            "tier": 1,
            "category": "analytics",
            "secondaryCategories": ["ai"],
            "status": "Active / Production-ready",
            "readiness": 9.0,
            "purpose": "Streamlit investment analytics product with beginner and advanced modes, live Yahoo Finance data, portfolio health diagnostics, Monte Carlo, efficient frontier optimization, ETF holdings overlap, and AMI insight handoff.",
            "executiveSummary": "Built a production investment analytics product that turns live market data into portfolio health scores, risk diagnostics, Monte Carlo scenarios, efficient-frontier optimization, and ETF overlap analysis — with beginner coaching and advanced quant workflows on the same engine.",
            "businessValue": "Makes institutional-style risk and allocation analysis usable for education and decision support without a Bloomberg terminal.",
            "recruiterTakeaway": "End-to-end quant product: live data, analytics core separated from UI, dual-audience UX, and AI insight routing.",
            "keyFeatures": [
                "Portfolio Health Score with plain-language what's working / not working",
                "Live Yahoo Finance ingestion and refreshable holdings",
                "Monte Carlo scenarios (P(loss), growth distributions)",
                "Efficient frontier optimizer (max Sharpe / min volatility)",
                "ETF Holdings Explorer for overlap and concentration",
                "Beginner Mode coaching + Advanced analytics tabs",
                "Applied Investment Insight → AMI handoff",
            ],
            "detailHighlights": [
                "Health scoring that translates risk metrics into actionable coaching",
                "Monte Carlo and efficient frontier on a shared analytics core",
                "ETF overlap diagnostics beyond ticker-level pie charts",
            ],
            "detailSections": [
                {
                    "title": "Portfolio Health",
                    "body": "Composite health score across return, risk, diversification, objective alignment, and macro fit — with explicit strengths and failure modes for the current mix.",
                },
                {
                    "title": "Risk & Allocation Modeling",
                    "body": "Correlation, contribution, drawdown, efficient frontier, and Monte Carlo paths support allocation trade-off analysis.",
                },
                {
                    "title": "ETF Holdings Intelligence",
                    "body": "Holdings-level overlap and concentration views help users see hidden redundancy inside ETF sleeves.",
                },
                {
                    "title": "Product Design",
                    "body": "Beginner and Advanced modes share one analytics engine so education and deeper quant work stay consistent.",
                },
            ],
            "caseStudy": {
                "problem": "Investors need accessible risk-adjusted analytics without institutional terminals or spreadsheet-only workflows.",
                "data": "Live equity/ETF prices via yfinance; user-defined holdings and benchmark returns.",
                "analysis": "Return/risk metrics, concentration flags, correlation structure, and health diagnostics.",
                "modeling": "Monte Carlo simulation, mean-variance optimization, and efficient frontier construction.",
                "insights": "Rule-based coaching and AMI handoff translate metrics into next questions and actions.",
                "results": "A live Streamlit product with dual UX modes and suite-integrated insight routing.",
            },
            "skills": [
                "Quantitative finance",
                "Risk modeling",
                "Monte Carlo simulation",
                "Portfolio optimization",
                "Product analytics UX",
                "API integration",
            ],
            "screenshotFolder": "Investment",
            "heroScreenshot": inv_hero,
            "screenshots": inv_shots,
            "screenshotChecklist": inv_check,
            "readmeStatus": "Strong — screenshots refreshed 2026-07-15; keep live URL and feature list current.",
        },
        "baseball-stat-app": {
            "name": "Baseball Stat App",
            "displayName": "Baseball Analytics",
            "oneLiner": "Full-season fantasy baseball platform: Decision Score drafts, shared leagues, lineup/trade ops, and research tools.",
            "liveUrl": "https://baseball-stat-app-d4jlymjc4iptaadc3kquwx.streamlit.app",
            "featured": True,
            "tier": 1,
            "category": "analytics",
            "secondaryCategories": ["applications"],
            "status": "Active / Evolving portfolio product",
            "readiness": 9.0,
            "purpose": "MLB analytics and fantasy baseball decision platform spanning historical exploration, ML projections, draft simulation, live draft rooms, shared leagues, lineup management, trade center, and AMI insight handoff.",
            "executiveSummary": "Developed a full-season fantasy baseball product with Decision Score draft recommendations, live/multiplayer draft rooms, uploaded draft import, shared league claims, lineup and trade workflows, research comparison, HOF case mode, and Baseball Insight → AMI handoff.",
            "businessValue": "Shows how to turn sports data into an operational decision system — not a static leaderboard.",
            "recruiterTakeaway": "Substantial product ownership: scoring engine, multiplayer workflows, in-season ops, and AI insight integration.",
            "keyFeatures": [
                "Draft Assistant with Decision Score / roster-fit recommendations",
                "Live Draft Room (solo + room-code multiplayer)",
                "Uploaded draft CSV/XLSX import",
                "Shared league invites and team claims",
                "Lineup management and Trade Center",
                "Research Mode player comparison",
                "HOF Case Mode and historical MLB exploration",
                "Baseball Insight → AMI analytical handoff",
            ],
            "detailHighlights": [
                "Decision Score separates market rank from model/roster-fit value",
                "Draft → season ops continuum (lineups, waivers, trades)",
                "Shared leagues and draft import for real-league workflows",
            ],
            "detailSections": [
                {
                    "title": "Draft Intelligence",
                    "body": "Draft Assistant and Live Draft Room combine Decision Score, roster fit, and market/model rank so picks are explained, not just listed.",
                },
                {
                    "title": "League Operations",
                    "body": "Uploaded draft import, shared league claims, lineup management, and Trade Center support post-draft season management.",
                },
                {
                    "title": "Research & History",
                    "body": "Research Mode comparisons and HOF Case Mode extend the product beyond fantasy into analytical storytelling.",
                },
                {
                    "title": "Suite Integration",
                    "body": "Baseball Insight routes analytical questions into AMI while preserving baseball context for return.",
                },
            ],
            "caseStudy": {
                "problem": "Fantasy managers need rigorous, workflow-aware tools for draft and in-season decisions — not disconnected stat tables.",
                "data": "Lahman historical database, market rankings, roster state, and derived projection features.",
                "analysis": "Trend, valuation, comparison, and significance-oriented research views.",
                "modeling": "ML-style projections and Decision Score blending market, scarcity, fit, and model signals.",
                "insights": "Recommendation cards explain team-fit vs raw-value tradeoffs at the moment of pick.",
                "results": "A multi-page product covering draft, league ops, research, and AI insight handoff.",
            },
            "skills": [
                "Sports analytics",
                "Decision scoring systems",
                "Statistical research UX",
                "Multiplayer workflow design",
                "Interactive dashboards",
                "Test-backed product logic",
            ],
            "screenshotFolder": "Baseball",
            "heroScreenshot": bb_hero,
            "screenshots": bb_shots,
            "screenshotChecklist": bb_check,
            "readmeStatus": "Feature-rich README; screenshots refreshed 2026-07-15 to match current draft/league ops surface.",
        },
        "applied-mathematical-intelligence": {
            "name": "Applied Mathematical Intelligence",
            "displayName": "Applied Mathematical Intelligence (AMI)",
            "oneLiner": "Multi-domain decision engine: solve problems, predict games, explore math ideas, and route insights across the suite.",
            "liveUrl": "https://applied-mathematical-intelligence-8l8bqrzpp6fghaj7xuig53.streamlit.app",
            "featured": True,
            "tier": 1,
            "category": "analytics",
            "secondaryCategories": ["ai"],
            "status": "Active / v3.6.1 feature-complete",
            "readiness": 9.0,
            "purpose": "Mathematical Thinking Lab and decision engine with action labs spanning problem solving, prediction, betting EV, disease modeling, AI training visualization, optimization, and cross-app insight routing.",
            "executiveSummary": "Designed Applied Mathematical Intelligence as a modular decision engine — action labs for solving problems, predicting games, exploring math ideas, modeling disease, training AI intuition, and optimizing decisions — with Command Center routing and insight return into sibling apps.",
            "businessValue": "Turns quantitative methods into interactive, interpretable decision tools for non-specialists and analysts alike.",
            "recruiterTakeaway": "Strong AI-evaluator / quant signal: structured labs, simulation engines, and suite-wide analytical handoffs.",
            "keyFeatures": [
                "Home dashboard of action-oriented math labs",
                "Solve a Problem structured decision workflow",
                "Predict a Game probability vs market framing",
                "Explore a Math Idea interactive explanations",
                "Betting EV, disease modeling, AI training, optimization labs",
                "23+ simulation engines and advanced reference domains",
                "Cross-app insight routing via Command Center",
            ],
            "detailHighlights": [
                "Pedagogical pattern: explain → simulate → interpret → math depth",
                "Suite-integrated analytical questions with return context",
                "Broad simulation registry across finance, sports, and systems",
            ],
            "detailSections": [
                {
                    "title": "Action Labs",
                    "body": "Primary labs focus on real decisions — solve, predict, explore — before deeper math reference material.",
                },
                {
                    "title": "Simulation Engines",
                    "body": "Reusable engines cover EV, epidemic curves, optimization tradeoffs, and AI training dynamics.",
                },
                {
                    "title": "Suite Intelligence",
                    "body": "AMI receives context from Baseball, Investment, and Music and can return structured insight paths through Command Center.",
                },
            ],
            "caseStudy": {
                "problem": "Quantitative methods are often trapped in lectures or notebooks instead of decision workflows.",
                "data": "Curated lab scenarios, simulation parameters, and cross-app analytical context.",
                "analysis": "Structured what/why/run/read/math loops for each lab.",
                "modeling": "EV, SIR, optimization, and training-curve engines with interpretable outputs.",
                "insights": "Plain-language interpretation layers keep math actionable.",
                "results": "A flagship lab product that also powers suite-wide insight handoffs.",
            },
            "skills": [
                "Applied statistics",
                "Simulation design",
                "Decision support",
                "AI interpretation UX",
                "Modular architecture",
            ],
            "technologies": ["Python", "Streamlit", "matplotlib", "pandas", "numpy", "Supabase"],
            "screenshotFolder": "Applied-Math",
            "heroScreenshot": ami_hero,
            "screenshots": ami_shots,
            "screenshotChecklist": ami_check,
            "readmeStatus": "Strong README; version and screenshots aligned to current AMI surface (2026-07-15).",
        },
        "nba-playoff-companion-ai": {
            "name": "NBA Playoff Companion AI",
            "displayName": "Basketball Playoff Companion",
            "oneLiner": "Fan-first 2026 playoff command center: live games, bracket, matchup intelligence, and legacy tracking.",
            "liveUrl": "https://nba-playoff-companion-ai-gd4sx677quejdfkvappv6o.streamlit.app",
            "featured": True,
            "tier": 2,
            "category": "applications",
            "secondaryCategories": ["analytics"],
            "status": "Active — 2026 playoff product",
            "readiness": 8.0,
            "purpose": "Single-team NBA playoff companion with home command center, live game center, bracket, matchup intelligence, player tracker, and legacy scoring.",
            "executiveSummary": "Built a fan-first Basketball Playoff Companion with live scoreboard resilience, playoff bracket context, matchup intelligence boards, and legacy tracking — designed as a narrative command center rather than a generic stats dump.",
            "businessValue": "Demonstrates live-data product craft: trust banners, fallbacks, and story-driven analytics for a high-interest domain.",
            "recruiterTakeaway": "Strong product analytics signal — live ingestion, matchup boards, and legacy scenario storytelling.",
            "keyFeatures": [
                "Home playoff dashboard with series outlook",
                "Live Game Center with CDN scoreboard fallbacks",
                "Playoff Bracket navigation",
                "Matchup Intelligence boards",
                "Legacy Tracker with path comparisons",
                "Player playoff story continuity into offseason modes",
            ],
            "detailHighlights": [
                "Live sports ingestion with honest safe-mode messaging",
                "Matchup intelligence beyond box scores",
                "Legacy path charts for playoff narrative analysis",
            ],
            "detailSections": [
                {
                    "title": "Live Playoff Command Center",
                    "body": "Home and Live Game Center keep series context, scoreboard state, and team outlook in one fan workflow.",
                },
                {
                    "title": "Matchup Intelligence",
                    "body": "Lineup and tactical boards connect roster construction to playoff storylines.",
                },
                {
                    "title": "Legacy Tracking",
                    "body": "Legacy ladders and path charts quantify how a playoff run changes a player's franchise narrative.",
                },
            ],
            "caseStudy": {
                "problem": "Playoff fans need one place for live context, matchups, and forward-looking player impact — not scattered box scores.",
                "data": "NBA API / CDN scoreboard feeds, curated bracket snapshots, and player/team metadata.",
                "analysis": "Series outlook, matchup pulse, and round-by-round context cards.",
                "modeling": "Legacy scoring with comparative path visualization.",
                "insights": "Trust-aware live modes clarify when data is current vs demo/safe.",
                "results": "A multi-page sports product with durable offseason continuity.",
            },
            "skills": [
                "Live data integration",
                "Sports analytics",
                "Narrative product UX",
                "Resilient API design",
            ],
            "screenshotFolder": "NBA",
            "heroScreenshot": nba_hero,
            "screenshots": nba_shots,
            "screenshotChecklist": nba_check,
            "readmeStatus": "Good docs; screenshots refreshed 2026-07-15.",
        },
        "ai-music-practice-coach": {
            "name": "AI Music Practice Coach",
            "displayName": "AI Music Practice Coach",
            "oneLiner": "Song-aware practice studio with catalog, control center, backing tracks, creative labs, and practice logging.",
            "liveUrl": "https://ai-music-practice-coach-6szqxqxqrqxdmryyewk8sq.streamlit.app",
            "featured": True,
            "tier": 2,
            "category": "applications",
            "secondaryCategories": ["ai"],
            "status": "Active / mature WIP",
            "readiness": 8.5,
            "purpose": "AI-powered music practice studio with curated song catalog, practice control center, backing track generation, creative lab, custom progression builder, and practice log.",
            "executiveSummary": "Created an AI Music Practice Coach that keeps an active song context across catalog, practice control center, backing studio, creative lab, custom progression builder, and practice logging — a complex product surface combining music theory, audio tooling, and AI-assisted workflows.",
            "businessValue": "Shows rare ability to ship domain-specific AI-assisted products with coherent cross-page state.",
            "recruiterTakeaway": "AI product design beyond chatbots — adaptive practice workflows with real studio tooling.",
            "keyFeatures": [
                "Curated multi-genre song catalog",
                "Practice Control Center for section-focused work",
                "Backing Track Studio with groove/BPM controls",
                "Creative Lab improvisation tools",
                "Custom Progression Builder",
                "Practice Log for session continuity",
                "Optional OpenAI coaching hub + AMI handoff",
            ],
            "detailHighlights": [
                "Unified active-song state across studio pages",
                "Backing generation aligned to chart harmony",
                "Practice logging for habit and progress loops",
            ],
            "detailSections": [
                {
                    "title": "Practice Intelligence",
                    "body": "Control Center focuses practice on song sections, keys, and instrument context instead of static PDFs.",
                },
                {
                    "title": "Studio Tools",
                    "body": "Backing Studio, Creative Lab, and Progression Builder support creation as well as repetition.",
                },
                {
                    "title": "Learning Continuity",
                    "body": "Practice Log and suite resume flows keep sessions recoverable across devices when cloud restore is enabled.",
                },
            ],
            "caseStudy": {
                "problem": "Musicians need adaptive, song-aware practice tools — not disconnected metronomes and PDFs.",
                "data": "Curated charts, user progressions, and session practice metadata.",
                "analysis": "Section-scoped practice recommendations and harmonic context.",
                "modeling": "Backing generation and progression construction tied to active song state.",
                "insights": "Practice log and coaching surfaces make next actions obvious.",
                "results": "A nine-page creative analytics studio with suite integration.",
            },
            "skills": [
                "AI-assisted product design",
                "Domain modeling",
                "Audio/practice tooling",
                "Complex UX state",
            ],
            "screenshotFolder": "Music",
            "heroScreenshot": mus_hero,
            "screenshots": mus_shots,
            "screenshotChecklist": mus_check,
            "readmeStatus": "README improved previously; screenshots refreshed 2026-07-15 to current studio pages.",
        },
        "future-lens-ai-transition-simulator": {
            "name": "Future Lens: AI Transition Simulator",
            "displayName": "Future Lens",
            "oneLiner": "Taxonomy-driven simulator exploring how skills evolve from 1980 to today and forward through 2050.",
            "liveUrl": "https://future-lens-ai-transition-simulator-m6n4kaku28ztzlxfts2xt6.streamlit.app",
            "featured": True,
            "tier": 2,
            "category": "ai",
            "secondaryCategories": [],
            "status": "Phase 1 prototype — demo narrative data",
            "readiness": 7.0,
            "purpose": "Explore how work, learning, creativity, sports, and investing evolved 1980→today and how AI may reshape skills through 2050 via domain→area→skill taxonomy.",
            "executiveSummary": "Prototyped Future Lens as a structured AI-transition simulator: domain wizard, evolution timelines, driver analysis, and 2050 scenario views that turn vague “future of work” talk into navigable skill-level exploration.",
            "businessValue": "Useful for strategy, workforce, and AI-impact conversations — frames uncertainty as explorable scenarios rather than hype.",
            "recruiterTakeaway": "Strong AI-evaluator / product-thinking signal: taxonomy design, scenario framing, and clear IA.",
            "keyFeatures": [
                "Domain → Area → Skill wizard across 11 domains",
                "Evolution timeline from 1980 through forecast decades",
                "Drivers view for forces shaping change",
                "Simulation views through 2050",
                "Workspace-scoped restore and Command Center deep links",
            ],
            "detailHighlights": [
                "Taxonomy-first information architecture",
                "Decade-bucketed narrative + forecast modes",
                "Suite activity integration despite prototype status",
            ],
            "detailSections": [
                {
                    "title": "Structured Exploration",
                    "body": "Users pick Domain → Area → Skill before reading evolution, drivers, advice, or simulation tabs.",
                },
                {
                    "title": "Scenario Thinking",
                    "body": "Timeline and 2050 views separate historical change from forward-looking narrative forecasts.",
                },
                {
                    "title": "Honest Scope",
                    "body": "Phase 1 uses curated demo narrative data — valuable for product framing, not claimed as precise forecasting.",
                },
            ],
            "caseStudy": {
                "problem": "AI impact discussions are usually vague slogans instead of skill-level exploration.",
                "data": "Curated taxonomy and decade narrative content across domains.",
                "analysis": "Drivers and evolution framing for each skill path.",
                "modeling": "Forward simulation tabs through 2050 scenario years.",
                "insights": "Users can compare human direction vs tools/methods by decade.",
                "results": "A clickable prototype that supports AI strategy and evaluator-style conversations.",
            },
            "skills": [
                "Scenario modeling",
                "Taxonomy design",
                "Narrative analytics",
                "Decision-support framing",
            ],
            "technologies": ["Python", "Streamlit", "Supabase"],
            "screenshotFolder": "Future-Lens",
            "heroScreenshot": fl_hero,
            "screenshots": fl_shots,
            "screenshotChecklist": fl_check,
            "readmeStatus": "Minimal README; portfolio site now carries accurate prototype framing and screenshots.",
        },
        "daniel-ai-command-center": {
            "name": "Daniel AI Command Center",
            "displayName": "AI Command Center",
            "oneLiner": "Suite homepage: continue workflows, coach insights, activity feed, and launchers for six apps.",
            "liveUrl": "https://daniel-ai-command-center-dexxnd7bf8jalxzqbyq55i.streamlit.app",
            "featured": True,
            "tier": 2,
            "category": "infrastructure",
            "secondaryCategories": ["ai"],
            "status": "Active — suite hub",
            "readiness": 8.0,
            "purpose": "Central hub for the Daniel AI Suite — continue/resume cards, coach insights, activity analytics, app directory, and deep links into sibling applications.",
            "executiveSummary": "Architected the AI Command Center as the suite’s product shell: resume where you left off across Music, Investment, Baseball, and more; coach activity insights; workspace profiles; and an app directory that treats the portfolio as one ecosystem.",
            "businessValue": "Proves platform thinking — shared activity schema, continuity UX, and cross-app navigation instead of isolated demos.",
            "recruiterTakeaway": "Platform / product analytics signal: multi-app orchestration, activity design, and user continuity.",
            "keyFeatures": [
                "Continue-where-you-left-off workflow cards",
                "App Directory launchers for suite apps",
                "Coach activity and weekly summary panels",
                "Workspace/account profile context",
                "Deep links into Music, Investment, Baseball, AMI, and more",
                "Supabase + local fallback persistence model",
            ],
            "detailHighlights": [
                "Separates resumable work from simple app launchers",
                "Cross-app activity makes the suite feel like one product",
                "Coach insights surface suite-level patterns",
            ],
            "detailSections": [
                {
                    "title": "Continuity UX",
                    "body": "Homepage Continue cards reconstruct active practice, portfolio, and analytics work from suite activity.",
                },
                {
                    "title": "Ecosystem Shell",
                    "body": "App Directory and deep links keep six applications one click from a shared home.",
                },
                {
                    "title": "Activity Intelligence",
                    "body": "Coach activity views summarize recent work across the suite for reflection and next steps.",
                },
            ],
            "caseStudy": {
                "problem": "A multi-app portfolio becomes fragmented without a shared home for resume state and activity.",
                "data": "Cross-app activity events, resume items, and workspace profiles.",
                "analysis": "Inferred active projects and coach insight summaries.",
                "modeling": "Typed deep-link contracts into sibling apps.",
                "insights": "Continue cards make prior work recoverable in one place.",
                "results": "A suite hub that elevates the portfolio from apps to platform.",
            },
            "skills": [
                "Platform architecture",
                "Activity analytics",
                "Cross-app integration",
                "Product systems design",
            ],
            "screenshotFolder": "Command-Center",
            "heroScreenshot": cc_hero,
            "screenshots": cc_shots,
            "screenshotChecklist": cc_check,
            "readmeStatus": "Functional README; screenshots now document Continue, directory, coach, and workspace views.",
        },
    }

    for repo in data["repos"]:
        patch = updates.get(repo["id"])
        if not patch:
            continue
        repo.update(patch)

    # Resume project bullets refresh
    data["resume"]["projectBullets"] = [
        {
            "name": "Baseball Analytics",
            "tech": "Python · Streamlit · scikit-learn",
            "bullets": [
                "Built full-season fantasy platform with Decision Score drafts, live draft rooms, shared leagues, and lineup/trade workflows",
                "Integrated research tools and AMI insight handoff for analytical follow-up questions",
            ],
        },
        {
            "name": "Investment Explorer",
            "tech": "Python · Streamlit · yfinance",
            "bullets": [
                "Shipped live portfolio health scoring, Monte Carlo, efficient frontier, and ETF overlap diagnostics",
                "Designed beginner/advanced modes on a shared analytics core; deployed on Streamlit Cloud",
            ],
        },
        {
            "name": "Applied Mathematical Intelligence",
            "tech": "Python · Streamlit",
            "bullets": [
                "Built modular decision labs for EV, prediction, disease modeling, and AI training interpretation",
                "Routed analytical questions across the suite via Command Center insight handoffs",
            ],
        },
        {
            "name": "SQL & Excel Analytics Workbooks",
            "tech": "Excel · SQL · pandas",
            "bullets": [
                "Created AI evaluator, investment, quant, and credit-risk workbooks with KPI dashboards and SQL practice",
                "Demonstrates fluency across Python products and spreadsheet-based business reporting",
            ],
        },
    ]

    PROJECTS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {PROJECTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
