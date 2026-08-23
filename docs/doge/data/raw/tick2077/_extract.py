# Extract Companyweb key figures from tick2077 HTML probes
import re
from pathlib import Path

RAW = Path(__file__).parent


def metric_block(t, label):
    m = re.search(label + r".{0,1200}", t, re.I | re.S)
    if not m:
        return None
    block = m.group(0)
    vals = re.findall(
        r"([0-9]{1,3}(?:\.[0-9]{3})+(?:,[0-9]+)?|-?[0-9]+,[0-9]+)", block
    )
    return vals[:15]


def extract(path: Path):
    t = path.read_text(encoding="utf-8", errors="replace")
    th_years = re.findall(r"<t[hd][^>]*>\s*(202[0-9])\s*</t[hd]>", t)
    dy = re.findall(r'data-year="(202[0-9])"', t)
    yh = sorted(set(re.findall(r">(202[0-9])<", t)))
    filing = re.findall(
        r"(?:neergelegd|filed|déposé|Laatste boekjaar|Dernier exercice|Last financial)[^<{]{0,100}",
        t,
        re.I,
    )[:8]
    # Highcharts categories often embed years
    cats = re.findall(r"categories\s*:\s*\[([^\]]+)\]", t)
    metrics = {}
    for lab in [
        "Omzet",
        "Turnover",
        "Chiffre d",
        "Winst/Verlies",
        "Profit/Loss",
        "Eigen vermogen",
        "Equity",
        "Balanstotaal",
        "Total assets",
        "Total de l",
        "Bruto",
        "Gross margin",
        "FTE",
        "Workforce",
        "Bedrijfsopbrengsten",
        "Activa",
        "Assets",
        "Schulden",
        "Debts",
    ]:
        v = metric_block(t, lab)
        if v:
            metrics[lab] = v
    # Also try JSON-LD / __NEXT or window.__ data
    euro_near_2025 = []
    for m in re.finditer(r"2025.{0,200}", t):
        chunk = m.group(0)
        nums = re.findall(r"[0-9]{1,3}(?:\.[0-9]{3})+", chunk)
        if nums:
            euro_near_2025.append((chunk[:80], nums[:5]))
    return {
        "file": path.name,
        "th_years": th_years[:24],
        "dy": dy[:24],
        "yh": yh[-10:],
        "filing": filing[:6],
        "cats": cats[:3],
        "metrics": metrics,
        "near_2025": euro_near_2025[:8],
    }


def main():
    for f in sorted(RAW.glob("*.html")):
        if f.name.startswith("kbo"):
            continue
        r = extract(f)
        print("====", r["file"])
        print(" th", r["th_years"], "dy", r["dy"], "yh", r["yh"])
        print(" filing", r["filing"][:4])
        print(" cats", r["cats"][:2])
        for k, v in r["metrics"].items():
            print(f"  {k}: {v}")
        if r["near_2025"]:
            print(" near2025", r["near_2025"][:4])


if __name__ == "__main__":
    main()
