# -*- coding: utf-8 -*-
"""Fetch Familiezorg Gent NL/EN/FR + KBO for tick 2096."""
import re
import ssl
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8,fr;q=0.7",
}
KBO = "0412914845"
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as r:
        return r.read().decode("utf-8", errors="replace")


def parse_num(s: str) -> float:
    s = s.replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", ".")
    # NL uses . as thousands
    # after removing dots of thousands and replacing comma - but EN uses commas as thousands
    # Better: detect
    return float(s) if s else 0.0


def nl_to_int(s: str) -> int:
    # "14.782.023" or "14,782,023" or "14 782 023"
    s = s.replace("\xa0", "").replace(" ", "")
    if "," in s and "." in s:
        # ambiguous
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        # could be decimal or thousands
        parts = s.split(",")
        if len(parts[-1]) == 3 and len(parts) > 1:
            s = s.replace(",", "")
        else:
            s = s.replace(",", ".")
    else:
        # dots as thousands if multiple
        parts = s.split(".")
        if len(parts) > 1 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(".", "")
        elif len(parts) == 2 and len(parts[1]) != 3:
            pass  # decimal
        else:
            s = s.replace(".", "")
    return int(round(float(s)))


def main():
    pages = {
        "familiezorg_gent_nl.html": f"https://www.companyweb.be/nl/{KBO}/familiezorg",
        "familiezorg_gent_en.html": f"https://www.companyweb.be/en/{KBO}/familiezorg",
        "familiezorg_gent_fr.html": f"https://www.companyweb.be/fr/{KBO}/familiezorg",
        "kbo_familiezorg_gent.html": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
            f"lang=nl&ondernemingsnummer={KBO}"
        ),
    }
    for name, url in pages.items():
        html = fetch(url)
        (RAW / name).write_text(html, encoding="utf-8")
        print("OK", name, len(html))

    nl = (RAW / "familiezorg_gent_nl.html").read_text(encoding="utf-8")
    ye = re.search(r"kernCijfers\s*=\s*\{\s*(20\d\d)", nl)
    rows = PAT.findall(nl)
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', nl)
    filed = re.search(r"[Nn]eergelegd op ([0-9.\-]+)", nl)
    title = re.search(r"<title>([^<]+)</title>", nl)
    print("YE", ye.group(1) if ye else None)
    print("title", re.sub(r"\s+", " ", title.group(1)).strip() if title else None)
    print("filed", filed.group(1) if filed else None)
    print("fte", fte.group(1) if fte else None)
    for r in rows[:4]:
        print("ROW", r)
        print("  parsed", [nl_to_int(x) if i else x for i, x in enumerate(r)])

    kbo = (RAW / "kbo_familiezorg_gent.html").read_text(encoding="utf-8", errors="replace")
    for pat in [
        r"Aanbestedende overheid",
        r"Actief",
        r"vestigingseenheden[^0-9]{0,40}(\d+)",
        r"E-mail[^<]{0,80}",
        r"mailto:([^\"']+)",
        r"Webadres[^<]{0,120}",
        r"Nacebel[^<]{0,200}",
        r"87\.\d+",
        r"88\.\d+",
        r"Vogelenzang[^<]{0,40}",
    ]:
        m = re.search(pat, kbo, re.I)
        if m:
            print("KBO", pat[:40], "->", m.group(0)[:100])

    # site contact
    for url, fn in [
        ("https://www.familiezorg.be/", "site_familiezorg.html"),
        ("https://www.familiezorg.be/contact", "site_contact.html"),
    ]:
        try:
            html = fetch(url)
            (RAW / fn).write_text(html, encoding="utf-8")
            print("SITE", fn, len(html))
            emails = set(re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", html))
            print(" emails", list(emails)[:8])
        except Exception as e:
            print("SITE FAIL", url, e)


if __name__ == "__main__":
    main()
