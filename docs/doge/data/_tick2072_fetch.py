# fetch Maria's Rustoord Moorslede YE2025 primary mirrors + KBO + site
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2072")
outdir.mkdir(parents=True, exist_ok=True)

urls = {
    "maria_en": "https://www.companyweb.be/en/0411600692/wzc-maria-s-rustoord",
    "maria_nl": "https://www.companyweb.be/nl/0411600692/wzc-maria-s-rustoord",
    "maria_fr": "https://www.companyweb.be/fr/0411600692/wzc-maria-s-rustoord",
    "maria_kbo": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411600692",
    "maria_site": "http://mariasrustoord.be/",
}


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


for name, url in urls.items():
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=40) as resp:
        data = resp.read()
        # KBO may be latin-1
        try:
            html = data.decode("utf-8")
        except UnicodeDecodeError:
            html = data.decode("latin-1", "replace")
    (outdir / f"{name}.html").write_text(html, encoding="utf-8")
    title = re.search(r"<title>([^<]+)", html)
    emp = re.search(r'Employees\s*=\s*"([^"]+)"', html) or re.search(
        r"Personeel[^0-9]{0,40}([\d,\.]+)", html
    )
    filed = re.search(r"filed on ([0-9\-]+)", html, re.I) or re.search(
        r"neergelegd op ([0-9\-]+)", html, re.I
    )
    print(
        name,
        "Y",
        year_of(html),
        "len",
        len(html),
        "title",
        (title.group(1)[:70] if title else None),
        "emp",
        emp.group(1) if emp else None,
        "filed",
        filed.group(1) if filed else None,
        "blocks",
        parse_blocks(html)[:3],
    )

# KBO status bits
kbo = (outdir / "maria_kbo.html").read_text(encoding="utf-8")
for pat in [
    r"Status[^<]{0,40}",
    r"Actief|Active|Actif",
    r"Rechtsvorm[^<]{0,80}",
    r"VZW|ASBL",
    r"Beselarestraat[^<]{0,40}",
    r"E-mail[^<]{0,80}",
    r"NACE[^<]{0,120}",
    r"Vestigingseenheid",
    r"aanbestedende",
]:
    ms = re.findall(pat, kbo, re.I)
    if ms:
        print("KBO", pat, ms[:3])
