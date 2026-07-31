# tick 182 — rq_178 VL Mijn Kortingsbon + MVP air-air (high clown)
# Completes concurrent seed of portals/lb/FOI with minister PQ cash bounds + close unit
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-28T10:45:00Z"

# Minister SV 89 (2022) + SV 718 (2023) — counts of VERSTUURDE bonnen (not necessarily redeemed)
sent_2020 = 9808
sent_2021 = 14629
sent_2022 = 29258  # "dubbel 2021" medium derived
face = 250
# 2019 redeemed washers+fridges only (cited in SV89 from prior Danen answer)
used_2019_wash_fridge = 2314 + 2329  # 4643
cash_2019_partial = used_2019_wash_fridge * face  # 1_160_750

src_pq718 = "https://docs.vlaamsparlement.be/pfile?id=1972510"
src_pq89 = "https://docs.vlaamsparlement.be/pfile?id=1894181"

# --- sources (append if not already present) ---
src = (base / "sources.csv").read_text(encoding="utf-8")
if "src_vl_mijn_kortingsbon_portal" not in src:
    with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
        f.write(
            "src_vl_mijn_kortingsbon_portal,Mijn Kortingsbon energiezuinige koelkast wasmachine diepvriezer (stop new 2026-01-01),"
            "https://www.vlaanderen.be/bouwen-wonen-en-energie/energieverbruik-en-kosten-verminderen/sociale-maatregelen-voor-energie/mijn-kortingsbon-voor-een-energiezuinige-koelkast-wasmachine-of-diepvriezer,"
            "Vlaanderen.be / Fluvius,2026-07-28,official_portal,"
            "250 EUR voucher means-tested fridge washer freezer; new applications stopped 01.01.2026; residual bon valid to expiry; no annual cash total on page\n"
        )
if "src_vl_mvp_warmtepomp_airair" not in src:
    with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
        f.write(
            "src_vl_mvp_warmtepomp_airair,Mijn VerbouwPremie warmtepomp incl lucht-lucht (airco dual-use rules),"
            "https://www.vlaanderen.be/bouwen-wonen-en-energie/bouwen-en-verbouwen/premies-voor-renovatie/mijn-verbouwpremie/mijn-verbouwpremie-voor-warmtepomp,"
            "Vlaanderen.be,2026-07-28,official_portal,"
            "lucht-lucht rates 300-600 EUR by income band; active cooling rules; pure airco excluded on paper; cash split air-air vs other WP not published\n"
        )
if "src_vl_kortingsbon_pq718" not in src:
    with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
        f.write(
            "src_vl_kortingsbon_pq718,SV 718 Bothuyne Demir kortingsbon 8 mei 2023 + annex,"
            f"{src_pq718},Vlaams Parlement,2026-07-28,parliamentary_qa,"
            '"Verstuurde bonnen 2022 ~2x 2021 and 3x 2020; Q1 2023 ~1/3 of 2022; annex tables per appliance not OCR-extracted this tick; redemption cash FOI; tick182"\n'
        )
if "src_vl_kortingsbon_pq89" not in src:
    with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
        f.write(
            "src_vl_kortingsbon_pq89,SV 89 Aerts Demir kortingsbonnen Fluvius 14 okt 2022,"
            f"{src_pq89},Vlaams Parlement,2026-07-28,parliamentary_qa,"
            f'"Verstuurd 2020 9808 / 2021 14629 strong; 2019 used wash 2314 fridge 2329 cited; annex paid-by-appliance FOI residual; tick182"\n'
        )

# --- budgets ---
bud = (base / "budgets.csv").read_text(encoding="utf-8")
rows = []
if "bud_vl_kortingsbon_sent_2020" not in bud:
    rows.extend(
        [
            ("bud_vl_kortingsbon_sent_2020", "vlaanderen_gov", 2020, sent_2020 * face, "", "", "outturn", "src_vl_kortingsbon_pq89", "strong", "Face value of 9808 VERSTUURDE bonnen x250; NOT cash paid (redemption unknown)"),
            ("bud_vl_kortingsbon_sent_2021", "vlaanderen_gov", 2021, sent_2021 * face, "", "", "outturn", "src_vl_kortingsbon_pq89", "strong", "Face value of 14629 VERSTUURDE bonnen x250; NOT cash paid"),
            ("bud_vl_kortingsbon_sent_2022", "vlaanderen_gov", 2022, sent_2022 * face, "", "", "outturn", "src_vl_kortingsbon_pq718", "medium", "Face value ~29258 sent (2x 2021 per minister) x250; medium derived; NOT cash paid"),
            ("bud_vl_kortingsbon_used_2019_wash_fridge", "vlaanderen_gov", 2019, cash_2019_partial, "", "", "outturn", "src_vl_kortingsbon_pq89", "medium", "2019 USED only wash 2314+fridge 2329 =4643 x250 =1.161m medium (cited prior PQ); excludes dryer freezer"),
            ("bud_vl_kortingsbon_face_unit", "vlaanderen_gov", 2025, face, "", "", "budgeted", "src_vl_mijn_kortingsbon_portal", "strong", "Unit face value 250 EUR/appliance; new apps stopped 2026-01-01"),
            ("bud_vl_mvp_airair_rate_low", "vlaanderen_gov", 2025, 300, "", "", "budgeted", "src_vl_mvp_warmtepomp_airair", "strong", "MVP lucht-lucht low income-band rate 300 EUR (portal)"),
            ("bud_vl_mvp_airair_rate_high", "vlaanderen_gov", 2025, 600, "", "", "budgeted", "src_vl_mvp_warmtepomp_airair", "strong", "MVP lucht-lucht higher band rate up to 600 EUR (portal)"),
            ("bud_vl_heat_premiums_2023_coa", "vlaanderen_gov", 2023, 22_000_000, "", "", "outturn", "src_ccrek_hernieuwbare_vl_2025", "strong", "CoA heat pump/boiler premiums ~22m 2023 (all WP types; air-air share unknown FOI)"),
        ]
    )
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write(",".join(str(x) for x in r) + "\n")

