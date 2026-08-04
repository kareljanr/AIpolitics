"""FOI sweep ranks 121-300: mark material partials."""
import csv
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

UPDATES = {
    "gap_sfpim_l5_stakes": (
        "NBB VOL YE2025: assets 11.679bn FVA 9.847bn equity 11.445bn; impairments 105.4m+56.2m; "
        "named >=10pct stakes (Proximus 53.5pct bpost 50pct Ethias 31.7pct BAC 25pct etc). "
        "Residual: SFPIM book/fair value per stake; impairments by company; dividends by stake"
    ),
    "gap_favv_budget_2024_26": (
        "Kamer 1281/014+022: 2026 spend 216.7m (pers 133.1 ops 81.1 invest 2.5); "
        "dot 114.5m retributions 65.6m heffingen 42.4m; dot path 116.0/113.8/114.5m 2024-26. "
        "Residual: full income outturn 2024-25"
    ),
    "gap_natlot_society_l5": (
        "AR2024: society 362.5m = good causes 217.5m + monopolierente 145m. "
        "Residual: named top50 good-cause EUR; 2025 definitive split"
    ),
    "gap_sck_dotatie_missions_2023_26": (
        "SCK Highlights gov-subs 94.2m 2024 / 98.8m 2025; Kamer 2026 working 57.974m "
        "MYRRHA P1 7.9 P2 1.65 phys-prot 9.921 invest 4.111. Residual: mission cash-by-year recon"
    ),
    "gap_astrid_toelage_reconcile": (
        "Triple public: IBZ 76.517m / contract ops 46.5m / statutory omzet 27.16m; "
        "Kamer BA 59.366m 2025-26. Residual: formal recon of perimeters"
    ),
    "gap_infrabel_jv2025_l5": (
        "JV2025: omzet 1.426bn state dot 606.3m infra fee 514.8m personnel 844.7m "
        "invest 1.266bn assets 25.73bn. Residual: FPS cash codes + project top20"
    ),
    "gap_we_l5_stakes": (
        "WE AR2025 consol assets 6.383bn equity 5.807bn result 251.6m. "
        "Residual: named book values top stakes"
    ),
    "gap_we_portfolio_book_l5": (
        "WE AR2025 write-downs 71.55m guarantee prov 101.8m portfolio ~4.48bn. "
        "Residual: named stakes + deals >=10m liberations"
    ),
    "gap_pmv_l5_stakes": (
        "PMV JR2025 assets 4.236bn equity 4.180bn dividend 3.8m; managed 1.941bn 2024. "
        "Residual: top50 stakes/loans matrix"
    ),
    "gap_smals_l5_members": (
        "Smals omzet ~578.9m; CoA sector split SS 62.9pct / federal 25.4pct; ONSS path 110.9m. "
        "Residual: full member invoice matrix"
    ),
}

path = "docs/doge/data/foi_queue.csv"
with open(path, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    fields = rdr.fieldnames
    rows = list(rdr)

n = 0
for r in rows:
    gid = r.get("gap_id")
    if gid not in UPDATES:
        continue
    if r.get("status") == "answered":
        continue
    r["status"] = "partial"
    r["response_summary"] = UPDATES[gid]
    r["updated_utc"] = NOW
    notes = r.get("notes") or ""
    tag = "sweep2026-08-05"
    if tag not in notes:
        r["notes"] = (notes + f" | {tag}: status partial material public fill").strip(" |")
    n += 1
    print("partial", gid)

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

from collections import Counter

print("updated", n)
print(dict(Counter(r.get("status") for r in rows)))
