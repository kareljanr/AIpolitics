# tick182 finish — encoding-safe
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-28T10:45:00Z"
sent_2020, sent_2021, sent_2022 = 9808, 14629, 29258
face = 250
cash_2019_partial = (2314 + 2329) * face
src_pq718 = "https://docs.vlaamsparlement.be/pfile?id=1972510"
src_pq89 = "https://docs.vlaamsparlement.be/pfile?id=1894181"


def read_any(p: Path):
    raw = p.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except Exception:
            continue
    return raw.decode("latin-1")


# sources
src_text = read_any(base / "sources.csv")
adds = []
if "src_vl_kortingsbon_pq718" not in src_text:
    adds.append(
        "src_vl_kortingsbon_pq718,SV 718 Bothuyne Demir kortingsbon 8 mei 2023 + annex,"
        + src_pq718
        + ",Vlaams Parlement,2026-07-28,parliamentary_qa,"
        '"Verstuurde bonnen 2022 ~2x 2021 and 3x 2020; Q1 2023 ~1/3 of 2022; '
        'annex tables FOI residual; redemption cash FOI; tick182"\n'
    )
if "src_vl_kortingsbon_pq89" not in src_text:
    adds.append(
        "src_vl_kortingsbon_pq89,SV 89 Aerts Demir kortingsbonnen Fluvius 14 okt 2022,"
        + src_pq89
        + ",Vlaams Parlement,2026-07-28,parliamentary_qa,"
        '"Verstuurd 2020 9808 / 2021 14629 strong; 2019 used wash 2314 fridge 2329 cited; '
        'annex paid-by-appliance FOI residual; tick182"\n'
    )
if adds:
    with open(base / "sources.csv", "ab") as f:
        for a in adds:
            f.write(a.encode("utf-8"))
    print("sources added", len(adds))

# budgets (first script may have added some)
bud_text = read_any(base / "budgets.csv")
if "bud_vl_kortingsbon_sent_2020" not in bud_text:
    rows = [
        f"bud_vl_kortingsbon_sent_2020,vlaanderen_gov,2020,{sent_2020*face},,,outturn,src_vl_kortingsbon_pq89,strong,Face value of 9808 VERSTUURDE bonnen x250; NOT cash paid (redemption unknown)",
        f"bud_vl_kortingsbon_sent_2021,vlaanderen_gov,2021,{sent_2021*face},,,outturn,src_vl_kortingsbon_pq89,strong,Face value of 14629 VERSTUURDE bonnen x250; NOT cash paid",
        f"bud_vl_kortingsbon_sent_2022,vlaanderen_gov,2022,{sent_2022*face},,,outturn,src_vl_kortingsbon_pq718,medium,Face value ~29258 sent (2x 2021 per minister) x250; medium derived; NOT cash paid",
        f"bud_vl_kortingsbon_used_2019_wash_fridge,vlaanderen_gov,2019,{cash_2019_partial},,,outturn,src_vl_kortingsbon_pq89,medium,2019 USED only wash 2314+fridge 2329 =4643 x250 =1.161m medium (cited prior PQ); excludes dryer freezer",
        "bud_vl_kortingsbon_face_unit,vlaanderen_gov,2025,250,,,budgeted,src_vl_mijn_kortingsbon_portal,strong,Unit face value 250 EUR/appliance; new apps stopped 2026-01-01",
        "bud_vl_mvp_airair_rate_low,vlaanderen_gov,2025,300,,,budgeted,src_vl_mvp_warmtepomp_airair,strong,MVP lucht-lucht low income-band rate 300 EUR (portal)",
        "bud_vl_mvp_airair_rate_high,vlaanderen_gov,2025,600,,,budgeted,src_vl_mvp_warmtepomp_airair,strong,MVP lucht-lucht higher band rate up to 600 EUR (portal)",
        "bud_vl_heat_premiums_2023_coa,vlaanderen_gov,2023,22000000,,,outturn,src_ccrek_hernieuwbare_vl_2025,strong,CoA heat pump/boiler premiums ~22m 2023 (all WP types; air-air share unknown FOI)",
    ]
    with open(base / "budgets.csv", "ab") as f:
        f.write(("\n".join(rows) + "\n").encode("utf-8"))
    print("budgets added")
else:
    print("budgets already present")

