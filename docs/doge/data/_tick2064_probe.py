# ephemeral probe tick2064
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2064")
outdir.mkdir(parents=True, exist_ok=True)


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


def parse_blocks(html):
    return re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )


cands = [
    ("olv_bornem_en", "https://www.companyweb.be/en/0436595020/seniorencentrum-onze-lieve-vrouw-vzw"),
    ("olv_bornem_nl", "https://www.companyweb.be/nl/0436595020/seniorencentrum-onze-lieve-vrouw-vzw"),
    ("olv_bornem_fr", "https://www.companyweb.be/fr/0436595020/seniorencentrum-onze-lieve-vrouw-vzw"),
    ("zusters_deinze_en", "https://www.companyweb.be/en/0454090355/bejaardenzorg-zusters-sint-vincentius"),
    ("zusters_deinze_nl", "https://www.companyweb.be/nl/0454090355/bejaardenzorg-zusters-sint-vincentius"),
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587/aiesh"),
    ("rew_en", "https://www.companyweb.be/en/0644638937/reseau-d-energies-de-wavre"),
]

for name, url in cands:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        emp = re.search(r'Employees\s*=\s*"([^"]+)"', html) or re.search(
            r'Personeel\s*=\s*"([^"]+)"', html
        )
        filed = re.search(r"filed on ([0-9\-]+)", html, re.I) or re.search(
            r"neergelegd op ([0-9\-]+)", html, re.I
        )
        title = re.search(r"<title>([^<]+)", html)
        print(
            "FETCH",
            name,
            "Y",
            year_of(html),
            "emp",
            emp.group(1) if emp else None,
            "filed",
            filed.group(1) if filed else None,
            (title.group(1)[:60] if title else ""),
            "blocks",
            parse_blocks(html)[:2],
        )
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])
