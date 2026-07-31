from pathlib import Path

cmt = Path("docs/doge/data/commitments.csv")
ct = cmt.read_text(encoding="utf-8")
lines = ct.splitlines()
out = []
changed = False
for line in lines:
    if line.startswith("cmt_wvl_prov_budget_2026") and "opcentiemen_2026" not in line:
        line = line.replace(
            '""opcentiemen_rate"":186.22',
            '""opcentiemen_2026"":128769361,""opcentiemen_2031"":150110481,""eigen_belastingen_2026"":57843000,""fiscal_total_2026"":186612461,""opcentiemen_rate"":186.22',
        )
        line = line.replace(
            "Schema M2 p15 exp 194.4m/216.6m strong tick85; invest+debt+AFM strong; subsidies class medium",
            "Schema M2+T2: exp 194.4m; opcent 128.8m rate 186.22; eigen tax 57.8m; invest+debt+AFM strong; subsidies class medium",
        )
        changed = True
    out.append(line)
if changed:
    cmt.write_text("\n".join(out) + ("\n" if ct.endswith("\n") else ""), encoding="utf-8")
    print("fixed")
else:
    print("no change needed")
