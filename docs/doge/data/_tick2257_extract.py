# tick 2257 — extract Val du Geer YE2025 from CW EN/NL/FR + KBO
import re
from pathlib import Path

RAW = Path(__file__).resolve().parent / "raw" / "tick2257"


def strip_tags(s: str) -> str:
    s = re.sub(r"<script[^>]*>.*?</script>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<style[^>]*>.*?</style>", " ", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&[a-z]+;", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def find_near(text: str, label: str, window: int = 180):
    hits = []
    for m in re.finditer(re.escape(label), text, re.I):
        chunk = text[m.start() : m.start() + window]
        nums = re.findall(r"[-+]?\d[\d.,]*", chunk)
        hits.append((chunk[:160], nums[:8]))
    return hits


def parse_eu_number(s: str):
    s = s.strip().replace(" ", "").replace("\xa0", "")
    neg = s.startswith("-") or s.startswith("(")
    s = s.strip("-() ")
    if re.match(r"^\d{1,3}(\.\d{3})+(,\d+)?$", s):
        s = s.replace(".", "").replace(",", ".")
    elif re.match(r"^\d{1,3}(,\d{3})+(\.\d+)?$", s):
        s = s.replace(",", "")
    elif "," in s and "." not in s:
        s = s.replace(",", ".")
    try:
        v = float(s)
        return -v if neg else v
    except ValueError:
        return None


def main():
    for lang in ("en", "nl", "fr"):
        html = (RAW / f"valdugeer_{lang}.html").read_text(encoding="utf-8", errors="replace")
        text = strip_tags(html)
        print("====", lang, "len", len(html), "text", len(text))
        # key phrases
        for lab in [
            "Last balance sheet year",
            "Balansjaar",
            "Dernier exercice",
            "Turnover",
            "Omzet",
            "Chiffre d'affaires",
            "Gross margin",
            "Bruto marge",
            "Marge brute",
            "Profit/Loss",
            "Winst/Verlies",
            "Bénéfice",
            "Equity",
            "Eigen vermogen",
            "Capitaux propres",
            "FTE",
            "Filing date",
            "Neerleggingsdatum",
            "Date de dépôt",
            "Staff",
            "Personnel",
        ]:
            hits = find_near(text, lab, 200)
            if hits:
                print(f"  {lab}: {hits[0]}")
                if len(hits) > 1:
                    print(f"    alt: {hits[1]}")

        # Look for year 2025 blocks with euros in HTML attributes / Vue
        # Often KPIs appear as: >10.750.401< or data values
        # Extract sequences around "2025"
        for m in re.finditer(r"2025", text):
            chunk = text[max(0, m.start() - 80) : m.start() + 120]
            if any(k in chunk.lower() for k in ("turnover", "omzet", "profit", "equity", "marge", "fte", "gross", "winst", "chiffre")):
                print("  ctx2025:", chunk)

    # KBO
    kbo = (RAW / "valdugeer_kbo.html").read_text(encoding="utf-8", errors="replace")
    kt = strip_tags(kbo)
    print("==== KBO snippet")
    for lab in ["Status", "Actief", "Adres", "Rechtsvorm", "Vestiging", "NACE", "Begin"]:
        hits = find_near(kt, lab, 150)
        if hits:
            print(lab, hits[0][0][:140])
    print(kt[:1500])

    # Also dump JSON-ish numbers from EN page: look for key financial table rows
    html = (RAW / "valdugeer_en.html").read_text(encoding="utf-8", errors="replace")
    # Companyweb often embeds like: "key":"omzet" ... values
    for pat in [
        r"omzet.{0,80}",
        r"turnover.{0,80}",
        r"bruto.{0,80}",
        r"grossMargin.{0,80}",
        r"winst.{0,80}",
        r"eigenVermogen.{0,80}",
        r"fte.{0,80}",
        r"rubriek.?70.{0,120}",
        r"10/15.{0,120}",
        r"9904.{0,120}",
    ]:
        ms = re.findall(pat, html, re.I)
        if ms:
            print("PAT", pat, "->", ms[:3])

    # Try structured: look for FAQ answers with euro amounts (seen in prior: turnover of €X)
    text = strip_tags(html)
    for m in re.finditer(r"(turnover|gross margin|profit/loss|equity|fte)[^\.]{0,40}of €?\s*([-€\d.,]+)", text, re.I):
        print("FAQ", m.group(0)[:120])

    # Table extraction: years as headers then rows
    # Find all euro amounts with nearby year
    pairs = re.findall(r"(202[0-9]).{0,40}?€\s*([\d.,]+)|€\s*([\d.,]+).{0,40}?(202[0-9])", text)
    print("year-euro pairs sample", pairs[:30])


if __name__ == "__main__":
    main()
