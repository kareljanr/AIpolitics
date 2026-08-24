# ephemeral parse tick2059 probe HTML
import re
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2059")


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


def parse_blocks(html):
    return re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )


for p in sorted(outdir.glob("*_en.html")):
    html = p.read_text(encoding="utf-8", errors="replace")
    emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
    filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
    title = re.search(r"<title>([^<]+)", html)
    blocks = parse_blocks(html)
    print(
        p.name,
        "Y",
        year_of(html),
        "emp",
        emp.group(1) if emp else None,
        "filed",
        filed.group(1) if filed else None,
    )
    print("  title", (title.group(1)[:70] if title else ""))
    print("  blocks", blocks[:3])
