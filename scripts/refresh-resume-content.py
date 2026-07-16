#!/usr/bin/env python3
"""Refresh resume section in projects.json for PDF + website resume pages."""

from __future__ import annotations

import json
from pathlib import Path

PROJECTS = Path(__file__).resolve().parent.parent / "Portfolio Website" / "data" / "projects.json"
DOCS_COPY = (
    Path(__file__).resolve().parent.parent
    / "Portfolio Website"
    / "assets"
    / "docs"
    / "resume-project-descriptions.md"
)
RESUME_MD = Path(__file__).resolve().parent.parent / "Resume" / "resume-project-descriptions.md"


def main() -> int:
    data = json.loads(PROJECTS.read_text(encoding="utf-8"))
    site = data["site"]
    linkedin = site.get("linkedin") or ""

    data["resume"]["headline"] = (
        "Mathematics & Statistics Professional · Quantitative Analytics · AI Decision-Support Applications"
    )
    data["resume"]["summary"] = (
        "Mathematics and Statistics professional with an M.A. in Statistics & Applied Mathematics (GPA 3.93), "
        "MBA in Finance & Investments (Finance GPA 4.00), actuarial exam foundation (SOA P, FM, MFE), and a "
        "deployed seven-app analytics portfolio. Builds decision-support products in Python/Streamlit spanning "
        "portfolio risk, sports analytics, simulation labs, and AI evaluation — with SQL/Excel reporting fluency "
        "and end-to-end ownership from data through deployment."
    )

    # Ensure Portfolio Developer is first and uses refreshed bullets
    portfolio_exp = {
        "title": "Analytics & AI Portfolio Developer",
        "organization": "Independent — Daniel AI Suite",
        "period": "2024 — Present",
        "bullets": [
            "Designed, built, and deployed seven interconnected Streamlit applications for portfolio analytics, fantasy baseball operations, applied math decision labs, playoff intelligence, music practice tooling, AI transition scenarios, and suite orchestration",
            "Implemented decision scoring, portfolio health diagnostics, Monte Carlo and efficient frontier modeling, live-data fallbacks, and cross-app resume/insight workflows with Supabase-backed persistence patterns",
            "Authored SQL & Excel analytics workbooks with KPI dashboards, pivot exercises, and 42+ structured queries including AI evaluator practice datasets",
        ],
    }
    other = [e for e in data["resume"]["experience"] if e.get("title") != "Analytics & AI Portfolio Developer"]
    # Keep teaching entries but compress first teaching role bullets already present
    data["resume"]["experience"] = [portfolio_exp] + other

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

    data["resume"]["technicalSkills"] = [
        "Statistics",
        "Probability",
        "Hypothesis Testing",
        "Python",
        "SQL",
        "Excel",
        "Pivot Tables",
        "Pandas",
        "Streamlit",
        "Data Visualization",
        "Machine Learning",
        "Monte Carlo Simulation",
        "Portfolio Optimization",
        "Financial Analysis",
        "Dashboard Development",
        "AI Evaluation",
        "Product Analytics",
        "Git / GitHub",
        "AI-Assisted Development",
        "Decision Support Systems",
    ]
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

    # Contact lines for resume pages / PDF helpers
    data["site"]["linkedin"] = linkedin or site.get("linkedin")
    PROJECTS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    # Keep bundled docs copy in sync with Resume markdown if present
    if RESUME_MD.exists():
        DOCS_COPY.write_text(RESUME_MD.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Synced {DOCS_COPY}")

    print(f"Updated resume content in {PROJECTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
