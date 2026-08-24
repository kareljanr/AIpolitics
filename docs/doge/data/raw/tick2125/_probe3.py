# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def fetch(label, url):
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=30, context=ctx).read().decode("utf-8", "replace")
    open(label + ".html", "w", encoding="utf-8").write(html)
    return html


def summarize(label, html):
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html) or re.search(
        r"Laatste balansi?aar[^0-9]*(\d{4})", html
    ) or re.search(r"Dernier exercice[^0-9]*(\d{4})", html)
    title = re.search(r"<title>([^<]+)", html)
    print(label, "last", last.group(1) if last else "?", "|", (title.group(1)[:80] if title else ""))
    for key in ["Financial data", "Financiële gegevens", "Données financières"]:
        idx = html.find(key)
        if idx > 0:
            text = re.sub(r"<[^>]+>", " ", html[idx : idx + 6000])
            text = re.sub(r"\s+", " ", text)
            print(" ", text[:500])
            break
    # filed date
    for pat in [r"filed on ([0-9-]{10})", r"neergelegd op ([0-9./]{8,})", r"déposées le ([0-9-]{10})"]:
        m = re.search(pat, html, re.I)
        if m:
            print("  filed", m.group(1))


def main():
    for label, url in [
        ("hoeksteen_nl", "https://www.companyweb.be/nl/0598966387/de-hoeksteen"),
        ("hoeksteen_en", "https://www.companyweb.be/en/0598966387/de-hoeksteen"),
        ("edegem_nl", "https://www.companyweb.be/nl/0685516024"),
        ("edegem_en", "https://www.companyweb.be/en/0685516024"),
        ("stilgeluk_en", "https://www.companyweb.be/en/0443249616/rusthuis-stil-geluk"),
        # Armonea/Colisee related guesses - Home Van Dievoet etc
        ("pappers_nace", "https://www.pappers.be/fr/recherche?q=maison+de+repos&code_naf=87.30"),
    ]:
        try:
            html = fetch(label, url)
            summarize(label, html)
            print("---")
        except Exception as e:
            print(label, "ERR", e)

    # Try Hainaut DI list / websoc for homes near Castel
    try:
        html = fetch(
            "hainaut_di",
            "https://websoc.hainaut.be/Recherche.aspx?Type=MR",
        )
        print("hainaut len", len(html))
    except Exception as e:
        print("hainaut ERR", e)

    # Probe a few more known Armonea homes via google-ish companyweb slugs
    for slug_kbo in [
        ("0432829147", "home-bethanie"),
        ("0405406887", "x"),
        ("0461234567", "x"),
        ("0417958152", "known"),  # already YES in entities
        ("0459770496", "known2"),
    ]:
        pass

    # Search companyweb by name for unused Jolimont
    for name in [
        "Les+Buissonnets",
        "Les+Chartriers",
        "La+Visitation+Lobbes",
        "Comme+Chez+Soi+Ecaussinnes",
        "Seniorie+de+Longtain",
        "Notre-Dame+de+la+Fontaine+Chievres",
    ]:
        url = f"https://www.companyweb.be/nl/{name}"  # won't work
        # Use KBO public search phonetic via GET if available
        try:
            q = name.replace("+", " ")
            html = fetch(
                f"kbo_{name[:12]}",
                f"https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetisch.html?searchWord={urllib.parse.quote(q)}&_ou=&filterEnkelActieve=true",
            )
            # extract ondernemingsnummer links
            nums = re.findall(r"ondernemingsnummer=(\d+)", html)
            print("KBO", name, nums[:8])
        except Exception as e:
            print("KBO", name, "ERR", e)


import urllib.parse

if __name__ == "__main__":
    main()
