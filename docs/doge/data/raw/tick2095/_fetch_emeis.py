# -*- coding: utf-8 -*-
"""Fetch emeis Belgium NL/EN/FR + KBO + site for tick 2095."""
import re
import ssl
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
KBO = "0887690451"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")


def num_eu(s: str) -> int:
    s = s.strip().replace("\xa0", "").replace(" ", "")
    # NL: 19.633.819 or EN: 19,633,819 or FR: 19 633 819 / 19.633.819
    if re.match(r"^-?\d{1,3}(\.\d{3})+$", s) or re.match(r"^-?\d{1,3}(\.\d{3})+,\d+$", s):
        s = s.replace(".", "").replace(",", ".")
    elif "," in s and "." in s:
        # EN style 19,633,819
        s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".")
    s = re.sub(r"[^\d.\-]", "", s)
    if "." in s and s.count(".") == 1 and len(s.split(".")[-1]) <= 2:
        return int(float(s))
    return int(float(s)) if s else 0


def main():
    pages = {
        "emeis_nl.html": f"https://www.companyweb.be/nl/{KBO}/emeis-belgium",
        "emeis_en.html": f"https://www.companyweb.be/en/{KBO}/emeis-belgium",
        "emeis_fr.html": f"https://www.companyweb.be/fr/{KBO}/emeis-belgium",
        "emeis_kbo.html": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO}",
    }
    for name, url in pages.items():
        html = fetch(url)
        (RAW / name).write_text(html, encoding="utf-8")
        print("OK", name, len(html))

    nl = (RAW / "emeis_nl.html").read_text(encoding="utf-8")
    rows = list(PAT.finditer(nl))
    for m in rows[:3]:
        print("YR", m.group(1), "winst", m.group(2), "eq", m.group(3), "bruto", m.group(4), "omzet", m.group(5))
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', nl)
    filed = re.search(r"[Nn]eergelegd op ([0-9.\-]+)", nl)
    addr = re.search(
        r'"straatNaam":\s*"([^"]+)",\s*"huisNummer":\s*"([^"]*)".*?"postcode":\s*"([^"]+)",\s*"gemeente":\s*"([^"]+)"',
        nl,
        re.S,
    )
    print("FTE", fte.group(1) if fte else None)
    print("filed", filed.group(1) if filed else None)
    if addr:
        print("addr", addr.group(1), addr.group(2), addr.group(3), addr.group(4))

    # YoY from first two years
    def parse_row(m):
        return {
            "y": int(m.group(1)),
            "pnl": num_eu(m.group(2)),
            "eq": num_eu(m.group(3)),
            "bruto": num_eu(m.group(4)),
            "omzet": num_eu(m.group(5)),
        }

    y25 = parse_row(rows[0])
    y24 = parse_row(rows[1])

    def pct(a, b):
        if b == 0:
            return "n/a"
        return f"{(a - b) / abs(b) * 100:+.2f}%"

    print("OMZET", y25["omzet"], pct(y25["omzet"], y24["omzet"]), "vs", y24["omzet"])
    print("BRUTO", y25["bruto"], pct(y25["bruto"], y24["bruto"]), "vs", y24["bruto"])
    print("PNL", y25["pnl"], pct(y25["pnl"], y24["pnl"]), "vs", y24["pnl"])
    print("EQ", y25["eq"], pct(y25["eq"], y24["eq"]), "vs", y24["eq"])

    # KBO details
    kbo = (RAW / "emeis_kbo.html").read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    print("KBO snippet:", text[180:900])
    ve = re.search(r"Aantal vestigingseenheden[^0-9]{0,40}(\d+)", kbo, re.I)
    print("VE", ve.group(1) if ve else None)
    for m in re.finditer(r"87\.\d{3}|88\.\d{3}|86\.\d{3}|68\.\d{3}", kbo):
        print("NACE", m.group(0))
        break

    # site
    for url, name in [
        ("https://www.emeis.be/", "emeis_site.html"),
        ("https://emeis.be/", "emeis_site2.html"),
        ("https://www.emeis.com/be-nl/", "emeis_site3.html"),
        ("https://www.emeis.com/be-fr/", "emeis_site4.html"),
    ]:
        try:
            html = fetch(url)
            (RAW / name).write_text(html, encoding="utf-8")
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
                    for x in ["example", "sentry", "wix", "schema", "cloudflare", "google"]
                )
            ]
            print("SITE", url, len(html), emails[:8])
        except Exception as e:
            print("SITE FAIL", url, e)


if __name__ == "__main__":
    main()
