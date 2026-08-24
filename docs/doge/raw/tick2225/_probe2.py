import re
import ssl
import urllib.request
from pathlib import Path

CTX = ssl.create_default_context()
OUT = Path(__file__).resolve().parent

# Enrich Reset: site, FTE YoY, NBB search page, full kern
urls = {
    "reset_site": "https://www.resetgenk.be/",
    "reset_site2": "https://reset.be/",
    "reset_nl_full": "https://www.companyweb.be/nl/0460015174/reset",
    "nbb_search": "https://consult.cbso.nbb.be/consult-enterprise/0460015174",
}

for k, u in urls.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        (OUT / f"{k}.html").write_text(html, encoding="utf-8")
        print("====", k, len(html), final)
        emails = sorted(
            set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))
        )
        print(
            "emails",
            [e for e in emails if "sentry" not in e and "wix" not in e.lower()][:12],
        )
        # FTE series if present
        for pat in [
            r"Personeel</th>.*?</tr>\s*<tr[^>]*>(.*?)</tr>",
            r"amountOfEmployees\s*=\s*\"([^\"]+)\"",
            r">(\d+[.,]?\d*)\s*FTE<",
        ]:
            ms = re.findall(pat, html, re.S | re.I)
            if ms:
                print("fte-ish", pat[:30], str(ms[0])[:200])
        # deposit refs
        deps = re.findall(r"2026-\d{8}", html)
        if deps:
            print("deps", deps[:8])
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        if "reset" in k and "site" in k:
            print("snip", text[:400])
    except Exception as e:
        print(k, type(e).__name__, e)

# deltas
om25, om24 = 6054875, 5450363
br25, br24 = 8910909, 8270329
pn25, pn24 = 19665, 134396
eq25, eq24 = 8275359, 8313051
print("omzet pct", round((om25 / om24 - 1) * 100, 2))
print("bruto pct", round((br25 / br24 - 1) * 100, 2))
print("bruto/omzet", round(br25 / om25, 2))
print("pnl pct", round((pn25 / pn24 - 1) * 100, 2))
print("equity pct", round((eq25 / eq24 - 1) * 100, 2))
