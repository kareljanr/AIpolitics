# fetch christine site ignoring SSL hostname mismatch
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2060")
ctx = ssl._create_unverified_context()


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / name).write_text(html, encoding="utf-8")
    print(name, len(html), url)
    return html


for u in [
    "https://www.wzcchristine.be/",
    "https://wzcchristine.be/",
    "https://www.rvtchristine.be/",
]:
    try:
        html = fetch("christine_site.html", u)
        emails = sorted(
            {
                m
                for m in re.findall(r"[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}", html)
                if not any(x in m.lower() for x in ["wix", "sentry", "google", "schema", "example"])
            }
        )
        print("EMAILS", emails[:15])
        title = re.search(r"<title>([^<]+)", html)
        print("TITLE", title.group(1) if title else None)
        break
    except Exception as e:
        print("FAIL", u, type(e).__name__, str(e)[:140])

# brochure PDF note
try:
    fetch(
        "christine_brochure.pdf",
        "https://www.rvtchristine.be/uploads/3/1/4/5/31452447/vast_verblijf.pdf",
    )
except Exception as e:
    print("PDF FAIL", type(e).__name__, str(e)[:140])
