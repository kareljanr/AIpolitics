# -*- coding: utf-8 -*-
"""Tick 1260 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AG Vespa Antwerpen JR2025 dual residual + every-10 progress refresh."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T07:40:00Z"
TICK = 1260
SRC = "src_vespa_jr2025_bbc"
SRC2 = "src_vespa_jr2025_gr00589"
ENT = "ag_vespa_antwerpen"
CITY = "city_antwerpen"
SRC_URL = "https://www.agvespa.be/sites/default/files/download-item/2_jaarrekening_bbc_2025.pdf"
SRC2_URL = "https://ebesluit.antwerpen.be/zittingen/25.0918.3949.0497/agendapunten/26.0519.6668.0751"
TOEL_URL = "https://www.agvespa.be/sites/default/files/download-item/3_toelichting_jr_2025.pdf"
GAP = "gap_vespa_gecorr_afm_neg_1_86m_fin_debt_179_63m_dbfm_109_4m_l5"
HIER = "Vlaanderen>Gemeenten>Antwerpen>AG_Vespa"


def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()


def patch_rq_target_and_append(path, target_id, new_target, spawn_row):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    has_spawn = False
    spawn_id = spawn_row.get("task_id")
    for line in lines[1:]:
        if not line:
            continue
        rid = next(csv.reader([line]))[0]
        if rid == spawn_id:
            has_spawn = True
        if rid == target_id:
            found = True
            out.append(csv_line(fields, new_target))
        else:
            out.append(line)
    if not has_spawn:
        out.append(csv_line(fields, spawn_row))
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found, not has_spawn


def patch_entity_notes_line(path, entity_id, extra, extra_fields=None):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    for line in lines[1:]:
        if not line:
            continue
        row = next(csv.DictReader([header, line]))
        if row.get("entity_id") == entity_id:
            found = True
            if extra_fields:
                row.update(extra_fields)
            notes = row.get("notes") or ""
            if extra not in notes:
                row["notes"] = (notes + "; " + extra).strip("; ")
            out.append(csv_line(fields, row))
        else:
            out.append(line)
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AG Vespa JR2025 BBC 43p + toelichting 10p (KBO 0267.402.076)",
            "url": SRC_URL,
            "publisher": "AG Vespa",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1260; RVB/GR 2026_GR_00589 29.06.2026; published jaarverslag 23.06.2026; "
                "assets 618.620m fin debt 179.628m AFM +7.296m gecorr -1.863m BBR +14.912m "
                "avail +63.189m city werk 3.672m invest-sub 12.760m PnL NBB -2.362m; "
                f"toelichting {TOEL_URL}"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2026_GR_00589 AG Vespa jaarrekeningen NBB+BBC 2025 goedkeuring",
            "url": SRC2_URL,
            "publisher": "Stad Antwerpen gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1260; GR 29.06.2026; assets 618.620.035,87; bedrijfsopbr 131.486.834,61 / "
                "kosten 132.656.345,71; te bestemmen verlies 2.361.661,91; BBR 14.911.690; "
                "cum BBR 63.498.689; AFM 7.295.849; restmiddelen 0; N-VA/Vooruit/GROEN/VB ja; "
                "PVDA/cd&v onthouding"
            ),
        },
    ],
)
print("sources", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    ENT,
    (
        "tick1260 JR2025 dual residual; KBO 0267.402.076; assets 618.620m fin debt 179.628m "
        "DBFM 109.4m gecorr AFM -1.863m BBR +14.912m city werk 3.672m invest-sub 12.760m "
        f"PnL -2.362m; FOI {GAP}"
    ),
    extra_fields={
        "website": "https://www.agvespa.be",
        "foi_email": "agvespa@antwerpen.be",
        "foi_postal": "Paradeplein 25 2018 Antwerpen",
        "name_nl": "AG Vespa (Autonoom Gemeentebedrijf Vastgoedbeheer en Stadsprojecten)",
        "name_en": "AG Vespa Antwerp municipal real estate / urban development AGB",
    },
)
print("entity vespa", ok)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "Vespa dual residual tick1260 (KBO 0267.402.076; assets 618.620m / fin debt 179.628m / "
        "DBFM 109.4m / gecorr AFM -1.863m / city werk 3.672m + invest-sub 12.760m)"
    ),
)
print("city_antwerpen notes", ok)

bud_rows = [
    ("bud_vespa_assets_2025", 618620036, "BBC J4 / NBB assets YE2025 618.620m (was 609.796m)"),
    ("bud_vespa_equity_nbb_2025", 310837047, "NBB EV YE2025 310.837m (kapitaal 213.675 + reserves 19.806 + kapitaalsub 77.356)"),
    ("bud_vespa_nettoactief_bbc_2025", 313813418, "BBC J4 nettoactief 313.813m"),
    ("bud_vespa_capital_2025", 213674608, "NBB kapitaal 213.675m after city inbreng +2.273m"),
    ("bud_vespa_capital_sub_2025", 77356216, "BBC/NBB kapitaalsubsidies 77.356m (was 68.398m)"),
    ("bud_vespa_cum_surplus_2025", 14148564, "BBC J4/T5 gecumuleerd overschot 14.149m (was 17.083m)"),
    ("bud_vespa_cash_2025", 53164169, "BBC J4 / NBB thesaurie 53.164m JUMP (was 40.518m)"),
    ("bud_vespa_inventory_2025", 76274605, "BBC/NBB voorraden 76.275m (comm 31.00 + wonen 4.22 + ontw 46.34)"),
    ("bud_vespa_mva_2025", 435680216, "BBC J4 MVA 435.680m (leasing 22.384m)"),
    ("bud_vespa_fva_2025", 8068220, "BBC J4 FVA 8.068m (toelichting 9.408m incl. achtergesteld)"),
    ("bud_vespa_fin_debt_2025", 179628090, "BBC T4 totale financiële schuld YE2025 179.628m"),
    ("bud_vespa_fin_debt_lt_2025", 173838865, "BBC T4/J4 LT financiële schuld 173.839m"),
    ("bud_vespa_fin_debt_st_due_2025", 5789224, "BBC T4 LT-binnen-jaar 5.789m (city 2.05 + DBFM 3.74)"),
    ("bud_vespa_dbfm_lt_2025", 109400000, "Toelichting B12 DBFM mastergebouw PZA LT 109.40m"),
    ("bud_vespa_city_subord_2025", 29600000, "Toelichting B12 city achtergesteld 29.60m"),
    ("bud_vespa_city_invest_loan_2025", 34850000, "Toelichting B12 city investeringskrediet 20j 0% 34.85m"),
    ("bud_vespa_expl_rec_2025", 137969376, "BBC J2 exploitatieontvangsten 137.969m"),
    ("bud_vespa_expl_exp_2025", 124991787, "BBC J2 exploitatieuitgaven 124.992m"),
    ("bud_vespa_expl_saldo_2025", 12977588, "BBC J2 exploitatiesaldo +12.978m (MJP +10.313m)"),
    ("bud_vespa_invest_exp_2025", 11285004, "BBC J2 investeringsuitgaven 11.285m (MJP 32.759m; 34% realisatie)"),
    ("bud_vespa_invest_saldo_2025", 5806965, "BBC J2 investeringssaldo +5.807m (MJP -23.325m)"),
    ("bud_vespa_fin_saldo_2025", -3872863, "BBC J2 financieringssaldo -3.873m"),
    ("bud_vespa_bbr_2025", 14911690, "BBC J2 budgettair resultaat +14.912m (MJP -19.025m)"),
    ("bud_vespa_bbr_cum_2025", 63498689, "BBC J2 gecumuleerd BBR 63.499m"),
    ("bud_vespa_bbr_avail_2025", 63188686, "BBC J2 beschikbaar BBR +63.189m (blocked huurwaarborg 0.310m)"),
    ("bud_vespa_afm_2025", 7295849, "BBC J2 AFM +7.296m (MJP +4.632m)"),
    ("bud_vespa_afm_gecorr_2025", -1863367, "BBC J2 gecorrigeerde AFM -1.863m (aangewezen 14.841m)"),
    ("bud_vespa_city_alg_sub_2025", 2542620, "BBC T2 algemene werkingssubsidie gemeente 2.543m"),
    ("bud_vespa_city_spec_sub_2025", 994368, "BBC T2 specifieke werkingssubsidie gemeente 0.994m"),
    ("bud_vespa_vl_spec_sub_2025", 134996, "BBC T2 specifieke werkingssubsidie Vlaanderen 0.135m"),
    ("bud_vespa_werkingssub_2025", 3671983, "BBC T2 werkingssubsidies totaal 3.672m"),
    ("bud_vespa_city_invest_sub_2025", 12759635, "BBC T2 investeringssubsidies van de gemeente 12.760m"),
    ("bud_vespa_goods_2025", 102740689, "BBC T2 goederen en diensten 102.741m"),
    ("bud_vespa_personnel_2025", 16946225, "BBC T2 personeel 16.946m / 178 pers / 168.9 VTE (NBB 17.317m)"),
    ("bud_vespa_interest_2025", 3378312, "BBC T2 rente aan financiële instellingen 3.378m (DBFM)"),
    ("bud_vespa_period_repay_2025", 5681740, "BBC T2/T4 periodieke aflossingen 5.682m"),
    ("bud_vespa_capital_increase_2025", 2272609, "BBC §7 / T5 kapitaalsinbreng Stad 2.273m (T2 vermeerdering 2.448m)"),
    ("bud_vespa_pnl_nbb_2025", -2361662, "NBB/toelichting netto resultaat -2.362m (BBC J5 -2.934m)"),
    ("bud_vespa_omzet_bouw_2025", 95768378, "NBB R02 omzet bouw- en stadsprojecten 95.768m"),
    ("bud_vespa_rental_sales_2025", 24339134, "NBB R01 verhuur en verkoop 24.339m"),
    ("bud_vespa_subsidies_r03_2025", 7594699, "NBB R03 subsidies 7.595m (woon 4.03 + city 2.88 + cap 0.12)"),
    ("bud_vespa_onderaanneming_2025", 90853038, "NBB R06 onderaannemingen 90.853m"),
    ("bud_vespa_provisions_2025", 29009903, "NBB voorzieningen 29.010m (Cadix 6.78 + Slachthuis 9.83 + NZ 8.50)"),
    ("bud_vespa_kuub_toelage_2025", 5951403, "BBC §7 toelage project Kuub 5.951m"),
    ("bud_vespa_offbal_area_2025", 16895342, "BBC §5 off-balance gebiedsontwikkeling 16.895m"),
    ("bud_vespa_politie_shell_2025", -6205484, "Toelichting analytisch politiepatrimonium saldo -6.205m"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "bbc_jr_realized",
            "source_id": SRC,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    ("comm_vespa_city_dual_16_30m_2025", "Vespa city dual werk 3.537m + invest-sub 12.760m", "16302223", "City operating+invest dual to real-estate AGB", "Citeer Stad Antwerpen JR2025-tegenhanger vs package lock 6.011m FOI"),
    ("comm_vespa_fin_debt_179_63m_2025", "Vespa financiële schuld YE2025 179.628m", "179628090", "LT 173.839 + binnen-jaar 5.789 (DBFM 109.4 + city 64.45)", "Crediteur-split DBFM/city achtergesteld/0%-krediet FOI"),
    ("comm_vespa_dbfm_109_4m_2025", "Vespa DBFM mastergebouw PZA LT 109.40m", "109400000", "Leasing/DBFM police HQ; cash-neutraal claim vs rente 3.378m", "Cash-neutraliteit + PZA-huur 9.426m FOI"),
    ("comm_vespa_gecorr_afm_neg_1_86m_2025", "Vespa gecorr AFM -1.863m (AFM +7.296m)", "-1863367", "Aangewezen aflossing 14.841m vs periodiek 5.682m", "Aangewezen-aflossing methodiek FOI"),
    ("comm_vespa_inventory_76_27m_2025", "Vespa voorraad 76.275m (comm/wonen/ontw)", "76274605", "Projectstock urban development + woon + commercieel", "Projectlijst + impair 5.28m FOI"),
    ("comm_vespa_kuub_5_95m_2025", "Vespa Kuub school toelage 5.951m", "5951403", "Extra toelage design&build school Jos Smolderenstraat", "Of in city invest-sub 12.760m FOI"),
    ("comm_vespa_offbal_16_90m_2025", "Vespa off-balance gebiedsontwikkeling 16.895m", "16895342", "Toekomstige verplichtingen + achtergesteld 6.85m dochters", "Projectlijst + opgenomen vs plafond FOI"),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AG Vespa / Stad Antwerpen / Groep Antwerpen vastgoed",
            "legal_basis": "BBC JR2025 AG Vespa + 2026_GR_00589",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2026",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary Vespa BBC JR2025 43p + toelichting 10p",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_vespa_gecorr_afm_neg_1_86m_2025", "Vespa gecorr AFM -1.86m while headline AFM +7.30m", "-1863367", "8.0", "6.5", "3.0"),
    ("lb_vespa_fin_debt_179_63m_2025", "Vespa fin debt 179.63m (DBFM 109.4 + city 64.45)", "179628090", "8.0", "8.5", "3.0"),
    ("lb_vespa_dbfm_master_109_4m_2025", "Vespa DBFM police HQ 109.4m (rente 3.38m / PZA huur 9.43m)", "109400000", "8.0", "8.5", "3.0"),
    ("lb_vespa_city_dual_16_30m_2025", "Vespa city dual werk+invest 16.30m vs 2026 lock 6.01m", "16302223", "7.5", "7.5", "3.0"),
    ("lb_vespa_inventory_76_27m_2025", "Vespa real-estate stock 76.27m (impair ~5.3m)", "76274605", "7.0", "8.0", "3.0"),
    ("lb_vespa_pnl_neg_2_36m_2025", "Vespa NBB loss -2.36m / BBC J5 -2.93m on 138m expl rec", "-2361662", "7.5", "6.5", "3.0"),
    ("lb_vespa_politie_shell_neg_6_21m_2025", "Vespa police-patrimonium analytical shell -6.21m", "-6205484", "8.0", "7.0", "3.0"),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + "_L5",
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": "AG Vespa JR2025 urban development / real estate Entity II Antwerpen",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Antwerp residents / Groep Antwerpen vastgoed / PZA",
            "stated_goal": "Local dual residual AGB map VL JR2025 urban development vehicle",
            "measured_outcome": "assets 618.620m / fin debt 179.628m / AFM +7.296m / gecorr -1.863m / avail BBR +63.189m / PnL -2.362m",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "DBFM cash-neutrality + city dual counterpart + 459-vs-178 FTE FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary Vespa BBC JR2025 43p; not TE-additive without city GE",
        }
        for iid, name, cost, absurd, cscore, diff in lrows
    ],
)
print("leaderboard", n)

n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "Creditor split of T4 fin debt 179.628090m (city achtergesteld 29.600m + "
                "city 0% 20y loan 34.850m + DBFM PZA LT 109.400m + ST-due 5.789224m) vs "
                "rente 3.378312m and PZA huur 9.425696m cash-neutrality; city dual "
                "2.542620+0.994368+12.759635+2.272609 vs 2026 package lock 6.011m and "
                "toelichting werkingstoelage 2.875368; Kuub 5.951403 inside/outside invest-sub; "
                "inventory 76.274605 project list; off-balance gebied 16.895342 + Handelsbeurs "
                "4.553138 + BGAPH 2.100000; Digipolis recv 0.839794 T-575/24; 459 vs 178/168.9 VTE; "
                "restmiddelen 0 vs avail BBR 63.188686; aangewezen aflossing 14.840955"
            ),
            "why_it_matters": (
                "Largest remaining Antwerp Entity II after Zorgbedrijf Antwerpen: assets 618.620m "
                "and fin debt 179.628m sit beside gecorr AFM -1.863m (headline AFM +7.296m) and "
                "NBB loss -2.362m; DBFM 109.4m plus city dual 16.3m vs prior 6.0m lock"
            ),
            "priority": "9",
            "recipient_body": "AG Vespa / Stad Antwerpen",
            "recipient_email": "agvespa@antwerpen.be",
            "recipient_postal": "Paradeplein 25 2018 Antwerpen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_vespa_dbfm_109_4m_2025",
            "linked_leaderboard_id": "lb_vespa_fin_debt_179_63m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1260",
    "title": "AG Vespa Antwerpen JR2025 dual residual + every-10 progress",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AG Vespa JR2025 BBC 43p text + toelichting 10p; KBO 0267.402.076; "
        "gecorr AFM -1.863m / fin debt 179.628m / DBFM 109.4m; every-10 refresh done"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1260 AG Vespa JR2025 dual residual + every-10; KBO 0267.402.076 43p BBC; "
        "assets 618.620m fin debt 179.628m AFM +7.296m gecorr -1.863m BBR +14.912m "
        "avail +63.189m city werk 3.672m invest-sub 12.760m cash 53.164m PnL -2.362m "
        "DBFM 109.4m; FOI ready not sent; next rq_1261 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1261",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa Antwerpen 1260 done; "
        "prefer AG Stedelijk Onderwijs Antwerpen / AG CIA Erfgoed / WAGSO Waregem "
        "or other unmined AGB/zorg with direct PDF; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat unpublished)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1260 after AG Vespa JR2025 dual residual + every-10; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1260", rq_new, rq_spawn)
print("research_queue 1260", found, "spawned_1261", spawned)

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1260",
            "ticks_completed": "1260",
            "paused": "no",
            "notes": (
                "tick1260 AG Vespa JR2025 dual residual + every-10; KBO 0267.402.076 43p BBC; "
                "assets 618.620m fin debt 179.628m AFM +7.296m gecorr -1.863m BBR +14.912m "
                "avail +63.189m city werk 3.672m invest-sub 12.760m cash 53.164m PnL -2.362m "
                "DBFM 109.4m; FOI ready; next rq_1261 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1260 - 2026-08-17 - rq_1260 AG Vespa dual residual + progress@1260
- Unit: AG Vespa (Autonoom Gemeentebedrijf Vastgoedbeheer en Stadsprojecten) JR2025 Entity II after city Antwerpen stub + Zorgbedrijf Antwerpen tick1246 (KBO 0267.402.076; 43p BBC text + 10p toelichting; GR 2026_GR_00589 29.06.2026). Distinct from Gent AGB cluster 1255–1259. Urban development / real estate vehicle; seat Paradeplein 25.
- EUR strong: assets **618.620m** (was 609.796m); cash **53.164m** JUMP; voorraden **76.275m**; fin debt **179.628m** (LT **173.839m** = DBFM PZA **109.40m** + city 0% **34.85m** + achtergesteld **29.60m**; binnen-jaar **5.789m**); expl rec **137.969m** / exp **124.992m** / saldo **+12.978m**; invest **+5.807m**; BBR **+14.912m** / avail **+63.189m**; AFM **+7.296m** / **gecorr −1.863m**; city werkingssub **3.672m** (alg **2.543m** + spec **0.994m**) + VL spec **0.135m** + city invest-sub **12.760m**; PnL NBB **−2.362m** / BBC J5 **−2.934m**; personnel **16.946m** / **178** / **168,9 VTE**; Kuub toelage **5.951m**; off-balance gebied **16.895m**.
- CSVs: sources+2/entities(upgrade+city note)/budgets+45/commitments+7/leaderboard+7 + FOI ready `gap_vespa_gecorr_afm_neg_1_86m_fin_debt_179_63m_dbfm_109_4m_l5` (not sent); rq_1260=done; spawn rq_1261; ticks=1260.
- Progress@1260: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E ~903 ready. Pure annual waste top10 **stable** vs 1250 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds Vespa fin debt 179.63m / DBFM 109.4m / gecorr AFM −1.86m + Gent AGB cluster 1255–1259.
- Coverage: 1251–1260 is residual dual L5 (Welzijnszorg Kempen · Cultuur Geel · EVA Lokeren · AG-O · Gent K&D/Erfgoed/IVA HH/District09/sogent · **Vespa**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1261 residual dual L5 VL JR2025 hole_fill (prefer AG Stedelijk Onderwijs / CIA Erfgoed / WAGSO Waregem).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
