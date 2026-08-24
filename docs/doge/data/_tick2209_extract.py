# -*- coding: utf-8 -*-
"""Deep extract Noordheuvel YE2025 + YoY + KBO + contact."""
import re
import html as H
from pathlib import Path
from urllib.request import Request, urlopen

RAW = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2209")
RAW.mkdir(parents=True, exist_ok=True)
SRC = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2208")
UA = "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)"


def fetch(url, name, timeout=45):
    path = RAW / name
    try:
        req = Request(url, headers={"User-Agent": UA})
        with urlopen(req, timeout=timeout) as r:
            data = r.read()
        path.write_bytes(data)
        print("OK", name, len(data))
        return path
    except Exception as e:
        print("FAIL", name, e)
        return None


def to_text(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    text = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n+", "\n", text))


def parse_money_list(chunk):
    out = []
    for m in re.finditer(
        r"(?:€\s*(-?[\d.,]+)|(?<=\n)-\s*(?=\n)|(?<=\s)-\s*(?=\n))", chunk
    ):
        if m.group(1) is None:
            out.append(None)
            continue
        raw = m.group(1).strip().replace("\xa0", "")
        neg = raw.startswith("-")
        raw = raw.lstrip("-")
        if "," in raw and "." in raw:
            if raw.rfind(",") > raw.rfind("."):
                val = raw.replace(".", "").replace(",", ".")
            else:
                val = raw.replace(",", "")
        elif "," in raw:
            val = raw.replace(",", "")
        else:
            parts = raw.split(".")
            if len(parts) > 2 or (len(parts) == 2 and len(parts[-1]) == 3):
                val = raw.replace(".", "")
            else:
                val = raw
        try:
            num = float(val) if "." in val and len(val.split(".")[-1]) <= 2 else int(float(val))
            out.append(-num if neg else num)
        except Exception:
            out.append(("-" if neg else "") + raw)
    return out


# Refresh CW NL/EN/FR + KBO + site
for lang in ["en", "nl", "fr"]:
    fetch(f"https://www.companyweb.be/{lang}/0415048944/noordheuvel", f"noordheuvel_{lang}.html")
fetch(
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0415048944",
    "kbo.html",
)
# prefer FARO/AIESH recheck quickly
fetch("https://www.companyweb.be/en/0893863017/faro", "faro_en.html")
fetch(
    "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut",
    "aiesh_en.html",
)

# site candidates
for url, name in [
    ("https://www.noordheuvel.be/", "site.html"),
    ("https://noordheuvel.be/", "site2.html"),
    ("https://www.maatwerknoordheuvel.be/", "site3.html"),
]:
    fetch(url, name)

print("\n===== METRICS =====")
for lang in ["en", "nl", "fr"]:
    p = RAW / f"noordheuvel_{lang}.html"
    if not p.exists():
        continue
    text = to_text(p)
    print(f"\n## {lang}")
    for pat in [
        r"Last balance sheet year\s*\n\s*(20\d{2})",
        r"Laatste balansjaar\s*\n\s*(20\d{2})",
        r"Dernier bilan\s*\n\s*(20\d{2})",
        r"filed on\s*([0-9.\-/]+)",
        r"neergelegd op\s*([0-9.\-/]+)",
        r"Company size\s*\n\s*([^\n]+)",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print(pat[:35], "->", m.group(1).strip())
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
        idx = text.find(key)
        if idx < 0:
            continue
        chunk = text[idx : idx + 700]
        print(key, "nums:", parse_money_list(chunk)[:8])
        # also show FTE floats
        ftes = re.findall(r"\b(\d+[.,]\d)\b", chunk)
        if key in ("Employees", "Personeel") or "Employees" in key:
            print("  fte-like:", ftes[:6])
        if key in ("Profit/Loss", "Winst/Verlies"):
            print("  raw:", repr(re.sub(r"\s+", " ", chunk[:350])))

print("\n===== KBO =====")
kbo = to_text(RAW / "kbo.html")
for pat in [
    r"Aantal vestigingseenheden \(VE\):\s*\n?\s*(\d+)",
    r"Status:\s*\n?\s*([^\n]+)",
    r"Rechtsvorm:\s*\n?\s*([^\n]+)",
    r"Begindatum:\s*\n?\s*([^\n]+)",
    r"88\.993",
    r"info@[^\s]+",
    r"www\.[^\s]+",
    r"\d{3}/\d{2}\.\d{2}\.\d{2}",
]:
    for m in re.finditer(pat, kbo, re.I):
        print(pat[:40], "->", (m.group(1) if m.lastindex else m.group(0))[:120])
lines = kbo.splitlines()
for i, line in enumerate(lines):
    low = line.lower()
    if any(x in low for x in ["brasschaat", "adres van de zetel", "telefoon", "e-mail", "webadres", "vestiging", "actief", "rechtsvorm", "begindatum", "naam in"]):
        ctx = " | ".join(lines[j].strip() for j in range(max(0, i - 1), min(len(lines), i + 3)) if lines[j].strip())
        print("CTX:", ctx[:220])

print("\n===== FARO/AIESH year =====")
for name in ["faro_en.html", "aiesh_en.html"]:
    t = to_text(RAW / name)
    m = re.search(r"Last balance sheet year\s*\n\s*(20\d{2})", t)
    print(name, "year", m.group(1) if m else "?")

print("\n===== SITE =====")
for name in ["site.html", "site2.html", "site3.html"]:
    p = RAW / name
    if not p.exists():
        continue
    t = to_text(p)
    print("---", name, "len", p.stat().st_size)
    for pat in [r"info@[a-z0-9.-]+", r"contact@[a-z0-9.-]+", r"\+32[^\n]{0,40}", r"Brasschaat[^\n]{0,40}", r"[A-Z][a-z]+straat[^\n]{0,40}"]:
        m = re.search(pat, t)
        if m:
            print(" ", m.group(0)[:80])
