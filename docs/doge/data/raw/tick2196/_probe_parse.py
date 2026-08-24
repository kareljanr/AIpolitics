import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2195"
os.makedirs(out, exist_ok=True)

used = (
    open("docs/doge/data/entities.csv", encoding="utf-8").read()
    + open("docs/doge/data/commitments.csv", encoding="utf-8").read()
    + open("docs/doge/data/leaderboard.csv", encoding="utf-8").read()
).replace(".", "")


def num(s):
    s = (s or "").strip().replace(" ", "").replace("\xa0", "")
    if s in ("", "-"):
        return None
    if re.search(r",\d{2}$", s) and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(",") > 1:
        s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    elif "," in s and "." not in s:
        parts = s.split(",")
        s = parts[0] + "." + parts[1] if len(parts) == 2 and len(parts[1]) == 2 else s.replace(",", "")
    return float(s)


def probe(name, kbo):
    d = re.sub(r"\D", "", kbo)
    if d in used:
        print("USED", name)
        return None
    url = f"https://www.companyweb.be/en/{d}/"
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except Exception as e:
        print("ERR", name, type(e).__name__, str(e)[:60])
        return None
    if "/error/404" in final:
        print("404", name)
        return None
    text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
    ym = re.search(r"Last balance sheet year (20\d\d)", text)
    year = ym.group(1) if ym else "?"
    m = re.search(
        r'2025\s*:\s*\{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    fte_m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    slug = final.rstrip("/").split("/")[-1]
    print(name, "year", year, "slug", slug, "kern", bool(m), "fte", fte_m.group(1) if fte_m else None)
    if m and year == "2025":
        w, e, b, o = m.groups()
        oo, bb = num(o), num(b)
        print(" ", "pnl", num(w), "equity", num(e), "bruto", bb, "omzet", oo)
        if oo and oo > 1e6:
            open(os.path.join(out, f"cand_{d}_en.html"), "w", encoding="utf-8").write(html)
            return (name, d, slug, num(w), num(e), bb, oo, fte_m.group(1) if fte_m else None)
    return None


print("=== FARO ===")
probe("faro", "0893863017")

hits = []
for name, kbo in [
    ("bewel", "0407229358"),
    ("pajottenland", "0413313535"),
    ("bw_zottegem", "0407657148"),
    ("kaliber", "0407201941"),
    ("aarova", "0451263992"),
    ("oesterbank", "0407762165"),
    ("werkhuizen_min", "0407699908"),
    ("trianval", "0419052074"),
    ("noordheuvel", "0415048944"),
    ("arcor", "0410962274"),
    ("acg", "0406611726"),
    ("entiris", "0407841151"),
    ("gandae", "0406711201"),
    ("odas", "0407201149"),
    ("kemphaan", "0425803472"),
    ("de_dagmoed", "0416317070"),
    ("de_dageraad", "0412607613"),
    ("aurora", "0407624484"),
    ("sociale_rehabilitatie", "0407407720"),
    ("rodea", "0430295562"),
    ("zonnehoeve", "0432166276"),
    ("ergasia", "0463149858"),
    ("vlotter", "0841843796"),
    ("mo_clean", "0453129362"),
    ("waardenmakerij", "0459644990"),
    ("de_ploeg", "0465913368"),
    ("de_sprong", "0466328686"),
    ("de_vlaspit", "0461019224"),
    ("ecoso", "0629934529"),
    ("manus_antwerpen", "0872564290"),
    ("werkplus", "0466950179"),
]:
    h = probe(name, kbo)
    if h:
        hits.append(h)
        if len(hits) >= 3:
            break

print("HITS", [(h[0], h[1], h[6]) for h in hits])