# --- commitments ---
cmt_path = base / "commitments.csv"
cmt_text = cmt_path.read_text(encoding="utf-8")
if "cmt_vl_mijn_kortingsbon_witgoed" not in cmt_text:
    meta = {
        "face_eur": 250,
        "sent_2020": sent_2020,
        "sent_2021": sent_2021,
        "sent_2022_est": sent_2022,
        "face_issued_2020": sent_2020 * face,
        "face_issued_2021": sent_2021 * face,
        "face_issued_2022_est": sent_2022 * face,
        "used_2019_wash_fridge_cash": cash_2019_partial,
        "new_apps_stopped": "2026-01-01",
        "note": "Sent face value upper-bounds only; cash paid = redeemed FOI; air-air MVP rates 300-600 no cash split",
    }
    meta_csv = '"' + json.dumps(meta, separators=(",", ":")).replace('"', '""') + '"'
    cmt = (
        "cmt_vl_mijn_kortingsbon_witgoed,Flanders Mijn Kortingsbon white goods + MVP air-air,"
        "vlaanderen_gov,Low-income Flanders households retailers Fluvius,"
        "Energiebesluit / Fluvius admin + MVP decree,2019-01-01,2019,2025,"
        f"{sent_2021 * face},{meta_csv},0,closed_new_apps,"
        f"{src_pq89},"
        "Means-tested voucher energy-efficient appliances + air-air heat pump premiums,"
        "Publish redeemed cash by appliance year; air-air vs other WP L5; prefer cash energy allowance,"
        "src_vl_kortingsbon_pq89,medium,Vlaanderen>Energie>Mijn_Kortingsbon,tick182\n"
    )
    with open(cmt_path, "a", encoding="utf-8", newline="") as f:
        f.write(cmt)

# --- leaderboard: update existing seed rows if present, else append ---
lb_path = base / "leaderboard.csv"
lb = lb_path.read_text(encoding="utf-8")
# rewrite the two seed lines with better notes if present
new_lb_kort = (
    "lb_vl_mijn_kortingsbon_appliances,Flanders Mijn Kortingsbon 250 EUR fridge/washer/freezer vouchers,"
    "Flanders,subsidy,Vlaanderen>Energie>Mijn_Kortingsbon_witgoed,"
    f"{sent_2021 * face},{sent_2020 * face + sent_2021 * face + sent_2022 * face},"
    f"Face issued ~3.66m 2021 / ~2.45m 2020 / ~7.3m 2022est (sent x250 medium); cash paid Unknown FOI; "
    f"2019 used wash+fridge only 1.16m medium; new apps stopped 2026-01-01; unit 250 strong portal,"
    "medium,src_vl_kortingsbon_pq89,Low-income Flanders households retailers Fluvius admin,"
    "Energy-efficient white goods for vulnerable households,"
    "Deadweight + admin sandwich HighCo; public pays for fridges/washers; cash transfer would dominate,"
    "8.5,5.5,4,7.0,"
    "Publish redeemed cash by appliance year; keep stop or replace with cash energy allowance,seed,,tick182\n"
)
new_lb_air = (
    "lb_vl_airco_mvp_luchtlucht,Flanders MVP air-to-air heat pump (aircon dual-use) premiums,"
    "Flanders,subsidy,Vlaanderen>Energie>MVP>lucht_lucht_airco,"
    "300,22000000,"
    "Unit rates 300-600 EUR strong portal; pure cooling excluded on paper but dual-use AC marketed as heat pump; "
    "cash split air-air vs other WP UNKNOWN FOI; parent CoA heat premiums 22m 2023 / 112m cum 2014-23,"
    "medium,src_vl_mvp_warmtepomp_airair,Homeowners installers airco vendors,"
    "Electrify heating via air-air heat pumps,"
    "Cooling-as-climate marketing; enforcement FOI; peak summer electricity load; deadweight comfort cooling,"
    "9.0,4.0,5,6.85,"
    "Publish L5 air-air vs other WP cash; ban premium if primary use cooling; income-target only,seed,,tick182\n"
)
lines = lb.splitlines()
out = []
has_kort = has_air = False
for line in lines:
    if line.startswith("lb_vl_mijn_kortingsbon_appliances,"):
        out.append(new_lb_kort.rstrip("\n"))
        has_kort = True
    elif line.startswith("lb_vl_airco_mvp_luchtlucht,"):
        out.append(new_lb_air.rstrip("\n"))
        has_air = True
    else:
        out.append(line)