# commitments
cmt_text = read_any(base / "commitments.csv")
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
    with open(base / "commitments.csv", "ab") as f:
        f.write(cmt.encode("utf-8"))
    print("cmt added")

# leaderboard
lb_text = read_any(base / "leaderboard.csv")
new_lb_kort = (
    "lb_vl_mijn_kortingsbon_appliances,Flanders Mijn Kortingsbon 250 EUR fridge/washer/freezer vouchers,"
    "Flanders,subsidy,Vlaanderen>Energie>Mijn_Kortingsbon_witgoed,"
    f"{sent_2021 * face},{sent_2020 * face + sent_2021 * face + sent_2022 * face},"
    "Face issued ~3.66m 2021 / ~2.45m 2020 / ~7.3m 2022est (sent x250 medium); cash paid Unknown FOI; "
    "2019 used wash+fridge only 1.16m medium; new apps stopped 2026-01-01; unit 250 strong portal,"
    "medium,src_vl_kortingsbon_pq89,Low-income Flanders households retailers Fluvius admin,"
    "Energy-efficient white goods for vulnerable households,"
    "Deadweight + admin sandwich HighCo; public pays for fridges/washers; cash transfer would dominate,"
    "8.5,5.5,4,7.0,"
    "Publish redeemed cash by appliance year; keep stop or replace with cash energy allowance,seed,,tick182"
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
    "Publish L5 air-air vs other WP cash; ban premium if primary use cooling; income-target only,seed,,tick182"
)
lines = lb_text.splitlines()
out = []
has_kort = has_air = False
for line in lines:
    if line.startswith("lb_vl_mijn_kortingsbon_appliances,"):
        out.append(new_lb_kort)
        has_kort = True
    elif line.startswith("lb_vl_airco_mvp_luchtlucht,"):
        out.append(new_lb_air)
        has_air = True
    else:
        out.append(line)
if not has_kort:
    out.append(new_lb_kort)
if not has_air:
    out.append(new_lb_air)
(base / "leaderboard.csv").write_bytes(("\n".join(out) + "\n").encode("utf-8"))
print("lb updated", has_kort, has_air)

# research_queue
rq_text = read_any(base / "research_queue.csv")
rqlines = rq_text.splitlines()
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
            '"tick182: portals+PQ: sent face 2020 2.45m / 2021 3.66m / 2022est 7.3m medium; 2019 used wash+fridge '
            '1.16m; cash redeemed FOI; air-air rates 300-600; gap_vl_odv_mvp_cash expanded ready"'
        )
        found = True
        break
assert found, "rq_178 missing"
(base / "research_queue.csv").write_bytes(("\n".join(rqlines) + "\n").encode("utf-8"))
print("rq_178 done")

# foi note
foi_text = read_any(base / "foi_queue.csv")
foilines = foi_text.splitlines()
for i, line in enumerate(foilines):
    if line.startswith("gap_vl_odv_mvp_cash,"):
        if "tick182" not in line:
            foilines[i] = (
                line.rstrip()
                + " |tick182: expanded items 4-5 air-air+kortingsbon; sent face bounds filled partial"
            )
        break
(base / "foi_queue.csv").write_bytes(("\n".join(foilines) + "\n").encode("utf-8"))

# loop_state
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
  - **Mijn Kortingsbon** face **250 EUR**/appliance; means-tested; **new apps stopped 2026-01-01**.
  - **Verstuurde** bonnen (SV89/718): **2020 9_808** · **2021 14_629** strong · **2022 ~29_258** medium (2x 2021).
  - Face-value issued (sent x250, **not cash paid**): **2.45m / 3.66m / ~7.3m** 2020-22.
  - **2019 used** wash 2_314 + fridge 2_329 → **1.161m** cash medium (prior PQ cite; partial).
  - **MVP lucht-lucht** rates **300-600 EUR** strong portal; cash split vs other WP **Unknown** (parent CoA heat premiums **22m 2023**).
- Wrote: sources portals+2 PQ; budgets face-issued series; cmt 1; lb 2; rq_178=done; FOI note.
- FOI: **gap_vl_odv_mvp_cash** ready (redeemed cash by appliance + air-air split) — human send only.
- Next: prio5 **rq_177**; deferred **rq_116** SWA.
"""
with open("docs/doge/loop_log.md", "ab") as f:
    f.write(entry.encode("utf-8"))

print("tick182 finish OK")
print((base / "loop_state.csv").read_text(encoding="utf-8"))
