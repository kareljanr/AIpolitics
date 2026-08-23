# ephemeral tick1998 — deeper probe AIESH/REW/Bornem + hospital alts
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1998")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data), url)


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
    return float(s)


def summarize(name):
    path = dst / f"{name}.html"
    if not path.exists():
        print("MISSING", name)
        return
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:120] if title else None))
    print(" blocks", blocks[:3])
    for lab in [
        "Last balance sheet year",
        "filed on",
        "neergelegd op",
        "déposés le",
        "Total assets",
        "Balans totaal",
        "Eigen vermogen",
        "Equity",
        "Brutomarge",
        "Gross margin",
        "Turnover",
        "Omzet",
        "Profit",
        "Winst",
    ]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160].replace("\n", " ")[:160]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:3])
    # alt patterns sometimes used when omzet empty
    for pat_name, pat in [
        ("winst_only", r'winst:\s*"([^"]+)"'),
        ("equity_only", r'eigen_vermogen:\s*"([^"]+)"'),
        ("bruto_only", r'bruto_marge:\s*"([^"]+)"'),
        ("omzet_only", r'omzet:\s*"([^"]+)"'),
        ("balans", r'balans_totaal:\s*"([^"]+)"'),
    ]:
        m = re.findall(pat, t)
        if m:
            print(" ", pat_name, m[:4])
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0 winst,equity,bruto,omzet", y0)
            if len(blocks) > 1:
                y1 = tuple(parse_amount(x) for x in blocks[1])
                print(" y1", y1)
        except Exception as e:
            print(" parse err", e)
    print()


urls = [
    ("aiesh_en", "https://www.companyweb.be/en/0201712587"),
    ("aiesh_nl", "https://www.companyweb.be/nl/0201712587"),
    ("rew_en", "https://www.companyweb.be/en/0644638937"),
    ("rew_nl", "https://www.companyweb.be/nl/0644638937"),
    ("bornem_en", "https://www.companyweb.be/en/0877556624"),
    ("bornem_nl", "https://www.companyweb.be/nl/0877556624"),
    # better UZB / Erasme candidates
    ("uzb_acad_en", "https://www.companyweb.be/en/0775387613/academisch-ziekenhuis-van-brussel"),
    ("uzb_acad_nl", "https://www.companyweb.be/nl/0775387613/academisch-ziekenhuis-van-brussel"),
    ("azjp_search", "https://www.companyweb.be/nl/search?q=AZ+Jan+Palfijn"),
    ("zas_search", "https://www.companyweb.be/nl/search?q=Ziekenhuis+aan+de+Stroom"),
]

for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, e)

for name in [
    "aiesh_en",
    "rew_en",
    "bornem_en",
    "uzb_acad_en",
    "uzb_acad_nl",
    "azsl_gent_en",
    "azsl_brugge_en",
    "erasme_en",
]:
    summarize(name)

# also dump azsl gent for any numeric year markers near filing
for name in ["azsl_gent_en", "azsl_brugge_en"]:
    t = (dst / f"{name}.html").read_text(encoding="utf-8", errors="replace")
    # find JSON-ish financial payload
    for m in re.finditer(r".{0,40}(202[45]).{0,80}(neergeleg|filed|balance|jaarrekening|omzet|winst).{0,40}", t, re.I):
        print("CTX", name, repr(m.group(0)[:180]))
