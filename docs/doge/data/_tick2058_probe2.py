# ephemeral probe2 tick2058 — 't Pandje + more
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2058")
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
        filed = re.search(r"filed on ([0-9\-]+)", html, re.I)
        title = re.search(r"<title>([^<]+)", html)
        print(
            "==",
            name,
            "Y",
            year,
            "filed",
            filed.group(1) if filed else None,
            "emp",
            emp.group(1) if emp else None,
            (title.group(1)[:60] if title else ""),
        )
        if blocks:
            print("  y0", tuple(parse_amount(x) for x in blocks[0]))
            if len(blocks) > 1:
                print("  y1", tuple(parse_amount(x) for x in blocks[1]))
        return year
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:160])
        return None


for n, u in [
    ("tpandje_en", "https://www.companyweb.be/en/0424249987"),
    ("tpandje_nl", "https://www.companyweb.be/nl/0424249987"),
    ("de_bolster_en", "https://www.companyweb.be/en/041515075"),  # maybe emmaus - wrong
    ("pz_hf_search", "https://www.companyweb.be/en/0400371161"),  # abdij
    ("wielant", "https://www.companyweb.be/en/0475400760"),  # famifamenne guess
    ("vulpia", "https://www.companyweb.be/en/0453287037"),  # samen ouder already
]:
    probe_cw(n, u)
