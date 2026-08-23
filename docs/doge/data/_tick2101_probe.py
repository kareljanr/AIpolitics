import re
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2100")
# parse CW snippet tables from candidate htmls
for p in sorted(RAW.glob("cand_*.html")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    # last balansjaar
    m = re.search(r"Laatste balansjaar\s*</[^>]+>\s*(\d{4})", t, re.I | re.S)
    year = m.group(1) if m else "?"
    # title / name
    name = re.search(r"<h1[^>]*>\s*([^<]+)", t)
    name = (name.group(1).strip() if name else p.stem)[:50]
    # kbo
    kbo = re.search(r"BE\s*(\d{4}\.?\d{3}\.?\d{3})", t)
    kbo = kbo.group(1) if kbo else p.stem.replace("cand_", "")
    # try extract 2025 row from table - look for Turnover/Omzet near 2025
    # companyweb often has JSON-like or table with years
    euros = {}
    # pattern from earlier hunt script
    for ym in re.finditer(
        r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
        r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
        t,
    ):
        euros[ym.group(1)] = ym.groups()[1:]
    # fallback: look for markdown-ish tables in fetched text
    if "2025" not in euros:
        # try: after "2025" find first few € amounts in financial section
        idx = t.find("Financiële gegevens")
        chunk = t[idx : idx + 4000] if idx >= 0 else t[:5000]
        # find years headers
        if "2025" in chunk and year == "2025":
            amounts = re.findall(r"€\s*([\d.\s]+)", chunk)
            amounts = [a.replace(".", "").replace(" ", "").strip() for a in amounts if a.strip()]
            euros["raw_amounts"] = amounts[:12]
    print(f"{p.name}|year={year}|{kbo}|{name}|euros={euros.get('2025') or euros.get('raw_amounts', euros) }")
