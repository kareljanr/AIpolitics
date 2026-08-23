# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
DATA = RAW.parents[1]  # docs/doge/data
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

taken_text = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken_lb = (DATA / "leaderboard.csv").read_text(encoding="utf-8", errors="replace")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as resp:
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
    return {
        "title": title.group(1)[:100] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "deltas": deltas[:10],
        "text": text,
    }


real = [
    ("wzc_sj_rumst", "0448190181"),
    ("wzc_xxe_aout", "0443082637"),
    ("wzc_prinsenhof", "0439442761"),
    ("wzc_haagwinde", "0410219433"),
    ("cile", "0202395052"),
    ("sibelga", "0222867266"),
    ("aquafin", "0440691388"),
    ("sofico", "0860325064"),
    ("brugel", "0828638456"),
    ("fluvius", "0477445084"),
    # more plausible unused public WZC/hospital/IGS
    ("wzc_olvh_haaltert", "0403200001"),
    ("zh_az_sint_jan", "0405678901"),
    ("igs_idea", "0202456789"),
    ("igs_interza", "0202567890"),
    ("igs_iveg", "0202678901"),
    ("igs_imosan", "0202789012"),
    ("wzc_rusthuis_meulenberg", "0425890123"),
]

for slug, kbo in real:
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    already = dotted in taken_text or kbo in taken_text or dotted in taken_lb
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        if "Error 404" in info["title"] or info["year"] == "?":
            print(f"SKIP {slug} {kbo} already={already} title={info['title'][:70]}")
            continue
        e25 = info["euros"].get("2025")
        e24 = info["euros"].get("2024")
        print(
            f"HIT {slug}|{kbo}|already={already}|y={info['year']}|neer={info['neer']}|"
            f"fte={info['ftes']}|e25={e25}|e24o={(e24[3] if e24 else None)}|"
            f"d={info['deltas'][:6]}|title={info['title'][:80]}"
        )
    except Exception as e:
        print(f"ERR {slug} {kbo} {type(e).__name__}: {e}")
