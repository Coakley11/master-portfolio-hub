#!/usr/bin/env python3
import json
import re
from collections import Counter
from pathlib import Path

p = Path(__file__).resolve().parent.parent / "Portfolio Website"
data = json.loads((p / "data/projects.json").read_text(encoding="utf-8"))
html = (p / "index.html").read_text(encoding="utf-8")
ids = re.findall(r'id="([^"]+)"', html)
dups = [i for i, c in Counter(ids).items() if c > 1]
print("duplicate ids:", dups or "none")
print("title:", data["site"]["title"])
print("flagship:", data["flagshipIds"])
print("roles:")
for r in data["roleTargets"]:
    print(" -", r["tier"] + ":", r["role"])
assert data["flagshipIds"][0] == "ai-music-practice-coach"
assert len(data["roleTargets"]) == 3
assert "music" in data["flagshipIds"][0]
print("routing:", [t["label"] for t in data["resumeRouting"]["tracks"]])
print("OK")
