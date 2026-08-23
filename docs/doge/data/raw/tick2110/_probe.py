# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
RAW.mkdir(parents=True, exist_ok=True)
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8,fr;q=0.7",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)


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
    return {
        "title": title.group(1)[:90] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "ftes": ftes[:8],
        "euros": euros,
        "deltas": deltas[:12],
        "text": text,
    }


cands = [
    ("faro", "0893863017"),
    ("aiesh", "0201712587"),
    ("rew", "0644638937"),
    ("sint_jozef_ninove", "0452865383"),
]

for slug, kbo in cands:
    for lang in ("en", "nl", "fr"):
        url = f"https://www.companyweb.be/{lang}/{kbo}"
        try:
            body = fetch(url)
            (RAW / f"{slug}_{lang}.html").write_bytes(body)
            info = parse(body.decode("utf-8", "ignore"))
            print(
                slug,
                lang,
                info["title"],
                "year",
                info["year"],
                "neer",
                info["neer"],
                "e25",
                info["euros"].get("2025"),
                "e24",
                info["euros"].get("2024"),
                "fte",
                info["ftes"][:4],
                "deltas",
                info["deltas"][:8],
            )
        except Exception as e:
            print(slug, lang, "ERR", e)

# also parse prior tick2109 faro/ninove if present
PRIOR = RAW.parent / "tick2109"
for name in ("faro.html", "faro_nl.html", "sint_jozef_ninove.html"):
    p = PRIOR / name
    if p.exists():
        info = parse(p.read_text(encoding="utf-8", errors="ignore"))
        print(
            "PRIOR",
            name,
            info["title"],
            "year",
            info["year"],
            "e25",
            info["euros"].get("2025"),
            "e24",
            info["euros"].get("2024"),
            "fte",
            info["ftes"][:4],
        )
