# -*- coding: utf-8 -*-
"""Hunt unused YE2025 WZC/zorg after SLG for tick 2100 hole-fill."""
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

done = set()
for path in [
    Path("docs/doge/data/entities.csv"),
    Path("docs/doge/data/commitments.csv"),
    Path("docs/doge/data/leaderboard.csv"),
]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            blob = " ".join(str(v or "") for v in row.values())
            for m in re.findall(r"0\d{9}|\d{4}\.\d{3}\.\d{3}", blob):
                done.add(re.sub(r"\D", "", m))

# Explicitly already done this sprint
done.update(
    {
        "0845064196",  # SLG
        "0627818345",  # AREWAL
        "0412914845",  # Familiezorg Gent
        "0887690451",  # emeis
        "0428374764",  # Begralim
        "0410151137",  # Sint-Lucia
        "0407601720",  # Lidwina
        "0413653827",  # SED
        "0471475527",  # Zilvervogel
        "0405112085",  # Familiezorg WV
        "0410853396",  # De Lovie
        "0877556624",  # AGB Bornem
        "0893863017",  # FARO
        "0201712587",  # AIESH
        "0644638937",  # REW
        "0889421308",  # Armonea
        "0723858144",  # Colisee
    }
)

cands = [
    ("0869769702", "korian-belgium"),
    ("0410958712", "senior-living-group-vlaanderen"),
    ("0415018755", "cand0415"),
    ("0425123456", "skip"),
    ("0409123456", "skip2"),
    ("0478123987", "cand"),
    ("0432505281", "rustoord-t-hoge"),
    ("0422620585", "wzc-sint-vincentius-erpe"),
    ("0471977452", "gpn-sz-wl"),
    ("0441313178", "kalvermarkt"),
    ("0480566704", "hof-ter-lande"),
    ("0598966387", "de-hoeksteen"),
    ("0685516024", "woonzorgnetwerk-edegem"),
    ("0406687990", "huis-perrekes"),
    ("0425728191", "ter-lammeken"),
    ("0475345821", "avondvrede"),
    ("0409705825", "de-mijlpaal"),
    ("0432161685", "ter-linden"),
    ("0405308859", "bethanie"),
    ("0418176295", "magnolia"),
    ("0421974538", "onderdale"),
    ("0438562119", "de-bijster"),
    ("0427819403", "zonnig-huis"),
    ("0419447286", "gielsbos"),
    ("0406912358", "philippus"),
    ("0462914805", "de-meander"),
    ("0473105916", "sint-anna-wzc"),
    ("0484216027", "sint-rochus"),
    ("0407890112", "den-houtmolen"),
    ("0413901223", "huize-van-waas"),
    ("0426531872", "sint-jozef-herent"),
    ("0448753094", "witte-meersen"),
    ("0459864105", "centrum-gheel"),
    ("0460975216", "pc-gheel"),
    ("0471086327", "olivetenhof"),
    ("0413203073", "cwzc-zonhoven"),  # already mined YE2024?
    ("0454090355", "zusters-deinze"),  # mined
    ("0521970559", "vulpia"),  # mined
    ("0408223456", "x"),
    ("0461563315", "sj-brugge"),  # mined
    ("0414703293", "mater-amabilis"),
    ("0431632776", "de-zwaluw"),
    ("0475837260", "ten-anker"),
    ("0639973732", "den-akker"),
    ("0428659430", "mater-dei"),
    ("0449425546", "wijshage"),
    ("0424830108", "stuyvenberg"),
    ("0416493254", "ben"),
    ("0459770496", "augustinus"),
    ("0428692191", "medemens"),
    ("0418352387", "lindelo"),
    ("0443072838", "ocura"),
    # more plausible unused
    ("0406554321", "a"),
    ("0411667788", "b"),
    ("0422778899", "c"),
    ("0433889900", "d"),
    ("0444990011", "e"),
    ("0455001122", "f"),
    ("0466112233", "g"),
    ("0477223344", "h"),
    ("0488334455", "i"),
    ("0401445566", "j"),
    ("0412556677", "k"),
    ("0423667788", "l"),
    ("0434778899", "m"),
    ("0445889900", "n"),
    ("0456990011", "o"),
    ("0467001122", "p"),
    ("0478112233", "q"),
    ("0489223344", "r"),
    ("0400334455", "s"),
    ("0411445566", "t"),
    # known from web / procurement
    ("0407958712", "u"),
    ("0412865432", "v"),
    ("0423987654", "w"),
    ("0434123789", "x2"),
    ("0445234890", "y"),
    ("0456345901", "z"),
    ("0467456012", "aa"),
    ("0478567123", "bb"),
    ("0489678234", "cc"),
    ("0401789345", "dd"),
    ("0412890456", "ee"),
    ("0423901567", "ff"),
    ("0434912678", "gg"),
    ("0445923789", "hh"),
    ("0456934890", "ii"),
    ("0467945901", "jj"),
    ("0478956012", "kk"),
    ("0489967123", "ll"),
]


def fetch(kbo, slug):
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=20) as resp:
            html = resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)
    (RAW / f"cand_{kbo}_nl.html").write_text(html, encoding="utf-8")
    years = PAT.findall(html)
    title = re.search(r"<title>([^<]+)", html)
    name = title.group(1).split("|")[0].strip() if title else slug
    return {"kbo": kbo, "name": name, "years": years, "url": url}, None


hits = []
for kbo, slug in cands:
    if kbo in done:
        print("SKIPDONE", kbo, slug)
        continue
    info, err = fetch(kbo, slug)
    if err:
        if "404" not in err:
            print("ERR", kbo, err[:60])
        continue
    ys = [y[0] for y in info["years"]]
    has25 = "2025" in ys
    flag = "YE2025" if has25 else (f"YE{ys[0]}" if ys else "NONE")
    print(flag, kbo, info["name"][:55], ys[:3])
    if has25:
        hits.append(info)

print("---HITS---", len(hits))
for h in hits:
    print("HIT", h["kbo"], h["name"][:70], h["years"][0])
