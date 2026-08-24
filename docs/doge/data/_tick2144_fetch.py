# -*- coding: utf-8 -*-
import urllib.request, re, ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
dst = Path("docs/doge/data/raw/tick2144")
dst.mkdir(parents=True, exist_ok=True)
blob = (
    Path("docs/doge/data/entities.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8", errors="replace")
    + Path("docs/doge/data/commitments.csv").read_text(encoding="utf-8", errors="replace")
).lower()


def get(url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read()


cands = [
    ("zonnelied", "0420607638", "zonnelied"),
    ("lidwina", "0407601720", "lidwina-vzw"),
    ("petits_sapins", "0426314901", "les-petits-sapins-de-waterloo"),
    ("maria_rustoord", "0458458325", "maria-rustoord-ingelmunster-v-z-w-"),
    ("rew_try1", "0200666123", None),
    # try REW via known patterns - search pappers / companyweb fr slug
]

# also try common REW enterprise numbers near AIEG/AIESH range and Wavre
for n in [
    "0202555004",  # AIEG known
    "0201712587",  # AIESH known
    "0220123456",
]:
    pass

# discover REW from rew.be mentions / footer
try:
    data = get("https://www.rew.be/")
    (dst / "rew_site.html").write_bytes(data)
    t = data.decode("utf-8", "replace")
    print("rew.be title", (re.search(r"<title>([^<]+)", t).group(1)[:80] if re.search(r"<title>", t) else None))
    for m in re.finditer(r"(BE\s?0\d{3}[\.\s]?\d{3}[\.\s]?\d{3}|0\d{3}\.\d{3}\.\d{3}|TVA[^<]{0,40}|BCE[^<]{0,40})", t, re.I):
        print(" rew num", re.sub(r"\s+", " ", m.group(0))[:100])
    for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t):
        print(" email", m.group(0))
except Exception as e:
    print("rew.be ERR", e)

# Try companyweb slug guesses for REW
for slug, digits in [
    ("reseau-d-energies-de-wavre", None),
    ("rew", None),
    ("reseau-d-electricite-de-wavre", None),
]:
    for base in ["https://www.companyweb.be/en/", "https://www.companyweb.be/fr/", "https://www.companyweb.be/nl/"]:
        # without digits won't work; skip
        pass

# pappers search
for u in [
    "https://www.pappers.be/fr/recherche?q=R%C3%A9seau+d%27%C3%89nergies+de+Wavre",
    "https://www.pappers.be/fr/recherche?q=REW+Wavre",
    "https://www.northdata.com/R%C3%A9seau+d%27%C3%89nergies+de+Wavre,+Wavre",
]:
    try:
        data = get(u)
        t = data.decode("utf-8", "replace")
        print("DISC", u[:70], len(t))
        for m in re.finditer(r"(0\d{3}[\.\s]?\d{3}[\.\s]?\d{3}|BE\s?0\d{9}|/company/[^\"']+)", t):
            s = re.sub(r"\s+", " ", m.group(0))
            if "0" in s:
                print(" ", s[:100])
    except Exception as e:
        print("DISC ERR", type(e).__name__, e)

for name, digits, slug in cands[:4]:
    dotted = digits[:4] + "." + digits[4:7] + "." + digits[7:]
    mined = digits in blob or dotted in blob or name.replace("_", " ") in blob
    urls = {
        f"{name}_en.html": f"https://www.companyweb.be/en/{digits}/{slug}",
        f"{name}_nl.html": f"https://www.companyweb.be/nl/{digits}/{slug}",
        f"{name}_fr.html": f"https://www.companyweb.be/fr/{digits}/{slug}",
        f"{name}_kbo.html": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={digits}",
    }
    print("===", name, digits, "mined", mined)
    for fn, url in urls.items():
        try:
            data = get(url)
            (dst / fn).write_bytes(data)
            print(" OK", fn, len(data))
        except Exception as e:
            print(" FAIL", fn, type(e).__name__, e)
    en = (dst / f"{name}_en.html").read_text(encoding="utf-8", errors="replace") if (dst / f"{name}_en.html").exists() else ""
    if not en:
        continue
    title = re.search(r"<title>([^<]+)", en)
    years = re.findall(r"\n(202[0-9])\s*:", en)
    last = re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", en, re.I)
    print(" title", title.group(1)[:90] if title else None)
    print(" years", years[:5], "last", last.group(1) if last else None)
    for y in ["2025", "2024"]:
        mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
        print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:220] if mm else None)
    fte = re.search(r'Employees\s*=\s*"([^"]+)"', en)
    filed = re.search(r"filed on ([0-9\-]+)", en, re.I)
    act = re.search(r'Principal activity[^"]*"([^"]+)"', en, re.I)
    size = re.search(r'Company size[^"]*"([^"]+)"', en, re.I)
    print(" fte", fte.group(1) if fte else None, "filed", filed.group(1) if filed else None)
    print(" act", act.group(1) if act else None, "size", size.group(1) if size else None)
    # KBO
    kbo = (dst / f"{name}_kbo.html").read_text(encoding="utf-8", errors="replace") if (dst / f"{name}_kbo.html").exists() else ""
    for pat in [
        r"Status</td>\s*<td[^>]*>\s*([^<]+)",
        r"Rechtsvorm</td>\s*<td[^>]*>\s*([^<]+)",
        r"Aantal vestigingseenheden[^0-9]*([0-9]+)",
        r"aanbestedende overheid",
    ]:
        m = re.search(pat, kbo, re.I | re.S)
        print(" kbo", pat[:30], "=>", (re.sub(r"\s+", " ", m.group(0 if (m and m.lastindex is None) else (m.group(1) if m else "")))[:120] if m else None))
