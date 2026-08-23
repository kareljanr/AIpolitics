# -*- coding: utf-8 -*-
"""Extract Sint-Lucia details + site contact for tick 2094."""
import re
import ssl
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


def get(url, name):
    req = urllib.request.Request(url, headers={**UA, "Accept-Language": "nl-BE,nl;q=0.9"})
    with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
        data = r.read()
    text = data.decode("utf-8", errors="replace")
    (OUT / name).write_text(text, encoding="utf-8")
    return text


def main():
    nl = (OUT / "lucia_nl.html").read_text(encoding="utf-8")
    # FTE
    for pat in [
        r'amountOfEmployees\s*=\s*"([^"]+)"',
        r'personeelsbestand[^0-9]{0,40}([0-9]+(?:[.,][0-9]+)?)',
        r'Workforce[^0-9]{0,40}([0-9]+(?:[.,][0-9]+)?)',
        r'"fte"\s*:\s*"?([0-9.]+)',
        r'VTE[^0-9]{0,20}([0-9]+(?:[.,][0-9]+)?)',
    ]:
        m = re.search(pat, nl, re.I)
        if m:
            print("FTE hit", pat[:40], m.group(1))
    # also look for chart personeel years
    idx = nl.lower().find("amountofemployees")
    if idx < 0:
        idx = nl.lower().find("personeelsbestand")
    if idx >= 0:
        print("FTE window:", re.sub(r"\s+", " ", nl[idx : idx + 500])[:400])
    # address
    for pat in [
        r"Steenweg[^<\n]{0,80}",
        r"Turnhout[^<\n]{0,40}",
        r"2300[^<\n]{0,60}",
        r"Korte[^<\n]{0,80}",
        r"Gasthuis[^<\n]{0,80}",
    ]:
        ms = re.findall(pat, nl)
        if ms:
            print("addr", pat[:20], ms[:3])
    # website mentions
    sites = sorted(
        set(
            re.findall(
                r"https?://(?:www\.)?(?:sint-?lucia|lucia|woonzorg|wzc)[a-z0-9./\-]*",
                nl,
                re.I,
            )
        )
    )
    print("sites in CW:", sites[:10])
    # VE
    for pat in [r"(\d+)\s*vestigings?eenhe", r"Establishment units[^0-9]{0,20}(\d+)"]:
        ms = re.findall(pat, nl, re.I)
        if ms:
            print("VE", ms[:5])

    # KBO deeper
    kbo = (OUT / "lucia_kbo.html").read_text(encoding="utf-8", errors="replace")
    # strip tags for readable bits
    text = re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    print("KBO snippet:", text[200:900])
    # NACE full
    for m in re.finditer(r"87\.101|88\.\d+|woonzorg|Rust|RVT|VZW", kbo, re.I):
        print("kbo kw", m.group(0), "at", m.start())
    # addresses on KBO
    for m in re.finditer(r"\d{4}\s+[A-Za-z\- ]+", text):
        if "Turnhout" in m.group(0) or m.group(0).startswith("2300"):
            print("kbo place", m.group(0)[:60])

    # try site
    for url, name in [
        ("https://www.sint-lucia.be/", "lucia_site.html"),
        ("https://sint-lucia.be/", "lucia_site2.html"),
        ("https://www.sintlucia.be/", "lucia_site3.html"),
        ("https://www.zorgbedrijfturnhout.be/", "zorgbedrijf.html"),
    ]:
        try:
            html = get(url, name)
            print("SITE OK", url, len(html))
            emails = sorted(
                set(
                    re.findall(
                        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html
                    )
                )
            )
            emails = [
                e
                for e in emails
                if not any(
                    x in e.lower()
                    for x in ["example", "sentry", "wix", "schema", "cloudflare"]
                )
            ]
            print("  emails", emails[:10])
            if "contact" in html.lower():
                print("  has contact")
        except Exception as e:
            print("SITE FAIL", url, e)

    # Bornem from prior tick copy
    prior = Path(__file__).resolve().parents[1] / "tick2086" / "bornem_jr.html"
    if prior.exists():
        html = prior.read_text(encoding="utf-8", errors="replace")
        print("PRIOR BORNEM links:")
        for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{0,100})', html, re.I):
            href, txt = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
            blob = (href + " " + txt).lower()
            if any(k in blob for k in ["jaarrekening", "agb", "2025", "2024", "pdf"]):
                print(" ", txt[:70], "->", href[:140])


if __name__ == "__main__":
    main()
