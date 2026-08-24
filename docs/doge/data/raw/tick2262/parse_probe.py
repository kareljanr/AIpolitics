import re
from pathlib import Path
import urllib.request
import ssl

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
raw = Path(__file__).resolve().parent

# recover stall URLs from tick2261
for name in ["faro_en", "aiesh_en", "rew_en"]:
    t = (raw.parent / "tick2261" / f"{name}.html").read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'rel="canonical" href="([^"]+)"', t)
    url = m.group(1) if m else None
    print(name, "canon", url)
    if url:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
        (raw / f"{name}.html").write_bytes(data)
        tt = data.decode("utf-8", "ignore")
        y = re.search(r"Last balance sheet year.*?<[^>]+>(\d{4})", tt, re.S)
        print(" ", "year", y.group(1) if y else "?", "len", len(data))

for name in ["cw_en", "cw_nl", "cw_fr", "lorraine_en", "agb_bornem", "kbo"]:
    p = raw / f"{name}.html"
    if not p.exists():
        print(name, "MISSING")
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    print("====", name, "len", len(t))
    y = re.search(r"Last balance sheet year.*?<[^>]+>(\d{4})", t, re.S)
    print(" year", y.group(1) if y else "?")
    filed = re.search(r"filed on ([0-9\-]+)", t, re.I)
    print(" filed", filed.group(1) if filed else "?")
    # extract table rows after Financial data
    block = re.search(r"Financial data.*?</table>", t, re.I | re.S)
    if block:
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", block.group(0), re.S)
        for row in rows[:8]:
            cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)
            cells = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c]
            if cells:
                print(" ", cells)
    # kbo specifics
    if name == "kbo":
        for pat in [
            r"Status van de entiteit.*?<[^>]+>([^<]+)",
            r"Toestand van de entiteit.*?<[^>]+>([^<]+)",
            r"Rechtsvorm.*?<[^>]+>([^<]+)",
            r"Aantal vestigingseenheden.*?<[^>]+>([^<]+)",
            r"Nace[^<]{0,40}",
        ]:
            m = re.search(pat, t, re.I | re.S)
            if m:
                print(" ", pat[:40], "->", re.sub(r"\s+", " ", m.group(0)[:120]))
    if name == "agb_bornem":
        for y in ["2025", "2024", "Jaarrekening"]:
            print(" ", y, t.count(y))
