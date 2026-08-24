# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218")

for name in ["veerkracht4_en.html", "opnieuw_en.html", "nbsw_en.html"]:
    t = (out / name).read_text(encoding="utf-8", errors="ignore")
    print("\n####", name)
    # find Nuxt/vue payload with financial years
    # companyweb often has window.__NUXT__ or similar
    for pat in [
        r"__NUXT__\s*=\s*(\{.+?\});?\s*</script>",
        r"financials\s*[:=]\s*(\{.+?\})",
        r"bookYears\s*[:=]\s*(\[.+?\])",
    ]:
        m = re.search(pat, t, re.S)
        if m:
            print(" hit", pat[:30], "len", len(m.group(1)))

    # Extract year blocks like 2025:{...}
    blocks = re.findall(r"(20(?:24|25))\s*:\s*(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})", t)
    print(" year blocks", len(blocks))
    for y, blk in blocks[:4]:
        # key numeric fields
        keys = [
            "omzet",
            "turnover",
            "bruto",
            "gross",
            "winst",
            "profit",
            "equity",
            "eigen",
            "fte",
            "employees",
            "marge",
            "result",
        ]
        hits = []
        for k in keys:
            for mm in re.finditer(rf'"{k}[^"]*"\s*:\s*(-?\d+(?:\.\d+)?)', blk, re.I):
                hits.append((mm.group(0)[:80]))
        print(" ", y, "hits", hits[:12], "blk_snip", blk[:200].replace("\n", " "))

    # Also look for visible table numbers near labels
    for lab in [
        "Turnover",
        "Gross margin",
        "Profit/Loss",
        "Equity",
        "Employees",
        "Added value",
        "Staff costs",
    ]:
        # after label, find euro amounts
        ms = re.findall(
            rf"{lab}.{{0,400}}?€\s*([\d\.\s]+(?:,\d+)?)", t, re.S | re.I
        )
        print(" ", lab, "euros", ms[:6])

    # try JSON.parse of financial object in script
    for m in re.finditer(r"(\{[^{}]*\"2025\"[^{}]*\{[^{}]{20,800}\}[^{}]*\})", t):
        snip = m.group(1)[:300]
        if "omzet" in snip.lower() or "turnover" in snip.lower() or "marge" in snip:
            print(" candidate json", snip[:250])
            break
