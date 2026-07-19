import csv
from pathlib import Path

rows = list(csv.DictReader(Path(__file__).with_name("fps_taxex_parsed_latest.csv").open(encoding="utf-8")))
keys = [
    "benefit",
    "wagen",
    "vehicle",
    "car",
    "meal",
    "voucher",
    "cheque",
    "option",
    "notional",
    "interest deduction",
    "participation exemption",
    "dtr",
    "fdi",
]
for r in rows:
    n = r["name"].lower()
    if any(k in n for k in keys):
        print(f"{float(r['amount_mio']):8.2f}", r["sheet"], r["year"], r["name"][:110])
