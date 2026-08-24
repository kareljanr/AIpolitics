# ephemeral site contact hunt tick2066
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2066")


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / name).write_text(html, encoding="utf-8")
    print(name, len(html), url)
    return html


candidates = [
    ("site_home.html", "https://www.svbejaardenzorg.be/"),
    ("site_contact.html", "https://www.svbejaardenzorg.be/contact/contactpersonen"),
    ("site_wzc.html", "https://www.svbejaardenzorg.be/main-aanbod/main-wzc"),
    ("site_bare.html", "http://www.svbejaardenzorg.be/"),
]

for name, url in candidates:
    try:
        html = fetch(name, url)
        emails = sorted(
            {
                m
                for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html)
                if not any(
                    x in m.lower()
                    for x in ["wix", "sentry", "example", "schema", "google", "cookie"]
                )
            }
        )
        print("EMAILS", name, emails[:15])
        tels = re.findall(r"(?:\+32|0)\s?[\d\s./\-]{7,}", html)
        print("TELS", name, tels[:8])
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:140])
