# tick 181 — Farys OV jaarrekening 2024 (full utility, not Creat Services)
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-28T10:25:00Z"
src_url = "https://www.farys.be/sites/farys/files/media/documents/WEB-250616_Farys_Jaarverslag2024.pdf"
src_url_2023 = "https://www.farys.be/sites/farys/files/media/documents/Jaarverslag_Farys_2023_v2.pdf"
src_url_2022 = "https://www.farys.be/sites/farys/files/media/documents/WEB_Farys_Jaarverslag2022.pdf"

# amounts in EUR (source tables in k€)
omzet_2024 = 506_292_000
omzet_2023 = 495_968_000
omzet_2022 = 453_987_000
bedrijfsopbr_2024 = 597_954_000
bedrijfsopbr_2023 = 567_695_000
bedrijfsopbr_2022 = 538_073_000
bedrijfskosten_2024 = 524_218_000
ebit_2024 = 73_736_000
ebit_2023 = 61_239_000
pbt_2024 = 38_609_000
net_2024 = 38_180_000
net_2023 = 29_230_000
net_2022 = 28_688_000
assets_2024 = 3_655_172_000
assets_2023 = 3_544_031_000
equity_2024 = 1_920_852_000
equity_2023 = 1_862_491_000
equity_2022 = 1_800_168_000
mva_2024 = 3_230_807_000
lt_debt_2024 = 1_337_381_000
st_debt_2024 = 370_339_000
lt_debt_2023 = 1_260_133_000
cap_sub_2024 = 245_272_000
cap_sub_2023 = 222_772_000
personnel_2024 = 96_761_000
fin_cost_2024 = 42_754_000
invest_mva_2024 = 190_130_000  # aanschaffingen materiële VA
bank_lt_2024 = 933_765_000
other_loans_lt_2024 = 371_250_000  # MTN / private placement

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_farys_ov_jv_2024,Farys OV geintegreerd jaarverslag 2024 maatschappelijke jaarrekening,"
        + src_url
        + ",Farys OV,2026-07-28,official_annual_report,"
        '"Omzet 506.3m bedrijfsopbr 598.0m net 38.2m assets 3.655bn equity 1.921bn '
        "LT debt 1.337bn ST 370m MVA 3.231bn cap sub 245m invest MVA 190m 2024; "
        'prior mislabeled Creat Services DV only; tick181"\n'
    )
    f.write(
        "src_farys_ov_jv_2023,Farys OV jaarverslag 2023 maatschappelijke jaarrekening,"
        + src_url_2023
        + ",Farys OV,2026-07-28,official_annual_report,"
        '"Comparative 2023: omzet 496.0m bedrijfsopbr 567.7m net 29.2m assets 3.544bn '
        'equity 1.862bn LT debt 1.260bn; tick181"\n'
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "farys,Farys OV,Farys,East/West Flanders public water sewer sport intercommunal,"
        "parastatal,sec_flanders,nl,https://www.farys.be,,,"
        "ex-TMVW; omzet 506m op.rev 598m assets 3.66bn 2024; dual DWG Pidpa Water-link SWDE; "
        "includes sport division; tick181\n"
    )

