# -*- coding: utf-8 -*-
"""Probe prefer stalls + find unused YE2025 MRS/WZC candidate for tick 2118."""
import csv
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
RAW.mkdir(parents=True, exist_ok=True)
DATA = RAW.parents[1]
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
csv.field_size_limit(10**7)


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
    emails = [
        e
        for e in re.findall(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", text, re.I)
        if "companyweb" not in e.lower() and "sentry" not in e.lower()
    ]
    return {
        "title": title.group(1)[:140] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "deltas": deltas[:10],
        "emails": emails[:6],
    }


# Prefer stalls
prefer = [
    ("faro", "0893863017"),
    ("aiesh", "0201712587"),
    ("rew", "0644638937"),
]
print("=== PREFER ===")
for slug, kbo in prefer:
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        e25 = info["euros"].get("2025")
        flag = "Y25" if info["year"] == "2025" or e25 else f"y{info['year']}"
        print(flag, slug, kbo, "e25", e25, "neer", info["neer"])
    except Exception as e:
        print("ERR", slug, e)

# Done KBOs / entity names from queue + entities
done_kbo = set()
done_names = set()
with (DATA / "research_queue.csv").open(encoding="utf-8-sig", newline="") as fh:
    for row in csv.DictReader(fh):
        blob = " ".join((row.get(k) or "") for k in row).lower()
        for m in re.findall(r"0\d{3}\.\d{3}\.\d{3}", blob):
            done_kbo.add(m.replace(".", ""))
        if row.get("entity_id"):
            done_names.add(row["entity_id"].lower())
with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
    for row in csv.DictReader(fh):
        blob = " ".join((row.get(k) or "") for k in row).lower()
        for m in re.findall(r"0\d{9,}", blob.replace(".", "")):
            if len(m) >= 10:
                done_kbo.add(m[:10])
        if row.get("entity_id"):
            done_names.add(row["entity_id"].lower())

# Candidate KBOs from recent tick probes / known Korian / Jolimont sisters / WZC
cands = [
    # from tick2117 leftover probe
    ("0443249616", "helianthus_or_cand"),
    # Korian / other MRS often in family
    ("0438687654", "cand_a"),
    ("0453380125", "cand_b"),
    ("0464822341", "cand_c"),
    ("0475123890", "cand_d"),
    # search-ish known from prior deferred notes — probe a few WZC
    ("0412210456", "cand_e"),
    ("0425123789", "cand_f"),
    ("0440123456", "cand_g"),
]

# Better: scrape companyweb search? Use known list from tick2108 cand files
cand_dir = RAW.parent / "tick2108"
extra = []
if cand_dir.exists():
    for p in cand_dir.glob("cand_*_nl.html"):
        m = re.search(r"cand_(\d+)_", p.name)
        if m:
            extra.append(m.group(1))
# Also tick2084
for dname in ("tick2084", "tick2117"):
    d = RAW.parent / dname
    if d.exists():
        for p in d.glob("cand_*"):
            m = re.search(r"cand_(\d+)", p.name)
            if m:
                extra.append(m.group(1))
        for p in d.glob("*helianthus*"):
            # try extract kbo from filename or later
            pass

# Unique cands not done
seen = set()
probe_list = []
for kbo in extra + [c[0] for c in cands]:
    if kbo in seen or kbo in done_kbo:
        continue
    seen.add(kbo)
    probe_list.append(kbo)

print("=== CANDIDATES (not done_kbo) count", len(probe_list), "===")
hits_y25 = []
for kbo in probe_list[:40]:
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"cand_{kbo}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        e25 = info["euros"].get("2025")
        title = info["title"]
        # filter nursing-ish
        nurse = any(
            x in title.lower()
            for x in (
                "wzc",
                "rust",
                "repos",
                "residence",
                "résidence",
                "woon",
                "senior",
                "mrs",
                "korian",
                "charmille",
                "helianthus",
                "home",
                "asbl",
                "vzw",
            )
        )
        flag = "Y25" if info["year"] == "2025" or e25 else f"y{info['year']}"
        print(flag, kbo, title[:90], "e25", e25)
        if (info["year"] == "2025" or e25) and nurse:
            hits_y25.append((kbo, info))
    except Exception as e:
        print("ERR", kbo, e)

print("=== Y25 NURSE HITS ===")
for kbo, info in hits_y25:
    print(kbo, info["title"][:100], info["euros"].get("2025"), info["deltas"][:6])
