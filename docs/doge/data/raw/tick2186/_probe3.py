import os
import re
import urllib.request

ua = {"User-Agent": "Mozilla/5.0"}
out = "docs/doge/data/raw/tick2186"

# Prefer large YE2025 with kern present
priority = [
    ("mariasteen", "0407079207"),
    ("blankedale", "0400999978"),
    ("kringwinkel_antwerpen", "0442423037"),
    ("de_wroeter", "0433138454"),
    ("a_kwadraat", "0406668540"),
    ("demival", "0407409007"),
    ("mirto", "0407656257"),
    ("mivas", "0407597958"),
    ("forena", "0425410920"),
    ("kunnig", "0404745465"),
    ("entiris", "0407841151"),
    ("bewel", "0407229358"),
    ("pajottenland", "0413313535"),
    ("bw_zottegem", "0407657148"),
    ("kaliber", "0407201941"),
    ("aarova", "0451263992"),
    ("acg", "0406611726"),
    ("oesterbank", "0407762165"),
    ("werkhuizen_min", "0407699908"),
    ("trianval", "0419052074"),
]


def parse_kern(html):
    m = re.search(
        r"window\.cw\.kernCijfers\s*=\s*(\{.*?\});",
        html,
        re.S,
    )
    # simpler: extract 2025 block
    m = re.search(
        r'2025\s*:\s*\{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    if not m:
        return None
    winst, equity, bruto, omzet = m.groups()

    def num(s):
        s = (s or "").strip().replace(" ", "").replace("\xa0", "")
        if s in ("", "-", "n/a", "N/A"):
            return None
        # EN: 1,841,558 or NL: 1.841.558 or mixed 1.841.558,50
        if re.search(r",\d{2}$", s) and "." in s:
            s = s.replace(".", "").replace(",", ".")
        elif s.count(",") > 1:
            s = s.replace(",", "")
        elif s.count(".") > 1:
            s = s.replace(".", "")
        elif "," in s and "." not in s:
            # could be 1841558,50 or 1,841,558 already handled
            parts = s.split(",")
            if len(parts) == 2 and len(parts[1]) == 2:
                s = parts[0] + "." + parts[1]
            else:
                s = s.replace(",", "")
        return float(s)

    fte_m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    fte = None
    if fte_m:
        fte = float(fte_m.group(1).replace(" FTE", "").replace(",", "."))
    filed_m = re.search(r"filed on ([0-9-]{10})", html, re.I)
    if not filed_m:
        filed_m = re.search(r"neergelegd op ([0-9-]{10})", html, re.I)
    year_m = re.search(r"Last balance sheet year\s*</[^>]*>\s*(\d{4})", html)
    if not year_m:
        year_m = re.search(r"Laatste balansjaar\s*</[^>]*>\s*(\d{4})", html)
    if not year_m:
        # plaintext after strip
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        year_m = re.search(r"Last balance sheet year (20\d\d)", text)
        if not year_m:
            year_m = re.search(r"Laatste balansjaar (20\d\d)", text)
    return {
        "winst": num(winst),
        "equity": num(equity),
        "bruto": num(bruto),
        "omzet": num(omzet),
        "fte": fte,
        "filed": filed_m.group(1) if filed_m else None,
        "year": year_m.group(1) if year_m else None,
    }


for name, kbo in priority:
    d = re.sub(r"\D", "", kbo)
    url = f"https://www.companyweb.be/en/{d}/"
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, timeout=25) as r:
        html = r.read().decode("utf-8", "replace")
        final = r.geturl()
    slug = final.rstrip("/").split("/")[-1]
    k = parse_kern(html)
    print(name, slug, k)
    if k and k.get("year") == "2025" and k.get("omzet"):
        open(os.path.join(out, f"pick_{d}_en.html"), "w", encoding="utf-8").write(html)
        print("  SELECTABLE", name, "omzet", k["omzet"], "pnl", k["winst"])
        break
    elif k and k.get("omzet"):
        # still save if 2025 kern exists even if year parse fail
        open(os.path.join(out, f"pick_{d}_en.html"), "w", encoding="utf-8").write(html)
        print("  SAVE_ANYWAY", name)
        if k.get("omzet") and k.get("omzet") > 1e6:
            print("  SELECTABLE_NOYEAR", name)
            break
