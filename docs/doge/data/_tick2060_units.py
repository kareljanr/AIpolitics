# summarize 2051-2059 for progress narrative
import csv
import re

csv.field_size_limit(10_000_000)
ids = {
    "vzw_wzc_van_lierde": "Van Lierde",
    "vzw_seniorenzorg_sint_vincentius_anzegem": "Ter Berk Anzegem",
    "vzw_wzc_walfergem": "Walfergem",
    "vzw_seniorenzorg_st_vincentius_lendelede": "Lendelede",
    "vzw_centrum_ganspoel": "Ganspoel",
    "vzw_huize_westerhauwe": "Westerhauwe",
    "vzw_groep_zorg_h_familie": "H. Familie",
    "vzw_tpandje_izegem": "t Pandje",
    "vzw_wzc_home_vrijzicht": "Vrijzicht",
}
with open("docs/doge/data/budgets.csv", encoding="utf-8-sig", newline="") as f:
    for b in csv.DictReader(f):
        eid = b.get("entity_id") or ""
        if eid in ids and b.get("year") == "2025" and "omzet" in (b.get("budget_id") or ""):
            print(ids[eid], b.get("amount_eur"), (b.get("notes") or "")[:90])

# also pnl
print("--- pnl ---")
with open("docs/doge/data/budgets.csv", encoding="utf-8-sig", newline="") as f:
    for b in csv.DictReader(f):
        eid = b.get("entity_id") or ""
        if eid in ids and b.get("year") == "2025" and "pnl" in (b.get("budget_id") or ""):
            print(ids[eid], b.get("amount_eur"), (b.get("notes") or "")[:90])
