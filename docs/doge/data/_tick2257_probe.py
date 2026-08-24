# tick 2257 probe — preferred stall check + FREE ETA candidates
import re
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent / "raw" / "tick2257"
RAW.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-doge/1.0)"}


def fetch(url: str, name: str) -> str:
    p = RAW / name
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        p.write_bytes(data)
        print(f"OK {name} {len(data)} {url}")
        return data.decode("utf-8", "replace")
    except Exception as e:
        print(f"FAIL {name} {e} {url}")
        return ""


def parse_cw(html: str, label: str) -> dict:
    out = {"label": label}
    m = re.search(r"Last balance sheet year.{0,200}?>(\d{4})<", html, re.I | re.S)
    if not m:
        m = re.search(r"balansjaar.{0,200}?>(\d{4})<", html, re.I | re.S)
    if m:
        out["year"] = m.group(1)
    # common KPI blocks
    for key, pat in [
        ("turnover", r"Turnover</[^>]*>.{0,400}?€\s*([\d.,]+)"),
        ("gross", r"Gross margin</[^>]*>.{0,400}?€\s*([\d.,]+)"),
        ("pnl", r"Profit/Loss</[^>]*>.{0,400}?([-€\s\d.,]+)"),
        ("equity", r"Equity</[^>]*>.{0,400}?€\s*([\d.,]+)"),
        ("fte", r">FTE</[^>]*>.{0,400}?>([\d.,]+)<"),
    ]:
        mm = re.search(pat, html, re.I | re.S)
        if mm:
            out[key] = mm.group(1).strip()
    # filing date
    fd = re.search(r"(?:Filing date|Neerleggingsdatum|Date de d.pôt).{0,120}?(\d{2}[-/.]\d{2}[-/.]\d{4})", html, re.I | re.S)
    if fd:
        out["filed"] = fd.group(1)
    # comparative table years
    years = re.findall(r">\s*(202[0-9])\s*<", html)
    out["years_seen"] = sorted(set(years))[-6:]
    print(label, out)
    return out


def eur(s: str | None):
    if not s:
        return None
    s = s.replace("€", "").replace(" ", "").replace("\xa0", "").strip()
    s = s.replace(".", "").replace(",", ".") if s.count(",") == 1 and s.count(".") >= 1 else s
    # BE/EU style: 10.750.401,00 or 10750401
    if re.match(r"^-?\d{1,3}(\.\d{3})+(,\d+)?$", s):
        s = s.replace(".", "").replace(",", ".")
    elif "," in s and "." not in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return s


def main():
    prefer = {
        "faro_en": "https://www.companyweb.be/en/0893863017",
        "aiesh_en": "https://www.companyweb.be/en/0201712587",
        "rew_en": "https://www.companyweb.be/en/0644638937",
        "agb_bornem_en": "https://www.companyweb.be/en/0877556624",
    }
    for name, url in prefer.items():
        html = fetch(url, name + ".html")
        if html:
            parse_cw(html, name)

    # Val du Geer known KBO 0407.841.646
    html = fetch("https://www.companyweb.be/en/0407841646", "valdugeer_en.html")
    if html:
        parse_cw(html, "valdugeer")
    for lang in ("nl", "fr"):
        fetch(f"https://www.companyweb.be/{lang}/0407841646", f"valdugeer_{lang}.html")
    fetch(
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0407841646",
        "valdugeer_kbo.html",
    )

    # Nekto / Erables: search via companyweb or leseta then CW
    # Try google-ish via CW search pages / known patterns
    for q, name in [
        ("nekto", "search_nekto.html"),
        ("les%20erables%20eta", "search_erables.html"),
        ("heropbeuring", "search_herop.html"),
    ]:
        fetch(f"https://www.companyweb.be/en/search?q={q}", name)

    # Nekto site contact for BCE
    fetch("https://www.nekto.be/", "site_nekto.html")
    fetch("https://www.nekto.be/contact", "site_nekto_contact.html")
    fetch("https://leseta.be/annuaire-eta/nekto/", "leseta_nekto.html")
    fetch("https://leseta.be/annuaire-eta/les-erables/", "leseta_erables.html")
    fetch("https://www.valdugeer.be/013/fr/Contact", "site_valdugeer_contact.html")
    fetch("https://www.leserables.be/", "site_erables.html")
    fetch("https://www.leserables.be/contact", "site_erables_contact.html")


if __name__ == "__main__":
    main()
