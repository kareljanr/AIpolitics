# -*- coding: utf-8 -*-
import csv, re, ssl, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path("docs/doge/data/raw/tick2169")
out.mkdir(parents=True, exist_ok=True)

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)


def fetch(url, p):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        p.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", p.name, type(e).__name__)
        return None


def parse(t):
    yb = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t or ""):
        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yb[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"([\d.,]+)\s*FTE", t or "")
    filed = re.search(r"filed on ([0-9-]{10})", t or "")
    title = re.search(r"<title>([^<]+)", t or "")
    nace = re.findall(r"(?:87|86|88)\.\d{3}", t or "")[:6]
    nbad = re.findall(r"(?:68|55|64|70)\.\d{3}", t or "")[:4]
    return (
        yb,
        fte.group(1) if fte else None,
        filed.group(1) if filed else None,
        title.group(1) if title else None,
        nace,
        nbad,
    )


# Prefer dual leftovers first
PREF = [
    ("0877556624", "agb_bornem"),
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
]

# Deferred named + other unused WZC
CANDS = [
    ("0644843825", "sint_vincentius_aaigem"),
    ("0787300696", "melis_home"),
    ("0400371161", "abdij_affligem"),
    ("0411600692", "maria_rustoord"),
    ("0453287037", "samen_ouder"),
    ("0454090355", "zusters_sv_deinze"),
    ("0417958152", "sint_camillus"),
    ("0445175263", "zilverlinde"),
    ("0452865383", "sint_jozef_srl"),
    ("0459770496", "sint_augustinus"),
    ("0448033201", "chateau_vert"),
    ("0463758978", "huize_vincent"),
    ("0421903676", "christine"),
    ("0650907810", "ventu"),
    ("0641760611", "numera"),
    ("0810616132", "molenheide"),
    ("0845064196", "slg_operaties"),
    ("0887690451", "emeis_belgium"),
    ("0413796456", "de_foyer"),
    ("0422152314", "sint_barbara_herselt"),
    ("0413055989", "sint_jozef_aarschot"),
    ("0448190181", "sint_jozef_rumst"),
    ("0449425546", "wijtshage"),
    ("0418234997", "witte_meren"),
    ("0414678562", "vander_stokken"),
    ("0416337262", "vrijzicht"),
    ("0633687439", "walfergem"),
    ("0462871549", "ry_chevreuil"),
    ("0471852036", "seniservices"),
]

# Skip already done this sprint
SKIP = {
    "0410127084",  # Sint Lodewijk
    "0755822317",  # Lork Hoeselt
    "0469969453",  # Anima hold
    "0446506836",  # Avondvrede
    "0698940725",  # Anima VL
    "0823488131",  # t Hofke
    "0470673890",  # Zorg-Saam
}


def report(kbo, label, t, st):
    if not t:
        print(st, kbo, "fail")
        return None
    if "Error 404" in t:
        print(st, kbo, "404")
        return None
    yb, fte, filed, title, nace, nbad = parse(t)
    y5 = yb.get("2025", {})
    y4 = yb.get("2024", {})
    print(st, kbo, (title or "")[:80])
    print("  fte", fte, "filed", filed, "nace", nace[:3], "bad", nbad[:2])
    print("  2025", y5)
    print("  2024", y4)
    strong = False
    if st == "FREE" and y5:
        omzet = (y5.get("omzet") or "").replace(",", "").replace("-", "")
        bruto = (y5.get("bruto_marge") or "").replace(",", "").lstrip("-")
        o = int(omzet) if omzet.isdigit() else 0
        b = int(bruto) if bruto.isdigit() else 0
        if (o >= 200000 or b >= 200000) and nace and not nbad:
            print("  >>> STRONG CANDIDATE")
            strong = True
        elif o >= 200000 or b >= 200000:
            print("  >>> CANDIDATE (check NACE)")
            strong = True
    return strong


print("=== PREF dual/AGB ===")
for kbo, label in PREF:
    st = "MINED" if kbo in mined else "FREE"
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_{kbo}_en.html")
    report(kbo, label, t, st)

print("\n=== CANDS ===")
strongs = []
for kbo, label in CANDS:
    if kbo in SKIP:
        print("SKIP", kbo, label)
        continue
    st = "MINED" if kbo in mined else "FREE"
    # reuse existing file if present
    p = out / f"{label}_{kbo}_en.html"
    if p.exists() and p.stat().st_size > 1000:
        t = p.read_text(encoding="utf-8", errors="ignore")
    else:
        t = fetch(f"https://www.companyweb.be/en/{kbo}", p)
    if report(kbo, label, t, st):
        strongs.append((kbo, label))

print("\nSTRONGS:", strongs)
