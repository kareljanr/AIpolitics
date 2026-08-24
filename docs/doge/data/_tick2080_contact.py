# -*- coding: utf-8 -*-
import re
from pathlib import Path

raw = Path("docs/doge/data/raw/tick2080")
for name in [
    "den_akker_site.html",
    "den_akker_site2.html",
    "den_akker_sint.html",
    "den_akker_en.html",
    "den_akker_nl.html",
    "den_akker_kbo.html",
]:
    t = (raw / name).read_text(encoding="utf-8", errors="replace")
    print("====", name)
    emails = set(re.findall(r"[\w.\-+]+@[\w.\-]+\.[A-Za-z]{2,}", t))
    for e in sorted(emails):
        el = e.lower()
        if any(
            x in el
            for x in [
                "sentry",
                "companyweb",
                "w3.org",
                "schema",
                "example",
                "google",
                "facebook",
                "cloudflare",
                "ingest.",
            ]
        ):
            continue
        print(" EMAIL", e)
    for m in re.finditer(r"mailto:([^\"'\s>]+)", t, re.I):
        print(" MAILTO", m.group(1))
    for m in re.finditer(
        r"(?:tel|phone|Telefoon|T\s*:)[^0-9]{0,25}([0-9][0-9 /\.\-]{7,})", t, re.I
    ):
        print(" TEL", m.group(1).strip()[:40])
    if "aanbested" in t.lower():
        print(" has aanbestedende hint")
    # look for contact@ / info@
    for m in re.finditer(r"(info|contact|onthaal|secretariaat)@[\w.\-]+", t, re.I):
        print(" HINT", m.group(0))
