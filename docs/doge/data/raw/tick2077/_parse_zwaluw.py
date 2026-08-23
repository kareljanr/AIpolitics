# Parse De Zwaluw Companyweb NL+EN+FR for YE2022-2025 key figures
import re
import json
from pathlib import Path

RAW = Path(__file__).parent


def parse_be_num(s):
    s = s.strip().replace("\xa0", "").replace(" ", "")
    if not s or s in ("-", "n.b.", "n/a", "N/A"):
        return None
    # Belgian: 5.443.008,42 or English 5,443,008.42
    if re.match(r"^-?\d{1,3}(\.\d{3})+(,\d+)?$", s):
        s = s.replace(".", "").replace(",", ".")
    elif re.match(r"^-?\d{1,3}(,\d{3})+(\.\d+)?$", s):
        s = s.replace(",", "")
    elif "," in s and "." not in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def extract_chart_series(t):
    """Pull Highcharts-like embedded year/value pairs from CW pages."""
    out = {}
    # Look for patterns like "name":"Omzet" ... data:[...]
    for m in re.finditer(
        r'"name"\s*:\s*"([^"]+)"\s*,\s*"data"\s*:\s*\[([^\]]+)\]', t
    ):
        name = m.group(1)
        nums = []
        for x in m.group(2).split(","):
            x = x.strip()
            if x in ("null", "None", ""):
                nums.append(None)
            else:
                try:
                    nums.append(float(x))
                except ValueError:
                    nums.append(None)
        out[name] = nums
    # categories years
    cats = re.search(r'"categories"\s*:\s*\[([^\]]+)\]', t)
    years = []
    if cats:
        years = re.findall(r"20\d{2}", cats.group(1))
    return years, out


def scrape_kpi_cards(t):
    """Companyweb KPI cards often have structure with year labels and values."""
    # Find blocks with class kpi or financial-figure
    results = {}
    # Pattern around latest year value displayed large
    for lab in [
        "Omzet",
        "Turnover",
        "Chiffre d'affaires",
        "Chiffre d&#x27;affaires",
        "Winst/Verlies",
        "Profit/Loss",
        "Eigen vermogen",
        "Equity",
        "Capitaux propres",
        "Bruto marge",
        "Gross margin",
        "Marge brute",
        "Bedrijfsopbrengsten",
        "Operating income",
        "Produits d",
        "FTE",
        "Workforce",
        "Balanstotaal",
        "Total assets",
        "Total de l",
        "Schulden",
        "Debts",
        "Dettes",
    ]:
        # find label then nearby number with Belgian format
        pat = re.compile(
            re.escape(lab) + r".{0,400}?>([-0-9][0-9\.\s,]{2,20})<",
            re.I | re.S,
        )
        m = pat.search(t)
        if m:
            results[lab] = m.group(1).strip()
    return results


def find_multi_year_table(t):
    """Find year columns 2022 2023 2024 2025 and row values."""
    # Sometimes CW embeds Vue/JSON state
    blobs = re.findall(r"\{[^{}]{0,80}\"year\"\s*:\s*202[0-9][^{}]{0,200}\}", t)
    rows = []
    for b in blobs:
        rows.append(b)
    # Also search for sequences of 4 years
    years = ["2022", "2023", "2024", "2025"]
    # Find all euro-like numbers near each year mention in financial section
    return rows


def dump_interesting(t, label):
    # Extract all occurrences of numbers that look like millions near key words
    print(f"\n--- {label} KPI cards ---")
    print(scrape_kpi_cards(t))
    years, series = extract_chart_series(t)
    print("chart years", years)
    for k, v in list(series.items())[:20]:
        print(f"  series {k}: {v}")
    # Look for financialStatements or similar JSON
    for key in [
        "financialStatements",
        "keyFigures",
        "annualAccounts",
        "ratios",
        "turnover",
        "equity",
        "fte",
    ]:
        idx = t.lower().find(key.lower())
        if idx >= 0:
            print(f"  found '{key}' at {idx}:", t[idx : idx + 200].replace("\n", " ")[:200])


def main():
    for name in ["zwaluw_nl.html", "zwaluw_en.html", "zwaluw_fr.html"]:
        t = (RAW / name).read_text(encoding="utf-8", errors="replace")
        dump_interesting(t, name)
        # Print context around "5.443.008" / "5,443"
        for needle in ["5.443.008", "5,443", "1.429.803", "9.070.655", "3.910.864", "2025"]:
            idx = t.find(needle)
            if idx >= 0:
                ctx = t[max(0, idx - 100) : idx + 150].replace("\n", " ")
                print(f"  ctx[{needle}]: ...{ctx}...")


if __name__ == "__main__":
    main()
