import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2187"
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
        print("USED", name, kbo)
        return None
    url = f"https://www.companyweb.be/en/{d}/"
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except Exception as e:
        print("ERR", name, type(e).__name__, str(e)[:80])
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
    if m:
        w, e, b, o = m.groups()
        print(" ", "pnl", num(w), "equity", num(e), "bruto", num(b), "omzet", num(o))
        if year == "2025" or (num(o) and num(o) > 500000):
            open(os.path.join(out, f"cand_{d}_en.html"), "w", encoding="utf-8").write(html)
            return (name, d, slug, num(w), num(e), num(b), num(o), fte_m.group(1) if fte_m else None, year)
    return None


print("=== stalls ===")
probe("faro", "0893863017")

print("=== free leftover ===")
hits = []
for name, kbo in [
    ("mirto", "0407656257"),
    ("blankedale", "0400999978"),
    ("kringwinkel_antwerpen", "0442423037"),
    ("de_wroeter", "0433138454"),
    ("demival", "0407409007"),
    ("mivas", "0407597958"),
    ("a_kwadraat", "0406668540"),
    ("forena", "0425410920"),
    ("kunnig", "0404745465"),
    ("bewel", "0407229358"),
    ("pajottenland", "0413313535"),
    ("bw_zottegem", "0407657148"),
    ("kaliber", "0407201941"),
    ("aarova", "0451263992"),
    ("oesterbank", "0407762165"),
]:
    h = probe(name, kbo)
    if h and h[-1] == "2025":
        hits.append(h)
        if len(hits) >= 3:
            break

print("HITS YE2025", hits)
