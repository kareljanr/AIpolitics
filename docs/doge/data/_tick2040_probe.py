# ephemeral probe tick2039 — preferred leftovers + unused WZC
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2039")
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
    return float(s)


def probe(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
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
            omzet = y0[3]
            return year == "2025" and omzet > 0
        return False
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])
        return False


urls = [
    ("agb_bornem_en", "https://www.companyweb.be/en/0877556624/autonoom-gemeentebedrijf-bornem"),
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587/association-intercommunale-d-electricite-du-sud-du-hainaut"),
    ("rew_en", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre"),
    ("samen_ouder_en", "https://www.companyweb.be/en/0453287037/woonzorg-samen-ouder"),
    ("cwzc_en", "https://www.companyweb.be/en/0413203073/christelijke-woon-en-zorgcentra"),
    ("linde_en", "https://www.companyweb.be/en/0467355403/woon-en-zorgcentrum-de-linde"),
    ("molenheide_en", "https://www.companyweb.be/en/0810616132/molenheide-woonzorgcentrum"),
    ("veilige_have_en", "https://www.companyweb.be/en/0449507205/woonzorgcentrum-veilige-have"),
    ("witte_meren_en", "https://www.companyweb.be/en/0412058827/woonzorgcentrum-de-witte-meren"),
]

live = []
for name, url in urls:
    if probe(name, url):
        live.append(name)
print("LIVE_YE2025", live)
