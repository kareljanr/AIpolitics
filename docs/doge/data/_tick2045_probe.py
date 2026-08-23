# ephemeral probe tick2045 — preferred leftovers + unused WZC YE2025
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2045")
outdir.mkdir(parents=True, exist_ok=True)


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    try:
        return float(s)
    except ValueError:
        return None


def probe_cw(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        title = re.search(r"<title>([^<]+)", html)
        year = None
        for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
            i = html.find(lab)
            if i >= 0:
                m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
                if m:
                    year = m.group(1)
                    break
        blocks = re.findall(
            r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
            html,
        )
        emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        print(
            "==",
            name,
            "Y",
            year,
            "blocks",
            len(blocks),
            "emp",
            emp.group(1) if emp else None,
            (title.group(1)[:70] if title else ""),
        )
        if blocks:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print("  y0 pnl/eq/bruto/omzet", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print("  y1", y1)
        return year, blocks
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])
        return None, []


for n, u in [
    ("agb_bornem_en", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut"),
    ("rew_en", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre"),
    ("curando_en", "https://www.companyweb.be/en/0445499422/curando"),
    ("integro_en", "https://www.companyweb.be/en/0654847196/integro"),
    ("huize_vincent_en", "https://www.companyweb.be/en/0463758978/woon-en-zorgcentrum-huize-vincent"),
    ("hof_waarbeek_en", "https://www.companyweb.be/en/0478728256/woonzorgcentrum-hof-ter-waarbeek"),
    ("avondvrede_en", "https://www.companyweb.be/en/0479628079/avondvrede-woon-en-zorgcentrum"),
    ("ter_kimme_en", "https://www.companyweb.be/en/0421535373/ter-kimme"),
]:
    probe_cw(n, u)
