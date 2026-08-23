# ephemeral fetch tick2042 — Psychogeriatrisch Centrum NL/EN/FR + KBO
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2042")
outdir.mkdir(parents=True, exist_ok=True)


def fetch(name, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        html = r.read().decode("utf-8", "replace")
    (outdir / f"{name}.html").write_text(html, encoding="utf-8")
    print("OK", name, len(html))
    return html


for name, url in [
    ("psychoger_nl", "https://www.companyweb.be/nl/0435357675/psychogeriatrisch-centrum"),
    ("psychoger_fr", "https://www.companyweb.be/fr/0435357675/psychogeriatrisch-centrum"),
    ("psychoger_en", "https://www.companyweb.be/en/0435357675/psychogeriatrisch-centrum"),
    ("arcus_korian", "https://www.korian.be/woonzorgcentra/arcus/neuropsychogeratrischcentrum-arcus/"),
    ("arcus_wzc", "https://www.korian.be/woonzorgcentra/arcus/woonzorgcentrum-arcus/"),
]:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:120])

# KBO
try:
    url = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435357675"
    html = fetch("kbo_0435357675", url)
    for label in ["Status", "Rechtsvorm", "Adres", "E-mailadres", "Email", "E-mail"]:
        i = html.find(label)
        if i >= 0:
            snippet = re.sub(r"<[^>]+>", " ", html[i : i + 400])
            snippet = re.sub(r"\s+", " ", snippet)[:180]
            print("KBO", label, ":", snippet)
except Exception as e:
    print("KBO FAIL", type(e).__name__, str(e)[:120])

# parse EN amounts + filing date
html = (outdir / "psychoger_en.html").read_text(encoding="utf-8")
blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    html,
)
print("blocks", blocks[:3])
emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
print("emp", emp.group(1) if emp else None)
for pat in [
    r"filed on ([0-9\-]+)",
    r"neergelegd op ([0-9\.\-]+)",
    r"déposés le ([0-9\-]+)",
    r"Last balance sheet year",
]:
    m = re.search(pat, html, re.I)
    if m:
        print("hit", pat, m.group(0)[:80] if m.lastindex is None or m.lastindex == 0 else m.group(1))
