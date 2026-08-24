# -*- coding: utf-8 -*-
"""Tick 2208 probe: FARO/AIESH/REW YE2025 check + Arcor/Noordheuvel extract."""
import re
import html as H
from pathlib import Path
from urllib.request import Request, urlopen

RAW = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2208")
RAW.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)"


def fetch(url, name, timeout=45):
    path = RAW / name
    try:
        req = Request(url, headers={"User-Agent": UA})
        with urlopen(req, timeout=timeout) as r:
            data = r.read()
        path.write_bytes(data)
        print(f"OK {name} {len(data)} {url}")
        return path
    except Exception as e:
        print(f"FAIL {name} {e} {url}")
        return None


def to_text(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    text = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    return re.sub(r"\n+", "\n", text)


def parse_eur_block(text, key):
    idx = text.find(key)
    if idx < 0:
        return None
    chunk = text[idx : idx + 500]
    # Prefer euro amounts with digit groups
    nums = re.findall(r"€\s*([\d.,]+)", chunk)
    if not nums:
        # bare number after key
        m = re.search(rf"{re.escape(key)}\s*([-\d.,]+)", chunk)
        if m and m.group(1) not in ("-", "—"):
            nums = [m.group(1)]
    if not nums:
        return None
    raw = nums[0].strip()
    if raw in ("-", "—", ""):
        return None
    # EN commas as thousands, or NL dots
    if "," in raw and "." in raw:
        if raw.rfind(",") > raw.rfind("."):
            # 1.234.567,89 NL
            val = raw.replace(".", "").replace(",", ".")
        else:
            # 1,234,567.89 EN
            val = raw.replace(",", "")
    elif "," in raw:
        # ambiguous: if 1-2 digits after comma -> decimal; else thousands EN
        parts = raw.split(",")
        if len(parts[-1]) <= 2 and len(parts) == 2 and "." not in raw:
            # could be 440,045 EN thousands OR 440,04 decimal — CW uses EN thousands
            val = raw.replace(",", "")
        else:
            val = raw.replace(",", "")
    else:
        # NL style 2.792.424 or plain
        parts = raw.split(".")
        if len(parts) > 2 or (len(parts) == 2 and len(parts[-1]) == 3):
            val = raw.replace(".", "")
        else:
            val = raw
    try:
        if "." in val and val.count(".") == 1 and len(val.split(".")[-1]) <= 2:
            return float(val)
        return int(float(val))
    except Exception:
        return raw


def sniff(path, label=None):
    if path is None or not path.exists():
        print("MISSING", label or path)
        return
    text = to_text(path)
    name = label or path.name
    print("====", name)
    m = re.search(r"<title>([^<]+)", path.read_text(encoding="utf-8", errors="replace"), re.I)
    if m:
        print(" title:", m.group(1).strip()[:120])
    html = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"companyweb\.be/(?:en|nl|fr)/(\d+)/([^\"'?\s]+)", html)
    if m:
        print(" kbo/slug:", m.group(1), m.group(2))
    for pat in [
        r"Last balance sheet year\s*\n?\s*(20\d{2})",
        r"Laatste balansjaar\s*\n?\s*(20\d{2})",
        r"Dernier bilan\s*\n?\s*(20\d{2})",
        r"Company size\s*\n?\s*([^\n]+)",
        r"filed on\s*([0-9.\-/]+)",
        r"neergelegd op\s*([0-9.\-/]+)",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print(" ", pat[:40], "->", m.group(1).strip())
    for key in [
        "Turnover",
        "Gross margin",
        "Profit/Loss",
        "Equity",
        "Employees",
        "Omzet",
        "Brutomarge",
        "Winst/Verlies",
        "Eigen vermogen",
        "Personeel",
    ]:
        v = parse_eur_block(text, key)
        if v is not None:
            print(f"  {key}: {v}")
        else:
            idx = text.find(key)
            if idx >= 0:
                chunk = re.sub(r"\s+", " ", text[idx : idx + 180])
                print(f"  {key} RAW: {chunk[:140]}")
    # YoY table rows sometimes have prior year nearby
    print()


# Prefer FARO / AIESH / REW first (correct KBOs)
TARGETS = [
    ("https://www.companyweb.be/en/0893863017/faro", "faro_en.html"),
    ("https://www.companyweb.be/nl/0893863017/faro", "faro_nl.html"),
    (
        "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut",
        "aiesh_en.html",
    ),
    ("https://www.companyweb.be/en/0200660697/rew", "rew_en.html"),  # may 404; try alt below
    ("https://www.companyweb.be/en/0200971459/rew", "rew_alt_en.html"),
]

print("--- fetching preferred stalls ---")
for url, name in TARGETS:
    fetch(url, name)

# Arcor 0410.962.274 / Noordheuvel 0415.048.944
print("--- fetching Arcor/Noord ---")
for lang, suffix in [("en", "en"), ("nl", "nl"), ("fr", "fr")]:
    fetch(f"https://www.companyweb.be/{lang}/0410962274/arcor", f"arcor_{suffix}.html")
    fetch(
        f"https://www.companyweb.be/{lang}/0415048944/noordheuvel",
        f"noordheuvel_{suffix}.html",
    )

# KBO identity
fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0410962274",
    "kbo_arcor.html",
)
fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0415048944",
    "kbo_noordheuvel.html",
)

# AGB Bornem quick check
fetch(
    "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb",
    "agb_bornem_probe.html",
)

print("\n=== SNIFF ===")
for name in [
    "faro_en.html",
    "faro_nl.html",
    "aiesh_en.html",
    "rew_en.html",
    "arcor_en.html",
    "arcor_nl.html",
    "noordheuvel_en.html",
    "noordheuvel_nl.html",
]:
    sniff(RAW / name if (RAW / name).exists() else None, name)
