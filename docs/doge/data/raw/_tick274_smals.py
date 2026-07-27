# tick 274 — Smals hole-fill writes
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-29T23:45:00Z"

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_smals_av_2025,Smals Activiteitenverslag 2025 kerncijfers omzet path + G-Cloud savings,"
        "docs/doge/data/raw/smals_activiteitenverslag_2025.pdf,Smals vzw,2026-07-29,agency,"
        "Omzet 407.7/439.5/515.6/573.6/578.9m 2021-25; staff 2350 end-2025 (1174 internal +1176 detached); "
        "private partners ~333m >57pct omzet; G-Cloud savings claim 54.4m; ReUse projects >45m; members 345; "
        "eHealth 19bn tx KSZ 2.15bn; tick274\n"
    )

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "smals,Smals vzw,Smals asbl,Smals public-sector shared ICT services VZW,asbl,sec_ss,bi,"
        "https://www.smals.be,,,Omzet 578.9m 2025; 2350 staff; cost-sharing in-house ICT for SS/health; "
        "dual e-health L5; tick274\n"
    )

# --- budgets ---
bud_rows = [
    "bud_smals_omzet_2021,smals,2021,407721909,,,outturn,src_smals_av_2025,strong,AV2025 kerncijfers omzet 407.721.909",
    "bud_smals_omzet_2022,smals,2022,439518806,,,outturn,src_smals_av_2025,strong,AV2025 kerncijfers omzet 439.518.806",
    "bud_smals_omzet_2023,smals,2023,515556116,,,outturn,src_smals_av_2025,strong,AV2025 kerncijfers omzet 515.556.116",
    "bud_smals_omzet_2024,smals,2024,573623499,,,outturn,src_smals_av_2025,strong,AV2025 kerncijfers omzet 573.623.499",
    "bud_smals_omzet_2025,smals,2025,578866778,,,outturn,src_smals_av_2025,strong,AV2025 kerncijfers omzet 578.866.778",
    "bud_smals_staff_headcount_2025,smals,2025,2350,,,outturn,src_smals_av_2025,strong,Headcount end-2025 2350 (FT 2026 + PT 324); amount is count not EUR",
    "bud_smals_private_partners_2025,smals,2025,333000000,,,outturn,src_smals_av_2025,strong,>57pct omzet ~333m to private sector partners (hardware software external specialists)",
    "bud_smals_gcloud_savings_claim_2025,smals,2025,54400000,,,estimate,src_smals_av_2025,medium,Self-reported G-Cloud common services savings 54.4m 2025 (not audited external)",
    "bud_smals_reuse_savings_claim_2025,smals,2025,45000000,,,estimate,src_smals_av_2025,medium,Self-reported ReUse project savings >45m 2025 (estimate not audited)",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

# --- commitments ---
cash_obj = {
    "omzet_2021": 407721909,
    "omzet_2022": 439518806,
    "omzet_2023": 515556116,
    "omzet_2024": 573623499,
    "omzet_2025": 578866778,
    "staff_2025": 2350,
    "internal_staff": 1174,
    "detached_staff": 1176,
    "external_ict_specialists_class": 1000,
    "private_partners_eur": 333000000,
    "private_partners_pct": 57,
    "gcloud_savings_claim": 54400000,
    "reuse_savings_claim": 45000000,
    "members_total": 345,
    "members_A": 15,
    "members_B": 133,
    "members_C": 197,
    "ehealth_tx_bn": 19,
    "ksz_messages_bn": 2.15,
    "note": "Cost-sharing VZW in-house ICT; omzet is member recharges not pure subsidy; L5 by member residual FOI; dual e-health INAMI 132.5m",
}
cash_json = json.dumps(cash_obj, separators=(",", ":"))
# CSV-escape quotes in JSON field
cash_csv = '"' + cash_json.replace('"', '""') + '"'
cmt = (
    "cmt_smals_omzet_path_2021_25,Smals shared ICT omzet path dual e-health SS stack,smals,"
    "Public SS health agencies members via recharges,Wet 15 jan 1990 art 17bis KSZ + Smals ASM,"
    "2021-01-01,2021,2025,578866778,"
    + cash_csv
    + ",0,active,docs/doge/data/raw/smals_activiteitenverslag_2025.pdf,"
    "Shared ICT services for social security and e-health,"
    "FOI L5 recharge matrix by member; dual unit-cost vs commercial IT; open statutory result,"
    "src_smals_av_2025,strong,Federal>SS>Smals>shared_ICT,tick274 omzet not pure waste middleman\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt)

# --- leaderboard ---
lb_rows = [
    "lb_smals_omzet_579m,Smals shared ICT omzet 578.9m 2025,federal,ops,Federal>SS>Smals>omzet,578866778,578866778,Strong AV2025: omzet 578.866.778 2025 (573.6m 2024); cost-sharing VZW recharges not pure subsidy; private partners ~333m,strong,src_smals_av_2025,SS and health public bodies members,Shared in-house ICT for SS/e-gov,Core digital SS backbone not pure waste; dual opacity L5 members,4,9.0,5,6.5,Publish L5 recharge by member; dual unit-cost commercial IT,seed,,tick274",
    "lb_smals_private_pass_333m,Smals private-sector pass-through ~333m 2025,federal,ops,Federal>SS>Smals>private_partners,333000000,333000000,Strong AV: >57pct omzet ~333m to private sector (hardware software external ICT specialists); residual contractor L5 FOI,strong,src_smals_av_2025,Private ICT vendors consultants,Procurement pass-through via shared services,Middleman procurement scale; not necessarily waste if scale savings real,5,8.5,5,6.55,Open top-20 private contractors; G-Cloud tender transparency,seed,,tick274",
    "lb_smals_staff_2350,Smals headcount 2350 end-2025 dual e-health,federal,ops,Federal>SS>Smals>staff,0,0,Strong AV: 2350 staff (1174 internal + 1176 detached) + >1000 external ICT specialists class; ICT 79pct; wage bill residual FOI,strong,src_smals_av_2025,Smals employees detached to members,ICT capacity for SS digitalisation,Core capacity; dual KSZ/eHealth ops opacity,3,7.5,4,5.75,FOI wage bill + detached charge matrix,seed,,tick274 headcount",
    "lb_smals_ehealth_dual_stack,Smals 579m dual INAMI e-health 132.5m stack,federal,ops,BE>Health_SS>Smals_ehealth_dual,0,0,Strong dual: Smals institutional omzet 578.9m vs INAMI e-health stack 132.5m (subset financing path); Smals is L5 delivery vehicle class; not additive,strong,src_smals_av_2025,Patients providers SS members,Digital SS and e-health infrastructure,Institutional dual map; residual member L5 FOI,4,8.5,5,6.55,Reconcile Smals eHealth member recharge vs INAMI 132.5m lines,seed,,tick274 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# --- foi_queue append + update ehealth ---
foi_line = (
    "gap_smals_l5_members,Federal>Smals>member_recharges_L5,smals,"
    "Machine-readable recharge/invoice matrix top members by EUR 2023-2025 (RIZIV eHealth RSZ KSZ RVA etc); "
    "wage bill cash-by-year; statutory net result/reserves; top-20 private contractors under 333m pass-through; "
    "reconcile eHealth member share vs INAMI 132.5m,"
    "Institutional omzet 578.9m strong; L5 end-receivers and e-health dual still opaque,6,"
    "Smals vzw openbaarheid / Bestuursorgaan / IBZ FOI,info@smals.be,https://www.smals.be,"
    "docs/doge/foi/drafts/gap_smals_l5_members.md,ready,2026-07-29,,,,,,"
    "cmt_smals_omzet_path_2021_25,lb_smals_omzet_579m|lb_smals_private_pass_333m,"
    f"{now},{now},tick274 draft ready human send; omzet filled\n"
)
foi_path = base / "foi_queue.csv"
text = foi_path.read_text(encoding="utf-8")
lines = text.splitlines()
out = []
for line in lines:
    if line.startswith("gap_ehealth_l5_vendors,") and "tick274" not in line:
        line = line.rstrip() + " | tick274: Smals institutional omzet 578.9m filled; residual INAMI L5 split still ready"
    out.append(line)
# avoid duplicate gap if re-run
if not any(l.startswith("gap_smals_l5_members,") for l in out):
    out.append(foi_line.rstrip("\n"))
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

# --- research_queue ---
rq_path = base / "research_queue.csv"
rq_lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq_lines:
    if line.startswith("rq_265,"):
        out.append(
            "rq_265,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after e-health/FAM).,"
            f"gap_smals_l5_members,2026-07-29T23:30:00Z,{now},"
            "tick274: Smals omzet 578.9m dual e-health; spawn rq_266"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_266,") for l in out):
    out.append(
        "rq_266,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; Controledienst ziekenfondsen; HDA; other FOI-adjacent after Smals).,,"
        f"{now},,Spawned tick274 after Smals; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

# --- loop_state ---
(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_265,274,no,"
    "Scheduler 60s. Next prio5 rq_266; rq_116 SWA deferred. FOI ready human send. tick274 Smals 578.9m dual e-health.\n",
    encoding="utf-8",
)

print("OK tick274 CSV writes")
