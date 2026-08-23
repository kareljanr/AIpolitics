# probe free WZC candidates for YE2025
import csv
import re
import ssl
import sys
import urllib.request
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2072")
outdir.mkdir(parents=True, exist_ok=True)

ents = list(csv.DictReader(open("docs/doge/data/entities.csv", encoding="utf-8-sig")))


def kbo_mined(digits: str) -> str | None:
    dotted = f"{digits[:4]}.{digits[4:7]}.{digits[7:]}"
    for e in ents:
        note = ((e.get("notes") or "") + (e.get("entity_id") or "") + (e.get("name_nl") or "")).lower()
        if digits in note or dotted in note:
            return e.get("entity_id")
    return None


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


cands = [
    ("maria_moorslede", "0411600692", "https://www.companyweb.be/en/0411600692/wzc-maria-s-rustoord"),
    ("mater_amabilis", "0417430293", "https://www.companyweb.be/en/0417430293/vzw-mater-amabilis-woon-en-zorgcentrum"),
    ("hof_ter_lande", "0480566704", "https://www.companyweb.be/en/0480566704/hof-ter-lande-woon-en-zorgcentrum"),
    ("heilig_hart_grimbergen", "0409724238", "https://www.companyweb.be/en/0409724238/woon-en-zorgcentrum-heilig-hart-te-grimbergen"),
    # prior raw names from tick2052
    ("avondvrede", None, "https://www.companyweb.be/en/search?q=avondvrede"),
]

# Resolve avondvrede/onderdale/oliveten/philippus from saved HTML if present
for raw in Path("docs/doge/data/raw/tick2052").glob("*avondvrede*"):
    print("raw2052", raw.name)
for raw in Path("docs/doge/data/raw/tick2052").glob("*philippus*"):
    print("raw2052", raw.name)
for raw in Path("docs/doge/data/raw/tick2052").glob("*oliveten*"):
    print("raw2052", raw.name)
for raw in Path("docs/doge/data/raw/tick2052").glob("*onderdale*"):
    print("raw2052", raw.name)

# extract KBOs from those raw files
extra = []
for pat in ["*avondvrede*", "*philippus*", "*oliveten*", "*onderdale*", "*ter_berk*", "*woonsprong*"]:
    for raw in Path("docs/doge/data/raw/tick2052").glob(pat):
        html = raw.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"companyweb\.be/(?:en|nl)/(\d{10})", html)
        title = re.search(r"<title>([^<]+)", html)
        if m:
            print("KBO from", raw.name, m.group(1), (title.group(1)[:50] if title else ""))
            extra.append((raw.stem.split("_")[0], m.group(1), f"https://www.companyweb.be/en/{m.group(1)}"))

for name, digits, url in cands + extra:
    if digits:
        hit = kbo_mined(digits)
        if hit:
            print("SKIP mined", name, digits, "->", hit)
            continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=35) as resp:
            html = resp.read().decode("utf-8", "replace")
        (outdir / f"{name}_en.html").write_text(html, encoding="utf-8")
        emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
        title = re.search(r"<title>([^<]+)", html)
        y = year_of(html)
        blocks = parse_blocks(html)
        print(
            "OK",
            name,
            "Y",
            y,
            "emp",
            emp.group(1) if emp else None,
            "filed",
            filed.group(1) if filed else None,
            (title.group(1)[:55] if title else ""),
            "blocks",
            blocks[:2],
        )
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:140])
