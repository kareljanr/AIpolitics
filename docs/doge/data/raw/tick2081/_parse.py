# -*- coding: utf-8 -*-
import csv
import re
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path("docs/doge/data/raw/tick2081")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def parse(path: Path) -> None:
    t = path.read_text(encoding="utf-8", errors="replace")
    print("====", path.name)
    title = re.search(r"<title>([^<]+)</title>", t)
    print("TITLE", title.group(1)[:140] if title else "?")
    m = re.search(r"kernCijfers\s*=\s*\{([^}]+\{[^}]+\}){1,4}", t, re.S)
    # extract year-keyed blocks
    for ym in re.finditer(
        r"(20\d\d)\s*:\s*\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"",
        t,
    ):
        print("Y", ym.group(1), "winst", ym.group(2), "equity", ym.group(3), "bruto", ym.group(4), "omzet", ym.group(5))
    filed = re.search(r"neergelegd op ([0-9\-]+)|filed on ([0-9\-]+)", t, re.I)
    print("FILED", filed.group(0) if filed else "?")
    fte = re.search(r"amountOfEmployees\s*=\s*\"([^\"]+)\"", t)
    print("FTE", fte.group(1) if fte else "?")
    spans = re.findall(r"<span>(\d+[\.,]\d)</span>", t)
    print("spans", spans[:5])


parse(RAW / "sint_barbara_nl.html")
parse(RAW / "sint_barbara_en.html")

# already done?
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        blob = " ".join((r.get(k) or "") for k in r).lower()
        if "sint-barbara" in blob or "0422.152.314" in blob or "0422152314" in blob:
            print("RQHIT", r["task_id"], r["status"], (r.get("title") or "")[:80])

with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if "barbara" in str(r).lower() and "herselt" in str(r).lower():
            print("ENT", r.get("entity_id"))

# KBO + site
kbo = (RAW / "kbo_sb.html").read_text(encoding="utf-8", errors="replace")
for line in kbo.splitlines():
    s = line.strip()
    if any(x in s for x in ["Actief", "Vereniging", "Herselt", "vestiging", "87.", "aanbested", "E-mail", "Webadres", "Naam"]):
        if s and "<" not in s[:3] and len(s) < 180:
            print("KBO", s)
# better extract
for pat in [
    r"Herselt[^<]{0,40}",
    r"Aantal vestigingseenheden \(VE\):.*?<strong>([^<]+)",
    r"87\.\d+",
    r"aanbestedende",
]:
    m = re.search(pat, kbo, re.I | re.S)
    if m:
        print("KBOPAT", re.sub(r"\s+", " ", m.group(0))[:120])

# fetch site
for name, url in [
    ("site.html", "https://www.wzc-sintbarbara.be/"),
    ("site2.html", "https://www.wzcsintbarbara.be/"),
    ("site3.html", "https://sintbarbara.be/"),
]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
            final = resp.geturl()
        (RAW / name).write_bytes(data)
        text = data.decode("utf-8", "replace")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [e for e in emails if "sentry" not in e and "wixpres" not in e and "example" not in e]
        print("SITE", name, len(data), final, "emails", emails[:10])
    except Exception as e:
        print("FAIL", name, e)

# bornem check
born = (RAW / "bornem_jr.html").read_text(encoding="utf-8", errors="replace")
print("BORNEM", sorted(set(re.findall(r"Jaarrekening\s+(20\d\d)", born))))
