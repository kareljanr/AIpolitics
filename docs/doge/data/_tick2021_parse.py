# ephemeral parse tick2021 PPC Pittem
import json
import re
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2021")
en = (outdir / "ppc_pittem_en.html").read_text(encoding="utf-8")
nl = (outdir / "ppc_pittem.html").read_text(encoding="utf-8")
fr = (outdir / "ppc_pittem_fr.html").read_text(encoding="utf-8")

# extract chart/vue data blobs
for label, html in [("EN", en), ("NL", nl), ("FR", fr)]:
    keys = [
        "omzet",
        "winst",
        "verlies",
        "eigenVermogen",
        "brutoMarge",
        "personeel",
        "turnover",
        "profit",
        "equity",
        "gross",
        "employees",
        "chiffre",
        "benefice",
        "capitaux",
        "marge",
        "personnel",
    ]
    found = {}
    for k in keys:
        ms = re.findall(rf'{k}\s*[:=]\s*"?([0-9][0-9.,\s\xa0]+)"?', html, re.I)
        if ms:
            found[k] = ms[:6]
    print(label, "keys", found)

# table-ish numbers near Financial
idx = en.find("Financial data")
snip = en[idx : idx + 8000] if idx >= 0 else en[:8000]
(outdir / "ppc_pittem_fin_snip.txt").write_text(snip, encoding="utf-8")
print("SNIP_HEAD", snip[:1500].replace("\n", " | "))

# Look for JSON arrays of yearly figures
for pat in [
    r"categories\s*:\s*(\[[^\]]+\])",
    r"series\s*:\s*(\[[\s\S]{0,2000}?\])",
    r"omzet:\s*\"([^\"]+)\"",
    r"winst[^:]*:\s*\"([^\"]+)\"",
    r"eigenVermogen:\s*\"([^\"]+)\"",
    r"brutoMarge:\s*\"([^\"]+)\"",
    r"personeel:\s*\"([^\"]+)\"",
]:
    ms = re.findall(pat, en)
    print("PAT", pat[:40], "->", ms[:8])

# filing date
for lab in ["Filing date", "Neerleggingsdatum", "Date de dépôt", "neergelegd"]:
    i = en.lower().find(lab.lower())
    if i < 0:
        i = nl.lower().find(lab.lower())
        src = nl
    else:
        src = en
    if i >= 0:
        print("FILING_CTX", lab, src[i : i + 200].replace("\n", " "))

# emails / website
for html in (en, nl):
    emails = set(re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html))
    print("emails", emails)
    sites = re.findall(r"https?://(?:www\.)?(?:ppc|kliniek|pittem|sint-?jozef)[^\s\"'<>]+", html, re.I)
    print("sites", sites[:10])
