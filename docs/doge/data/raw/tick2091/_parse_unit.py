# -*- coding: utf-8 -*-
import re
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2091")
t = (RAW / "sed_nl.html").read_text(encoding="utf-8", errors="replace")
kt = (RAW / "kbo_sed.html").read_text(encoding="utf-8", errors="replace")

for pat in [
    r'"website"\s*:\s*"([^"]+)"',
    r'"email"\s*:\s*"([^"]+)"',
    r'"telephone"\s*:\s*"([^"]+)"',
    r'"streetAddress"\s*:\s*"([^"]+)"',
    r'"postalCode"\s*:\s*"([^"]+)"',
    r'"addressLocality"\s*:\s*"([^"]+)"',
    r'itemprop="url"[^>]*href="([^"]+)"',
    r'itemprop="email"[^>]*>([^<]+)',
    r"Hoofdactiviteit.*?<[^>]+>([^<]{5,120})",
    r'amountOfEmployeesPrev\s*=\s*"([^"]+)"',
    r'previousAmountOfEmployees\s*=\s*"([^"]+)"',
    r"commerci[^<]{0,40}</[^>]*>\s*<[^>]+>([^<]+)",
    r"Volledige naam</[^>]*>\s*<[^>]+>([^<]+)",
    r"www\.[a-z0-9.\-]+",
    r"[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}",
]:
    ms = list(re.finditer(pat, t, re.I | re.S))
    for m in ms[:5]:
        val = m.group(1) if m.lastindex else m.group(0)
        print("NL", pat[:55], "->", val[:140])

print("---KBO---")
text = re.sub(r"<script[\s\S]*?</script>", " ", kt)
text = re.sub(r"<style[\s\S]*?</style>", " ", text)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"&nbsp;", " ", text)
text = re.sub(r"\s+", " ", text)
for key in [
    "Status",
    "Actief",
    "Stationsstraat",
    "3440",
    "Zoutleeuw",
    "Aanbestedende",
    "vestigingseenhe",
    "RSZ",
    "BTW",
    "Nace",
    "87.",
    "88.",
    "www",
    "@",
    "SINT-ELISABETH",
    "Elisabeth",
]:
    low = text.lower()
    k = key.lower()
    if k in low:
        i = low.index(k)
        print(key, "::", text[max(0, i - 50) : i + 100])

# count VE from KBO page structure
ves = re.findall(r"vestigingseenheid|Établissement", kt, re.I)
print("VE mentions", len(ves))
