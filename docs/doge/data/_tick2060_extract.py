# ephemeral extract Christine tick2060
import re
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2060")
en = (outdir / "christine_en.html").read_text(encoding="utf-8", errors="replace")
nl = (outdir / "christine_nl.html").read_text(encoding="utf-8", errors="replace")
kbo = (outdir / "christine_kbo.html").read_text(encoding="utf-8", errors="replace")


def euro(s):
    if re.fullmatch(r"-?\d{1,3}(,\d{3})+", s):
        return s.replace(",", "")
    return s.replace(".", "").replace(",", ".") if "," in s else s.replace(",", "")


blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    en,
)
for i, (w, ev, bm, om) in enumerate(blocks[:3]):
    print(f"Y-{i}", "pnl", euro(w), "eq", euro(ev), "bruto", euro(bm), "omzet", euro(om))


def f(x):
    return float(euro(x))


o25, o24 = f(blocks[0][3]), f(blocks[1][3])
p25, p24 = f(blocks[0][0]), f(blocks[1][0])
e25, e24 = f(blocks[0][1]), f(blocks[1][1])
b25, b24 = f(blocks[0][2]), f(blocks[1][2])
print("omzet pct", round((o25 - o24) / o24 * 100, 2))
print("pnl pct", round((p25 - p24) / abs(p24) * 100, 2), "DROP" if p25 < p24 else "JUMP")
print("eq pct", round((e25 - e24) / e24 * 100, 2))
print("bruto pct", round((b25 - b24) / b24 * 100, 2))

# address / aanbestedende
for lab in ["aanbestedende", "Aanbestedende", "streetAddress", "Gerardus"]:
    i = en.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", en[i : i + 180])
        print("EN", re.sub(r"\s+", " ", sn)[:160])
i = kbo.lower().find("aanbestedende")
print("KBO aanbestedende idx", i)
if i >= 0:
    sn = re.sub(r"<[^>]+>", " ", kbo[i : i + 250])
    print(re.sub(r"\s+", " ", sn)[:200])

# NACE visible
for m in re.finditer(r"87\.10\d|87\.101|87\.102", kbo):
    print("NACE near", kbo[max(0, m.start() - 40) : m.start() + 60].replace("\n", " ")[:100])

# CW contact emails in page scripts
emails = re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", en + nl)
print("ALL emails sample", [e for e in sorted(set(emails)) if "companyweb" not in e.lower()][:20])

# zip city
m = re.search(r"Gerardus Stijnenlaan[^,<]{0,40}", en)
print("ADDR", m.group(0) if m else None)
title = re.search(r"<title>([^<]+)", en)
print("TITLE", title.group(1) if title else None)
