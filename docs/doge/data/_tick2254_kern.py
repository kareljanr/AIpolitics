# -*- coding: utf-8 -*-
import re
import json
from pathlib import Path

OUT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2254")

for lang in ["en", "nl", "fr"]:
    t = (OUT / f"erables_{lang}.html").read_text(encoding="utf-8", errors="replace")
    print("====", lang)
    m = re.search(r"window\.cw\.kernCijfers\s*=\s*(\{.*?\});\s*window", t, re.S)
    if not m:
        m = re.search(r"kernCijfers\s*=\s*(\{.*?\});", t, re.S)
    if m:
        raw = m.group(1)
        # JS object may use unquoted keys / single quotes — normalize lightly
        print(raw[:1500])
        print("---")
    else:
        print("no kernCijfers")
    # alternate: chart datasets
    for pat in [
        r"brutomarge[^\n]{0,200}",
        r"eigenVermogen[^\n]{0,200}",
        r"Gross margin[^\n]{0,200}",
        r"Equity[^\n]{0,200}",
        r'"bruto[^"]*"\s*:\s*"([^"]+)"',
        r'"equity[^"]*"\s*:\s*"([^"]+)"',
        r"Marge brute.{0,300}",
        r"Capitaux propres.{0,300}",
    ]:
        ms = re.findall(pat, t, re.I)
        if ms:
            print(pat[:40], [re.sub(r"\s+", " ", str(x))[:120] for x in ms[:4]])
