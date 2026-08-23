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
    return {
        "title": title.group(1)[:90] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
    }


cands = [
    ("faro", "0893863017"),
    ("aiesh", "0201712587"),
    ("rew", "0644638937"),
    ("hydrobru", "0400066228"),
    ("inasep", "0206613595"),
    ("ipalle", "0267314471"),
    ("teo", "0216549565"),
    ("sedilec", "0267444057"),
    ("sim", "0401407066"),
    ("iecbw", "0206607759"),
    ("wzc_denolm", "0435223551"),
    ("wzc_wingerd", "0412123568"),
    ("wzc_immaculata", "0425333868"),
    ("wzc_hh_lier", "0459840267"),
    ("wzc_sj_merksem", "0408263294"),
    ("wzc_olv_dend", "0405669590"),
    ("wzc_bijster", "0421316280"),
    ("wzc_hofveldeke", "0465873655"),
]

for slug, kbo in cands:
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        e25 = info["euros"].get("2025")
        e24 = info["euros"].get("2024")
        print(
            f"{slug}|{kbo}|y={info['year']}|neer={info['neer']}|"
            f"fte={info['ftes']}|e25={e25}|e24_omzet={(e24[3] if e24 else None)}|"
            f"title={info['title']}"
        )
    except Exception as e:
        print(slug, "ERR", type(e).__name__, e)
