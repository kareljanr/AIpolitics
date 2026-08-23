# deeper parse PPC Pittem equity/bruto/filing
import re
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2021")
en = (outdir / "ppc_pittem_en.html").read_text(encoding="utf-8")
nl = (outdir / "ppc_pittem.html").read_text(encoding="utf-8")

# equity variants
for pat in [
    r"eigenVermogen[^\"]{0,40}\"([^\"]+)\"",
    r"Equity[^\d]{0,80}([\d,.\s\xa0]+)",
    r"equity:\s*\"([^\"]+)\"",
    r"Eigen vermogen.{0,400}",
    r"Capitaux propres.{0,400}",
    r"brutoMarge:\s*\"([^\"]+)\"",
    r"Gross margin.{0,400}",
    r"Bruto.{0,300}",
    r"personeel:\s*\"([^\"]+)\"",
    r"Employees.{0,300}",
    r"FTE.{0,80}",
    r"(\d{2}-\d{2}-\d{4})",
    r"filed.{0,80}",
    r"neerlegg(?:ing|ingsdatum).{0,120}",
    r"Last balance sheet year.{0,120}",
]:
    ms = re.findall(pat, en, re.I | re.S)
    print("EN", pat[:50], "n", len(ms), "sample", [m[:120] if isinstance(m, str) else m for m in ms[:4]])

# NL equity
for pat in [
    r"eigenVermogen:\s*\"([^\"]+)\"",
    r"Eigen vermogen.{0,500}",
    r"Brutomarge.{0,400}",
    r"brutoMarge:\s*\"([^\"]+)\"",
    r"Personeel.{0,300}",
    r"neerlegg.{0,150}",
    r"(\d{2}[-/.]\d{2}[-/.]\d{4})",
]:
    ms = re.findall(pat, nl, re.I | re.S)
    print("NL", pat[:50], "n", len(ms), "sample", [m[:150] if isinstance(m, str) else m for m in ms[:5]])

# Extract table rows from snip
snip = (outdir / "ppc_pittem_fin_snip.txt").read_text(encoding="utf-8")
# pull euro amounts near Profit/Turnover/Equity/Gross
for key in ["Profit", "Turnover", "Equity", "Gross", "Employees", "2025", "2024"]:
    i = snip.find(key)
    print("KEY", key, "idx", i)
    if i >= 0:
        print(snip[i : i + 350].replace("\n", " "))
