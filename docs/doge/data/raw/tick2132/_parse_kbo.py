# -*- coding: utf-8 -*-
import re
from pathlib import Path
from html.parser import HTMLParser

html = Path("docs/doge/data/raw/tick2132/maagd_kbo.html").read_text(
    encoding="utf-8", errors="replace"
)
text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", "\n", text)
text = re.sub(r"\n+", "\n", text)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
Path("docs/doge/data/raw/tick2132/maagd_kbo.txt").write_text(
    "\n".join(lines), encoding="utf-8"
)
for i, ln in enumerate(lines):
    low = ln.lower()
    if any(
        k in low
        for k in [
            "status",
            "rechtsvorm",
            "adres",
            "straat",
            "nace",
            "vestiging",
            "functie",
            "naam",
            "actief",
            "vzw",
            "aalst",
            "rozen",
        ]
    ):
        print(f"{i}: {ln}")
