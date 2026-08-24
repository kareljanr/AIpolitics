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
    + open("docs/doge/data/research_queue.csv", encoding="utf-8").read()
)
used_compact = used_txt.replace(".", "")

# From VL parliament enclave list + Crevits names (enterprise nrs padded)
cands = [
    ("atelier_alternatief", "0465227440"),
    ("sense_operations", "0466843281"),
    ("kringwinkel_antwerpen", "0442423037"),
    ("kringwinkel_maasland", "0417701992"),
    ("waardenmakerij", "0459644990"),
    ("de_ploeg", "0465913368"),
    ("de_sprong", "0466328686"),
    ("de_vlaspit", "0461019224"),
    ("de_wroeter", "0433138454"),
    ("diepen_boomgaard", "0421285252"),
    ("ecoso", "0629934529"),
    ("maasbij", "0465820031"),
    ("kringloopcentrum_kust", "0892003783"),
    ("manus_antwerpen", "0872564290"),
    ("mo_clean", "0453129362"),
    ("sw_poperinge", "0431297632"),
    ("sobao", "0863423427"),
    ("waak_wsw", "0457351040"),
    ("werkplus", "0466950179"),
    ("aarova", "0451263992"),
    ("acg", "0406611726"),
    ("a_kwadraat", "0406668540"),
    ("arcor", "0410962274"),
    ("sociale_rehabilitatie", "0407407720"),
    ("aurora", "0407624484"),
    ("blankedale", "0400999978"),
    ("pajottenland", "0413313535"),
    ("bw_zottegem", "0407657148"),
    ("de_brug", "0408347828"),
    ("de_dageraad", "0412607613"),
    ("de_dagmoed", "0416317070"),
    ("kemphaan", "0425803472"),
    ("oesterbank", "0407762165"),
    ("demival", "0407409007"),
    ("odas", "0407201149"),
    ("gandae", "0406711201"),
    ("kaliber", "0407201941"),
    ("lidwina", "0407601720"),
    ("mariasteen", "0407079207"),
    ("mirto", "0407656257"),
    ("mivas", "0407597958"),
    ("noordheuvel", "0415048944"),
    ("rodea", "0430295562"),
    ("forena", "0425410920"),
    ("trianval", "0419052074"),
    ("twi", "0454926733"),
    ("vlotter", "0841843796"),
    ("werkwuizen_min", "0407699908"),
    ("zonnehoeve", "0432166276"),
    ("kunnig", "0404745465"),
    ("ergasia", "0463149858"),
    ("entiris", "0407841151"),
    ("bewel", "0407229358"),
]


def probe(name, kbo):
    d = re.sub(r"\D", "", kbo)
    if d in used_compact:
        print("USED", name, kbo)
        return None
    url = f"https://www.companyweb.be/en/{d}/"
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except Exception as e:
        print("ERR", name, kbo, type(e).__name__, str(e)[:80])
        return None
    if "/error/404" in final:
        print("404", name, kbo)
        return None
    year_m = re.search(r"Last balance sheet year[^0-9]{0,40}(20\d\d)", html)
    year = year_m.group(1) if year_m else "?"
    slug = final.rstrip("/").split("/")[-1]
    # kern
    km = re.search(
        r'2025\s*:\s*\{\s*winst:\s*"([^"]+)".*?bruto_marge:\s*"([^"]+)".*?omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    if not km:
        km2 = re.search(
            r"Profit/Loss € ([^ ]+).*?Turnover € ([^ ]+).*?Equity € ([^ ]+).*?Gross margin € ([^ ]+)",
            re.sub(r"\s+", " ", html),
            re.I,
        )
    else:
        km2 = None
    print(f"OK {name} {kbo} year={year} slug={slug} kern={bool(km)}")
    if year == "2025":
        path = os.path.join(out, f"cand_{d}_en.html")
        open(path, "w", encoding="utf-8").write(html)
        if km:
            print("  YE2025 winst/bruto/omzet", km.groups())
        return (name, d, slug, html)
    return None


hits = []
for name, kbo in cands:
    h = probe(name, kbo)
    if h:
        hits.append(h)
        if len(hits) >= 6:
            break

print("HITS", len(hits))
for h in hits:
    print("CAND", h[0], h[1], h[2])
