# tick 597 — ILVO dual agri research hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T15:00:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


# --- entities ---
with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "ilvo,ILVO Instituut Landbouw Visserij Voedingsonderzoek,"
        "ILVO Institut Recherche Agriculture Peche Alimentation,"
        "Flanders Research Institute Agriculture Fisheries Food dual VO EV CRA-W,"
        "agency,sec_flanders,nl,https://ilvo.vlaanderen.be,,,"
        "IVA+EV dual; staff 756 FTE 710.7 Dec2024; basisdotatie 29pct op funds; "
        "CoA BO2025 IVA exp 24.9m rev 2.6m EV ESR in 34.4m out 50.3m; "
        "EV BE0262.172.489; dual CRA-W WAL agri research; tick597\n"
    )
    f.write(
        "ilvo_vo,ILVO-VO IVA Intern Verzelfstandigd Agentschap,"
        "ILVO-VO Agence interne flamande,"
        "ILVO Flemish government IVA without legal personality structural endowment arm,"
        "agency,ilvo,nl,https://ilvo.vlaanderen.be,,,"
        "VO arm; staff 206 FTE 191.6 Dec2024; CoA BO2025 inkomsten 2.6m uitgaven 24.9m VAK VEK; tick597\n"
    )
    f.write(
        "ilvo_ev,ILVO-EV Eigen Vermogen,"
        "ILVO-EV Patrimoine propre,"
        "ILVO Own Capital competitive research and paid services arm,"
        "parastatal,ilvo,nl,https://ilvo.vlaanderen.be,,,"
        "EV arm BE0262.172.489; staff 550 FTE 519.1 Dec2024; CoA BO2025 ESR in 34.4m out 50.3m; tick597\n"
    )

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ilvo_ar_2024,ILVO Annual Report 2024 financial and human capital,"
        "https://ilvo.vlaanderen.be/uploads/documents/act-verslag-2024-EN.pdf,"
        "ILVO Flanders,2026-07-31,official_annual_report,"
        "Strong tick597: VO/EV dual; base endowment 29pct total operating funds 2024; "
        "project financing 71pct; funding mix ALZ 29+9 VLAIO 4 VL domains 6 federal 12 EU 14 other 25; "
        "staff Dec2024 756 (VO 206 EV 550) FTE 710.7 (191.6/519.1); raw ilvo_annual_report_2024_en.pdf\n"
    )
    f.write(
        "src_ccrek_vl_budget_2025_ilvo,Rekenhof Onderzoek Vlaamse begroting 2025 ILVO IVA EV ESR,"
        "https://www.ccrek.be/sites/default/files/Docs/2024_61_BegrotingVG_2025.pdf,"
        "Rekenhof Court of Audit Flanders,2026-07-31,official_audit,"
        "Strong tick597 p52: IVA ILVO inkomsten 2.6m uitgaven 24.9m VAK/VEK; "
        "EV ILVO ESR inkomsten 34.4m ESR uitgaven 50.3m; BBT placement opacity; raw ccrek_begroting_vg_2025.pdf\n"
    )
    f.write(
        "src_dual_agri_ilvo_vo_ev_tick597,Dual ILVO VO EV agri research structure 2024-25,"
        "docs/doge/raw/ilvo_annual_report_2024_en.pdf,DOGE synthesis ILVO AR2024 + CoA BO2025,"
        "2026-07-31,synthesis,"
        "Strong dual: VO structural 24.9m exp FTE 192 vs EV competitive ESR 50.3m out FTE 519; "
        "total staff 756; dual CRA-W WAL class; tick597\n"
    )

