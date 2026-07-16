#!/usr/bin/env python3
"""Generate daniel-cohen-resume.pdf from projects.json resume section."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent
JSON_PATH = HUB / "Portfolio Website" / "data" / "projects.json"
OUT_PATH = HUB / "Portfolio Website" / "assets" / "docs" / "daniel-cohen-resume.pdf"


def ensure_fpdf():
    try:
        from fpdf import FPDF  # noqa: F401
        return True
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2", "-q"])
        return True


def ascii_safe(text: str) -> str:
    return (
        text.replace("\u2014", " - ")
        .replace("\u2013", "-")
        .replace("\u00b7", " | ")
        .replace("\u2192", "->")
    )


def build_pdf(resume: dict, site: dict) -> None:
    from fpdf import FPDF

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_margins(18, 18, 18)

    def section(title: str) -> None:
        pdf.ln(4)
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(30, 58, 95)
        pdf.cell(0, 7, title.upper(), new_x="LMARGIN", new_y="NEXT")
        pdf.set_draw_color(203, 213, 225)
        pdf.line(18, pdf.get_y(), 192, pdf.get_y())
        pdf.ln(3)
        pdf.set_text_color(51, 65, 85)

    epw = pdf.epw

    def body(text: str, size: int = 10) -> None:
        pdf.set_font("Helvetica", "", size)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(epw, 5, ascii_safe(text))

    def bullet(text: str) -> None:
        pdf.set_font("Helvetica", "", 9)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(epw, 4.5, ascii_safe(f"- {text}"))

    # Header
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(30, 58, 95)
    pdf.cell(0, 10, ascii_safe(resume["name"]), new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(0, 6, ascii_safe(resume["headline"]), new_x="LMARGIN", new_y="NEXT", align="C")
    github = site.get("github", "").replace("https://", "")
    linkedin = site.get("linkedin") or ""
    contact = f"GitHub: {github}"
    if linkedin:
        contact += "  |  LinkedIn: available via portfolio contact"
    pdf.cell(0, 5, ascii_safe(contact), new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, "Portfolio: deploy URL on applications / LinkedIn Featured", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(2)

    section("Professional Summary")
    body(resume["summary"])

    section("Education")
    for edu in resume["education"]:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 5, ascii_safe(f"{edu['degree']} - {edu['school']}"), new_x="LMARGIN", new_y="NEXT")
        if edu.get("detail"):
            pdf.set_font("Helvetica", "I", 9)
            pdf.set_text_color(100, 116, 139)
            body(edu["detail"], 9)
            pdf.set_text_color(51, 65, 85)

    if resume.get("credentials"):
        section("Credentials and Certifications")
        for cred in resume["credentials"]:
            bullet(cred)

    section("Experience")
    for exp in resume["experience"]:
        pdf.set_font("Helvetica", "B", 10)
        line = exp["title"]
        if exp.get("period"):
            line += f"  ({exp['period']})"
        pdf.cell(0, 5, ascii_safe(line), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "I", 9)
        pdf.set_text_color(71, 85, 105)
        pdf.cell(0, 4, ascii_safe(exp["organization"]), new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(51, 65, 85)
        for b in exp["bullets"]:
            bullet(b)
        pdf.ln(1)

    section("Selected Projects")
    for proj in resume["projectBullets"]:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 5, ascii_safe(f"{proj['name']} | {proj['tech']}"), new_x="LMARGIN", new_y="NEXT")
        for b in proj["bullets"]:
            bullet(b)
        pdf.ln(1)

    section("Technical Skills")
    body(" | ".join(resume["technicalSkills"]), 9)

    section("Target Roles")
    body(" | ".join(resume["targetRoles"]), 9)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT_PATH))
    print(f"Wrote {OUT_PATH}")


def main() -> int:
    ensure_fpdf()
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    build_pdf(data["resume"], data["site"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
