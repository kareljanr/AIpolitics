from pathlib import Path
import re
import ssl
import urllib.request

dst = Path("docs/doge/data/raw/tick2010")
t = (dst / "zorgkas_kbo.html").read_text(encoding="utf-8", errors="replace")
for lab in [
    "Status",
    "Actief",
    "Naam",
    "vestigingseenheden",
    "E-mail",
    "Webadres",
    "Adres",
    "Rechtsvorm",
    "Oprichting",
]:
    i = t.find(lab)
    if i >= 0:
        print(lab, repr(t[i : i + 200]))

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
for name, url in [
    ("zorgkas_site2", "https://www.vlaamsezorgkas.be/nl"),
    ("zorgkas_contact", "https://www.vlaamsezorgkas.be/nl/contact"),
    ("zorgkas_info", "https://www.vlaanderen.be/vlaamse-zorgkas"),
]:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data), resp.geturl()[:120])
        txt = data.decode("utf-8", errors="replace")
        emails = sorted(
            set(
                re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", txt)
            )
        )
        print(" emails", [e for e in emails if "sentry" not in e and "wix" not in e][:15])
    except Exception as e:
        print("FAIL", name, e)
