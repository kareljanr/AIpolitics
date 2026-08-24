# ephemeral tick2075 probe — SJ Brugge + stalls
import re
import pathlib
import urllib.request
import ssl

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = pathlib.Path("docs/doge/data/raw/tick2075")
raw.mkdir(parents=True, exist_ok=True)

targets = [
    ("sj_brugge_fr", "https://www.companyweb.be/fr/0461563315/sint-jozef-wonen-leven-en-zorg-sint-michiels-brugge"),
    ("sj_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461563315"),
]
for name, url in targets:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            body = r.read()
            (raw / f"{name}.html").write_bytes(body)
            print(name, "OK", len(body), r.geturl())
    except Exception as e:
        print(name, "FAIL", e)


def plain_of(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\s+", " ", t)
    return text, t


text, plain = plain_of(raw / "sj_brugge_en.html")
print("---EN KEYS---")
for pat in [
    r"filed their annual financial statements\?[^.?]{0,220}",
    r"Address.{0,140}",
    r"Company number.{0,80}",
    r"Legal form.{0,80}",
    r"Status.{0,60}",
    r"Principal activity.{0,140}",
    r"Establishments.{0,60}",
    r"Contracting authority.{0,120}",
    r"Start date.{0,80}",
    r"Employees.{0,80}",
    r"Turnover.{0,180}",
    r"Profit/Loss.{0,180}",
    r"Equity.{0,180}",
    r"Gross margin.{0,180}",
]:
    m = re.search(pat, plain, re.I)
    if m:
        print(m.group(0)[:240])

print("---CW VARS---")
for m in re.finditer(r'window\.cw\.([a-zA-Z0-9_]+)\s*=\s*"([^"]*)"', text):
    k, v = m.group(1), m.group(2)
    if any(
        x in k.lower()
        for x in [
            "email",
            "adres",
            "straat",
            "naam",
            "national",
            "status",
            "rechts",
            "gemeente",
            "post",
            "tel",
            "website",
            "ondernem",
        ]
    ):
        print(k, "=", v)

_, nlp = plain_of(raw / "sj_brugge_nl.html")
for label, pat in [
    ("NL balans", r"balansjaar\s+20[12][0-9].{0,120}"),
    ("NL filed", r"neergelegd op [^.]{0,40}"),
    ("NL aanbest", r"aanbestedende.{0,80}"),
    ("NL omzet", r"Omzet.{0,160}"),
]:
    m = re.search(pat, nlp, re.I)
    print(label, m.group(0)[:200] if m else None)

if (raw / "sj_kbo.html").exists():
    _, kbo = plain_of(raw / "sj_kbo.html")
    print("---KBO---")
    for pat in [
        r"Status van de onderneming.{0,80}",
        r"Rechtsvorm.{0,100}",
        r"Adres van de zetel.{0,160}",
        r"E-mailadres.{0,80}",
        r"Telefoonnummer.{0,80}",
        r"Aantal vestigingseenheden.{0,40}",
        r"Aanbestedende overheid.{0,80}",
        r"87\.101.{0,40}",
        r"NACE.{0,100}",
    ]:
        m = re.search(pat, kbo, re.I)
        if m:
            print(m.group(0)[:200])
