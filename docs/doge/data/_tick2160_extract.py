from pathlib import Path
import re
from html import unescape

RAW = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2160")


def extract(path: Path):
    t = path.read_text(encoding="utf-8", errors="ignore")
    plain = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    plain = re.sub(r"<style[\s\S]*?</style>", " ", plain, flags=re.I)
    plain = re.sub(r"<[^>]+>", "\n", plain)
    plain = unescape(plain)
    plain = re.sub(r"[ \t]+", " ", plain)
    plain = re.sub(r"\n\s*\n+", "\n", plain)
    out = path.with_suffix(".txt")
    out.write_text(plain, encoding="utf-8")
    print("===", path.name, "len", len(t), "plain", len(plain))
    bal = re.search(r"Last balance sheet year\s*\n\s*(\d{4})", plain)
    if not bal:
        bal = re.search(r"Laatste balansjaar\s*\n\s*(\d{4})", plain)
    print("balance", bal.group(1) if bal else "?")
    # FAQ turnover
    for pat in [
        r"recorded a total turnover of\s*€\s*([0-9\.,]+)",
        r"noteerde .*? een omzet van\s*€\s*([0-9\.,]+)",
        r"a enregistré un chiffre d.affaires total de\s*€\s*([0-9\.,]+)",
    ]:
        m = re.search(pat, plain, re.I)
        if m:
            print("faq_omzet", m.group(1))
    # table-ish lines near Profit/Loss / Turnover
    for key in [
        "Profit/Loss",
        "Turnover",
        "Equity",
        "Gross margin",
        "Winst/Verlies",
        "Omzet",
        "Eigen vermogen",
        "Brutomarge",
        "Bénéfice/Perte",
        "Chiffre d",
        "Capitaux propres",
        "Marge brute",
        "Employees",
        "Werknemers",
        "Employés",
        "filed on",
        "neergelegd",
        "déposés",
        "Company size",
        "Bedrijfsgrootte",
        "Full name",
        "Volledige naam",
        "Commercial name",
        "Commerciële naam",
        "Established",
        "Oprichting",
        "VAT number",
        "Enterprise number",
        "Ondernemingsnummer",
        "Legal form",
        "Rechtsvorm",
        "NACE",
        "Establishments",
        "Vestigingseenheden",
    ]:
        for m in re.finditer(re.escape(key), plain):
            snip = plain[max(0, m.start() - 40) : m.start() + 180].replace("\n", " | ")
            print("HIT", key, ":", snip[:220])
            break
    # chart data
    omz = re.findall(r'omzet:\s*"([0-9,\.]+)"', t)
    pnl = re.findall(r'(?:winst|profit|pnl):\s*"([0-9,\.\-]+)"', t, re.I)
    print("json omzet", omz[:6])
    # also look for series arrays
    for lab in ["profit", "omzet", "equity", "bruto", "fte"]:
        ms = re.findall(rf'{lab}[^"]*"([0-9,\.\-]+)"', t, re.I)
        if ms:
            print("series", lab, ms[:8])


for name in [
    "hof_ter_lande_en.html",
    "hof_ter_lande_nl.html",
    "hof_ter_lande_fr.html",
    "hof_ter_lande_kbo.html",
    "olv_kempen_en.html",
]:
    p = RAW / name
    if p.exists():
        extract(p)
    else:
        print("MISSING", name)
