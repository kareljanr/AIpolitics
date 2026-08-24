import re
import urllib.request
import ssl
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = Path(__file__).resolve().parent

targets = {
    "apre": "https://www.companyweb.be/en/0407598354",
    "renaitre": "https://www.companyweb.be/en/0407851148",
    "citeco": "https://www.companyweb.be/en/0460976761",
    "sipres": "https://www.companyweb.be/en/0423643540",
    "stallbois": "https://www.companyweb.be/en/0407149877",
    "apn": "https://www.companyweb.be/en/0411929207",
    # other possible Walloon free ETAs
    "creahm": "https://www.companyweb.be/en/0422028539",  # guess skip if 404
}


def clean_cells(row):
    cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
    return [re.sub(r"\s+", " ", c) for c in cells if c]


def parse(name, html):
    print("====", name)
    y = re.search(r"Last balance sheet year.*?<[^>]+>(\d{4}|N/A)", html, re.S | re.I)
    print(" year", y.group(1) if y else None)
    filed = re.search(r"filed on ([0-9.\-/]+)", html, re.I)
    print(" filed", filed.group(1) if filed else None)
    nm = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    if nm:
        print(" name", re.sub(r"<[^>]+>|\s+", " ", nm.group(1)).strip()[:90])
    st = re.search(r"Status.*?<[^>]+>(Active|Actif|Actief)", html, re.S | re.I)
    print(" status", st.group(1) if st else None)
    nace = re.search(r"Principal activity.*?<[^>]+>([^<]+)", html, re.S | re.I)
    print(" nace", nace.group(1).strip()[:80] if nace else None)
    block = re.search(r"Financial data.*?</table>", html, re.I | re.S)
    if block:
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", block.group(0), re.S)
        for row in rows[:8]:
            cells = clean_cells(row)
            if cells:
                print(" ", cells)
    else:
        print("  NO TABLE / opaque?")


for name, url in targets.items():
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        (raw / f"{name}_en.html").write_bytes(data)
        html = data.decode("utf-8", "ignore")
        if "Error 404" in html or "Page not found" in html:
            print("====", name, "404")
            continue
        parse(name, html)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