rows = [
    ("bud_farys_omzet_2024", "farys", 2024, omzet_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Omzet 506.292m 2024 (k€ table)"),
    ("bud_farys_omzet_2023", "farys", 2023, omzet_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Omzet 495.968m 2023 comparative in JV2024"),
    ("bud_farys_omzet_2022", "farys", 2022, omzet_2022, "", "", "outturn", "src_farys_ov_jv_2023", "strong", "Omzet 453.987m 2022 from JV series"),
    ("bud_farys_bedrijfsopbr_2024", "farys", 2024, bedrijfsopbr_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Bedrijfsopbrengsten 597.954m 2024"),
    ("bud_farys_bedrijfsopbr_2023", "farys", 2023, bedrijfsopbr_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Bedrijfsopbrengsten 567.695m 2023 comparative JV2024"),
    ("bud_farys_bedrijfsopbr_2022", "farys", 2022, bedrijfsopbr_2022, "", "", "outturn", "src_farys_ov_jv_2023", "strong", "Bedrijfsopbrengsten 538.073m 2022"),
    ("bud_farys_bedrijfskosten_2024", "farys", 2024, bedrijfskosten_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Bedrijfskosten 524.218m 2024"),
    ("bud_farys_ebit_2024", "farys", 2024, ebit_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Bedrijfswinst 73.736m 2024"),
    ("bud_farys_ebit_2023", "farys", 2023, ebit_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Bedrijfswinst 61.239m 2023"),
    ("bud_farys_net_2024", "farys", 2024, net_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Te bestemmen winst 38.180m 2024"),
    ("bud_farys_net_2023", "farys", 2023, net_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Te bestemmen winst 29.230m 2023"),
    ("bud_farys_net_2022", "farys", 2022, net_2022, "", "", "outturn", "src_farys_ov_jv_2023", "strong", "Te bestemmen winst 28.688m 2022"),
    ("bud_farys_pbt_2024", "farys", 2024, pbt_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Winst voor belasting 38.609m 2024"),
    ("bud_farys_assets_2024", "farys", 2024, assets_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Balanstotaal 3655.172m end-2024"),
    ("bud_farys_assets_2023", "farys", 2023, assets_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Balanstotaal 3544.031m end-2023"),
    ("bud_farys_equity_2024", "farys", 2024, equity_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Eigen vermogen 1920.852m end-2024"),
    ("bud_farys_equity_2023", "farys", 2023, equity_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Eigen vermogen 1862.491m end-2023"),
    ("bud_farys_mva_2024", "farys", 2024, mva_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Materiele vaste activa 3230.807m end-2024 (~88pct assets)"),
    ("bud_farys_lt_debt_2024", "farys", 2024, lt_debt_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Schulden >1jr 1337.381m end-2024 (bank 933.8m + MTN/other 371.3m)"),
    ("bud_farys_st_debt_2024", "farys", 2024, st_debt_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Schulden <=1jr 370.339m end-2024"),
    ("bud_farys_lt_debt_2023", "farys", 2023, lt_debt_2023, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Schulden >1jr 1260.133m end-2023"),
    ("bud_farys_cap_subsidies_2024", "farys", 2024, cap_sub_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Kapitaalsubsidies 245.272m end-2024"),
    ("bud_farys_personnel_2024", "farys", 2024, personnel_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Bezoldigingen sociale lasten pensioenen 96.761m 2024"),
    ("bud_farys_fin_cost_2024", "farys", 2024, fin_cost_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Financiele kosten 42.754m 2024"),
    ("bud_farys_invest_mva_2024", "farys", 2024, invest_mva_2024, "", "", "outturn", "src_farys_ov_jv_2024", "strong", "Aanschaffingen MVA 190.130m 2024"),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(",".join(str(x) for x in r) + "\n")

meta = {
    "2024_omzet": omzet_2024,
    "2024_bedrijfsopbr": bedrijfsopbr_2024,
    "2023_omzet": omzet_2023,
    "2022_omzet": omzet_2022,
    "2024_net": net_2024,
    "2024_assets": assets_2024,
    "2024_equity": equity_2024,
    "2024_lt_debt": lt_debt_2024,
    "2024_st_debt": st_debt_2024,
    "2024_mva": mva_2024,
    "2024_cap_subsidies": cap_sub_2024,
    "2024_personnel": personnel_2024,
    "2024_invest_mva": invest_mva_2024,
    "note": "East/West Flanders water+sewer+sport; dual DWG Pidpa Water-link; prior tick mislabeled Creat Services DV",
}
meta_csv = '"' + json.dumps(meta, separators=(",", ":")).replace('"', '""') + '"'
cmt = (
    "cmt_farys_2022_24,Farys Flanders water multi-year,farys,"
    "East West Flanders households munis sport participants,"
    "Municipal intercommunal OHV + VMM tariffs + sport contracts,2022-01-01,2022,2024,"
    f"{omzet_2024},{meta_csv},0,active,{src_url},"
    "Produce distribute drink water sewer sport infrastructure Flanders,"
    "Publish dual unit-cost Farys DWG Pidpa Water-link; open multi-year debt CAPEX path,"
    "src_farys_ov_jv_2024,strong,Vlaanderen>Water>Farys,tick181\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt)

lb = (
    "lb_farys_vl_water,Farys Flanders water omzet 506m op.rev 598m 2024,"
    "Flanders,ops,Vlaanderen>Water>Farys,506292000,3655172000,"
    "Omzet 506.3m bedrijfsopbr 598.0m strong JV; assets 3.66bn equity 1.92bn LT debt 1.34bn "
    "net 38.2m invest MVA 190m; dual DWG Pidpa Water-link; sport+water perimeter,"
    "strong,src_farys_ov_jv_2024,East West Flanders households munis,"
    "Essential drinking water sewer plus sport infra,"
    "Core public service tariff-regulated; large debt stock for network CAPEX; dual VL water,"
    "2,9.0,5,5.8,"
    "Publish dual unit-cost VL water companies; open multi-year invest vs tariff path,seed,,tick181\n"
)
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    f.write(lb)

# research_queue
rq_path = base / "research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
found = False
for i, line in enumerate(lines):
    if line.startswith("rq_176,"):
        lines[i] = (
            "rq_176,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,"
            "L5,gg_belgium,"
            '"Prefer public primary fills (Farys ov full accounts Antwerp register Mons '
            "BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open "
            'rq; do not idle while public work remains.",'
            ",2026-07-28T10:05:00Z,2026-07-28T10:25:00Z,"
            '"tick181: Farys OV JV2024 omzet 506m op.rev 598m net 38.2m assets 3.66bn '
            'equity 1.92bn LT debt 1.34bn; VL water dual complete; spawn rq_177"'
        )
        found = True
        break
assert found, "rq_176 not found"
if not any(l.startswith("rq_177,") for l in lines):
    lines.append(
        "rq_177,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,"
        "L5,gg_belgium,"
        '"Prefer public primary fills (Antwerp register Mons BI2026 FPS taxex other large '
        "FOI-adjacent utilities/SOEs) if new PDFs appear; else next open rq; do not idle "
        'while public work remains.",'
        ",2026-07-28T10:25:00Z,,"
        '"Spawned tick181 after Farys OV; rq_116 SWA deferred Oct-Dec 2026"'
    )
rq_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_176,181,no,"
    '"Scheduler 60s. Next prio5 rq_177 hole-fill Antwerp/Mons/taxex; rq_116 SWA deferred. '
    'FOI ready human send. tick181 Farys OV omzet 506m assets 3.66bn VL water dual complete."\n',
    encoding="utf-8",
)

entry = f"""
### {now} - tick 181
- Unit: **rq_176** (FOI-adjacent hole-fill - **Farys OV jaarrekening 2024**)
- Found (strong primary integrated annual report maatschappelijke jaarrekening; prior public files were Creat Services DV only):
  - **Omzet EUR 506.292m 2024** (496.0m 2023 / 454.0m 2022) · bedrijfsopbrengsten **597.954m**.
  - **Bedrijfswinst 73.736m** · PBT **38.609m** · **net 38.180m** (29.2m 2023).
  - Assets **3.655bn** · MVA **3.231bn** (~88pct) · equity **1.921bn** · cap subsidies **245m**.
  - LT debt **1.337bn** (bank 934m + MTN/other 371m) · ST debt **370m** · invest MVA **190m**.
  - Personnel **96.8m** · fin. costs **42.8m** · sport+water+sewer perimeter (ex-TMVW).
  - **VL water dual complete:** DWG 838m + Pidpa 403m + Water-link 255m + **Farys 506m** (+ SWDE/Vivaqua/Aquafin).
- Wrote: sources 2; entity 1; budgets 25; cmt 1; lb 1; rq_176=done; seeded **rq_177**.
- FOI: Antwerp/Mons + other ready stack human send; Farys ov gap closed by public fill.
- Next: prio5 **rq_177**; deferred **rq_116** SWA.
"""
log_path = Path("docs/doge/loop_log.md")
with open(log_path, "ab") as f:
    f.write(entry.encode("utf-8"))

print("tick181 write OK")
print((base / "loop_state.csv").read_text(encoding="utf-8"))
for line in rq_path.read_text(encoding="utf-8").splitlines():
    if line.startswith("rq_176") or line.startswith("rq_177"):
        print(line[:160])
