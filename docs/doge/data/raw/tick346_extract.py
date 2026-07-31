from pathlib import Path
import re

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")
text = (raw / "adeps_ra_2025.txt").read_text(encoding="utf-8")

# Print pages 1-20 fully for budget
pages = text.split("---PAGE")
for p in pages:
    head = p[:20]
    if any(
        x in p
        for x in [
            "NOTRE BUDGET",
            "Notre budget",
            "49.891",
            "SUBVENTIONS",
            "Subventions",
            "8.319",
            "PERSONNEL",
            "441",
            "1.215",
        ]
    ):
        print("=" * 40, "PAGE", p[:30].replace("\n", " "))
        print(p[:3500])
        print()

# also search audit for budget figures
at = (raw / "adeps_audit_2025.txt").read_text(encoding="utf-8")
print("=== AUDIT BUDGET HITS ===")
for i, line in enumerate(at.splitlines()):
    if re.search(
        r"\d[\d\s.,]{3,}\s*(€|EUR|euros|millions)|budget\s*(de\s*)?(l.?AGS|total|ordinaire)|49[\s.,]?891|millions?\s*d.?euros",
        line,
        re.I,
    ):
        if len(line.strip()) < 200:
            print(f"{i}: {line.strip()}")
