# ephemeral tick2002 probe3 — Emmaüs / AZ Sint-Maarten full trilang + KBO + site
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2002")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data), url)
    return data.decode("utf-8", errors="replace")


def summarize(name, t):
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:140] if title else None))
    print(" blocks", blocks[:3])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "déposés le", "Employees"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 140]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:3])
    # activity / legal form markers
    for needle in ["Principal activity", "Hoofdactiviteit", "Activité principale", "Hospital", "ziekenhuis", "VZW", "ASBL"]:
        i = t.find(needle)
        if i >= 0:
            print(" ", needle, repr(t[i : i + 100]))
    print()


urls = [
    ("emmaus_en", "https://www.companyweb.be/en/0411515075"),
    ("emmaus_nl", "https://www.companyweb.be/nl/0411515075"),
    ("emmaus_fr", "https://www.companyweb.be/fr/0411515075"),
    ("emmaus_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411515075"),
    ("sintmaarten_site", "https://www.azsintmaarten.be/"),
    ("emmaus_site", "https://www.emmaus.be/"),
    # also try AZ Monica correct search via known patterns
    ("monica_en", "https://www.companyweb.be/en/search?query=AZ+Monica+Deurne"),
]

for name, url in urls:
    try:
        t = fetch(name, url)
        if "kbo" in name:
            clean = re.sub(r"<[^>]+>", " ", t)
            clean = re.sub(r"\s+", " ", clean)
            for needle in [
                "Actief",
                "Rechtsvorm",
                "E-mailadres",
                "E-mail",
                "Webadres",
                "Maatschappelijke",
                "Emma",
                "Sint-Maarten",
                "vestiging",
                "Aanbested",
            ]:
                i = clean.lower().find(needle.lower())
                if i >= 0:
                    print("KBO", needle, repr(clean[max(0, i - 30) : i + 140]))
            emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", clean)))
            print("KBO emails", emails[:10])
        elif "site" in name:
            emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))
            print("site emails", emails[:20])
            title = re.search(r"<title>([^<]+)</title>", t)
            print("site title", title.group(1)[:120] if title else None)
        else:
            summarize(name, t)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
