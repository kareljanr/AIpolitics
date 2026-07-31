# tick378: New Samusocial RA2025 budget 72.4m financing+mission L5
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

TOTAL = 72444781.05

def pct_eur(p):
    return round(TOTAL * p / 100.0)

# financing shares
fin = {
    "cocom": 38.8,
    "fedasil": 36.7,
    "rbc": 17.6,
    "inami": 3.3,
    "iriscare": 1.3,
    "brusshelp": 0.7,
    "autres": 0.7,
    "maribel": 0.5,
    "dons_2024_carry": 0.3,
    "actiris": 0.1,
}
# missions
mis = {
    "hebergement_urgence": 50.5,
    "hebergement_fedasil": 34.6,
    "frais_support": 11.0,
    "maraudes": 2.5,
    "housing": 1.4,
}

# --- entities note update not needed; new_samusocial exists ---
# lightly add notes via entity if needed - skip new entity

# --- sources ---
src_row = (
    "src_samusocial_ra_2025,"
    "New Samusocial Rapport activite 2025 budget financement missions,"
    "https://samusocial.be/wp-content/uploads/2026/06/Samusocial_Rapport25_A4_V6-WEB-FR.pdf,"
    "New Samusocial ASBL,"
    "2026-08-01,primary_annual_report,"
    '"RA2025 p125: budget 72444781.05 EUR; financing COCOM 38.8 Fedasil 36.7 RBC 17.6 INAMI 3.3; missions urgence 50.5 Fedasil 34.6 support 11; dons 529822; dual COCOM BI2026 71.9m"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_row + "\n")
print("sources +1")

# --- budgets ---
rows = [
    ("bud_samusocial_budget_2025", "new_samusocial", 2025, 72444781, "budgeted", "Budget calendar 2025 total 72444781.05 EUR RA p125 strong"),
    ("bud_samusocial_cocom_2025", "new_samusocial", 2025, pct_eur(38.8), "budgeted", f"COCOM share 38.8pct = {pct_eur(38.8)} of total; dual SCR dot ~27.4m 2026 path"),
    ("bud_samusocial_fedasil_2025", "new_samusocial", 2025, pct_eur(36.7), "budgeted", f"Fedasil financing 36.7pct = {pct_eur(36.7)}"),
    ("bud_samusocial_rbc_2025", "new_samusocial", 2025, pct_eur(17.6), "budgeted", f"Region Bruxelles-Capitale 17.6pct = {pct_eur(17.6)}"),
    ("bud_samusocial_inami_2025", "new_samusocial", 2025, pct_eur(3.3), "budgeted", f"INAMI 3.3pct = {pct_eur(3.3)}"),
    ("bud_samusocial_iriscare_2025", "new_samusocial", 2025, pct_eur(1.3), "budgeted", f"Iriscare 1.3pct = {pct_eur(1.3)}"),
    ("bud_samusocial_brusshelp_2025", "new_samusocial", 2025, pct_eur(0.7), "budgeted", f"BrussHelp 0.7pct = {pct_eur(0.7)}"),
    ("bud_samusocial_autres_2025", "new_samusocial", 2025, pct_eur(0.7), "budgeted", f"Autres 0.7pct = {pct_eur(0.7)} (Lama CAP48 Loterie Ilot)"),
    ("bud_samusocial_maribel_2025", "new_samusocial", 2025, pct_eur(0.5), "budgeted", f"Maribel 0.5pct = {pct_eur(0.5)}"),
    ("bud_samusocial_dons_carry_2025", "new_samusocial", 2025, 201386, "budgeted", "Dons prives 2024 carried to 2025 201385.76 EUR text (0.3pct class)"),
    ("bud_samusocial_actiris_2025", "new_samusocial", 2025, pct_eur(0.1), "budgeted", f"Actiris 0.1pct = {pct_eur(0.1)}"),
    ("bud_samusocial_mission_urgence_2025", "new_samusocial", 2025, pct_eur(50.5), "budgeted", f"Mission hebergement urgence 50.5pct = {pct_eur(50.5)} (regul centres familles MNA medicalise)"),
    ("bud_samusocial_mission_fedasil_2025", "new_samusocial", 2025, pct_eur(34.6), "budgeted", f"Mission hebergement Fedasil DPI 34.6pct = {pct_eur(34.6)} Laeken Koekelberg Anderlecht Forest"),
    ("bud_samusocial_mission_support_2025", "new_samusocial", 2025, pct_eur(11.0), "budgeted", f"Frais de support 11pct = {pct_eur(11.0)}"),
    ("bud_samusocial_mission_maraudes_2025", "new_samusocial", 2025, pct_eur(2.5), "budgeted", f"Maraudes 2.5pct = {pct_eur(2.5)}"),
    ("bud_samusocial_mission_housing_2025", "new_samusocial", 2025, pct_eur(1.4), "budgeted", f"Housing Casas Frida Vesta Step Forward Issue 1.4pct = {pct_eur(1.4)}"),
    ("bud_samusocial_dons_collected_2025", "new_samusocial", 2025, 529822, "outturn", "Private dons collected 2025 529822 EUR for 2026 projects"),
]
# Verify sum of financing pcts
fin_sum = sum(fin.values())
mis_sum = sum(mis.values())
print("fin pct sum", fin_sum, "mis pct sum", mis_sum)

with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, eid, yr, amt, basis, notes in rows:
        # pct-derived lines strong (source total+pct); label method
        f.write(
            f'{bid},{eid},{yr},{int(amt)},,,,{basis},src_samusocial_ra_2025,strong,"{notes}"\n'
        )
print("budgets +", len(rows))

# --- commitments ---
cmt = (
    "cmt_samusocial_budget_2025,New Samusocial budget 2025 multi-funder L5,new_samusocial,"
    "Homeless persons Brussels emergency shelter Fedasil DPI families,"
    "ASBL New Samusocial multi-funder COCOM Fedasil RBC,"
    "2025-01-01,2025,2025,72444781,"
    '"{""budget_m"":72.445,""cocom_pct"":38.8,""cocom_m"":28.109,'
    '""fedasil_pct"":36.7,""fedasil_m"":26.587,""rbc_pct"":17.6,""rbc_m"":12.750,'
    '""inami_pct"":3.3,""iriscare_pct"":1.3,""urgence_pct"":50.5,""fedasil_mission_pct"":34.6,'
    '""support_pct"":11,""maraudes_pct"":2.5,""housing_pct"":1.4,'
    '""dons_collected_2025"":529822,""dons_carry_2024"":201386,'
    '""hosts_2025"":11383,""shelter_requests"":56951,""street_prestations"":23402,'
    '""phone_calls"":48638,""exits_street"":2159,""devices"":16,'
    '""budget_2026_coa_m"":71.925,""budget_2025_coa_prior_m"":41.827,'
    '""note"":""Strong RA2025 p125 pct*total; CoA flag missing general accounts 2020-24 residual; dual COCOM OAA""}",'
    "0,active,https://samusocial.be/wp-content/uploads/2026/06/Samusocial_Rapport25_A4_V6-WEB-FR.pdf,"
    "Emergency homelessness reception multi-funder Brussels,"
    "Transmit full accounts 2020-25; open FTE payroll; reconcile COCOM cash codes,"
    "src_samusocial_ra_2025,strong,Bruxelles>COCOM>NewSamusocial>budget_2025,"
    "tick378: 72.445m COCOM 38.8pct Fedasil 36.7 urgence 50.5\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("cmt +1")

# --- leaderboard ---
lbs = [
    (
        "lb_samusocial_budget_72m_2025",
        "New Samusocial budget 72.4m 2025",
        "Brussels",
        "ops",
        "Bruxelles>COCOM>NewSamusocial>budget",
        72444781,
        72444781,
        "Strong RA2025: calendar budget 72.445m; multi-funder; dual COCOM BI2026 71.9m; prior CoA 2025 41.8m understates full multi-fund",
        "strong",
        "src_samusocial_ra_2025",
        "Homeless persons Brussels 11383 hosted",
        "Emergency shelter street outreach housing transition",
        "Core social; multi-fund opacity risk; accounts FOI residual CoA flag",
        5,
        6.5,
        4,
        5.48,
        "Publish full accounts 2020-25; unit cost per night/host",
        "seed",
        "",
        "tick378",
    ),
    (
        "lb_samusocial_cocom_28m_2025",
        "Samusocial COCOM financing ~28.1m 2025",
        "Brussels",
        "transfer",
        "Bruxelles>COCOM>NewSamusocial>COCOM_share",
        pct_eur(38.8),
        pct_eur(38.8),
        "Strong: 38.8pct of 72.445m; dual SCR subvention ~27.4m 2026 path",
        "strong",
        "src_samusocial_ra_2025",
        "Homeless reception via COCOM policy",
        "Primary community commission financing share",
        "Core transfer; reconcile cash code vs SCR",
        3,
        5.5,
        3,
        4.43,
        "Open COCOM cash article multi-year",
        "seed",
        "",
        "tick378",
    ),
    (
        "lb_samusocial_fedasil_27m_2025",
        "Samusocial Fedasil financing ~26.6m 2025",
        "federal",
        "transfer",
        "Federal>Fedasil>NewSamusocial",
        pct_eur(36.7),
        pct_eur(36.7),
        "Strong: 36.7pct financing; mission hebergement Fedasil DPI centres 34.6pct of budget",
        "strong",
        "src_samusocial_ra_2025",
        "Asylum seekers DPI Brussels centres",
        "Federal asylum reception via ASBL operator",
        "Core federal-ASBL dual; Laeken Koekelberg Anderlecht Forest",
        3,
        5.5,
        4,
        4.48,
        "Publish per-centre EUR and occupancy KPIs",
        "seed",
        "",
        "tick378",
    ),
    (
        "lb_samusocial_urgence_37m_2025",
        "Samusocial emergency shelter mission ~36.6m 2025",
        "Brussels",
        "ops",
        "Bruxelles>NewSamusocial>hebergement_urgence",
        pct_eur(50.5),
        pct_eur(50.5),
        "Strong: 50.5pct mission; phone regul isolated families MNA medicalised centres",
        "strong",
        "src_samusocial_ra_2025",
        "Emergency shelter seekers Brussels",
        "Primary emergency accommodation mission",
        "Core social; capacity saturation KPIs public",
        3,
        6.0,
        3,
        4.78,
        "Publish unit cost per host-night; refusal rates",
        "seed",
        "",
        "tick378",
    ),
    (
        "lb_samusocial_support_8m_2025",
        "Samusocial support costs ~8.0m 2025",
        "Brussels",
        "ops",
        "Bruxelles>NewSamusocial>frais_support",
        pct_eur(11.0),
        pct_eur(11.0),
        "Strong: 11pct frais de support of 72.445m",
        "strong",
        "src_samusocial_ra_2025",
        "ASBL overhead staff admin",
        "Support overhead share",
        "Overhead opacity vs frontline; FTE residual FOI",
        5,
        4.5,
        3,
        4.38,
        "Open payroll FTE split support vs field",
        "seed",
        "",
        "tick378",
    ),
    (
        "lb_samusocial_rbc_13m_2025",
        "Samusocial BCR financing ~12.8m 2025",
        "Brussels",
        "transfer",
        "Bruxelles>RBC>NewSamusocial",
        pct_eur(17.6),
        pct_eur(17.6),
        "Strong: Region Bruxelles-Capitale 17.6pct of budget",
        "strong",
        "src_samusocial_ra_2025",
        "Homeless policy Brussels region",
        "Regional multi-fund contribution",
        "Triple-fund COCOM+RBC+Fedasil complexity",
        4,
        5.0,
        3,
        4.33,
        "Publish regional budget article codes",
        "seed",
        "",
        "tick378",
    ),
]
with (DATA / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for row in lbs:
        parts = [
            row[0], row[1], row[2], row[3], row[4],
            str(row[5]), str(row[6]), f'"{row[7]}"', row[8], row[9],
            row[10], row[11], f'"{row[12]}"',
            str(row[13]), str(row[14]), str(row[15]), str(row[16]),
            f'"{row[17]}"', row[18], row[19], f'"{row[20]}"',
        ]
        f.write(",".join(parts) + "\n")
print("lb +", len(lbs))

# update entity notes for new_samusocial
ent = (DATA / "entities.csv").read_text(encoding="utf-8")
old_e = "new_samusocial,New Samusocial,New Samusocial ASBL,Brussels homelessness emergency ASBL,asbl,cocom,fr,https://www.samusocial.be,,,COCOM OAA; budget 71.9m 2026; CoA flags missing general accounts 2020-24; tick234"
new_e = "new_samusocial,New Samusocial,New Samusocial ASBL,Brussels homelessness emergency ASBL,asbl,cocom,fr,https://www.samusocial.be,,,COCOM OAA; RA2025 budget 72.445m multi-funder; BI2026 71.9m; CoA accounts 2020-24 residual; tick234+378"
if old_e in ent:
    (DATA / "entities.csv").write_text(ent.replace(old_e, new_e), encoding="utf-8")
    print("entity updated")
else:
    print("WARN entity row not exact")

# research queue
rq_path = DATA / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_369,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T03:15:00Z,,Spawned tick377 after Iriscare RA2024; rq_116 SWA deferred"
)
new = (
    "rq_369,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_samusocial_accounts_l5,2026-08-01T03:15:00Z,2026-08-01T03:45:00Z,"
    "tick378: Samusocial RA2025 budget 72.445m multi-funder L5; FOI accounts residual; spawn rq_370"
)
if old not in text:
    raise SystemExit("rq_369 not found")
rq_path.write_text(text.replace(old, new), encoding="utf-8")
with rq_path.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_370,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T03:45:00Z,,Spawned tick378 after Samusocial 72.4m; rq_116 SWA deferred\n"
    )
print("rq done")

# foi
foi_row = (
    "gap_samusocial_accounts_l5,Bruxelles>COCOM>NewSamusocial>accounts_L5,new_samusocial,"
    "General accounts / jaarrekening 2020-2025 (CoA flagged never transmitted 2020-24); FTE payroll "
    "support vs field; cash-by-year COCOM SCR article + Fedasil + RBC grants; per-centre occupancy EUR; "
    "reconcile RA budget 72.445m vs BI2026 71.925m and prior CoA 41.8m perimeter,"
    "RA2025 budget L5 public; full accounts and end-receiver residual; CoA opacity flag,7,"
    "New Samusocial / COCOM / Vivalis transparence,,,docs/doge/foi/drafts/gap_samusocial_accounts_l5.md,"
    "ready,2026-08-01,,,,,cmt_samusocial_budget_2025,lb_samusocial_budget_72m_2025,"
    "2026-08-01T03:45:00Z,2026-08-01T03:45:00Z,"
    "tick378 draft ready human send only; updates CoA 2020-24 accounts gap"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_row + "\n")
print("foi +1")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T03:45:00Z,rq_369,378,no,"
    "Scheduler 60s. Next prio5 rq_370; rq_116 SWA deferred. FOI ready. tick378 Samusocial 72.4m multi-funder.\n",
    encoding="utf-8",
)
print("state 378 OK")
