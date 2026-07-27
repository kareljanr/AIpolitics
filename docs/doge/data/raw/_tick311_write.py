# tick 311 — rq_302 Smals CoA deepen external IT 206m + omzet split
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T18:15:00Z"
unit = "rq_302"

src_line = (
    "src_ccrek_smals_egov_2025,"
    "Rekenhof consultancy 2025 ch5 Smals Egov Select detachement broker,"
    "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
    "Rekenhof / Cour des comptes,2026-07-30,court_audit,"
    "Smals omzet 573.6m 2024: SS 62.9pct fed admin 25.4pct other 11.7pct; "
    "staff Dec2024 2251 (1143 int + 1108 det); external IT specialists billed >206m 2024; "
    "ProUnity sole broker; tick311\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

ent_path = ROOT / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
# update smals notes
lines = []
for L in ent.splitlines(True):
    if L.startswith("smals,") and "tick311" not in L:
        L = (
            "smals,Smals vzw,Smals asbl,Smals public-sector shared ICT services VZW,"
            "asbl,sec_ss,bi,https://www.smals.be,,,,"
            "Omzet 573.6m 2024 / 578.9m 2025; CoA: SS 62.9pct fed 25.4pct; "
            "external IT specialists billed >206m 2024; staff 2251 Dec2024; dual Egov Select; tick311\n"
        )
    lines.append(L)
ent = "".join(lines)
if "egov_select," not in ent:
    ent = ent.rstrip("\n") + "\n"
    ent += (
        "egov_select,Egov Select vzw,Egov Select asbl,"
        "Egov Select federal IT recruitment and detachment VZW,"
        "asbl,sec_federal,bi,,,,"
        "IT detachments to FODs police defence cultural/scientific; "
        "private-sector pay scales; dual Smals SS-focused; CoA 2025; tick311\n"
    )
ent_path.write_text(ent, encoding="utf-8")

bud_rows = [
    "bud_smals_omzet_ss_share_2024,smals,2024,360794400,,,estimate,src_ccrek_smals_egov_2025,strong,"
    "CoA: 62.9pct of 573.6m omzet to social security institutions ~360.8m",
    "bud_smals_omzet_fed_admin_share_2024,smals,2024,145694400,,,estimate,src_ccrek_smals_egov_2025,strong,"
    "CoA: 25.4pct of omzet to federal administrations ~145.7m",
    "bud_smals_omzet_other_share_2024,smals,2024,67111200,,,estimate,src_ccrek_smals_egov_2025,strong,"
    "CoA: 11.7pct other members ~67.1m",
    "bud_smals_external_it_specialists_2024,smals,2024,206000000,,,outturn,src_ccrek_smals_egov_2025,strong,"
    "CoA: Smals billed members >206m EUR 2024 for external IT specialists (ProUnity broker path)",
    "bud_smals_staff_dec_2024,smals,2024,2251,,,outturn,src_ccrek_smals_egov_2025,strong,"
    "CoA Dec2024: 2251 employees (1143 internal + 1108 detached); IT 77.9pct of headcount; not EUR",
    "bud_smals_detached_dec_2024,smals,2024,1108,,,outturn,src_ccrek_smals_egov_2025,strong,"
    "Detached at members 1108 eoy2024; not EUR",
    "bud_smals_ext_consultancy_share_omzet_2024,smals,2024,36,,,outturn,src_ccrek_smals_egov_2025,strong,"
    "External IT consultancy share of Smals omzet 36pct 2024 (was 17.8pct 2014); amount is percent not EUR",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

cmt_rows = [
    (
        "cmt_smals_external_it_206m_2024,Smals external IT specialists billed to members >206m 2024,"
        "smals,External IT consultants via Smals broker ProUnity,"
        "Smals framework agreements + BSM pass-through,2017-01-01,2024,2024,206000000,"
        '"{""billed_2024_m"":206,""floor"":true,""broker"":""ProUnity"",'
        '""omzet_2024"":573600000,""ext_share_omzet_pct"":36,'
        '""ext_share_2014_pct"":17.8,""private_partners_class_m"":333,'
        '""note"":""External specialists are subset of ~333m private pass-through (also hardware software); sole broker bidder risk""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Temporary specialized IT capacity for members,"
        "Open top contractors; dual-broker competition; market rate checks,"
        "src_ccrek_smals_egov_2025,strong,Federal>SS>Smals>external_IT,tick311 dual CoA consultancy"
    ),
    (
        "cmt_smals_omzet_client_split_2024,Smals omzet client-sector split 2024 CoA,"
        "smals,SS institutions FODs other members,Smals ASM member categories A B C,"
        "2024-01-01,2024,2024,573600000,"
        '"{""ss_pct"":62.9,""fed_admin_pct"":25.4,""other_pct"":11.7,'
        '""ss_m"":360.8,""fed_admin_m"":145.7,""other_m"":67.1,'
        '""staff_dec2024"":2251,""detached"":1108,""internal"":1143,""it_staff_pct"":77.9}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Show who pays Smals recharges,"
        "FOI member L5 still gap_smals_l5_members,"
        "src_ccrek_smals_egov_2025,strong,Federal>SS>Smals>client_split,tick311"
    ),
    (
        "cmt_egov_select_model,Egov Select federal IT detachment dual Smals,"
        "egov_select,FODs police defence scientific cultural federal bodies,"
        "Egov Select statutes + ASM 2001,2001-01-01,2024,2025,0,"
        '"{""role"":""recruit_select_detach_IT"",""pay_scale"":""private_sector_comparable"",'
        '""no_infra"":true,""no_external_broker"":true,'
        '""access_smals_frameworks"":true,'
        '""note"":""Absolute EUR residual FOI; dual Smals SS-focused in-house ICT""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Federal IT staff detachment outside SS Smals perimeter,"
        "FOI annual recharge total and FTE; dual Smals map,"
        "src_ccrek_smals_egov_2025,strong,Federal>IT>Egov_Select,tick311"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

lb_rows = [
    (
        "lb_smals_external_it_206m,Smals external IT specialists billed >206m 2024,federal,ops,"
        "Federal>SS>Smals>external_IT,206000000,206000000,"
        "Strong CoA: >206m 2024 billed to members for external IT specialists; ProUnity sole broker; share of omzet 36pct,"
        "strong,src_ccrek_smals_egov_2025,Member orgs taxpayers,Temporary specialized IT capacity,"
        "Sole broker + rank-skip opacity; dual private pass-through 333m,"
        "6,8.0,4,6.7,Open top-20 external firms; dual-broker tender; market rate cap,"
        "seed,,tick311 high material middleman"
    ),
    (
        "lb_smals_fed_admin_146m,Smals recharges to federal administrations ~146m 2024,federal,ops,"
        "Federal>SS>Smals>fed_admin_share,145694400,145694400,"
        "Strong CoA: 25.4pct of 573.6m omzet to federal administrations ~145.7m dual SS 360.8m,"
        "strong,src_ccrek_smals_egov_2025,FODs federal agencies,Shared ICT outside pure SS,"
        "Cross-perimeter IT middleman,"
        "4,7.5,3,5.7,FOI fed admin top members L5,"
        "seed,,tick311"
    ),
    (
        "lb_smals_broker_sole_prounity,Smals IT broker sole-bidder ProUnity risk,federal,ops,"
        "Federal>SS>Smals>broker,0,0,"
        "Strong CoA: latest framework sole offer ProUnity; commission -3pct negotiated; no dual-broker as tendered,"
        "strong,src_ccrek_smals_egov_2025,All Smals framework beneficiaries,Centralized IT consultant procurement,"
        "Competition failure on broker layer,"
        "7,5.0,3,5.8,Re-tender multi-broker; publish commission rate,"
        "seed,,tick311 mechanism not size"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# update FOI gap_smals notes
foi_path = ROOT / "foi_queue.csv"
foi = foi_path.read_text(encoding="utf-8")
old_note = "tick283: CGVS Smals/eGOV 1.809m public line"
if old_note in foi:
    foi = foi.replace(
        old_note,
        old_note
        + " | tick311: CoA external IT >206m 2024 + omzet split; residual member L5 + Egov EUR still ready",
    )
    foi_path.write_text(foi, encoding="utf-8")

# new FOI for Egov absolute EUR
foi_line = (
    "gap_egov_select_budget,Federal>IT>Egov_Select>recharges_FTE,egov_select,"
    "Annual recharge total and FTE detached 2023-2026; top client FODs by EUR; wage bill; "
    "reconcile any FPS budget lines,"
    "CoA model strong; absolute EUR missing; dual Smals external 206m material,"
    "5,Egov Select / FOD BOSA openbaarheid,,"
    "https://bosa.belgium.be,"
    "docs/doge/foi/drafts/gap_egov_select_budget.md,ready,2026-07-30,,,,,,"
    "cmt_egov_select_model,lb_smals_external_it_206m,"
    "2026-07-30T18:15:00Z,2026-07-30T18:15:00Z,tick311 draft ready human send\n"
)
with (foi_path).open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_302,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after progress@310 (AGMJ if extractable; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T17:15:00Z,,Spawned tick309 after CoA consultancy; do after rq_300 progress@310"
)
new = (
    "rq_302,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills after progress@310 (AGMJ if extractable; other FOI-adjacent). Prefer before idle.,"
    "gap_egov_select_budget|gap_smals_l5_members,2026-07-30T17:15:00Z,2026-07-30T18:15:00Z,"
    "tick311: Smals external IT >206m 2024 + omzet split SS 63pct/fed 25pct; Egov Select model; spawn rq_303"
)
if old not in text:
    raise SystemExit("rq_302 not found")
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_303,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; Ypto NMBS IT dual Smals; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T18:15:00Z,,Spawned tick311 after Smals CoA deepen; rq_116 SWA deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},311,no,"
    "Scheduler 60s. Next prio5 rq_303; rq_116 SWA deferred. FOI ready. "
    "tick311 Smals external IT >206m 2024 CoA.\n",
    encoding="utf-8",
)
print("OK")
