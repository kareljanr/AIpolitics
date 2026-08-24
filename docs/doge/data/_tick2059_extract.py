# ephemeral extract Home Vrijzicht tick2059
import re
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2059")
en = (outdir / "vrijzicht_en.html").read_text(encoding="utf-8", errors="replace")
nl = (outdir / "vrijzicht_nl.html").read_text(encoding="utf-8", errors="replace")
fr = (outdir / "vrijzicht_fr.html").read_text(encoding="utf-8", errors="replace")
kbo = (outdir / "vrijzicht_kbo.html").read_text(encoding="utf-8", errors="replace")
site = (outdir / "vrijzicht_site.html").read_text(encoding="utf-8", errors="replace")


def parse_blocks(html):
    return re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )


def euro(s):
    s = s.replace(".", "").replace(",", ".") if "," in s and "." in s else s
    # CW uses 195,194 style (US comma thousands) in EN
    if re.fullmatch(r"-?\d{1,3}(,\d{3})+", s):
        return s.replace(",", "")
    if re.fullmatch(r"-?\d{1,3}(\.\d{3})*(,\d+)?", s):
        return s.replace(".", "").replace(",", ".")
    return s.replace(",", "")


blocks = parse_blocks(en)
print("BLOCKS raw", blocks[:4])
for i, (w, ev, bm, om) in enumerate(blocks[:3]):
    print(f"Y-{i}", "pnl", euro(w), "eq", euro(ev), "bruto", euro(bm), "omzet", euro(om))

emp = re.search(r'Employees\s*=\s*"([^"]+)"', en)
filed = re.search(r"filed on ([0-9\-]+)", en, re.I)
print("EMP", emp.group(1) if emp else None, "FILED", filed.group(1) if filed else None)

# NL labels
for lab in ["Laatste balansjaar", "Omzet", "Winst", "Eigen vermogen", "Bruto marge", "Werknemers"]:
    i = nl.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", nl[i : i + 200])
        sn = re.sub(r"\s+", " ", sn).strip()
        print("NL", sn[:160])

# chart years
years = re.findall(r'"jaar"\s*:\s*"?(20\d{2})"?', en)
print("YEARS", years[:10])
# another pattern
years2 = re.findall(r"year[s]?[^0-9]{0,20}(20\d{2})", en, re.I)
print("YEARS2", years2[:10])

# address
for pat in [
    r"streetAddress[^>]*>([^<]+)",
    r"(\d{4}\s+[A-Za-z\- ]+)",
    r"([A-Za-z][A-Za-z\- ]+\s+\d+[A-Za-z]?),\s*8906",
]:
    m = re.search(pat, en)
    if m:
        print("ADDR", m.group(0)[:120])

title = re.search(r"<title>([^<]+)", en)
print("TITLE", title.group(1) if title else None)

# KBO
for lab in [
    "Adres van de zetel",
    "E-mail",
    "Rechtsvorm",
    "Status",
    "Ondernemingsnummer",
    "Datum van oprichting",
    "Aantal buitengewone",
]:
    i = kbo.find(lab)
    if i >= 0:
        sn = re.sub(r"<[^>]+>", " ", kbo[i : i + 320])
        sn = re.sub(r"\s+", " ", sn).strip()
        print("KBO", sn[:200])

emails = set()
for html in [nl, en, fr, kbo, site]:
    for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html or ""):
        low = m.lower()
        if not any(x in low for x in ["companyweb", "sentry", "example", "w3.org", "schema", "google", "cookie"]):
            emails.add(m)
print("EMAILS", sorted(emails))

# site title / contact
st = re.search(r"<title>([^<]+)", site)
print("SITE TITLE", st.group(1) if st else None)
phones = re.findall(r"(0\d{1,2}[\s./-]?\d{2,3}[\s./-]?\d{2}[\s./-]?\d{2})", site)
print("PHONES", phones[:8])

# deltas
def f(x):
    return float(euro(x))


if len(blocks) >= 2:
    o25, o24 = f(blocks[0][3]), f(blocks[1][3])
    p25, p24 = f(blocks[0][0]), f(blocks[1][0])
    e25, e24 = f(blocks[0][1]), f(blocks[1][1])
    b25, b24 = f(blocks[0][2]), f(blocks[1][2])
    print("omzet pct", round((o25 - o24) / o24 * 100, 2) if o24 else None)
    print("pnl delta", p25 - p24, "FLIP" if (p25 > 0) != (p24 > 0) else ("JUMP" if p25 > p24 else "DROP"))
    print("eq pct", round((e25 - e24) / e24 * 100, 2) if e24 else None)
    print("bruto pct", round((b25 - b24) / b24 * 100, 2) if b24 else None)
