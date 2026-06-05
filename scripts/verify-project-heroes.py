#!/usr/bin/env python3
import json
from pathlib import Path

hub = Path(__file__).resolve().parent.parent
data = json.loads((hub / "Portfolio Website/data/projects.json").read_text(encoding="utf-8"))
deploy = hub / "Portfolio Website/assets/screenshots"
flagship = set(data.get("flagshipIds", []))

print("=== Project card / detail hero verification ===")
all_ok = True
for repo in data["repos"]:
    shots = repo.get("screenshots") or []
    if not shots:
        continue
    hero = shots[0].replace("assets/screenshots/", "")
    ok = (deploy / hero.replace("/", "\\")).exists()
    all_ok = all_ok and ok
    tag = "FLAGSHIP" if repo["id"] in flagship else f"tier {repo.get('tier')}"
    status = "OK" if ok else "MISSING"
    print(f"{status:7} [{tag:8}] {repo['id']}: {hero}")

print()
print("All heroes OK" if all_ok else "Some heroes missing")
