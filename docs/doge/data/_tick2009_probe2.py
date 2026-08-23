# ephemeral tick2009 probe2 — NBB PDFs + more unused hospitals
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2009")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url, binary=False):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        data = resp.read()
    ext = ".pdf" if binary or url.endswith(".pdf") else ".html"
    (dst / f"{name}{ext}").write_bytes(data)
    print("FETCH", name, len(data), resp.geturl()[:100])
    return data


urls = [
    # Jan Palfijn YE2025 NBB via staatsbladmonitor / data.be deposit
    ("palfijn_nbb", "http://cdn.staatsbladmonitor.be/2026pdf/2026-00292847.pdf", True),
    ("palfijn_sbm", "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0262926616", False),
    # Zottegem / Turnhout mirrors
    ("zottegem_fr", "https://www.companyweb.be/fr/0418558166/algemeen-ziekenhuis-sint-elisabeth-zottegem", False),
    ("turnhout_nl", "https://www.companyweb.be/nl/0897191602/az-turnhout", False),
    ("turnhout_fr", "https://www.companyweb.be/fr/0897191602/az-turnhout", False),
    # Waregem OLV Lourdes — common KBOs to try via search pages
    ("waregem_cw", "https://www.companyweb.be/nl/search?q=0416.711.492", False),
    ("yperman_cw", "https://www.companyweb.be/en/0405.749.941", False),  # guess
    ("deinze_cw", "https://www.companyweb.be/en/search?q=Sint-Vincentius+Deinze", False),
    ("izegem_cw", "https://www.companyweb.be/en/search?q=Sint-Jozef+Izegem", False),
    # Upswitch / pappers for Palfijn
    ("palfijn_pappers", "https://www.pappers.be/nl/company/algemeen-ziekenhuis-jan-palfijn-gent-0262926616", False),
]

for name, url, *rest in [(u[0], u[1], u[2] if len(u) > 2 else False) for u in urls]:
    try:
        fetch(name, url, binary=rest)
    except Exception as e:
        print("FAIL", name, e)


def summarize_html(name):
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
    print(" title", (title.group(1)[:120] if title else None))
    print(" blocks", blocks[:2])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "Laatste balansjaar", "2025", "omzet"]:
        i = t.find(lab)
        if i >= 0 and lab in ("Last balance sheet year", "filed on", "neergelegd op", "Laatste balansjaar"):
            print(" ", lab, repr(t[i : i + 160]))
    # money-ish
    euros = re.findall(r"€\s*([\d.,]+)", t)
    print(" euro samples", euros[:8])
    print()


for n in [
    "palfijn_sbm",
    "zottegem_fr",
    "turnhout_nl",
    "turnhout_fr",
    "waregem_cw",
    "yperman_cw",
    "deinze_cw",
    "izegem_cw",
    "palfijn_pappers",
]:
    summarize_html(n)

pdf = dst / "palfijn_nbb.pdf"
if pdf.exists():
    print("PDF size", pdf.stat().st_size)
    # try pdftotext or pypdf
    try:
        import pypdf

        r = pypdf.PdfReader(str(pdf))
        text = "\n".join((p.extract_text() or "") for p in r.pages[:8])
        print("PDF text head", text[:2000])
    except Exception as e:
        print("pypdf fail", e)
        try:
            raw = pdf.read_bytes()
            # crude string extract
            chunks = re.findall(rb"[\x20-\x7e]{6,}", raw)
            joined = b"\n".join(chunks[:80]).decode("ascii", errors="ignore")
            print("crude", joined[:1500])
        except Exception as e2:
            print("crude fail", e2)
