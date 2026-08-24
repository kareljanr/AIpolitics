# -*- coding: utf-8 -*-
import re
from pathlib import Path
from html.parser import HTMLParser
kbo=Path("docs/doge/data/raw/tick2143/careion_kbo.html").read_text(encoding="utf-8", errors="replace")
# strip tags lightly
text=re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
text=re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text=re.sub(r"<[^>]+>", "\n", text)
text=re.sub(r"\n+", "\n", text)
lines=[l.strip() for l in text.splitlines() if l.strip()]
for i,l in enumerate(lines):
    if any(k in l.lower() for k in ["status","rechtsvorm","adres","straat","anderlecht","vestiging","nace","naam","begindatum","ondernemingsnummer","email","e-mail","btw","actief","stopgezet","aanbested"]):
        print(f"{i}: {l}")
        for j in range(1,3):
            if i+j < len(lines):
                print(f"   +{j}: {lines[i+j]}")
en=Path("docs/doge/data/raw/tick2143/careion_cw_en.html").read_text(encoding="utf-8", errors="replace")
# extract useful
for pat in [r"Principal activity[^<\n]{0,120}", r"Established[^<\n]{0,80}", r"Company size[^<\n]{0,80}", r"VAT[^<\n]{0,80}", r"Commercial name[^<\n]{0,120}", r"Address[^<\n]{0,160}", r"email[^\"'<> ]{0,60}", r"info@[a-zA-Z0-9.\-]+", r"@[a-zA-Z0-9.\-]+\.[a-z]{2,}", r"NACE[^<\n]{0,120}", r"Website[^<\n]{0,120}"]:
    ms=re.findall(pat, en, re.I)
    if ms:
        print("EN", pat[:30], "=>", ms[:3])
# try find site
for pat in [r"https?://[a-zA-Z0-9./\-]+care[^\"'<> ]*", r"https?://[a-zA-Z0-9./\-]*seniors[^\"'<> ]*", r"https?://[a-zA-Z0-9./\-]*ion[^\"'<> ]*"]:
    ms=re.findall(pat, en, re.I)
    print("url", pat[:40], ms[:5])
