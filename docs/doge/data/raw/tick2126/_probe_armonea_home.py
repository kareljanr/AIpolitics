# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
import pathlib

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
OUT = pathlib.Path(__file__).resolve().parent
KBO = "0500937791"


def fetch(label, url):
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
    (OUT / f"{label}.html").write_text(html, encoding="utf-8")
    return html


def extract_metric(html, label):
    idx = html.find(label)
    if idx < 0:
        return None
    chunk = re.sub(r"<[^>]+>", "|", html[idx : idx + 1800])
    chunk = re.sub(r"\s+", " ", chunk)
    # find euro amounts after label
    amounts = re.findall(r"€\s*\|\s*\|\s*([-\d,]+)", chunk)
    pcts = re.findall(r"\|\s*([<>\s-]*\d[\d.,]*%|&lt;\s*-1000%)", chunk)
    return {"chunk": chunk[:350], "amounts": amounts[:4], "pcts": pcts[:3]}


def main():
    pages = {
        "ah_en": f"https://www.companyweb.be/en/{KBO}/armonea-home",
        "ah_nl": f"https://www.companyweb.be/nl/{KBO}/armonea-home",
        "ah_fr": f"https://www.companyweb.be/fr/{KBO}/armonea-home",
        "ah_en2": f"https://www.companyweb.be/en/{KBO}",
        "ah_nl2": f"https://www.companyweb.be/nl/{KBO}",
        "ah_fr2": f"https://www.companyweb.be/fr/{KBO}",
        "ah_kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    }
    for label, url in pages.items():
        try:
            html = fetch(label, url)
            title = re.search(r"<title>([^<]+)", html)
            last = re.search(
                r"(?:Last balance sheet year|Laatste balansi?aar|Dernier exercice)[^0-9]*(\d{4})",
                html,
            )
            print(label, "ok", len(html), "title", title.group(1)[:70] if title else "?", "year", last.group(1) if last else "?")
            for lab in [
                "Turnover",
                "Omzet",
                "Chiffre d",
                "Gross margin",
                "Brutomarge",
                "Marge brute",
                "Profit/Loss",
                "Winst/Verlies",
                "Bénéfice/Perte",
                "Equity",
                "Eigen vermogen",
                "Capitaux propres",
                "Average number of employees",
                "Gemiddeld aantal werknemers",
                "Personnel",
            ]:
                m = extract_metric(html, lab)
                if m and m["amounts"]:
                    print(" ", lab, m["amounts"], m["pcts"], m["chunk"][:180])
            for pat in [
                r"filed on ([0-9-]{10})",
                r"neergelegd op ([0-9./]{8,})",
                r"déposées le ([0-9-]{10})",
                r"neerlegging[^0-9]*([0-9./-]{8,})",
            ]:
                mm = re.search(pat, html, re.I)
                if mm:
                    print("  filed", mm.group(1))
                    break
            # size / FTE elsewhere
            for pat in [
                r"Medium-sized[^0-9]*([\d.,]+)",
                r"Small[^0-9]*([\d.,]+)",
                r"Micro[^0-9]*([\d.,]+)",
                r"Large[^0-9]*([\d.,]+)",
                r">([\d]+(?:[.,]\d+)?)\s*FTE",
                r"([\d]+(?:[.,]\d+)?)\s*FTE",
            ]:
                mm = re.search(pat, html, re.I)
                if mm:
                    print("  size/fte", mm.group(0)[:80])
                    break
            print("---")
        except Exception as e:
            print(label, "ERR", e)

    # KBO details
    try:
        html = (OUT / "ah_kbo.html").read_text(encoding="utf-8", errors="ignore")
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        for needle in [
            "Rechtsvorm",
            "Status",
            "Adres",
            "Nace",
            "Vestiging",
            "Bestuur",
            "Kapitaal",
            "Armonea",
            "E-mail",
            "Webadres",
            "Nombre",
            "Forme",
        ]:
            idx = text.lower().find(needle.lower())
            if idx >= 0:
                print(text[idx : idx + 220])
    except Exception as e:
        print("kbo parse", e)


if __name__ == "__main__":
    main()
