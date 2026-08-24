import os
import re
import urllib.request

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2186"
os.makedirs(out, exist_ok=True)

used_txt = (
    open("docs/doge/data/entities.csv", encoding="utf-8").read()
    + open("docs/doge/data/commitments.csv", encoding="utf-8").read()
    + open("docs/doge/data/leaderboard.csv", encoding="utf-8").read()
)
used_digits = set(re.findall(r"0\d{9}", used_txt.replace(".", "")))


def digits(s):
    return re.sub(r"\D", "", s)


cands = [
    ("mariasteen", "0405612587"),
    ("de_winning", "0415307911"),
    ("atelier_groot_eiland", "0471807593"),
    ("bronsgroen", "0867350855"),
    ("ambroos", "0478395541"),
    ("den_dikken_eik", "0428156908"),
    ("feraluc", "0421571584"),
    ("wjelin", "0400328856"),
    ("beschutte_meulebeke", "0407689956"),
    ("de_schakel", "0446022334"),
    ("vlot", "0409232015"),
    ("t_veuruit", "0417958152"),
    ("bw_oosterzele", "0407664220"),  # near MAAAT
    ("de_werkbank", "0472098703"),
    ("levanto", "0465104900"),
    ("fixit", "0413796451"),
    ("de_passage", "0424830108"),
    ("werk_met_zin", "0452865381"),
    ("sociale_werkplaats_brugge", "0409970203"),
    ("kompas_maatwerk", "0439442761"),
    ("de_kringloopwinkel", "0410142031"),
    ("natuurwerk", "0810616130"),
    ("groene_kring", "0823488130"),
    ("hands_on", "0414678560"),
    ("sofia", "0463758970"),
    ("werkgelegenheid_oostende", "0416337260"),
]

for name, kbo in cands:
    d = digits(kbo)
    if d in used_digits or d in used_txt.replace(".", ""):
        print("USED", name, kbo)
        continue
    url = f"https://www.companyweb.be/en/{d}/"
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        year_m = re.search(r"Last balance sheet year[^0-9]{0,40}(20\d\d)", html)
        year = year_m.group(1) if year_m else "?"
        # activity hint
        act = ""
        am = re.search(r"Main activity</[^>]*>\s*<[^>]*>\s*([^<]+)", html)
        if not am:
            am = re.search(r"Hoofdactiviteit[^<]{0,40}", html)
        if am:
            act = re.sub(r"\s+", " ", am.group(0))[:80]
        slug = final.rstrip("/").split("/")[-1]
        print(f"HIT {name} {kbo} year={year} slug={slug} act={act} final={final}")
        if year == "2025":
            open(os.path.join(out, f"cand_{d}_en.html"), "w", encoding="utf-8").write(html)
            # pull NL+FR+KBO too if looks maatwerk-ish
            low = (slug + html[:3000]).lower()
            if any(
                x in low
                for x in [
                    "maatwerk",
                    "beschut",
                    "sheltered",
                    "sociale werk",
                    "work adapted",
                    "travail adapte",
                    "88.993",
                    "atelier",
                ]
            ) or "gross margin" in html.lower():
                print("  -> YE2025 candidate saved")
    except Exception as e:
        print("ERR", name, kbo, type(e).__name__, str(e)[:100])
