#!/usr/bin/env python3
"""Generate the portfolio resume PDF.

Default output is a CANDIDATE file under Resume/candidate/ so the public
daniel-cohen-resume.pdf is never overwritten by accident. Pass --publish to
write the public file (only after the candidate has been approved).

Employment dates are cross-checked against Portfolio Website/data/projects.json
so the PDF cannot drift from the website's factual employment history.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
JSON_PATH = HUB / "Portfolio Website" / "data" / "projects.json"
CANDIDATE = HUB / "Resume" / "candidate" / "daniel-cohen-resume-candidate.pdf"
PUBLIC = HUB / "Portfolio Website" / "assets" / "docs" / "daniel-cohen-resume.pdf"
FONT_DIR = Path("C:/Windows/Fonts")

NAVY = (30, 58, 95)
TEXT = (38, 50, 66)
MUTED = (88, 99, 115)
RULE = (170, 182, 198)

CONTACT = [
    "Queens, New York",
    "daniel.cohen11@yahoo.com",
    "linkedin.com/in/daniel-cohen-355319340",
    "github.com/Coakley11",
]
PORTFOLIO = "coakley11.github.io/master-portfolio-hub"

HEADLINE = "Quantitative Analysis  •  Software Projects  •  Excel  •  Python & SQL"

SUMMARY = (
    "Quantitative professional with an M.A. in Statistics & Applied Mathematics (GPA 3.93), an MBA in Finance & "
    "Investments (Finance GPA 4.00), and Society of Actuaries Exams P, FM, and MFE. More than a decade of paid work "
    "teaching college and K–12 mathematics and statistics, with hands-on responsibility for electronic records, grading "
    "and scoring, accuracy review, written feedback, Excel, and remote instruction, plus earlier bookkeeping and "
    "bank-reconciliation work. Separately builds independent technical projects in Python, SQL, and Excel — applications "
    "and workbooks involving statistical modeling, simulation, data validation, and AI-output evaluation practice. "
    "Open to remote part-time, contract, and project-based analytical work."
)

# (title, org, period, [bullets]) — periods must match projects.json (checked below)
EXPERIENCE = [
    ("Independent Tutoring Business", "Self-employed", "Current", [
        "One-on-one instruction, adapting explanations to each student's questions and needs.",
    ]),
    ("Full-Time High School Mathematics Teacher", "The Montfort Academy, Mount Vernon, NY", "2024 — 2026", [
        "Taught Algebra II, Geometry, and Pre-Calculus; supported Chemistry and Physics laboratory sessions.",
        "Maintained electronic student records (grades, attendance, rosters, assignment completion) and corrected recorded information when needed.",
        "Created, administered, graded, and recorded exams, homework, quizzes, and written responses; reviewed work for mathematical accuracy, reasoning, and completeness.",
        "Tracked performance across marking periods, prepared progress information, and communicated professionally with parents.",
    ]),
    ("Permanent Full-Time Substitute Teacher", "Yeshiva Har Torah, Queens, NY", "2021 — 2024", [
        "Followed detailed teacher plans and school procedures across changing K–8 classrooms, subjects, and schedules.",
        "Often received unfamiliar assignments on short notice and independently determined how to deliver the lesson and maintain continuity; maintained and reviewed student work and classroom records.",
    ]),
    ("College Mathematics & Statistics Instructor", "Kingsborough CC · Queens College · Pace University · Yeshiva University", "2012 — 2020", [
        "Kingsborough Community College (CUNY), 2014–2019: Quantitative Reasoning and algebra courses. Queens College (CUNY): Business Statistics lab, 2012; Adjunct Lecturer in Probability & Statistics and Calculus, 2015–2019. Pace University and Yeshiva University, 2020: complete college courses taught remotely by Zoom.",
        "Independently prepared syllabi and materials, graded exams, homework, and multi-step quantitative solutions, identified where reasoning or calculations went wrong, and assigned partial credit.",
        "Used answer keys and established scoring procedures (including Scantron-based assessment at Kingsborough); entered and maintained results in electronic grading systems and spreadsheets and met grading and reporting deadlines.",
        "Used Excel and computer-lab instruction for formulas, sorting, charts, descriptive and inferential statistics, and financial applications; communicated with students by email about exams, assignments, and deadlines.",
    ]),
    ("College Assistant, Academic Tutor & Private Tutor", "Queens College (2011–2014); tutoring organizations and private clients", "2011 — 2024", [
        "Reviewed student work in mathematics, statistics, economics, finance, and SAT preparation; identified errors and gave targeted explanations and written feedback.",
    ]),
    ("Bookkeeping / Accounting Support", "Village Copier, New York, NY", "c. 2009 — 2010", [
        "Performed bookkeeping-related spreadsheet work and bank reconciliation, comparing printed and online bank records with electronic records and investigating discrepancies.",
        "Entered financial information, used Excel calculations (sums, averages), and corrected entries when amounts or records did not match; cross-checked source documents to find data-entry errors and duplicate items.",
    ]),
    ("Accounting / Financial Work", "CureMD", "c. 2007", [
        "Accounting and financial work, including Excel charts related to profit-and-loss information.",
    ]),
]

PROJECTS_INTRO = (
    "Independent technical projects involving quantitative analysis, software development, and AI-assisted applications "
    "(2024–Present): seven deployed Python/Streamlit applications plus SQL and Excel workbooks."
)
PROJECTS = [
    ("AI Music Practice Coach", "Python, Streamlit, OpenAI API, Supabase",
     "A nine-page practice studio — song catalog, section-focused practice, generated backing tracks, composition tools, "
     "multitrack layering, recording analysis, and practice log — sharing one active-song state, with autosave, optional "
     "cross-device restore, and a large automated test suite."),
    ("Baseball Analytics", "Python, Streamlit, scikit-learn, Supabase",
     "A multi-user fantasy baseball system: Decision Score draft recommendations, live draft rooms, uploaded-draft import "
     "validation, shared leagues, and lineup and trade tools."),
    ("Investment Explorer", "Python, Streamlit, yfinance",
     "Portfolio analysis with a health score, Monte Carlo simulation, efficient-frontier optimization, and ETF overlap "
     "analysis, presented for both beginner and advanced users."),
    ("Applied Mathematical Intelligence (AMI) and Command Center", "Python, Streamlit, Supabase",
     "Modular labs for problem solving, game prediction, expected value, disease modeling, and AI-training visualization, "
     "with a shared hub that routes users and results across the suite."),
    ("SQL & Excel workbooks", "Excel, SQL",
     "Practice workbooks with PivotTables, KPI dashboards, and structured SQL queries across finance, insurance, credit "
     "risk, and sports data, including an AI-evaluation practice workbook (150-row dataset, prompt rating, pairwise "
     "comparison) — independent practice, not paid evaluation work."),
    ("Other projects", "Python, Streamlit",
     "NBA Playoff Companion (live games, bracket, matchup analysis) and Future Lens (prototype AI-transition scenario "
     "simulator)."),
]

SKILLS = [
    ("Used in paid work",
     "Excel (formulas, sorting, charts, PivotTables, grade and bookkeeping records); grading and scoring against answer keys "
     "and criteria; electronic records; reports and written feedback; Word, Google Docs, Zoom, Google Meet; professional email."),
    ("Quantitative knowledge",
     "Probability, statistical inference, regression, and financial mathematics, from graduate coursework, SOA Exams P/FM/MFE, and college-level teaching."),
    ("Project-based skills",
     "Python (Pandas, NumPy, scikit-learn), SQL, Streamlit, Plotly, APIs, Git/GitHub, Supabase; Monte Carlo simulation and "
     "portfolio optimization; automated and regression testing; AI-assisted development; AI-output evaluation practice."),
]

EDUCATION = [
    ("M.A., Statistics & Applied Mathematics", "Hunter College", "GPA 3.93"),
    ("MBA, Finance & Investments", "Baruch College, Zicklin School of Business", "Overall GPA 3.88 · Finance GPA 4.00"),
    ("B.A., Mathematics & Economics", "Queens College, CUNY Honors College", "Magna Cum Laude"),
]
CREDENTIALS = (
    "Arthur D. Gayer Memorial Award in Economics (Queens College)  •  Society of Actuaries: Exams P (Probability), FM (Financial Mathematics), MFE (Models for Financial Economics)  •  "
    "NYS Certification: CST Mathematics (004), Educating All Students (EAS)"
)


def ensure_fpdf() -> None:
    try:
        import fpdf  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2", "-q"])


def check_against_site() -> list[str]:
    """Return mismatches between this PDF's employment periods and projects.json."""
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    site_periods = " | ".join(f"{e['organization']} {e['period']}" for e in data["resume"]["experience"])
    problems = []
    norm = lambda p: p.replace(" — ", "–").replace("—", "–").replace(" ", "")
    expect = {
        "Montfort": "2024–2026", "Har Torah": "2021–2024", "Village Copier": "c.2009–2010", "CureMD": "c.2007",
    }
    for name, period in expect.items():
        row = next((e for e in data["resume"]["experience"] if name in e["organization"]), None)
        if not row or norm(row["period"]) != period:
            problems.append(f"{name}: site period {row['period'] if row else None!r} != PDF {period}")
    if "Montfort" in site_periods and "Present" in next(e["period"] for e in data["resume"]["experience"] if "Montfort" in e["organization"]):
        problems.append("Montfort marked Present on site")
    return problems


