import re
from pathlib import Path

html = Path("docs/doge/data/raw/tick2103/korian_nl.html").read_text(
    encoding="utf-8", errors="ignore"
)
for m in re.finditer(r'Employees\s*=\s*"([^"]+)"', html):
    print("EMP", m.group(0))
for m in re.finditer(r"(20\d\d).{0,60}([\d.,]+)\s*FTE", html):
    print("YR_FTE", m.group(1), m.group(2))
i = html.find("neergelegd op 15-08-2026")
print("FILED idx", i)
if i >= 0:
    chunk = re.sub(r"<[^>]+>", " ", html[i - 250 : i + 200])
    print(re.sub(r"\s+", " ", chunk)[:400])

# try EN for employees history
en = Path("docs/doge/data/raw/tick2103/korian_en.html").read_text(
    encoding="utf-8", errors="ignore"
)
for m in re.finditer(r'Employees\s*=\s*"([^"]+)"', en):
    print("EN_EMP", m.group(0))
# look nearby FAQ answer for FTE
m = re.search(r"Er werken .{0,80}FTE", html)
print("FAQ_FTE", m.group(0) if m else None)
m = re.search(r"There (?:are|work) .{0,100}FTE", en, re.I)
print("EN_FAQ", m.group(0) if m else None)

# search numeric tables near '47'
for m in re.finditer(r">47[,.]4<", html):
    print("47.4 at", m.start())

# extract all FTE-like assignments in JS
for m in re.finditer(r"[\"']([^\"']*FTE[^\"']*)[\"']", html):
    s = m.group(1)
    if any(c.isdigit() for c in s):
        print("FTESTR", s[:120])

kbo = Path("docs/doge/data/raw/tick2103/korian_kbo.html").read_text(
    encoding="utf-8", errors="ignore"
)
text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [l.strip() for l in text.splitlines() if l.strip()]
for i, l in enumerate(lines):
    low = l.lower()
    if any(
        x in low
        for x in [
            "status",
            "juridische",
            "rechtsvorm",
            "nace",
            "satenrozen",
            "actief",
            "naamloos",
            "korian",
            "vestiging",
            "ondernemingsnummer",
            "begindatum",
        ]
    ):
        print(i, l[:140])

# YoY calc
omzet, omzet24 = 36661929, 35127187
bruto, bruto24 = 23130494, 30615545
pnl, pnl24 = 3410765, 6790713
eq, eq24 = 194558071, 191147306


def yoy(a, b):
    return (a / b - 1) * 100


print(
    f"omzet YoY {yoy(omzet, omzet24):+.2f}% bruto {yoy(bruto, bruto24):+.2f}% "
    f"pnl {yoy(pnl, pnl24):+.2f}% eq {yoy(eq, eq24):+.2f}%"
)
