# -*- coding: utf-8 -*-
import re, ssl, urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2173")


def fetch(url, p):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
        data = r.read()
    p.write_bytes(data)
    return data.decode("utf-8", "ignore")


def parse(t):
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(r"(?:filed on|neergelegd op)\s*([0-9-]{10})", t or "", re.I)
    title = re.search(r"<title>([^<]+)", t or "")
    last = re.search(
        r"(?:Last balance sheet year|Laatste balansjaar|Dernier bilan)[^0-9]*(\d{4})",
        t or "",
        re.I,
    )
    return yb, fte.group(1) if fte else None, filed.group(1) if filed else None, title.group(1) if title else None, last.group(1) if last else None


for kbo, label, lang in [
    ("0666821451", "senes", "en"),
    ("0666821451", "senes", "nl"),
    ("0666821451", "senes", "fr"),
    ("0870166709", "best1", "en"),
    ("1026468648", "best2", "en"),
]:
    t = fetch(f"https://www.companyweb.be/{lang}/{kbo}", out / f"{label}_{kbo}_{lang}.html")
    yb, fte, filed, title, last = parse(t)
    print(label, lang, (title or "")[:70], "last", last, "fte", fte, "filed", filed)
    print("  y5", yb.get("2025"))
    print("  y4", yb.get("2024"))