def build(out: Path) -> None:
    from fpdf import FPDF

    pdf = FPDF(unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_font("A", "", str(FONT_DIR / "arial.ttf"))
    pdf.add_font("A", "B", str(FONT_DIR / "arialbd.ttf"))
    pdf.add_font("A", "I", str(FONT_DIR / "ariali.ttf"))
    pdf.add_font("A", "BI", str(FONT_DIR / "arialbi.ttf"))
    pdf.set_margins(15, 13, 15)
    pdf.add_page()
    pdf.set_title("Daniel Cohen — Resume")
    pdf.set_author("Daniel Cohen")
    epw = pdf.epw
    SZ = 9.6

    def font(style="", size=SZ, color=TEXT):
        pdf.set_font("A", style, size)
        pdf.set_text_color(*color)

    def need(h: float) -> None:
        """Start a new page if h mm will not fit (avoids orphan headings/bullets)."""
        if pdf.get_y() + h > pdf.h - 14:
            pdf.add_page()

    def lines_for(text: str, w: float, h: float) -> float:
        n = len(pdf.multi_cell(w, h, text, dry_run=True, output="LINES"))
        return n * h

    def section(title: str) -> None:
        need(22)
        pdf.ln(2.6)
        font("B", 10, NAVY)
        pdf.cell(0, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(*RULE)
        pdf.set_line_width(0.25)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin + epw, pdf.get_y())
        pdf.ln(1.6)

    def para(text: str, size=SZ, color=TEXT) -> None:
        font("", size, color)
        need(lines_for(text, epw, 4.2))
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(epw, 4.2, text, align="L", new_x="LMARGIN", new_y="NEXT")

    def bullet(text: str) -> None:
        font("", SZ - 0.2)
        need(lines_for(text, epw - 5, 4.4))
        y = pdf.get_y()
        pdf.set_x(pdf.l_margin + 1.5)
        pdf.cell(3, 4.4, "•")
        pdf.set_xy(pdf.l_margin + 5, y)
        pdf.multi_cell(epw - 5, 4.4, text, align="L", new_x="LMARGIN", new_y="NEXT")

    def head(left: str, right: str, sub: str | None = None) -> None:
        need(20)
        font("B", 9.6)
        pdf.cell(epw - 42, 4.6, left)
        font("", SZ, MUTED)
        pdf.cell(42, 4.6, right, align="R", new_x="LMARGIN", new_y="NEXT")
        if sub:
            font("I", SZ - 0.3, MUTED)
            pdf.cell(0, 4.4, sub, new_x="LMARGIN", new_y="NEXT")

    # Header
    font("B", 20, NAVY)
    pdf.cell(0, 9, "DANIEL COHEN", align="C", new_x="LMARGIN", new_y="NEXT")
    font("B", 9.6, TEXT)
    pdf.cell(0, 5, HEADLINE, align="C", new_x="LMARGIN", new_y="NEXT")
    font("", 8.6, MUTED)
    pdf.cell(0, 4.2, "  |  ".join(CONTACT), align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 4.2, f"Portfolio: {PORTFOLIO}", align="C", new_x="LMARGIN", new_y="NEXT")

    section("Professional Summary")
    para(SUMMARY)

    section("Education & Credentials")
    for deg, school, detail in EDUCATION:
        font("B", 9.4)
        dw = pdf.get_string_width(deg) + 2
        pdf.cell(dw, 4.4, deg)
        font("", SZ - 0.1, MUTED)
        pdf.cell(epw - dw - 52, 4.4, f"— {school}")
        pdf.cell(52, 4.4, detail, align="R", new_x="LMARGIN", new_y="NEXT")
    font("", SZ - 0.4, MUTED)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(epw, 4, CREDENTIALS, new_x="LMARGIN", new_y="NEXT")

    section("Skills")
    for label, text in SKILLS:
        need(lines_for(text, epw - 44, 4.4))
        y = pdf.get_y()
        font("B", SZ - 0.2)
        pdf.cell(44, 4.4, label)
        pdf.set_xy(pdf.l_margin + 44, y)
        font("", SZ - 0.2)
        pdf.multi_cell(epw - 44, 4.4, text, align="L", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(0.8)

    section("Professional Experience")
    for title, org, period, bullets in EXPERIENCE:
        font("", SZ - 0.2)
        need(4.6 + 4.4 + sum(lines_for(b, epw - 5, 4.4) for b in bullets))  # keep each entry on one page
        head(title, period, org)
        for b in bullets:
            bullet(b)
        pdf.ln(1.1)

    section("Independent Technical Projects — Daniel AI Suite")
    para(PROJECTS_INTRO, SZ - 0.2, MUTED)
    pdf.ln(0.8)
    for name, tech, desc in PROJECTS:
        font("B", 9.2)
        pdf.set_x(pdf.l_margin)
        pdf.cell(pdf.get_string_width(name) + 2, 4.2, name)
        font("I", 8.4, MUTED)
        pdf.cell(0, 4.2, tech, new_x="LMARGIN", new_y="NEXT")
        font("", SZ - 0.2)
        pdf.set_x(pdf.l_margin + 1.5)
        pdf.multi_cell(epw - 1.5, 4.4, desc, align="L", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(0.9)

    out.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out))
    print(f"Wrote {out}  ({pdf.page_no()} pages)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--publish", action="store_true", help="write the public daniel-cohen-resume.pdf (after approval)")
    args = ap.parse_args()
    ensure_fpdf()
    problems = check_against_site()
    if problems:
        print("Employment history mismatch with projects.json:")
        for p in problems:
            print(" -", p)
        return 1
    build(PUBLIC if args.publish else CANDIDATE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
