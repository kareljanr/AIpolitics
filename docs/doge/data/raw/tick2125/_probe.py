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


def main():
    urls = [
        (
            "addr_mechelen",
            "https://www.companyweb.be/en/search/address?addressQuery=2800%2bMechelen%3bStationsstraat%3b102&City=Mechelen&Country=BE&Number=102&PostalCode=2800&Street=Stationsstraat",
        ),
        (
            "addr_uccle",
            "https://www.companyweb.be/en/search/address?addressQuery=1180%2bUkkel%3bAlsembergsesteenweg%3b1037&City=Ukkel&Country=BE&Number=1037&PostalCode=1180&Street=Alsembergsesteenweg",
        ),
        (
            "addr_kontich",
            "https://www.companyweb.be/en/search/address?addressQuery=2550%2bKontich%3bSatenrozen%3b1B&City=Kontich&Country=BE&Number=1B&PostalCode=2550&Street=Satenrozen",
        ),
    ]
    for label, url in urls:
        try:
            html = fetch(label, url)
            links = re.findall(r'href="(/en/\d{10}/[^"]+)"', html)
            names = re.findall(r'<a[^>]+href="/en/\d{10}/[^"]+"[^>]*>([^<]{2,80})</a>', html)
            print(label, "len", len(html), "links", len(set(links)))
            for n, l in list(dict.fromkeys(zip(names, links)))[:25]:
                print(" ", n.strip()[:50], l)
        except Exception as e:
            print(label, "ERR", e)

    # Probe candidates that might be unused YE2025 MRS
    cands = [
        ("0445175263", "cand_0445175263"),  # from tick2108 list
        ("0452865383", "cand_0452865383"),
        ("0480566704", "cand_0480566704"),
        ("0598966387", "cand_0598966387"),
        ("0685516024", "cand_0685516024"),
        ("0877556624", "cand_0877556624"),
        ("0887690451", "cand_0887690451"),
        ("0893863017", "cand_faro"),  # FARO confirm
        ("0422620585", "cand_0422620585"),
        ("0845064196", "cand_0845064196"),
    ]
    for kbo, label in cands:
        try:
            html = fetch(label, f"https://www.companyweb.be/en/{kbo}")
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            title = re.search(r"<title>([^<]+)", html)
            print(label, "last", last.group(1) if last else None, "|", (title.group(1)[:70] if title else ""))
            idx = html.find("Financial data")
            if idx > 0:
                text = re.sub(r"<[^>]+>", " ", html[idx : idx + 5000])
                text = re.sub(r"\s+", " ", text)
                print(" ", text[:350])
        except Exception as e:
            print(label, "ERR", e)


if __name__ == "__main__":
    main()
