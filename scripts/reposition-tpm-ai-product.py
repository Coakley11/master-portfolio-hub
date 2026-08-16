#!/usr/bin/env python3
"""One-shot repositioning: Technical Product / AI Product as primary career story."""

from __future__ import annotations

import json
from pathlib import Path

PROJECTS = Path(__file__).resolve().parent.parent / "Portfolio Website" / "data" / "projects.json"


def main() -> int:
    data = json.loads(PROJECTS.read_text(encoding="utf-8"))

    # --- Site / hero ---
    data["site"]["title"] = "Daniel Cohen — AI & Technical Product"
    data["site"]["tagline"] = (
        "Product Strategy · Technical Systems · AI-Enabled Products · Fully Remote U.S."
    )
    # Keep existing PDF as fallback; dedicated TPM / AI PM PDFs can be dropped in later
    data["site"]["resumePdf"] = "assets/docs/daniel-cohen-resume.pdf"
    data["site"]["resumeDownload"] = "assets/docs/daniel-cohen-resume.pdf"
    data["site"]["resumeTechnicalProduct"] = "assets/docs/daniel-cohen-resume.pdf"
    data["site"]["resumeAiProduct"] = "assets/docs/daniel-cohen-resume.pdf"
    data["site"]["resumeTechnicalProductLabel"] = "Technical Product Manager Resume"
    data["site"]["resumeAiProductLabel"] = "AI Product Manager Resume"
    data["site"]["resumeNote"] = (
        "Primary CTAs use the current portfolio resume PDF until dedicated "
        "Technical Product and AI Product resume files are added under assets/docs/."
    )

    # --- Resume section ---
    data["resume"]["headline"] = (
        "AI & Technical Product · Product Strategy · Technical Systems · AI-Enabled Products"
    )
    data["resume"]["summary"] = (
        "Mathematics and Statistics professional (M.A. Statistics & Applied Mathematics, GPA 3.93; "
        "MBA Finance & Investments, Finance GPA 4.00; SOA Exams P, FM, MFE) who owns product direction "
        "for a seven-app AI suite through independent portfolio ownership. Defines what products should do, "
        "translates goals into requirements and workflows, reasons through technical dependencies and system "
        "behavior, directs AI-assisted implementation, validates releases, diagnoses failures, and decides "
        "what happens next. Seeking fully remote U.S. roles as Technical Product Manager / AI Technical Product, "
        "AI Product Manager, and adjacent Technical Product Owner / Product Strategy positions. Quantitative "
        "analytics, SQL/Python, and AI evaluation strengthen that product work — they are not a separate career identity."
    )
    data["resume"]["experience"][0]["title"] = "Independent Product Owner — Daniel AI Suite"
    data["resume"]["experience"][0]["bullets"] = [
        "Owned product direction across seven interconnected Streamlit applications — problem framing, feature prioritization, requirements, acceptance criteria, workflow design, and release readiness",
        "Designed multi-page product systems with persistence, multi-user state, APIs, recommendation engines, and cross-app resume/insight orchestration (Supabase-backed patterns)",
        "Directed AI-assisted implementation while personally validating expected vs. actual behavior, diagnosing defects, prioritizing fixes, and regression-checking before release",
    ]
    data["resume"]["targetRoles"] = [
        "Technical Product Manager",
        "AI Technical Product",
        "AI Product Manager",
        "Technical Product Owner",
        "Product Strategy",
    ]
    data["resume"]["targetRoleGroups"] = [
        {
            "label": "Primary",
            "roles": ["Technical Product Manager", "AI Technical Product"],
        },
        {
            "label": "Secondary",
            "roles": ["AI Product Manager"],
        },
        {
            "label": "Adjacent",
            "roles": ["Technical Product Owner", "Product Strategy"],
        },
    ]
    data["resume"]["projectBullets"] = [
        {
            "name": "AI Music Practice Coach",
            "tech": "Python · Streamlit · OpenAI · Supabase",
            "bullets": [
                "Owned product direction for a multi-page practice studio: practice, creative, backing tracks, logging, AI coaching, persistence, and cross-page context",
                "Defined state ownership, acceptance criteria, and release readiness while directing AI-assisted implementation and regression checks",
            ],
        },
        {
            "name": "Baseball Analytics",
            "tech": "Python · Streamlit · scikit-learn · Supabase",
            "bullets": [
                "Designed shared leagues, live draft rooms, imports, lineup/trade workflows, and Decision Score recommendations as a multi-user product system",
                "Sequenced features for draft → season ops continuity; validated persistence, permissions, and collaborative behavior",
            ],
        },
        {
            "name": "AI Command Center + AMI",
            "tech": "Python · Streamlit · Supabase",
            "bullets": [
                "Architected suite orchestration: resumable workflows, context handoffs, activity continuity, and modular AI decision labs",
                "Routed users to the right tool and returned explainable analytical insights across sibling applications",
            ],
        },
        {
            "name": "Investment Explorer",
            "tech": "Python · Streamlit · yfinance",
            "bullets": [
                "Turned Monte Carlo, efficient frontier, and health scoring into adjustable, explainable decision workflows for beginners and advanced users",
                "Separated analytics core from UX so complex quant methods become product choices, not chart galleries",
            ],
        },
    ]
    data["resume"]["technicalSkills"] = [
        "Product Strategy",
        "Requirements",
        "Acceptance Criteria",
        "Workflow Architecture",
        "Feature Prioritization",
        "Release Readiness",
        "AI Feature Design",
        "AI Evaluation",
        "Python",
        "Streamlit",
        "SQL",
        "Excel",
        "Supabase",
        "APIs",
        "Git / GitHub",
        "Statistics",
        "Product Metrics",
        "Regression Testing",
        "AI-Assisted Development",
    ]

    # --- Career profile ---
    data["careerProfile"]["subtitle"] = (
        "Deliberate trajectory into AI & Technical Product ownership — "
        "product judgment, systems thinking, and quantitative depth · Fully remote U.S."
    )
    data["careerProfile"]["sections"]["professionalBackground"]["paragraphs"] = [
        "Daniel Cohen holds an M.A. in Statistics & Applied Mathematics (Hunter College, GPA 3.93), an MBA in Finance & Investments (Baruch College — Zicklin, Finance GPA 4.00), and a B.A. in Mathematics & Economics (Queens College — Magna Cum Laude). Society of Actuaries exams P/1, FM/2, and MFE ground his work in probability, financial mathematics, and risk thinking.",
        "Earlier career work in mathematics education — college lecturing, Business Statistics labs with Excel, and ongoing quantitative instruction — built durable strengths: explaining complexity, diagnosing where people get stuck, adapting to different users, structuring ambiguous material, and making rapid decisions under time pressure. Those strengths now transfer into product and systems ownership.",
    ]
    data["careerProfile"]["sections"]["analyticsAiTransition"] = {
        "title": "From Education Strengths to Product Ownership",
        "paragraphs": [
            "This is a deliberate career trajectory, not a random collection of AI or data projects. Teaching developed the ability to clarify goals, diagnose failure modes, and guide people through complex workflows. The Daniel AI Suite — seven deployed Streamlit applications plus SQL/Excel workbooks — moved those abilities into product ownership.",
            "Across the suite, Daniel decides what to build, defines product behavior, designs user workflows, specifies requirements and acceptance criteria, manages state and persistence decisions, directs AI-assisted implementation, tests expected vs. actual behavior, diagnoses defects, prioritizes fixes, and iterates based on observed usage. He has not held a formal employer Product Manager title; evidence is independent portfolio ownership of live systems.",
            "Quantitative analytics, statistics, Python/SQL, and AI evaluation remain strong supporting capabilities. They make him sharper at technical product work — they are not five equal career directions.",
        ],
    }
    data["careerProfile"]["sections"]["portfolioHighlights"]["items"] = [
        {
            "title": "AI Music Practice Coach (flagship)",
            "text": "Technical product ownership: multi-page workflows, state ownership, persistence, AI coaching, acceptance criteria, and release decisions.",
        },
        {
            "title": "Baseball Analytics",
            "text": "Multi-user product system: shared leagues, live draft, imports, permissions, lineup/trade ops, and recommendation sequencing.",
        },
        {
            "title": "Command Center + AMI",
            "text": "Product orchestration: resumable work, context handoffs, routing to the right tool, and modular AI decision support.",
        },
        {
            "title": "Investment Explorer",
            "text": "Decision-product design: complex analytics translated into adjustable, explainable user workflows.",
        },
        {
            "title": "Supporting suite",
            "text": "NBA Playoff Companion, Future Lens, and SQL/Excel workbooks remain available as depth — not competing primary identities.",
        },
    ]
    data["careerProfile"]["sections"]["coreTechnicalSkills"]["title"] = "Supporting Quantitative & Technical Foundation"
    data["careerProfile"]["sections"]["coreTechnicalSkills"]["skills"] = [
        "Statistics",
        "SQL",
        "Python",
        "Excel",
        "Pandas",
        "Streamlit",
        "Supabase",
        "APIs",
        "Git / GitHub",
        "Experimentation",
        "Product Metrics",
        "AI Evaluation",
        "Data Visualization",
        "Simulation",
        "Optimization",
    ]
    data["careerProfile"]["sections"]["targetRoles"] = {
        "title": "Target Roles",
        "intro": (
            "Fully remote U.S. Primary focus is Technical Product / AI Technical Product. "
            "Secondary: AI Product Manager. Adjacent: Technical Product Owner / Product Strategy. "
            "Evidence comes from independent portfolio ownership and AI-assisted product development — "
            "not a prior corporate PM title."
        ),
        "roles": [
            {
                "role": "PRIMARY — Technical Product Manager / AI Technical Product",
                "fit": "Owns product behavior, requirements, technical dependencies, state/persistence, acceptance criteria, defect triage, and release readiness across multi-page live systems (Music Coach, Baseball, Command Center).",
            },
            {
                "role": "SECONDARY — AI Product Manager",
                "fit": "Designs AI-enabled product surfaces: coaching workflows, evaluation criteria, human-in-the-loop validation, and AI-assisted prototyping with clear product ownership of outcomes.",
            },
            {
                "role": "ADJACENT — Technical Product Owner / Product Strategy",
                "fit": "Frames problems, prioritizes roadmaps, sequences features, and turns strategy into workflows recruiters can click through in the Daniel AI Suite.",
            },
        ],
    }

    # --- Executive summary ---
    data["executiveSummaryDoc"]["title"] = (
        "Why Daniel Cohen Fits AI & Technical Product Roles"
    )
    data["executiveSummaryDoc"]["subtitle"] = (
        "One coherent direction: product ownership of AI-enabled systems — fully remote U.S."
    )
    data["executiveSummaryDoc"]["keyStrengths"] = [
        "Primary target: Technical Product Manager / AI Technical Product (fully remote U.S.)",
        "Secondary: AI Product Manager · Adjacent: Technical Product Owner / Product Strategy",
        "Independent ownership of a seven-app suite: requirements, workflows, validation, release decisions",
        "Quantitative foundation (M.A. Statistics, MBA Finance, SOA exams) that strengthens technical product judgment",
        "AI-assisted development directed with personal ownership of acceptance criteria and regression checks",
        "Clear teaching → product trajectory: explaining complexity and diagnosing problems transferred into systems ownership",
    ]
    data["executiveSummaryDoc"]["productOwnership"]["title"] = (
        "Product & Technical Product Evidence (Portfolio-Built)"
    )
    data["executiveSummaryDoc"]["careerDirection"]["text"] = (
        "Daniel is targeting fully remote U.S. roles as Technical Product Manager / AI Technical Product, "
        "AI Product Manager, and adjacent Technical Product Owner / Product Strategy positions. "
        "Quantitative analytics, AI evaluation, and engineering fluency support that direction; they are not "
        "presented as equal alternate careers. Evidence is the deployed Daniel AI Suite under independent "
        "product ownership — not a claimed corporate PM title."
    )

    # --- About ---
    data["aboutMe"] = {
        "headline": "AI & Technical Product · Product Strategy · Technical Systems · AI-Enabled Products",
        "subheadline": (
            "M.A. Statistics · MBA Finance · SOA Exams · Fully Remote U.S. · "
            "Independent product ownership of a live application suite"
        ),
        "paragraphs": [
            "I define what products should do — then translate goals into requirements, workflows, and acceptance criteria. Across seven live applications I reason through technical dependencies and system behavior, direct AI-assisted implementation, validate releases, diagnose failures, and decide what happens next.",
            "My earlier education career built the same muscles product work needs: explaining complexity, diagnosing stuck points, adapting to different users, and structuring ambiguity. The Daniel AI Suite is the deliberate next step — product and systems ownership with quantitative depth underneath.",
            "Statistics, SQL, Python, and AI evaluation remain visible supporting strengths. They make me better at Technical Product and AI Product work; they are not five competing career identities.",
        ],
        "pillars": [
            {
                "title": "Product Judgment",
                "text": "Problem framing, prioritization, requirements, user journeys, and release decisions across multi-page products.",
            },
            {
                "title": "Systems Thinking",
                "text": "State ownership, persistence, cross-page behavior, multi-user flows, APIs, and suite-level orchestration.",
            },
            {
                "title": "AI-Enabled Products",
                "text": "AI coaching surfaces, evaluation criteria, human-in-the-loop validation, and AI-assisted prototyping under product ownership.",
            },
            {
                "title": "Quantitative Foundation",
                "text": "Statistics, finance, SQL/Python, and decision analytics that strengthen technical product credibility.",
            },
        ],
    }

    # --- Homepage featured work (product patterns, not analytics-first) ---
    data["featuredAnalytics"] = [
        {
            "icon": "🎯",
            "title": "Requirements & Acceptance",
            "text": "Translate goals into product behavior, acceptance criteria, and regression checks before release.",
        },
        {
            "icon": "🧭",
            "title": "Workflow & State Ownership",
            "text": "Decide what is canonical vs temporary, what persists, and what happens across page transitions.",
        },
        {
            "icon": "🔗",
            "title": "Multi-User & Suite Systems",
            "text": "Shared leagues, live sessions, permissions, resumable work, and cross-app context handoffs.",
        },
        {
            "icon": "🤖",
            "title": "AI Product Surfaces",
            "text": "Coaching, evaluation criteria, and human-in-the-loop validation inside real product workflows.",
        },
        {
            "icon": "📊",
            "title": "Decision-Product Design",
            "text": "Turn complex analytics into adjustable, explainable choices for users — not chart dumps.",
        },
        {
            "icon": "🧪",
            "title": "Validate · Diagnose · Iterate",
            "text": "Expected vs actual testing, defect triage, prioritization, and release readiness decisions.",
        },
    ]

    # Music first; Command Center + AMI as third slot via music, baseball, command center, investment
    # AMI stays accessible; Command Center carries orchestration story in showcase
    data["flagshipIds"] = [
        "ai-music-practice-coach",
        "baseball-stat-app",
        "daniel-ai-command-center",
        "investment-portfolio-analyzer",
    ]

    data["summary"] = {
        "headline": "AI & Technical Product",
        "paragraphs": [
            "Product Strategy · Technical Systems · AI-Enabled Products",
            "I combine product judgment, systems thinking, technical fluency, quantitative reasoning, and AI-assisted product development to own what products should do — from requirements through validation and the next release decision.",
            "Fully remote U.S. · Primary: Technical Product Manager / AI Technical Product · Secondary: AI Product Manager · Adjacent: Technical Product Owner / Product Strategy",
        ],
        "skills": [
            "Product Strategy",
            "Requirements",
            "Acceptance Criteria",
            "Workflow Design",
            "Technical Dependencies",
            "AI Feature Design",
            "Release Readiness",
            "Python",
            "SQL",
            "Streamlit",
            "Supabase",
            "Statistics",
            "AI-Assisted Development",
        ],
    }

    data["recruiterQuickScan"] = [
        {
            "question": "What roles?",
            "answer": "Primary: Technical Product Manager / AI Technical Product. Secondary: AI Product Manager. Adjacent: Technical Product Owner / Product Strategy — fully remote U.S.",
        },
        {
            "question": "What does he own?",
            "answer": "Product direction: requirements, workflows, state/persistence, acceptance criteria, validation, defect triage, and release decisions on live systems.",
        },
        {
            "question": "Why the teaching → product path?",
            "answer": "Education built explaining complexity, diagnosing stuck points, and structuring ambiguity — now applied to product and systems ownership.",
        },
        {
            "question": "What proves it?",
            "answer": "Flagships: AI Music Practice Coach, Baseball Analytics, Command Center + AMI, Investment Explorer — plus the full live suite.",
        },
        {
            "question": "Where is the resume?",
            "answer": "Resume Hub CTAs for Technical Product and AI Product paths (current PDF until dedicated files are added).",
        },
    ]

    data["roleTargets"] = [
        {
            "tier": "Primary",
            "role": "Technical Product Manager / AI Technical Product",
            "fit": "Owns product behavior, technical dependencies, workflows, acceptance criteria, and release readiness across multi-page AI-enabled systems.",
        },
        {
            "tier": "Secondary",
            "role": "AI Product Manager",
            "fit": "Designs AI product surfaces, evaluation criteria, and human-in-the-loop workflows with clear ownership of outcomes.",
        },
        {
            "tier": "Adjacent",
            "role": "Technical Product Owner / Product Strategy",
            "fit": "Frames problems, prioritizes features, and turns strategy into shippable product workflows.",
        },
    ]

    data["resumeRouting"] = {
        "workArrangement": "Primarily seeking fully remote U.S. roles.",
        "defaultPdf": "assets/docs/daniel-cohen-resume.pdf",
        "intro": (
            "Two primary resume paths for recruiters. Until dedicated PDF files are supplied, "
            "both CTAs use the current portfolio resume — emphasis differs by role family."
        ),
        "tracks": [
            {
                "id": "technical-pm",
                "tier": "Primary",
                "label": "Technical Product Manager Resume",
                "pdf": "assets/docs/daniel-cohen-resume.pdf",
                "leadWith": "AI Music Practice Coach, Baseball Analytics, Command Center",
                "emphasis": (
                    "Strongest evidence: state ownership, multi-user systems, requirements, "
                    "acceptance criteria, defect triage, and release readiness."
                ),
            },
            {
                "id": "ai-pm",
                "tier": "Secondary",
                "label": "AI Product Manager Resume",
                "pdf": "assets/docs/daniel-cohen-resume.pdf",
                "leadWith": "AI Music Practice Coach, AMI, Command Center, Future Lens (prototype)",
                "emphasis": (
                    "Strongest evidence: AI feature design, coaching/evaluation surfaces, "
                    "human-in-the-loop validation, and AI-assisted product iteration."
                ),
            },
            {
                "id": "product-strategy",
                "tier": "Adjacent",
                "label": "Technical Product Owner / Product Strategy",
                "pdf": "assets/docs/daniel-cohen-resume.pdf",
                "leadWith": "Full suite prioritization story — Music, Baseball, Investment, Command Center",
                "emphasis": (
                    "Strongest evidence: problem framing, roadmap thinking, feature sequencing, "
                    "and strategy translated into working product workflows."
                ),
            },
        ],
        "supportingDoc": "assets/docs/resume-project-descriptions.md",
    }

    data["capabilityGroups"] = [
        {
            "name": "Product Management",
            "skills": [
                "Product strategy",
                "Problem framing",
                "Feature prioritization",
                "Roadmaps / backlogs",
                "User journeys",
                "Requirements",
                "Acceptance criteria",
                "Release decisions",
                "Product metrics",
                "Iterative improvement",
            ],
        },
        {
            "name": "Technical Product",
            "skills": [
                "Technical requirements",
                "Workflow architecture",
                "Data / state flows",
                "Persistence",
                "APIs",
                "Technical dependencies",
                "Edge cases",
                "QA / UAT",
                "Defect triage",
                "Regression testing",
                "Release readiness",
            ],
        },
        {
            "name": "AI Product",
            "skills": [
                "AI feature design",
                "Prompt / system behavior",
                "Human-in-the-loop workflows",
                "AI evaluation criteria",
                "Model-output validation",
                "Failure-mode reasoning",
                "AI-assisted prototyping",
            ],
        },
        {
            "name": "Quantitative & Technical Foundation",
            "skills": [
                "Statistics",
                "SQL",
                "Python",
                "Excel",
                "Pandas",
                "Streamlit",
                "Supabase",
                "Git / GitHub",
                "APIs",
                "Hypothesis testing",
                "Simulation",
                "Optimization",
                "Data visualization",
                "Experimentation",
                "Product metrics",
            ],
        },
    ]

    # --- Per-project product framing (repos) ---
    by_id = {r["id"]: r for r in data["repos"]}

    if "ai-music-practice-coach" in by_id:
        p = by_id["ai-music-practice-coach"]
        p["tier"] = 1
        p["featured"] = True
        p["oneLiner"] = (
            "Flagship technical product: multi-page practice studio with state ownership, "
            "AI coaching, persistence, and release discipline."
        )
        p["recruiterTakeaway"] = (
            "Technical Product flagship — not 'just a music app': practice, creative, backing, "
            "logging, AI coaching, persistence, cross-page context, acceptance criteria, and regression discipline."
        )
        p["capabilityTags"] = [
            "Product architecture",
            "State ownership",
            "AI coaching",
            "Acceptance criteria",
        ]
        p["productFraming"] = {
            "productProblem": (
                "Musicians need adaptive, song-aware practice across tools — not disconnected metronomes, "
                "PDFs, and chatbots."
            ),
            "myProductRole": (
                "Owned product direction: what surfaces exist, which feature owns state, what persists, "
                "what counts as acceptance, and when a release is good enough to proceed."
            ),
            "productTechnicalDecisions": [
                "Canonical vs temporary practice context across pages",
                "Persistence and cross-device resume when cloud restore is enabled",
                "Cross-page active-song state and workflow handoffs",
                "Optional OpenAI coaching hub + AMI insight handoff",
                "Acceptance criteria and regression checks for studio workflows",
                "Feature sequencing: catalog → control center → studio → log",
            ],
            "whyProductWork": (
                "Demonstrates Technical Product Management: deciding system behavior, owning state, "
                "validating implementations, and iterating under release constraints."
            ),
        }

    if "baseball-stat-app" in by_id:
        p = by_id["baseball-stat-app"]
        p["tier"] = 1
        p["featured"] = True
        p["oneLiner"] = (
            "Multi-user fantasy product system: shared leagues, live draft, persistence, and season ops."
        )
        p["recruiterTakeaway"] = (
            "Product/system layer — not merely analytics: shared leagues, live draft rooms, timers, "
            "imports, permissions, recommendations, and lineup/trade workflows."
        )
        p["capabilityTags"] = [
            "Multi-user systems",
            "Live workflows",
            "Persistence",
            "Feature sequencing",
        ]
        p["productFraming"] = {
            "productProblem": (
                "Fantasy managers need a reliable operational product from draft through in-season "
                "decisions — not disconnected stat tables."
            ),
            "myProductRole": (
                "Defined product scope across draft intelligence, league operations, research, and "
                "AI insight handoff; sequenced features for continuity and collaborative use."
            ),
            "productTechnicalDecisions": [
                "Live/multiplayer draft room behavior and room-code flows",
                "Shared league invites, claims, and permission-sensitive actions",
                "Uploaded draft import validation",
                "Decision Score recommendation presentation vs raw rankings",
                "Lineup and Trade Center season-ops workflows",
                "Persistence and reliability expectations for collaborative sessions",
            ],
            "whyProductWork": (
                "Shows Technical Product ownership of multi-user state, collaborative behavior, "
                "and feature sequencing under real workflow pressure."
            ),
        }

    if "daniel-ai-command-center" in by_id:
        p = by_id["daniel-ai-command-center"]
        p["tier"] = 1
        p["featured"] = True
        p["oneLiner"] = (
            "Suite product shell: resumable workflows, context handoffs, and routing to the right tool."
        )
        p["recruiterTakeaway"] = (
            "Product orchestration — continuity across apps: resume/continue, activity, deep links, "
            "and coach insights that treat the portfolio as one system."
        )
        p["capabilityTags"] = [
            "Orchestration",
            "Resumable work",
            "Context handoffs",
            "Suite navigation",
        ]
        p["productFraming"] = {
            "productProblem": (
                "A multi-app suite fragments without a shared home for resume state, activity, and navigation."
            ),
            "myProductRole": (
                "Defined the Command Center as the product shell: what continues, what launches, "
                "and how context returns from AMI and sibling apps."
            ),
            "productTechnicalDecisions": [
                "Continue-where-you-left-off cards vs simple app launchers",
                "Workspace/account context and activity schemas",
                "Deep links and routing into Music, Baseball, Investment, AMI, and more",
                "Supabase + local fallback persistence model",
                "Coach activity summaries for suite-level next steps",
            ],
            "whyProductWork": (
                "Evidence of platform-style Technical Product thinking: continuity, handoffs, "
                "and modular system behavior across products."
            ),
        }

    if "applied-mathematical-intelligence" in by_id:
        p = by_id["applied-mathematical-intelligence"]
        p["tier"] = 1
        p["featured"] = True
        p["oneLiner"] = (
            "Modular AI decision labs with explainable outputs and suite insight routing."
        )
        p["recruiterTakeaway"] = (
            "Paired with Command Center: modular decision-support architecture, explainable outputs, "
            "and analytical handoffs that support AI Product workflows."
        )
        p["capabilityTags"] = [
            "AI decision labs",
            "Explainable outputs",
            "Modular workflows",
            "Suite handoffs",
        ]
        p["productFraming"] = {
            "productProblem": (
                "Quantitative methods are often trapped in notebooks instead of decision workflows users can run."
            ),
            "myProductRole": (
                "Designed AMI as modular action labs with interpretation layers and return paths into sibling apps."
            ),
            "productTechnicalDecisions": [
                "Action-lab IA: solve / predict / explore before deep reference",
                "Explainable output patterns and assumption visibility",
                "Cross-app insight routing via Command Center",
                "AI training / overfitting interpretation surfaces",
            ],
            "whyProductWork": (
                "Supports AI Product Manager fit: structured AI/quant surfaces with clear product behavior "
                "and validation-friendly outputs."
            ),
        }

    if "investment-portfolio-analyzer" in by_id:
        p = by_id["investment-portfolio-analyzer"]
        p["tier"] = 1
        p["featured"] = True
        p["oneLiner"] = (
            "Decision-product design: complex portfolio analytics turned into explainable user choices."
        )
        p["recruiterTakeaway"] = (
            "Decision-product framing — Monte Carlo and optimization matter because they become "
            "adjustable, explainable workflows for beginners and advanced users."
        )
        p["capabilityTags"] = [
            "Decision-product design",
            "Explainable workflows",
            "Dual-audience UX",
            "Quant depth",
        ]
        p["productFraming"] = {
            "productProblem": (
                "Investors need risk-adjusted decisions without institutional terminals or spreadsheet-only chaos."
            ),
            "myProductRole": (
                "Owned product framing for beginner vs advanced modes on one analytics core, with coaching "
                "that turns metrics into next actions."
            ),
            "productTechnicalDecisions": [
                "Shared analytics core with dual UX modes",
                "Health scoring that surfaces strengths and failure modes",
                "Monte Carlo / efficient frontier as user-adjustable workflows",
                "ETF overlap diagnostics beyond ticker pies",
                "AMI insight handoff for follow-up questions",
            ],
            "whyProductWork": (
                "Shows Product Strategy + Technical Product skill: sophistication underneath, "
                "clear choices on top."
            ),
        }

    PROJECTS.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {PROJECTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
