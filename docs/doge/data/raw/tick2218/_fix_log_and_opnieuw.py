# -*- coding: utf-8 -*-
import re
from pathlib import Path

# Deduplicate loop_log: keep first 2218 block, replace second with race note
log = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
t = log.read_text(encoding="utf-8")
marker = "## Tick 2218 - 2026-08-26T18:20:00Z - rq_2218 Veerkracht 4 Menen"
first = t.find(marker)
second = t.find(marker, first + 1)
if second < 0:
    print("no duplicate")
else:
    # end of second block = next ## after second, or EOF
    nxt = t.find("\n## ", second + 10)
    if nxt < 0:
        nxt = len(t)
    race = (
        "\n### 2026-08-26T18:25:00Z - tick 2218 race note\n"
        "- Concurrent agent closed rq_2218 as **Veerkracht 4** YE2025 Medium "
        "(bruto JUMP 3.76m / empty omzet / pnl JUMP +72% / equity JUMP +20%) "
        "and committed first. This agent independently fetched the same CW/KBO "
        "euros and confirms the fill; duplicate log block removed. "
        "Next open head **rq_2219** (Opnieuw&Co / NBSW YE2025 free).\n"
    )
    t = t[:second] + race + t[nxt:]
    log.write_text(t, encoding="utf-8")
    print("deduped log; race note inserted")

# Parse Opnieuw
out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218")
html = (out / "opnieuw_en.html").read_text(encoding="utf-8", errors="ignore")
blocks = re.findall(
    r"(20(?:24|25))\s*:\s*(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})", html
)
for y, b in blocks:
    print("YEAR", y)
    print(b[:450])
print("FTE", re.findall(r"([\d,]+)\s*FTE", html)[:5])
m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
print("amount", m.group(1) if m else None)
f = re.search(r"filed on ([0-9\-]+)", html, re.I)
print("filed", f.group(1) if f else None)
print("title", re.search(r"<title>([^<]+)", html).group(1)[:80])
