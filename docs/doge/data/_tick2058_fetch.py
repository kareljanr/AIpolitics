# ephemeral fetch tick2058 — 't Pandje YE2025
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2058")
outdir.mkdir(parents=True, exist_ok=True)
KBO = "0424249987"


def decode(encoded):
    r = int(encoded[:2], 16)
    email = ""
    for n in range(2, len(encoded), 2):
        email += chr(int(encoded[n : n + 2], 16) ^ r)
    return email


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar"]:
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


URLS = {
    "tpandje_nl": f"https://www.companyweb.be/nl/{KBO}/t-pandje",
    "tpandje_en": f"https://www.companyweb.be/en/{KBO}/t-pandje",
    "tpandje_fr": f"https://www.companyweb.be/fr/{KBO}/t-pandje",
    "tpandje_kbo": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO}",
    "tpandje_site": "https://www.tpandje.be/",
    "tpandje_contact": "https://www.tpandje.be/contact",
    "tpandje_site2": "https://tpandje.be/",
    "faro_en": "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed",
    "aiesh_en": "https://www.companyweb.be/en/0201712587/aiesh",
    "rew_en": "https://www.companyweb.be/en/0644638937/rew",
}

for n, u in URLS.items():
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{n}.html").write_text(html, encoding="utf-8")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", html)))
        cf = [decode(x) for x in re.findall(r"email-protection#([a-f0-9]+)", html, re.I)]
        emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
        filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
        print(
            "OK",
            n,
            "Y",
            year_of(html),
            "emp",
            emp.group(1) if emp else None,
            "filed",
            filed.group(1) if filed else None,
            "blocks",
            parse_blocks(html)[:2],
            "emails",
            [e for e in emails if "sentry" not in e and "wix" not in e and "example" not in e][:8],
            "cf",
            cf[:4],
        )
    except Exception as e:
        print("FAIL", n, type(e).__name__, str(e)[:160])

kbo = (outdir / "tpandje_kbo.html").read_text(encoding="utf-8", errors="replace")
print("aanbestedende", "aanbestedende" in kbo.lower())
text = re.sub(r"<script[\s\S]*?</script>", "", kbo)
text = re.sub(r"<[^>]+>", "\n", text)
lines = [l.strip() for l in text.splitlines() if l.strip()]
for i, l in enumerate(lines):
    low = l.lower()
    if any(
        x in low
        for x in [
            "vestiging",
            "aanbested",
            "actief",
            "adres van de zetel",
            "rechtsvorm",
            "e-mail",
            "izegem",
            "87.",
            "naam",
            "status",
        ]
    ):
        print(i, l[:120], "|", (lines[i + 1][:80] if i + 1 < len(lines) else ""))
