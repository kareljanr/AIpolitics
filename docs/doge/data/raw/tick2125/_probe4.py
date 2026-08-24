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


def probe_kbo(kbo):
    url = f"https://www.companyweb.be/en/{kbo}"
    try:
        html = fetch(f"x_{kbo}", url)
    except Exception as e:
        print(kbo, "ERR", e)
        return
    if "Error 404" in html[:500]:
        print(kbo, "404")
        return
    last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
    title = re.search(r"<title>([^<]+)", html)
    idx = html.find("Financial data")
    fin = ""
    if idx > 0:
        fin = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html[idx : idx + 3500]))[:280]
    print(kbo, "last", last.group(1) if last else "?", "|", (title.group(1)[:70] if title else ""))
    print(" ", fin)


def main():
    # Probe plausible unused continuum KBOs near recent fills / Charleroi MRS
    for kbo in [
        "0408123456",
        "0426830125",
        "0438123456",
        "0448123456",
        "0454123456",
        "0468123456",
        "0470123456",
        "0407125890",
        "0425620585",
        "0435620585",
        "0445620585",
        "0457620585",
        "0467620585",
        "0417958152",  # known mined?
        "0459770496",  # known
        "0440123456",
        "0420123789",
        "0460123789",
        "0470123789",
        "0480123789",
        "0409123789",
        "0419123789",
        "0429123789",
        "0439123789",
        "0449123789",
        "0459123789",
        "0469123789",
        "0479123789",
        "0406540765",
        "0416540765",
        "0426540765",
        "0436540765",
        "0446540765",
        "0456540765",
        "0466540765",
        "0476540765",
        "0408540765",
        "0418540765",
        "0428540765",
        "0438540765",
        "0448540765",
        "0458540765",
        "0468540765",
        "0478540765",
    ]:
        pass  # too random

    # Better targeted: Korian/Armonea/Vivalto leftover homes from prior notes
    targeted = [
        "0424830108",  # Stuyvenberg mined
        "0453581304",  # Buitenhof mined?
        "0405311530",  # Elisabeth mined
        "0412640671",  # Residence 3 mined
        "0466961859",  # Buissons mined
        "0451031489",  # Sittelles mined
        "0457649265",  # Charmilles mined
        "0416116637",  # La Charmille mined
        "0407699017",  # Entraide mined
        "0899812184",  # Strebo mined
        "0463961490",  # Le Bosquet mined
        "0435565236",  # Buurthuis mined
        "0748968276",  # Unite mined
        "0442694142",  # Sebrechts mined
        "0459540765",  # RSW mined
        "0462316153",  # Castel mined
        # Unused guesses from prior candidate lists / nearby
        "0443249616",  # Stil Geluk YE2024
        "0480566704",  # Hof Ter Lande YE2024
        "0422620585",  # Sint-Vincentius YE2024
        "0787300696",  # Melis Home YE2025 UNUSED small
        "0598966387",  # Hoeksteen empty
        "0685516024",  # Edegem empty
        # Try more Armonea sister ops entities
        "0869703978",  # companyweb itself
        "0410958712",  # SLG VZW
        "0889421308",  # Armonea holding
        "0821289991",  # Always Home
        "0845064196",  # SLG Operaties
        # Try other MRS KBOs spotted in tick folders
        "0412210456",
        "0425123789",
        "0438687654",
        "0453380125",
        "0464822341",
        "0475123890",
        "0466266429",
        # Wood Side
        "0441675147",
        # Additional continuum: try Home Fabiola / similar via known Belgian MRS KBOs
        "0406401234",
        "0428401234",
        "0448401234",
        "0468401234",
        "0409405678",
        "0429405678",
        "0449405678",
        "0469405678",
    ]
    # Only probe a tighter useful set
    useful = [
        "0787300696",
        "0889421308",  # Armonea
        "0410958712",  # SLG VZW
        "0441675147",
        "0443249616",
        "0422620585",
        "0480566704",
        # Try finding Le Planty / Buissonnets legal entity via KBO search POST later
    ]
    for kbo in useful:
        probe_kbo(kbo)

    # KBO phonetic via POST form
    import urllib.parse

    for q in ["Buissonnets", "Chartriers Mons", "Longtain", "Planty", "Melis Home"]:
        data = urllib.parse.urlencode(
            {"searchWord": q, "filterEnkelActieve": "true", "_ou": ""}
        ).encode()
        req = urllib.request.Request(
            "https://kbopub.economie.fgov.be/kbopub/zoeknaamfonetischform.html",
            data=data,
            headers={**UA, "Content-Type": "application/x-www-form-urlencoded"},
        )
        try:
            html = urllib.request.urlopen(req, timeout=30, context=ctx).read().decode("utf-8", "replace")
            open(f"kboq_{q[:12].replace(' ', '_')}.html", "w", encoding="utf-8").write(html)
            nums = re.findall(r"ondernemingsnummer=(\d+)", html)
            # names near
            names = re.findall(r"<a[^>]+ondernemingsnummer=(\d+)[^>]*>\s*([^<]{0,80})", html)
            print("Q", q, "nums", nums[:8], "pairs", names[:8])
        except Exception as e:
            print("Q", q, "ERR", e)


if __name__ == "__main__":
    main()
