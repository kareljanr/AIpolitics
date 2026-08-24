import os
import re
import urllib.request
import html as H

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2193"
os.makedirs(out, exist_ok=True)

used = (
    open("docs/doge/data/entities.csv", encoding="utf-8").read()
    + open("docs/doge/data/commitments.csv", encoding="utf-8").read()
    + open("docs/doge/data/leaderboard.csv", encoding="utf-8").read()
).replace(".", "")

cands = [
    ("0465707391", "sw-web", "sociale-werkplaatsen-web"),
    ("0407657148", "bwz", "beschermde-werkplaats-zottegem"),
    ("0419461652", "schakel", "de-schakel"),
    ("0464028204", "boskat", "bos-kat"),
    ("0430686037", "age", "atelier-groot-eiland"),
]
for d, short, slug in cands:
    print(("USED" if d in used else "FREE"), short, d)

probes = {
    "faro_en": "https://www.companyweb.be/en/0893863017/faro",
    "aiesh_en": "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut",
    "agb_bornem_en": "https://www.companyweb.be/en/0877556624/agb-bornem",
    "rew_en": "https://www.companyweb.be/en/search?q=0200938156",
}


def dump(key, url):
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
        open(os.path.join(out, f"{key}.html"), "w", encoding="utf-8").write(html)
        text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))
        ym = (
            re.search(r"Last balance sheet year (20\d\d)", text)
            or re.search(r"Laatste balansjaar\s*(20\d\d)", text)
            or re.search(r"Dernier bilan\s*(20\d\d)", text)
        )
        print(key, "OK", len(html), "year", ym.group(1) if ym else "?", final[:90])
        for y in (2025, 2024):
            m = re.search(
                rf'{y}\s*:\s*\{{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
                html,
                re.S,
            )
            if m:
                print(" ", y, "pnl/eq/bruto/omzet", m.groups())
        em = re.search(r"Employees[^0-9]{0,40}([0-9][0-9.,]*)", text)
        if em:
            print("  emp", em.group(1))
        return html, text
    except Exception as e:
        print(key, type(e).__name__, e)
        return None, None


for k, u in probes.items():
    dump(k, u)

# fetch top FREE YE2025 candidates
for d, short, slug in cands:
    if d in used:
        continue
    dump(f"{short}_en", f"https://www.companyweb.be/en/{d}/{slug}")
    dump(f"{short}_nl", f"https://www.companyweb.be/nl/{d}/{slug}")
