# tick 180 — Water-link OV jaarrekening 2025
import json
import re
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-28T10:05:00Z"
src_url = (
    "https://water-link2025.jaarverslag.org/wp-content/uploads/sites/1050/"
    "2026/06/JAARREKENING-2025_24062026.pdf"
)
jv_url = "https://water-link2025.jaarverslag.org/"

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_waterlink_jr_2025,Water-link OV jaarrekening 2025 statutair VOL NBB-style,"
        + src_url
        + ",Water-link OV,2026-07-28,official_annual_report,"
        '"Omzet 254.5m bedrijfsopbr 426.9m net 16.5m assets 571.5m equity 313.7m '
        "debt 250.2m LT fin 37.7m dividend-like 4.16m 2025; omzet 2024 225.9m; "
        'KBO 0204.923.881; tick180"\n'
    )
    f.write(
        "src_waterlink_jv_2025,Water-link jaarverslag 2025 kerncijfers ops,"
        + jv_url
        + ",Water-link OV,2026-07-28,official_annual_report,"
        '"Ops: produce 154.2m m3 staff 488 invest water 15.4m sewer 57m; '
        '213k drink clients 628k inh; tick180"\n'
    )

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "water_link,Water-link OV,Water-link,"
        "Antwerp region public water and sewer intercommunal,"
        "parastatal,sec_flanders,nl,https://www.water-link.be,,,"
        "Antwerp metro drink+sewer+industry; omzet 254.5m op.rev 426.9m assets "
        "571.5m 2025 KBO 0204923881; dual DWG Pidpa Farys; tick180\n"
    )

