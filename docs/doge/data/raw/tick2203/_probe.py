# tick2203 probe — FREE YE2025 maatwerk candidates + stall check
from pathlib import Path
import re
import urllib.request

RAW = Path("docs/doge/data/raw/tick2203")
RAW.mkdir(parents=True, exist_ok=True)

ent = Path("docs/doge/data/entities.csv").read_text(encoding="utf-8").lower()
lb = Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8").lower()
notes = Path("docs/doge/data/research_queue.csv").read_text(encoding="utf-8").lower()

cands = [
    ("kromme", "0454426489", "kromme-boom"),
    ("vlotter", "0841843796", "vlotter-maatwerk-vzw"),
    ("ijsedal", "0407602017", "ijsedal-maatwerkbedrijf"),
    ("de_ploeg", "0465913368", "maatwerkbedrijf-de-ploeg"),
    ("werkplus", "0466950179", "werkplus-maatwerk"),
    ("oesterbank", "0475123890", "oesterbank"),  # guess — may 404
]

for name, kbo, slug in cands:
    keys = [name, kbo, kbo[:4] + "." + kbo[4:7] + "." + kbo[7:]]
    status = []
    for k in keys:
        if k.lower() in ent:
            status.append("ENT")
        if k.lower() in lb:
            status.append("LB")
        if k.lower() in notes and "done" in notes:
            pass
    print(name, kbo, status or ["FREE"])


def fetch(url, out):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)",
            "Accept-Language": "en,nl;q=0.9",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            data = r.read()
        Path(out).write_bytes(data)
        print("OK", out, len(data), r.status if hasattr(r, "status") else "")
        return data
    except Exception as e:
        print("FAIL", url, e)
        return None


def parse(path):
    p = Path(path)
    if not p.exists():
        print("missing", path)
        return
    text = p.read_text(encoding="utf-8", errors="replace")
    print("====", path, "len", len(text))
    m = re.search(r"filed on ([0-9-]+)", text)
    print("filed", m.group(1) if m else None)
    # last book year near span
    years = re.findall(r"Laatste balansjaar|last book year|Last financial year", text, re.I)
    if re.search(r"<span>\s*2025\s*</span>", text):
        print("has span 2025")
    if re.search(r"<span>\s*2024\s*</span>", text):
        print("has span 2024")
    m = re.search(r"total turnover of .([0-9.,]+)", text)
    print("faq_turnover", m.group(1) if m else None)
    empty = bool(re.search(r"did not publish any turnover", text, re.I))
    print("empty_omzet", empty)
    m = re.search(r"gross margin of .([0-9.,]+)", text, re.I)
    print("faq_gross", m.group(1) if m else None)
    m = re.search(r"profit.*?of .([0-9.,-]+)|loss.*?of .([0-9.,-]+)", text, re.I)
    print("faq_pnl_snip", m.group(0)[:80] if m else None)
    parts = re.split(r'title="Section [^"]+"', text)
    for part in parts[1:12]:
        lab = re.search(r">\s*([A-Za-z /]+)<", part[:600])
        euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", part)
        plain = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", part)
        pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", part)
        if euros or (plain and lab):
            print(
                (lab.group(1).strip() if lab else "?")[:40],
                "e",
                euros[:3],
                "p",
                plain[:4],
                "pct",
                pct[:2],
            )


# Parse already-downloaded kromme/vlotter from tick2202
parse("docs/doge/data/raw/tick2202/kromme.html")
parse("docs/doge/data/raw/tick2202/vlotter.html")

# Live stall re-check FARO / REW / AIESH + fetch FREE candidates EN
UA_FETCH = [
    ("stall_faro", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("stall_rew", "https://www.companyweb.be/en/0200931596/reseau-denergies-de-wavre"),
    ("stall_aiesh", "https://www.companyweb.be/en/0200787832/aiesh"),
    ("kromme_en", "https://www.companyweb.be/en/0454426489/de-kromme-boom"),
    ("ijsedal_en", "https://www.companyweb.be/en/0407602017/ijsedal-maatwerkbedrijf"),
    ("de_ploeg_en", "https://www.companyweb.be/en/0465913368/maatwerkbedrijf-de-ploeg"),
    ("vlotter_en", "https://www.companyweb.be/en/0841843796/vlotter-maatwerk-vzw"),
    ("werkplus_en", "https://www.companyweb.be/en/0466950179/werkplus-maatwerk"),
]

for name, url in UA_FETCH:
    out = RAW / f"{name}.html"
    data = fetch(url, out)
    if data and len(data) > 5000:
        parse(out)
