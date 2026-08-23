# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2085")
for lang in ["nl", "en", "fr"]:
    t = (RAW / f"medemens_{lang}.html").read_text(encoding="utf-8", errors="replace")
    print("===", lang)
    print("amount", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t).group(1))
    print("spans", re.findall(r"<span>([\d.,]+)</span>", t)[:8])
    # personnel series in js
    for key in ["personeel", "fte", "employees"]:
        ms = re.findall(rf"{key}[\"']?\s*:\s*[\"']?([\d.,]+)", t, re.I)
        if ms:
            print(key, ms[:6])

site = (RAW / "med_site.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", site)))
print("emails", [e for e in emails if "sentry" not in e.lower() and "wix" not in e.lower()][:20])
for m in re.finditer(r"mailto:([^\"'\s>]+)", site, re.I):
    print("MAILTO", m.group(1))

# contact page
UA = "Mozilla/5.0"
for name, url in [
    ("med_contact.html", "https://www.demedemens.be/contact"),
    ("med_contact2.html", "https://www.demedemens.be/nl/contact"),
]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
        text = data.decode("utf-8", "replace")
        text = re.sub(r"pk\.[A-Za-z0-9._\-]+", "pk.REDACTED", text)
        (RAW / name).write_text(text, encoding="utf-8")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)))
        emails = [e for e in emails if not any(x in e.lower() for x in ("sentry", "wix", "example", "cloudflare", "redacted"))]
        print(name, emails[:10])
    except Exception as e:
        print("FAIL", name, e)