# --- budgets ---
rows = [
    ("bud_waterlink_omzet_2025", "water_link", 2025, 254546322, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Omzet code 70 254.546m 2025"),
    ("bud_waterlink_omzet_2024", "water_link", 2024, 225867491, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Omzet code 70 225.867m 2024"),
    ("bud_waterlink_bedrijfsopbr_2025", "water_link", 2025, 426904160, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Bedrijfsopbrengsten 70/76A 426.904m 2025 incl geprod VA 82.6m andere 89.7m"),
    ("bud_waterlink_bedrijfsopbr_2024", "water_link", 2024, 379527688, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Bedrijfsopbrengsten 379.528m 2024"),
    ("bud_waterlink_bedrijfskosten_2025", "water_link", 2025, 406667574, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Bedrijfskosten 406.668m 2025"),
    ("bud_waterlink_ebit_2025", "water_link", 2025, 20236586, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Bedrijfswinst 20.237m 2025 (13.509m 2024)"),
    ("bud_waterlink_net_profit_2025", "water_link", 2025, 16509006, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Winst boekjaar 16.509m 2025 code 9904"),
    ("bud_waterlink_net_profit_2024", "water_link", 2024, 16917021, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Winst boekjaar 16.917m 2024"),
    ("bud_waterlink_pbt_2025", "water_link", 2025, 23150163, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Winst voor belasting 23.150m 2025"),
    ("bud_waterlink_tax_2025", "water_link", 2025, 6686574, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Belastingen op resultaat 6.687m 2025"),
    ("bud_waterlink_assets_2025", "water_link", 2025, 571527021, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Balanstotaal 571.527m end-2025"),
    ("bud_waterlink_assets_2024", "water_link", 2024, 540413698, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Balanstotaal 540.414m end-2024"),
    ("bud_waterlink_equity_2025", "water_link", 2025, 313680510, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Eigen vermogen 313.681m end-2025"),
    ("bud_waterlink_equity_2024", "water_link", 2024, 299741405, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Eigen vermogen 299.741m end-2024"),
    ("bud_waterlink_debt_total_2025", "water_link", 2025, 250160647, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Schulden totaal 250.161m end-2025"),
    ("bud_waterlink_fin_debt_lt_2025", "water_link", 2025, 37746967, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Financiele schulden LT kredietinstellingen 37.747m end-2025"),
    ("bud_waterlink_dividend_2025", "water_link", 2025, 4160297, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Uit te keren winst vergoeding inbreng 4.160m 2025 (dividend-like to munis)"),
    ("bud_waterlink_cap_subsidies_2025", "water_link", 2025, 1767056, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Kapitaalsubsidies passief 1.767m end-2025 (was 0.177m 2024)"),
    ("bud_waterlink_personnel_2025", "water_link", 2025, 57585141, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Bezoldigingen sociale lasten pensioenen 57.585m 2025"),
    ("bud_waterlink_invest_water_2025", "water_link", 2025, 15400000, "", "", "outturn", "src_waterlink_jv_2025", "strong", "JV kern: 15.4m invest drinkwater vervanging/uitbreiding 2025"),
    ("bud_waterlink_invest_sewer_2025", "water_link", 2025, 57000000, "", "", "outturn", "src_waterlink_jv_2025", "strong", "JV kern: 57m invest riolering vervanging/uitbreiding 2025"),
    ("bud_waterlink_geprod_va_2025", "water_link", 2025, 82643584, "", "", "outturn", "src_waterlink_jr_2025", "strong", "Geproduceerde vaste activa code 72 82.644m 2025 (capitalised production)"),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(",".join(str(x) for x in r) + "\n")

# --- commitments ---
meta = {
    "2025_omzet": 254546322,
    "2025_bedrijfsopbr": 426904160,
    "2024_omzet": 225867491,
    "2025_net": 16509006,
    "2025_assets": 571527021,
    "2025_equity": 313680510,
    "2025_debt": 250160647,
    "2025_fin_debt_lt": 37746967,
    "2025_dividend": 4160297,
    "2025_personnel": 57585141,
    "invest_water": 15400000,
    "invest_sewer": 57000000,
    "staff": 488,
    "prod_m3": 154169158,
    "kbo": "0204923881",
    "note": "Antwerp metro drink+sewer+industry; dual DWG Pidpa Farys SWDE",
}
meta_csv = '"' + json.dumps(meta, separators=(",", ":")).replace('"', '""') + '"'
cmt_line = (
    "cmt_waterlink_2024_25,Water-link Antwerp water multi-year,water_link,"
    "Antwerp metro households industry munis,"
    "Municipal intercommunal OHV + VMM tariffs,2024-01-01,2024,2025,254546322,"
    + meta_csv
    + ",0,active,"
    + src_url
    + ",Produce distribute drink water sewer industry Antwerp,"
    "Publish dual unit-cost VL water; open multi-year CAPEX vs tariff; track Farys residual,"
    "src_waterlink_jr_2025,strong,Vlaanderen>Water>Water-link,tick180\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt_line)

# --- leaderboard ---
lb = (
    "lb_waterlink_antwerp_water,Water-link Antwerp water omzet 255m op.rev 427m 2025,"
    "Flanders,ops,Vlaanderen>Water>Water-link,254546322,571527021,"
    "Omzet 254.5m bedrijfsopbr 426.9m strong JR; assets 571.5m equity 314m net 16.5m "
    "debt 250m LT fin 37.7m; invest water 15.4m sewer 57m; dividend-like 4.16m,"
    "strong,src_waterlink_jr_2025,Antwerp metro households industry,"
    "Essential drinking water sewer industry water,"
    "Core public service; capitalised production large; dual DWG Pidpa Farys,"
    "2,8.0,5,5.3,"
    "Publish dual unit-cost Water-link Pidpa DWG Farys; open CAPEX path,seed,,tick180\n"
)
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    f.write(lb)

# --- research_queue ---
rq_path = base / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
lines = text.splitlines()
found = False
for i, line in enumerate(lines):
    if line.startswith("rq_175,"):
        lines[i] = (
            "rq_175,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,"
            "L5,gg_belgium,"
            '"Prefer public primary fills (Farys ov full accounts water-link Antwerp '
            "register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; "
            'else next open rq; do not idle while public work remains.",'
            ",2026-07-28T09:45:00Z,2026-07-28T10:05:00Z,"
            '"tick180: Water-link JR2025 omzet 254.5m op.rev 426.9m net 16.5m assets '
            '571.5m equity 314m debt 250m; Farys ov still opaque; spawn rq_176"'
        )
        found = True
        break
assert found, "rq_175 not found"
if not any(l.startswith("rq_176,") for l in lines):
    lines.append(
        "rq_176,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,"
        "L5,gg_belgium,"
        '"Prefer public primary fills (Farys ov full accounts Antwerp register Mons '
        "BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open "
        'rq; do not idle while public work remains.",'
        ",2026-07-28T10:05:00Z,,"
        '"Spawned tick180 after Water-link; rq_116 SWA deferred Oct-Dec 2026"'
    )
rq_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

# --- loop_state ---
(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_175,180,no,"
    '"Scheduler 60s. Next prio5 rq_176 hole-fill Farys ov/Antwerp/Mons/taxex; '
    "rq_116 SWA deferred. FOI ready human send. tick180 Water-link omzet 255m "
    'op.rev 427m."\n',
    encoding="utf-8",
)

# --- loop_log ---
log_path = Path("docs/doge/loop_log.md")
entry = f"""
### {now} - tick 180
- Unit: **rq_175** (FOI-adjacent hole-fill - **Water-link OV jaarrekening 2025**)
- Found (strong primary statutaire jaarrekening VOL; vector-rendered pages):
  - **Omzet EUR 254.546m 2025** (225.867m 2024) · bedrijfsopbrengsten **426.904m** · bedrijfskosten **406.668m**.
  - **Bedrijfswinst 20.237m** · PBT **23.150m** · tax **6.687m** · **net profit 16.509m** (16.917m 2024).
  - Assets **571.527m** · equity **313.681m** · inbreng **189.275m** · reserves **120.613m**.
  - Debt total **250.161m** · LT fin debt **37.747m** · capital subsidies **1.767m**.
  - Uit te keren winst (vergoeding inbreng) **4.160m** · personnel **57.585m**.
  - JV ops: produce **154.2m m³** · staff **488** · invest water **15.4m** + sewer **57m**.
  - KBO **0204.923.881** · Grant Thornton unqualified · dual VL water with DWG/Pidpa; Farys ov residual.
- Wrote: sources 2; entity 1; budgets 22; cmt 1; lb 1; rq_175=done; seeded **rq_176**.
- FOI: residual Farys ov full accounts + Antwerp/Mons FOIs human send.
- Next: prio5 **rq_176**; deferred **rq_116** SWA.
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + entry, encoding="utf-8")

print("tick180 write OK")
for line in rq_path.read_text(encoding="utf-8").splitlines():
    if line.startswith("rq_175") or line.startswith("rq_176"):
        print(line[:180])
print((base / "loop_state.csv").read_text(encoding="utf-8"))