# --- budgets ---
bud_rows = [
    ("bud_ilvo_iva_exp_2025", "ilvo_vo", 2025, 24900000, "ILVO IVA uitgaven 24.9m VAK/VEK BO2025 CoA; tick597", "strong", "src_ccrek_vl_budget_2025_ilvo"),
    ("bud_ilvo_iva_rev_2025", "ilvo_vo", 2025, 2600000, "ILVO IVA inkomsten 2.6m BO2025 CoA; tick597", "strong", "src_ccrek_vl_budget_2025_ilvo"),
    ("bud_ilvo_ev_esr_in_2025", "ilvo_ev", 2025, 34400000, "ILVO EV ESR inkomsten 34.4m BO2025 CoA; tick597", "strong", "src_ccrek_vl_budget_2025_ilvo"),
    ("bud_ilvo_ev_esr_out_2025", "ilvo_ev", 2025, 50300000, "ILVO EV ESR uitgaven 50.3m BO2025 CoA; tick597", "strong", "src_ccrek_vl_budget_2025_ilvo"),
    ("bud_ilvo_iva_exp_class_2025", "ilvo", 2025, 24900000, "ILVO combined label IVA exp arm 24.9m 2025 CoA; tick597", "strong", "src_ccrek_vl_budget_2025_ilvo"),
    ("bud_ilvo_ev_out_class_2025", "ilvo", 2025, 50300000, "ILVO combined label EV ESR out arm 50.3m 2025 CoA; tick597", "strong", "src_ccrek_vl_budget_2025_ilvo"),
    ("bud_ilvo_staff_2024", "ilvo", 2024, 0, "ILVO staff headcount 756 Dec2024 (not EUR); tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_fte_2024", "ilvo", 2024, 0, "ILVO FTE 710.7 Dec2024 VO 191.6 EV 519.1 (not EUR); tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_vo_fte_2024", "ilvo_vo", 2024, 0, "ILVO-VO FTE 191.6 staff 206 Dec2024 (not EUR); tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_ev_fte_2024", "ilvo_ev", 2024, 0, "ILVO-EV FTE 519.1 staff 550 Dec2024 (not EUR); tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_base_endow_share_2024", "ilvo", 2024, 0, "ILVO base endowment 29pct of total operating funds 2024 (share not EUR); tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_project_share_2024", "ilvo", 2024, 0, "ILVO project-based financing 71pct of operating funds 2024 (share not EUR); tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_alz_basic_share_2024", "ilvo", 2024, 0, "ILVO ALZ basic funding 29pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_alz_endow_share_2024", "ilvo", 2024, 0, "ILVO ALZ endowment 9pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_vlaio_share_2024", "ilvo", 2024, 0, "ILVO VLAIO 4pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_federal_share_2024", "ilvo", 2024, 0, "ILVO federal governments 12pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_eu_share_2024", "ilvo", 2024, 0, "ILVO EU 14pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_other_private_share_2024", "ilvo", 2024, 0, "ILVO other private Business Unit 25pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_vl_domains_share_2024", "ilvo", 2024, 0, "ILVO Flemish policy areas 6pct 2024 mix; tick597", "strong", "src_ilvo_ar_2024"),
    ("bud_ilvo_ev_vo_ratio_2024", "ilvo", 2024, 0, "ILVO EV/VO balance about 2/3-1/3 2024 AR text; tick597", "strong", "src_ilvo_ar_2024"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, ent, year, amt, note, conf, src in bud_rows:
        f.write(f"{bid},{ent},{year},{amt},,,outturn,{src},{conf},{note}\n")

# --- commitments ---
cmt_ilvo = {
    "2025_iva_exp_m": 24.9,
    "2025_iva_rev_m": 2.6,
    "2025_ev_esr_in_m": 34.4,
    "2025_ev_esr_out_m": 50.3,
    "2024_staff": 756,
    "2024_fte": 710.7,
    "2024_vo_fte": 191.6,
    "2024_ev_fte": 519.1,
    "2024_base_endow_pct": 29,
    "2024_project_pct": 71,
    "note": "Dual VO structural IVA + EV competitive Own Capital; CoA BO2025 + AR2024",
}
cmt_dual = {
    "iva_exp_m": 24.9,
    "ev_out_m": 50.3,
    "fte_vo": 191.6,
    "fte_ev": 519.1,
    "base_endow_pct": 29,
    "note": "Dual ILVO VO/EV agri research; dual CRA-W WAL class residual",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_ilvo_ar_coa_2024_25,ILVO dual VO EV agri research 2024-25,ilvo,'
        f'Flanders farmers fisheries food industry EU,VL ALZ basisdotatie + competitive EV projects,'
        f'2024-01-01,2024,2030,50300000,"{esc_json(cmt_ilvo)}",0,active,'
        f'https://ilvo.vlaanderen.be,Agri fisheries food sustainability research,'
        f'Publish full cash total operating funds + multi-year basisdotatie FOI,'
        f'src_ilvo_ar_2024,strong,Vlaanderen>Agri_Research>ILVO,tick597 AR2024+CoA primary new entity\n'
    )
    f.write(
        f'cmt_dual_ilvo_vo_ev_2025,Dual ILVO VO structural + EV competitive 2024-25,ilvo,'
        f'Flanders agri research dual structure,AR2024 + CoA BO2025,'
        f'2024-01-01,2024,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual VO/EV agri research agency,FOI full recon + CRA-W dual residual,'
        f'src_dual_agri_ilvo_vo_ev_tick597,strong,BE>dual>ILVO_VO_EV,tick597\n'
    )

# --- leaderboard ---
lb = [
    (
        "lb_ilvo_ev_esr_out_50m_2025",
        "ILVO-EV ESR uitgaven 50.3m BO2025 dual VO",
        "Flanders",
        "ops",
        "Vlaanderen>Agri_Research>ILVO>EV_out_50m",
        50300000,
        50300000,
        "Strong CoA: EV ESR out 50.3m in 34.4m; competitive research arm dual VO 24.9m",
        "src_ccrek_vl_budget_2025_ilvo",
        "VL ALZ EV ILVO",
        "Competitive agri research paid services",
        "Core public science; ESR deficit path opacity",
        3,
        7.5,
        5,
        5.55,
        "Full EV jaarrekening FOI",
    ),
    (
        "lb_ilvo_iva_exp_25m_2025",
        "ILVO-VO IVA uitgaven 24.9m BO2025",
        "Flanders",
        "ops",
        "Vlaanderen>Agri_Research>ILVO>IVA_exp_25m",
        24900000,
        24900000,
        "Strong CoA: IVA exp 24.9m rev 2.6m; structural VO arm FTE 192",
        "src_ccrek_vl_budget_2025_ilvo",
        "VL taxpayers ALZ",
        "Structural agri research endowment",
        "BBT placement opacity CoA note",
        4,
        7.0,
        5,
        5.55,
        "Publish multi-year basisdotatie",
    ),
    (
        "lb_ilvo_ev_esr_in_34m_2025",
        "ILVO-EV ESR inkomsten 34.4m BO2025",
        "Flanders",
        "ops",
        "Vlaanderen>Agri_Research>ILVO>EV_in_34m",
        34400000,
        34400000,
        "Strong CoA: EV ESR income 34.4m vs out 50.3m",
        "src_ccrek_vl_budget_2025_ilvo",
        "EU federal private competitive",
        "Project competitive research income",
        "Income mix recon FOI residual",
        3,
        7.0,
        4,
        5.05,
        "L5 income mix FOI",
    ),
    (
        "lb_ilvo_fte_711_2024",
        "ILVO staff 756 FTE 710.7 2024 dual VO EV",
        "Flanders",
        "ops",
        "Vlaanderen>Agri_Research>ILVO>fte_711",
        0,
        0,
        "Strong AR2024: 756 staff FTE 710.7 VO 191.6 EV 519.1; EV/VO ~2/3-1/3",
        "src_ilvo_ar_2024",
        "ILVO staff",
        "Operate agri research labs living labs",
        "Core ops dual structure FTE",
        3,
        6.5,
        3,
        4.75,
        "Benchmark dual agri FTE",
    ),
    (
        "lb_ilvo_base_endow_29pct_2024",
        "ILVO base endowment 29pct op funds 2024",
        "Flanders",
        "ops",
        "Vlaanderen>Agri_Research>ILVO>base_endow_29pct",
        0,
        0,
        "Strong AR2024: structural 29pct project 71pct; absolute total op funds not published",
        "src_ilvo_ar_2024",
        "VL ALZ",
        "Structural share of operating resources",
        "Absolute EUR total FOI residual",
        4,
        6.5,
        6,
        5.55,
        "FOI absolute total werkingsmiddelen",
    ),
    (
        "lb_dual_ilvo_vo_ev_2025",
        "Dual ILVO VO 24.9m + EV 50.3m agri research 2025",
        "Flanders",
        "ops",
        "BE>dual>ILVO_VO_EV_2025",
        24900000,
        50300000,
        "Strong dual: VO IVA exp 24.9m FTE 192 vs EV ESR out 50.3m FTE 519; basisdotatie 29pct",
        "src_dual_agri_ilvo_vo_ev_tick597",
        "Flanders agri research dual",
        "Map dual VO EV agri agency",
        "BBT opacity + absolute total residual",
        4,
        8.0,
        5,
        6.15,
        "FOI dual recon + CRA-W",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        (
            lid, title, jur, cat, hpath, annual, stock, note, src,
            spenders, purpose, mech, prio, scale, opac, pidx, hook,
        ) = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"{spenders},{purpose},{mech},{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick597\n"
        )

# --- foi ---
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_ilvo_total_op_funds_l5_2024,Vlaanderen>ILVO>total_op_funds_L5_2024,ilvo,"
        "Absolute total werkingsmiddelen 2024 recon to 29pct basisdotatie; multi-year IVA basisdotatie cash; "
        "EV full ESR/statutory recon 34.4/50.3m; BBT placement; dual CRA-W unit-cost,"
        "AR2024 mix+staff strong CoA BO2025 arms strong tick597; absolute total residual,5,"
        "ILVO / Agentschap Landbouw en Zeevisserij / openbaarheid,,https://ilvo.vlaanderen.be,"
        "docs/doge/foi/drafts/gap_ilvo_total_op_funds_l5_2024.md,ready,2026-07-31,,,,"
        "cmt_ilvo_ar_coa_2024_25|cmt_dual_ilvo_vo_ev_2025,"
        "lb_ilvo_ev_esr_out_50m_2025|lb_dual_ilvo_vo_ev_2025,"
        f"{utc},{utc},tick597 ILVO AR+CoA primary; residual absolute total human send\n"
    )

# --- research_queue ---
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_588,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T14:45:00Z,,Spawned tick596 after Flanders Make dual SOC; rq_116 deferred; progress@600 in 4"
)
new = (
    "rq_588,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T14:45:00Z,2026-07-31T15:00:00Z,"
    "tick597: ILVO dual VO/EV CoA 24.9m/50.3m staff 756; spawn rq_589; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_588 row not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_589,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:00:00Z,,Spawned tick597 after ILVO dual agri; rq_116 deferred; progress@600 in 3\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_588,597,no,"
    "tick597 ILVO dual VO/EV CoA 24.9m/50.3m staff 756; next rq_589; progress@600 in 3; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick597 CSV writes OK")
