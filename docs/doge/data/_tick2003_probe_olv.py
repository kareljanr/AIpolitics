# ephemeral tick2003 — OLV Aalst trilang + KBO + site
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2003")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))
    return data.decode("utf-8", errors="replace")


for name, url in [
    ("olv_fr", "https://www.companyweb.be/fr/0410424222"),
    ("olv_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410424222"),
    ("olv_site", "https://www.olvz.be/"),
]:
    try:
        t = fetch(name, url)
        if "kbo" in name:
            clean = re.sub(r"<[^>]+>", " ", t)
            clean = re.sub(r"\s+", " ", clean)
            for needle in [
                "Actief",
                "Rechtsvorm",
                "E-mail",
                "Webadres",
                "Aalst",
                "OLV",
                "Aanbested",
                "vestiging",
                "Moorselbaan",
            ]:
                i = clean.lower().find(needle.lower())
                if i >= 0:
                    print("KBO", needle, repr(clean[max(0, i - 30) : i + 140]))
            print("emails", sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", clean)))[:10])
        elif "site" in name:
            emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))
            print("site emails", [e for e in emails if not e.endswith(".png")][:15])
            title = re.search(r"<title>([^<]+)</title>", t)
            print("title", title.group(1)[:120] if title else None)
        else:
            blocks = re.findall(
                r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
                t,
            )
            print("blocks", blocks[:2])
            i = t.find("déposés le")
            if i >= 0:
                print("filed", repr(t[i : i + 80]))
            em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
            print("FTE", em[:2])
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
