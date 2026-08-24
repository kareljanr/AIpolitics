# -*- coding: utf-8 -*-
"""Hunt unused YE2025 dual after Korian Belgium for tick 2105."""
import csv
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

csv.field_size_limit(10**7)
RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}

done = set()
for path in [
    Path("docs/doge/data/entities.csv"),
    Path("docs/doge/data/commitments.csv"),
    Path("docs/doge/data/leaderboard.csv"),
    Path("docs/doge/data/research_queue.csv"),
]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            blob = " ".join(str(v or "") for v in row.values())
            for m in re.findall(r"0\d{9}|\d{4}\.\d{3}\.\d{3}", blob):
                done.add(re.sub(r"\D", "", m))

# Explicitly skip known preferred stalls / just-mined
done.update(
    {
        "0869769702",  # Korian Belgium
        "0410958712",  # SLG Vlaanderen
        "0845064196",  # SLG Operaties
        "0412914845",  # Familiezorg Gent
        "0627818345",  # AREWAL
        "0887690451",  # emeis
        "0723858144",  # Colisee / Always Home path
        "0415018755",  # Always Home? wait Always Home separate
        "0889421308",  # Armonea
        "0877556624",  # AGB Bornem
        "0893863017",  # FARO
        "0201712587",  # AIESH
        "0644638937",  # REW
        "0897436971",  # ORES SC
        "0727639263",  # Comnexio
        "0219511295",  # Intradel
    }
)

# Candidate KBOs: WZC / zorg / Korian-adjacent / water-DSO leftovers
cands = [
    ("0422152314", "wzc-sint-barbara-herselt"),
    ("0449507205", "wzc-veilige-have-aalter"),
    ("0410219433", "wzc-haagwinde-maarkedal"),
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
    ("0471086327", "olivetenhof"),
    ("0459864105", "centrum-gheel"),
    ("0460975216", "pc-gheel"),
    ("0408221095", "placeholder"),
    ("0411667788", "placeholder2"),
    ("0423456789", "bad"),
    ("0432505281", "rustoord-t-hoge"),
    ("0422620585", "wzc-sint-vincentius-erpe"),
    ("0441313178", "kalvermarkt"),
    ("0471977452", "gpn-sz-wl"),
    ("0480566704", "hof-ter-lande"),
    ("0598966387", "de-hoeksteen"),
    ("0685516024", "woonzorgnetwerk-edegem"),
    ("0415018755", "caria"),
    # Korian path daughters / related
    ("0406554321", "a"),
    ("0478123987", "b"),
    ("0434123789", "c"),
    ("0456345901", "d"),
    ("0467456012", "e"),
    ("0401789345", "f"),
    ("0412890456", "g"),
    ("0423901567", "h"),
    ("0434912678", "i"),
    ("0445923789", "j"),
    ("0456934890", "k"),
    ("0467945901", "l"),
    ("0478956012", "m"),
    # waste / water dual leftovers possibly YE2025 refresh
    ("0206787251", "copidec"),
    ("0267431485", "idefin"),
    ("0216606724", "inbw"),
    ("0206735912", "hygea-check"),
    ("0839927651", "hygea"),
    ("0206679385", "aide"),
    ("0200750471", "seda"),
    ("0870691527", "ibram"),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=45) as resp:
        return resp.read()


hits = []
for kbo, slug in cands:
    if kbo in done:
        print(f"SKIP done {kbo} {slug}")
        continue
    url = f"https://www.companyweb.be/nl/{kbo}/{slug}"
    try:
        body = fetch(url)
    except Exception as e:
        print(f"FAIL {kbo} {slug}: {e}")
        continue
    path = RAW / f"cand_{kbo}_nl.html"
    path.write_bytes(body)
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body.decode("utf-8", "ignore"))))
    title_m = re.search(r"<title>([^<]+)</title>", body.decode("utf-8", "ignore"), re.I)
    # retry title from text
    if not title_m:
        title = slug
    else:
        title = title_m.group(1)[:90]
    # get title from html better
    tm = re.search(r"<title>([^<]+)</title>", body.decode("utf-8", "ignore"), re.I)
    title = tm.group(1)[:100] if tm else slug
    lb = re.search(r"Laatste balansjaar\s+(\d{4})", text)
    om = re.search(r"Omzet\s+€\s*([\d\.,]+)", text)
    pnl = re.search(r"Winst/Verlies\s+€\s*([-]?[\d\.,]+)", text)
    eq = re.search(r"Eigen vermogen\s+€\s*([-]?[\d\.,]+)", text)
    bruto = re.search(r"Brutomarge\s+€\s*([-]?[\d\.,]+)", text)
    fte = re.search(r"(?:Personeel|Bedrijfsgrootte)[^\d]*([\d\.,]+)\s*FTE", text)
    year = lb.group(1) if lb else "?"
    print(
        f"{kbo} lb={year} omzet={om.group(1) if om else '?'} "
        f"pnl={pnl.group(1) if pnl else '?'} eq={eq.group(1) if eq else '?'} "
        f"bruto={bruto.group(1) if bruto else '?'} name={title}"
    )
    if year == "2025":
        hits.append((kbo, slug, title, om, pnl, eq, bruto, text))

print("--- YE2025 HITS ---")
for h in hits:
    print(h[0], h[1], h[2][:80])
