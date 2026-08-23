# ephemeral tick2009 probe4 — more unused hospitals with possible CW figures
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2009")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))


def summarize(name):
    path = dst / f"{name}.html"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:130] if title else None))
    print(" blocks", blocks[:2])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "Laatste balansjaar"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 170]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2])
    print()


urls = [
    # AZ Oudenaarde common KBO guesses via known names
    ("oudenaarde_en", "https://www.companyweb.be/en/0405.832.515".replace(".", "")),
    ("oudenaarde2", "https://www.companyweb.be/en/0417.850.711".replace(".", "")),
    ("vesalius_en", "https://www.companyweb.be/en/0412.123.185".replace(".", "")),  # may fail
    ("vesalius2", "https://www.companyweb.be/nl/search?q=AZ+Vesalius"),
    ("deinze_en", "https://www.companyweb.be/en/0405.501.xxx"),  # placeholder skip
    ("izegem_sj", "https://www.companyweb.be/nl/0405.832.xxx"),
    # Known from prior probes
    ("klina_en", "https://www.companyweb.be/en/0434302850/algemeen-ziekenhuis-klina"),
    ("monica_en", "https://www.companyweb.be/en/0459768815/monica"),
    ("mm_en", "https://www.companyweb.be/en/0405236067"),
    # Psychiatric / other: PC Bethanie / Alexianen / etc
    ("bethanie", "https://www.companyweb.be/en/search?q=0411.668.931"),
    # Try staatsbladmonitor pages for Waregem/Yperman deposits
    ("waregem_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0405460592"),
    ("yperman_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0462915078"),
    ("zottegem_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0418558166"),
    ("turnhout_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0897191602"),
]
# fix broken placeholders — real KBOs from web where known
urls = [
    ("klina_en", "https://www.companyweb.be/en/0434302850/algemeen-ziekenhuis-klina"),
    ("monica_en", "https://www.companyweb.be/en/0459768815/monica"),
    ("waregem_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0405460592"),
    ("yperman_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0462915078"),
    ("zottegem_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0418558166"),
    ("turnhout_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0897191602"),
    ("palfijn_sbm2", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0262926616"),
    # Sint-Jozef Izegem — search KBO via CW slug guess
    ("sj_izegem", "https://www.companyweb.be/nl/0405542593"),
    ("sv_deinze", "https://www.companyweb.be/nl/0411720245"),
    ("az_oudenaarde", "https://www.companyweb.be/nl/0406548741"),
    ("az_vesalius", "https://www.companyweb.be/nl/0412123185"),
]
for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name, _ in urls:
    summarize(name)
