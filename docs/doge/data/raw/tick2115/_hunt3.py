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
    "Accept-Language": "nl-BE,nl;q=0.9,fr;q=0.8,en;q=0.7",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

taken = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken += (
    "0412.640.671 0405.311.530 0443.082.637 0452.865.383 0445.175.263 "
    "0417.958.152 0466.961.859 0435.357.675 0869.769.702 0887.690.451 "
    "0893.863.017 0201.712.587 0644.638.937 0877.556.624 0427.821.963"
)

cands = [
    ("les_sittelles", "0451031489"),
    ("charmilles_sambreville", "0457649265"),
    ("la_charmille_vzw", "0416116637"),  # Jolimont path — aanbestedende
    # More Korian-path guesses / known from jaarrekening/northdata
    ("slg_wallonie", "0427821963"),
    ("sl_finance", "0000000000"),
]


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
    nace = re.findall(r"(87\.\d{3}|86\.\d{3})", text)
    emails = [
        e
        for e in re.findall(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)
        if "companyweb" not in e.lower()
    ]
    return {
        "title": title.group(1)[:120] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "deltas": deltas[:10],
        "nace": nace[:6],
        "emails": emails[:6],
    }


for slug, kbo in cands:
    if kbo == "0000000000":
        continue
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    already = dotted in taken or kbo in taken
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        e25 = info["euros"].get("2025")
        flag = "Y25" if info["year"] == "2025" or e25 else f"y{info['year']}"
        print(
            f"{flag} {'TAKEN' if already else 'FREE'} {slug} {dotted}\n"
            f"  title={info['title']}\n"
            f"  neer={info['neer']} e25={e25} e24={info['euros'].get('2024')}\n"
            f"  fte={info['ftes']} nace={info['nace']} deltas={info['deltas']}\n"
            f"  emails={info['emails']}"
        )
    except Exception as e:
        print(f"ERR {slug} {dotted} {e}")
