# -*- coding: utf-8 -*-
import re
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
for name in ("wilgendries.html", "wilgendries_home.html", "ninove_nl.html", "ninove_kbo_nl.html"):
    p = RAW / name
    if not p.exists():
        print("missing", name)
        continue
    html = p.read_text(encoding="utf-8", errors="ignore")
    print("===", name)
    print("mailto", re.findall(r"mailto:([^\"'\s>]+)", html, re.I)[:10])
    print("email", re.findall(r"[\w.+-]+@[\w.-]+\.\w+", html)[:20])
    text = unescape(re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.I | re.S))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    for key in ("email", "E-mail", "maatschappelijke", "Wilgendries", "Geraards"):
        idx = text.find(key)
        if idx >= 0:
            print(key, "->", text[idx : idx + 280])
