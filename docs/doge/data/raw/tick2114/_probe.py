# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
DATA = RAW.parents[1]
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

taken = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken += (DATA / "leaderboard.csv").read_text(encoding="utf-8", errors="replace")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


def parse(html: str):
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title = re.search(r"<title>([^<]+)</title>", html, re.I)
    lb = re.search(
        r"(?:Laatste balansjaar|Last balance sheet year|Dernier bilan)\s+(\d{4})",
        text,
        re.I,
    )
    euros = {m.group(1): m.groups()[1:] for m in PAT.finditer(html)}
    ftes = re.findall(r"([\d\.,]+)\s*FTE", text)
    neer = re.search(
        r"(?:neergelegd op|filed on|déposés le)\s+([\d\-]+)", text, re.I
    )
    deltas = re.findall(
        r"(Omzet|Turnover|Chiffre d.affaires|Brutomarge|Gross margin|"
        r"Marge brute|Winst/Verlies|Profit/Loss|Bénéfice/Perte|"
        r"Eigen vermogen|Equity|Capitaux propres|"
        r"Werknemers|Employees|Employés)"
        r"[^%]{0,80}?([+\-−]?\s*[\d\.,]+\s*%)",
        text,
        re.I,
    )
    kbo_m = re.search(r"BE\s*(\d{4})[.\s]?(\d{3})[.\s]?(\d{3})", html)
    kbo = (
        f"{kbo_m.group(1)}.{kbo_m.group(2)}.{kbo_m.group(3)}" if kbo_m else "?"
    )
    return {
        "title": title.group(1)[:110] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "deltas": deltas[:8],
        "kbo": kbo,
        "text": text,
    }


print("=== Cached tick2113 prefer ===")
for name in ["faro_nl.html", "aiesh_nl.html", "rew_nl.html", "buissons_nl.html"]:
    p = Path("docs/doge/data/raw/tick2113") / name
    if not p.exists():
        print("MISS", name)
        continue
    info = parse(p.read_text(encoding="utf-8", errors="ignore"))
    e25 = info["euros"].get("2025")
    e24 = info["euros"].get("2024")
    print(
        f"{name}|kbo={info['kbo']}|y={info['year']}|e25={e25}|"
        f"e24o={(e24[3] if e24 else None)}|title={info['title'][:70]}"
    )

print("\n=== LIVE prefer FARO/AIESH/REW/Buissons ===")
prefer = [
    ("faro", "0893863017"),
    ("aiesh", "0200979465"),
    ("rew", "0203621555"),
    ("buissons", "0426317554"),
]
for slug, kbo in prefer:
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        e25 = info["euros"].get("2025")
        e24 = info["euros"].get("2024")
        print(
            f"{slug}|{dotted}|y={info['year']}|neer={info['neer']}|"
            f"e25={e25}|e24o={(e24[3] if e24 else None)}|"
            f"fte={info['ftes']}|d={info['deltas'][:4]}|"
            f"title={info['title'][:80]}"
        )
    except Exception as e:
        print(f"ERR {slug} {type(e).__name__}: {e}")

print("\n=== Prior tick2111 unused YE2025 scan ===")
p11 = Path("docs/doge/data/raw/tick2111")
for p in sorted(p11.glob("*.html")):
    html = p.read_text(encoding="utf-8", errors="ignore")
    info = parse(html)
    e25 = info["euros"].get("2025")
    if not (info["year"] == "2025" or e25):
        continue
    already = info["kbo"] != "?" and (
        info["kbo"] in taken or info["kbo"].replace(".", "") in taken
    )
    print(
        f"{p.name}|kbo={info['kbo']}|already={already}|y={info['year']}|"
        f"e25={e25}|fte={info['ftes']}|title={info['title'][:65]}"
    )
