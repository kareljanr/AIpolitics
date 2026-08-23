import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2015")
t = (dst / "azzeno_en.html").read_text(encoding="utf-8", errors="replace")

# year-ish strings near balance / filed / chart
for lab in [
    "Last balance sheet year",
    "filed on",
    "financial year",
    "Book year",
    "2024",
    "2025",
    "2008",
    "2026",
]:
    idxs = [m.start() for m in re.finditer(re.escape(lab), t)]
    print(lab, "count", len(idxs))
    for i in idxs[:3]:
        print(" ", repr(re.sub(r"\s+", " ", t[max(0, i - 40) : i + 120])[:160]))

# chart year labels
years = re.findall(r'"jaar"\s*:\s*"?(\d{4})"?', t)
print("jaar fields", years[:20])
years2 = re.findall(r"year[^0-9]{0,20}(20\d{2})", t, flags=re.I)
print("year near", years2[:20])
# highcharts categories
cats = re.findall(r"categories\s*:\s*\[([^\]]+)\]", t)
print("categories", cats[:3])
# dates around filing
for m in re.finditer(r"neergelegd|filed on|deposit|202[4-6]", t, flags=re.I):
    pass
# social balance year
for pat in [
    r"Last social balance year.{0,80}",
    r"Laatste sociale balans.{0,80}",
    r"socialBalanceYear.{0,40}",
    r"balansjaar.{0,60}",
]:
    ms = re.findall(pat, t, flags=re.I)
    if ms:
        print("PAT", pat, ms[:5])

# Try other unused hospitals
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
candidates = [
    ("az_jan_yperman", "https://www.companyweb.be/en/0412125545"),
    ("az_sint_lucas_gent", "https://www.companyweb.be/en/0411353721"),
    ("az_sint_lucas_brugge", "https://www.companyweb.be/en/0408194657"),
    ("az_groeninge", "https://www.companyweb.be/en/0412118540"),
    ("az_turnhout", "https://www.companyweb.be/en/0412065867"),
    ("az_vesalius", "https://www.companyweb.be/en/0422144559"),
    ("az_jan_portaels", "https://www.companyweb.be/en/0412065867"),
    ("az_klina", "https://www.companyweb.be/en/0425136458"),
    ("az_rivierenland", "https://www.companyweb.be/en/0455868415"),
    ("az_diest", "https://www.companyweb.be/en/0412228837"),
]


def summarize_bytes(name, data):
    t = data.decode("utf-8", errors="replace")
    (dst / f"{name}.html").write_bytes(data)
    title = re.search(r"<title>([^<]+)</title>", t)
    year = re.search(
        r"Last balance sheet year\s*</div>\s*<div class=\"font-medium \"?>\s*(\d{4})",
        t,
    )
    filed = re.search(r"filed on ([0-9\-]+)", t)
    blocks = re.findall(
        r'winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"',
        t,
    )
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(
        "==",
        name,
        "==",
        (title.group(1)[:90] if title else None),
        "year",
        year.group(1) if year else None,
        "filed",
        filed.group(1) if filed else None,
        "FTE",
        em[:1],
        "blocks",
        len(blocks),
        "omzet0",
        blocks[0][3] if blocks else None,
    )


for name, url in candidates:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
            data = resp.read()
        if b"Error 404" in data[:500]:
            print("404", name)
            continue
        summarize_bytes(name, data)
    except Exception as e:
        print("FAIL", name, e)