if not has_kort:
    out.append(new_lb_kort.rstrip("\n"))
if not has_air:
    out.append(new_lb_air.rstrip("\n"))
lb_path.write_text("\n".join(out) + "\n", encoding="utf-8")

# --- research_queue: mark rq_178 done ---
rq_path = base / "research_queue.csv"
rqlines = rq_path.read_text(encoding="utf-8").splitlines()
found = False
for i, line in enumerate(rqlines):
    if line.startswith("rq_178,"):
        rqlines[i] = (
            "rq_178,VL appliance airco fridge washer subsidies high clown,hole_fill,9,done,"
            "L5,vlaanderen_gov,"
            "Map cash L5 for (1) Mijn Kortingsbon / Fluvius 250 EUR energy-efficient fridge freezer washer "
            "(new apps stopped 2026-01-01) annual paid 2021-2025 by appliance; (2) Mijn VerbouwPremie "
            "lucht-lucht warmtepomp (airco dual-use) cash split vs other heat pumps 2023-2026. Primary VEKA "
            "Fluvius CoA; seed FOI if totals missing. High absurdity: public pay for white goods and cooling-as-climate.,"
            "gap_vl_odv_mvp_cash,2026-07-27T11:26:25Z,2026-07-28T10:45:00Z,"
            f'"tick182: portals+PQ: sent face 2020 2.45m / 2021 3.66m / 2022est 7.3m medium; 2019 used wash+fridge '
            f'1.16m; cash redeemed FOI; air-air rates 300-600; gap_vl_odv_mvp_cash expanded ready"'
        )
        found = True
        break
assert found, "rq_178 missing"
# ensure rq_177 still open for next
rq_path.write_text("\n".join(rqlines) + "\n", encoding="utf-8")

# --- foi_queue note update ---
foi_path = base / "foi_queue.csv"
foilines = foi_path.read_text(encoding="utf-8").splitlines()
for i, line in enumerate(foilines):
    if line.startswith("gap_vl_odv_mvp_cash,"):
        # append note only if tick182 not already there
        if "tick182" not in line:
            foilines[i] = line.rstrip() + " |tick182: expanded items 4-5 air-air+kortingsbon; sent face bounds filled partial"
        break
foi_path.write_text("\n".join(foilines) + "\n", encoding="utf-8")

# --- loop_state ---
(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_178,182,no,"
    '"Scheduler 60s. Next prio5 rq_177 Antwerp/Mons/taxex; rq_116 SWA deferred. '
    "FOI ready human send. tick182 Mijn Kortingsbon face issued ~3.7m 2021; air-air MVP rates; cash L5 FOI.\"\n",
    encoding="utf-8",
)

entry = f"""
### {now} - tick 182
- Unit: **rq_178** (high-clown — **Mijn Kortingsbon white goods + MVP lucht-lucht airco**)
- Found (strong portals + medium/strong parliamentary QA; **no invent of redeemed cash**):
  - **Mijn Kortingsbon** face **250 EUR**/appliance; means-tested; **new apps stopped 2026-01-01** (residual bon redeemable to expiry).
  - **Verstuurde** bonnen (minister SV89/718): **2020 9_808** · **2021 14_629** strong · **2022 ~29_258** medium (2x 2021).
  - Face-value issued (sent x250, **not cash paid**): **2.45m / 3.66m / ~7.3m** 2020-22.
  - **2019 used** wash 2_314 + fridge 2_329 → **1.161m** cash medium (prior PQ cite; partial appliances).
  - **MVP lucht-lucht** rates **300-600 EUR** strong portal; pure cooling excluded on paper; dual-use AC marketing risk; cash split vs other WP **Unknown** (parent CoA heat premiums **22m 2023**).
  - Energiekaart MVP has category counts (interactive; per-type WP not public in text); FOI residual.
- Wrote: sources 4 (portals+2 PQ); budgets 8; cmt 1; lb 2 updated; rq_178=done; FOI gap_vl_odv_mvp_cash note.
- FOI: **gap_vl_odv_mvp_cash** ready expanded (redeemed cash by appliance + air-air split) — human send only.
- Next: prio5 **rq_177**; deferred **rq_116** SWA.
"""
with open(Path("docs/doge/loop_log.md"), "ab") as f:
    f.write(entry.encode("utf-8"))

print("tick182 complete")
print((base / "loop_state.csv").read_text(encoding="utf-8"))
