import urllib.request, re, ssl
from pathlib import Path

RAW = Path("docs/doge/data/raw/tick2103")
RAW.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

cands = [
    ("faro", "https://www.companyweb.be/en/0893863017/faro"),
    ("aiesh", "https://www.companyweb.be/en/0201712587/aiesh"),
    ("rew", "https://www.companyweb.be/en/0644638937/rew"),
    ("korian", "https://www.companyweb.be/en/0869769702/korian-belgium"),
    ("agb_bornem", "https://www.companyweb.be/en/0877556624/agb-bornem"),
    ("comnexio", "https://www.companyweb.be/en/0727639263/comnexio"),
]

pat = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

for name, url in cands:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            html = r.read().decode("utf-8", errors="ignore")
        (RAW / f"{name}_en.html").write_text(html, encoding="utf-8")
        m = re.search(r"Latest balance sheet year\s*</[^>]+>\s*(\d{4})", html, re.I | re.S)
        if not m:
            m = re.search(r"Laatste balansjaar\s*</[^>]+>\s*(\d{4})", html, re.I | re.S)
        if not m:
            m = re.search(r"Dernier exercice\s*</[^>]+>\s*(\d{4})", html, re.I | re.S)
        year = m.group(1) if m else "?"
        t = re.search(r"<h1[^>]*>\s*([^<]+)", html)
        title = re.sub(r"\s+", " ", t.group(1)).strip()[:70] if t else name
        euros = {
            ym.group(1): {
                "pnl": ym.group(2),
                "eq": ym.group(3),
                "bruto": ym.group(4),
                "omzet": ym.group(5),
            }
            for ym in pat.finditer(html)
        }
        # alternate: look for chart data years
        years_found = sorted(set(re.findall(r"\b(202[3-6])\b", html[:15000])))
        print(f"{name}|year={year}|{title}|e25={euros.get('2025')}|e24={euros.get('2024')}|yrs={years_found[:6]}|len={len(html)}")
    except Exception as e:
        print(f"{name}|FAIL|{type(e).__name__}:{e}")
