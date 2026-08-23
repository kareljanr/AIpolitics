# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
DATA = RAW.parents[1]
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)

taken = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken += (DATA / "leaderboard.csv").read_text(encoding="utf-8", errors="replace")
# do-not-redo + recent notes
dn = (
    "0412.640.671 0405.311.530 0443.082.637 0452.865.383 0445.175.263 "
    "0417.958.152 0448.190.181 0440.691.388 0202.395.052 0477.445.084 "
    "0893.863.017 0201.712.587 0644.638.937 0466.961.859"
)
taken += dn

# from tick2108 hunt + common unused + sisters of taken
cands = [
    # correct prefer
    ("aiesh", "0201712587"),
    ("rew", "0644638937"),
    ("buissons", "0466961859"),  # deferred but confirm live
    # unused WZC/MRS guesses / prior probes with real KBOs
    ("wzc_haagwinde", "0410219433"),
    ("wzc_denolm", "0413863017"),
    ("wzc_immaculata", "0407899064"),
    ("wzc_wingerd", "0425890123"),
    ("wzc_bijster", "0410678901"),
    ("wzc_olv_dendermonde", "0405123456"),
    ("wzc_olv_haaltert", "0417958000"),
    ("wzc_sj_merksem", "0405678901"),
    ("wzc_hof_schoten", "0877556624"),
    ("wzc_buitenhof", "0685516024"),
    ("wzc_zusterhof", "0598966387"),
    ("wzc_familiehof", "0480566704"),
    # from tick2108 cand files
    ("cand_0201712587", "0201712587"),
    ("cand_0417958152", "0417958152"),  # camillus TAKEN
    ("cand_0443249616", "0443249616"),
    ("cand_0445175263", "0445175263"),
    ("cand_0452865383", "0452865383"),  # ninove TAKEN
    ("cand_0466266429", "0466266429"),
    ("cand_0480566704", "0480566704"),
    ("cand_0598966387", "0598966387"),
    ("cand_0644638937", "0644638937"),  # REW
    ("cand_0685516024", "0685516024"),
    ("cand_0877556624", "0877556624"),
    ("cand_0887690451", "0887690451"),
    ("cand_0893863017", "0893863017"),  # FARO
    # more MRS/WZC Walloon/Flemish
    ("mrs_val_des_roses", "0400123456"),
    ("wzc_ter_lant", "0439442761"),
    ("igs_interza", "0203333333"),
    ("igs_iveka", "0203444444"),
    ("sedilec", "0203555555"),
    ("teo", "0203666666"),
    ("iecbw", "0203777777"),
    ("hydrobru", "0203888888"),
    ("sim_limburg", "0203999999"),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as resp:
        return resp.read()


def parse(html: str):
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title = re.search(r"<title>([^<]+)</title>", html, re.I)
    lb = re.search(
        r"(?:Laatste balansjaar|Last balance sheet year|Dernier bilan)\s+(\d{4})",
        text,
        re.I,
    )
    euros = {m.group(1): m.groups()[1:] for m in PAT.finditer(html)}
    ftes = re.findall(r"([\d\.,]+)\s*FTE", text)
    neer = re.search(
        r"(?:neergelegd op|filed on|déposés le)\s+([\d\-]+)", text, re.I
    )
    deltas = re.findall(
        r"(Omzet|Turnover|Chiffre d.affaires|Brutomarge|Gross margin|"
        r"Marge brute|Winst/Verlies|Profit/Loss|Bénéfice/Perte|"
        r"Eigen vermogen|Equity|Capitaux propres|"
        r"Werknemers|Employees|Employés)"
        r"[^%]{0,80}?([+\-−]?\s*[\d\.,]+\s*%)",
        text,
        re.I,
    )
    return {
        "title": title.group(1)[:100] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:4],
        "deltas": deltas[:8],
    }


# First parse existing tick2108 cand htmls for YE2025 unused
print("=== tick2108 cand HTML ===")
p08 = Path("docs/doge/data/raw/tick2108")
for p in sorted(p08.glob("cand_*.html")):
    html = p.read_text(encoding="utf-8", errors="ignore")
    info = parse(html)
    kbo_m = re.search(r"BE\s*(\d{4})[.\s]?(\d{3})[.\s]?(\d{3})", html)
    kbo = (
        f"{kbo_m.group(1)}.{kbo_m.group(2)}.{kbo_m.group(3)}" if kbo_m else "?"
    )
    already = kbo != "?" and (kbo in taken or kbo.replace(".", "") in taken)
    e25 = info["euros"].get("2025")
    if info["year"] == "2025" or e25:
        print(
            f"{p.name}|{kbo}|already={already}|y={info['year']}|"
            f"e25={e25}|fte={info['ftes']}|title={info['title'][:70]}"
        )

print("\n=== LIVE hunt ===")
seen = set()
for slug, kbo in cands:
    if kbo in seen:
        continue
    seen.add(kbo)
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    already = dotted in taken or kbo in taken
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        if "Error 404" in info["title"] or info["year"] == "?":
            print(f"SKIP {slug} {dotted} already={already} title={info['title'][:60]}")
            continue
        e25 = info["euros"].get("2025")
        e24 = info["euros"].get("2024")
        flag = "TAKEN" if already else "FREE"
        print(
            f"{flag} {slug}|{dotted}|y={info['year']}|neer={info['neer']}|"
            f"e25={e25}|e24o={(e24[3] if e24 else None)}|"
            f"fte={info['ftes']}|d={info['deltas'][:5]}|"
            f"title={info['title'][:75]}"
        )
    except Exception as e:
        print(f"ERR {slug} {dotted} {type(e).__name__}: {e}")
