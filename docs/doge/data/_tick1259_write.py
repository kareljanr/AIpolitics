# -*- coding: utf-8 -*-
"""Tick 1259 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AGB sogent JR2025 dual residual (Stad Gent urban development / real estate)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T07:40:00Z"
TICK = 1259
SRC = "src_sogent_jr2025_bbc"
SRC2 = "src_sogent_jr2025_gr00692"
ENT = "agb_sogent"
CITY = "city_gent"
SRC_URL = "https://sogent.be/uploads/Jaarrekeningen/2025/20260511_DO_JRR-2025-BBC.pdf"
SRC2_URL = "https://raadpleegomgeving.stad.gent/zittingen/25.0902.9427.5248/agendapunten/26.0512.0179.0437"
GAP = "gap_sogent_afm_neg_3_90m_icc_35m_fin_debt_96_31m_l5"
HIER = "Vlaanderen>Gemeenten>Gent>AGB_sogent"


def append_rows(path, new_rows):
    """Append dict rows using existing header; do not rewrite the file."""
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
    """Replace only the target task_id line; append spawn if missing. No full rewrite of other rows."""
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


def patch_entity_notes_line(path, entity_id, extra):
    """Replace only the matching entity line; leave all other bytes/rows untouched."""
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
            "title": "sogent JR2025 BBC 160p + VOL-kap (KBO 0367.300.594)",
            "url": SRC_URL,
            "publisher": "AGB sogent",
            "accessed_date": "2026-08-17",
            "source_class": "primary_pdf",
            "notes": (
                "tick1259; RVB 28.05.2026; published 29.05.2026; GR 2026_GR_00692 23.06.2026; "
                "expl -2.465m AFM -3.901m gecorr -10.107m BBR +10.455m avail +0.372m; "
                "ICC capital +35m; fin debt 96.310m; assets 329.980m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2026_GR_00692 AGB sogent jaarrekening 2025 goedkeuring",
            "url": SRC2_URL,
            "publisher": "Stad Gent gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1259; GR 22-23.06.2026; RVB 28.05.2026 vaststelling vennootschap + BBC; "
                "36 voor / 3 tegen / 5 onthouding"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "AGB sogent (Stadsontwikkelingsbedrijf Gent)",
            "name_fr": "AAG sogent (développement urbain Gand)",
            "name_en": "AGB sogent (Ghent urban development / real estate vehicle)",
            "level": "municipal_agency",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://sogent.be",
            "foi_email": "info@sogent.be",
            "foi_postal": "Voldersstraat 1 9000 Gent",
            "notes": (
                "tick1259; KBO 0367.300.594; Entity II urban development / real estate; "
                "JR2025 BBC 160p text; assets 329.980m fin debt 96.310m AFM -3.901m "
                f"ICC inbreng 35m; FOI {GAP}"
            ),
        }
    ],
)
print("entities", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    "sogent dual residual tick1259 (KBO 0367.300.594; assets 329.980m / fin debt 96.310m / AFM -3.901m / ICC +35m / city werkingssub 5.359m)",
)
print("city_gent notes", ok)

bud_rows = [
    ("bud_sogent_assets_2025", 329979626, "VOL-kap assets YE2025 329.980m JUMP (was 289.619m)"),
    ("bud_sogent_equity_2025", 204820634, "VOL-kap EV YE2025 204.821m (inbreng 191.817m + kapitaalsub 14.507m)"),
    ("bud_sogent_inbreng_2025", 191816905, "VOL-kap geplaatst kapitaal 191.817m after ICC +35m"),
    ("bud_sogent_cum_loss_2025", -1503964, "VOL-kap overgedragen verlies -1.504m (was -1.631m)"),
    ("bud_sogent_cash_2025", 9744030, "VOL-kap liquide middelen 9.744m JUMP (was 6.126m)"),
    ("bud_sogent_inventory_re_2025", 73561335, "VOL-kap voorraad onroerend te koop 73.561m"),
    ("bud_sogent_fva_2025", 64031380, "VOL-kap financiële vaste activa 64.031m (deelnemingen verbonden 49.285m)"),
    ("bud_sogent_mva_buildings_2025", 73160892, "VOL-kap terreinen/gebouwen 73.161m JUMP (was 38.745m; ICC)"),
    ("bud_sogent_fin_debt_2025", 96309993, "BBC T4 totale financiële schuld YE2025 96.310m"),
    ("bud_sogent_fin_debt_lt_2025", 86665771, "BBC/VOL LT financiële schuld 86.666m (achtergesteld 58.393m + bank 28.273m)"),
    ("bud_sogent_fin_debt_st_2025", 8151500, "VOL ST financiële schuld bank 8.152m (was 16.226m)"),
    ("bud_sogent_subord_debt_2025", 58392889, "VOL achtergestelde leningen LT 58.393m (was 48.094m)"),
    ("bud_sogent_expl_rec_2025", 34456155, "BBC J2 exploitatieontvangsten 34.456m"),
    ("bud_sogent_expl_exp_2025", 36921568, "BBC J2 exploitatieuitgaven 36.922m"),
    ("bud_sogent_expl_saldo_2025", -2465413, "BBC J2 exploitatiesaldo -2.465m (MJP -9.788m)"),
    ("bud_sogent_invest_exp_2025", 38336555, "BBC J2 investeringsuitgaven 38.337m JUMP (MJP 9.262m)"),
    ("bud_sogent_invest_saldo_2025", -37526131, "BBC J2 investeringssaldo -37.526m (MJP -8.218m)"),
    ("bud_sogent_fin_rec_2025", 60438747, "BBC J2 financieringsontvangsten 60.439m (kapitaal 35m + leningen 18.771m)"),
    ("bud_sogent_fin_saldo_2025", 50446955, "BBC J2 financieringssaldo +50.447m"),
    ("bud_sogent_bbr_2025", 10455411, "BBC J2 budgettair resultaat +10.455m (MJP -7.509m)"),
    ("bud_sogent_bbr_avail_2025", 371698, "BBC J2 beschikbaar BBR +0.372m (cum 0.388m - blocked 16.645)"),
    ("bud_sogent_afm_2025", -3900806, "BBC J2 AFM -3.901m (MJP -11.163m)"),
    ("bud_sogent_afm_gecorr_2025", -10107159, "BBC J2 gecorrigeerde AFM -10.107m (MJP -17.197m)"),
    ("bud_sogent_city_alg_sub_2025", 3501378, "BBC T2 algemene werkingssubsidie gemeente 3.501m"),
    ("bud_sogent_city_spec_sub_2025", 1857546, "BBC T2 specifieke werkingssubsidie gemeente 1.858m"),
    ("bud_sogent_vl_spec_sub_2025", 1281752, "BBC T2 specifieke werkingssubsidie Vlaanderen 1.282m"),
    ("bud_sogent_werkingssub_2025", 6640675, "BBC T2 werkingssubsidies totaal 6.641m"),
    ("bud_sogent_other_ops_rec_2025", 14413128, "BBC T2 andere operationele ontvangsten 14.413m JUMP (was 7.388m)"),
    ("bud_sogent_goods_2025", 28264947, "BBC T2 goederen en diensten 28.265m"),
    ("bud_sogent_personnel_2025", 7172804, "BBC T2 personeel 7.173m / 61 personen (geen FTE)"),
    ("bud_sogent_new_loans_2025", 18771333, "BBC T2/T4 nieuwe leningen andere entiteiten 18.771m (niet banken)"),
    ("bud_sogent_icc_capital_2025", 35000000, "BBC T2/toelichting kapitaalsverhoging ICC-overdracht Stad 35.000m"),
    ("bud_sogent_city_guarantee_2025", 16884323, "BBC T off-balance city borg bankleningen sogent 16.884m"),
    ("bud_sogent_modest_guarantee_2025", 18719760, "BBC T off-balance sogent borg Modest 18.720m"),
    ("bud_sogent_theloop_guarantee_2025", 5000000, "BBC T off-balance sogent borg Grondbank The Loop 5.000m"),
    ("bud_sogent_pnl_2025", 127350, "VOL-kap PnL +0.127m (geen dividend); BBC T5 overschot +0.127m"),
    ("bud_sogent_omzet_2025", 13063301, "VOL-kap omzet 13.063m (was 21.396m)"),
    ("bud_sogent_op_profit_2025", 745526, "VOL-kap bedrijfswinst 0.746m (was 1.431m)"),
    ("bud_sogent_interest_2025", 1274747, "BBC T2 rente aan financiële instellingen 1.275m"),
    ("bud_sogent_invest_buildings_2025", 35697364, "BBC T2 invest terreinen/gebouwen 35.697m (ICC)"),
    ("bud_sogent_nonperiod_repay_2025", 8472856, "BBC T2/T4 niet-periodieke aflossingen 8.473m"),
    ("bud_sogent_period_repay_2025", 1435393, "BBC T2/T4 periodieke aflossingen 1.435m"),
    ("bud_sogent_provisions_2025", 8643470, "VOL-kap voorzieningen 8.643m (was 9.187m)"),
    ("bud_sogent_debts_2025", 116515523, "VOL-kap schulden totaal 116.516m"),
    ("bud_sogent_city_invest_sub_2025", 293949, "BBC T2 investeringssubsidie gemeente 0.294m"),
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
    ("comm_sogent_city_dual_sub_5_36m_2025", "sogent city dual werkingssub 5.359m (alg 3.501 + spec 1.858)", "5358924", "City operating dual to urban-development AGB", "Citeer Stad Gent JR2025-tegenhanger FOI"),
    ("comm_sogent_icc_capital_35m_2025", "sogent ICC kapitaalsinbreng Stad 35m (niet in MJP)", "35000000", "Transfer investeringsproject ICC city → AGB", "Boekwaarde vs markt + restverbintenis FOI"),
    ("comm_sogent_fin_debt_96_31m_2025", "sogent financiële schuld YE2025 96.310m", "96309993", "LT 86.666 + ST 8.152 + binnen-jaar 1.493", "Crediteur-split achtergesteld 58.393m FOI"),
    ("comm_sogent_new_loans_18_77m_2025", "sogent nieuwe leningen andere entiteiten 18.771m", "18771333", "Niet-bancaire opname 2025", "Crediteur/rente/achtergesteld FOI"),
    ("comm_sogent_afm_neg_3_90m_2025", "sogent AFM -3.901m / gecorr -10.107m", "-3900806", "Expl -2.465m na periodieke aflossing 1.435m", "MJP pad + gecorrigeerde aflossing 7.642m FOI"),
    ("comm_sogent_inventory_73_56m_2025", "sogent voorraad onroerend te koop 73.561m", "73561335", "Projectstock urban development", "Projectlijst + verwachte verkoop FOI"),
    ("comm_sogent_guarantees_2025", "sogent borg Modest 18.720m + The Loop 5m; city borg 16.884m", "40604083", "Off-balance guarantees dual", "Opgenomen vs plafond + risicoklasse FOI"),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AGB sogent / Stad Gent / Groep Gent vastgoed",
            "legal_basis": "BBC JR2025 AGB sogent + 2026_GR_00692",
            "decision_date": "2026-06-23",
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
            "notes": f"tick{TICK}; primary sogent BBC JR2025 160p",
        }
        for cid, title, env, goal, cut in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_sogent_afm_neg_3_90m_2025", "sogent AFM -3.90m / gecorr -10.11m on 34.46m expl rec", "-3900806", "8.0", "7.5", "3.0"),
    ("lb_sogent_icc_capital_35m_2025", "sogent ICC city capital transfer 35m off-MJP", "35000000", "8.5", "8.5", "3.0"),
    ("lb_sogent_fin_debt_96_31m_2025", "sogent fin debt 96.31m (subord 58.39m + bank ~36.4m)", "96309993", "8.0", "8.5", "3.0"),
    ("lb_sogent_city_dual_5_36m_2025", "sogent city dual werkingssub 5.36m plus 0.29m invest sub", "5358924", "7.0", "6.5", "3.0"),
    ("lb_sogent_invest_38_34m_2025", "sogent invest spend 38.34m vs MJP 9.26m (ICC buildings)", "38336555", "8.0", "8.0", "3.0"),
    ("lb_sogent_inventory_73_56m_2025", "sogent real-estate stock for sale 73.56m (no project list)", "73561335", "7.5", "8.0", "3.0"),
    ("lb_sogent_guarantees_40_60m_2025", "sogent+city off-balance guarantees ~40.6m (Modest/The Loop/city borg)", "40604083", "8.0", "7.5", "3.0"),
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
            "tco_notes": "AGB sogent JR2025 urban development / real estate Entity II Gent",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Gent residents / Groep Gent vastgoed",
            "stated_goal": "Local dual residual AGB map VL JR2025 urban development vehicle",
            "measured_outcome": "assets 329.980m / fin debt 96.310m / AFM -3.901m / ICC +35m / avail BBR +0.372m / PnL +0.127m",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Loan-creditor + ICC book-vs-market + inventory project-list FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary sogent BBC JR2025 160p; not TE-additive without city GE",
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
                "Creditor split of new loans 18.771333m (andere entiteiten, not banks) and "
                "subordinated LT 58.392889m vs bank LT 28.272881m + ST 8.151500m; ICC 35m "
                "capital transfer book vs market + remaining city commitments; inventory "
                "real-estate-for-sale 73.561335m project list; other ops rec 14.413128m vs "
                "omzet 13.063301m split; city dual lines 3.501378+1.857546+0.293949 vs Stad "
                "Gent JR2025 counterpart; VL spec 1.281752 programme; guarantees city "
                "16.884323 / Modest 18.719760 / The Loop 5.000000 drawn vs ceiling; FTE "
                "behind 61 persons / personnel 7.172804m"
            ),
            "why_it_matters": (
                "Largest remaining Gent Entity II: AFM -3.901m and gecorr -10.107m on "
                "34.456m expl rec; 35m ICC capital off-MJP plus 38.337m invest; 96.310m "
                "fin debt and ~40.6m off-balance guarantees sit beside available BBR only +0.372m"
            ),
            "priority": "9",
            "recipient_body": "AGB sogent / Stad Gent",
            "recipient_email": "info@sogent.be",
            "recipient_postal": "Voldersstraat 1 9000 Gent",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_sogent_icc_capital_35m_2025",
            "linked_leaderboard_id": "lb_sogent_icc_capital_35m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1259",
    "title": "AGB sogent Gent JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB sogent JR2025 BBC 160p text + VOL-kap; KBO 0367.300.594; "
        "ICC +35m / AFM -3.901m / fin debt 96.310m"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1259 AGB sogent JR2025 dual residual; KBO 0367.300.594 160p text; "
        "assets 329.980m fin debt 96.310m AFM -3.901m gecorr -10.107m BBR +10.455m "
        "avail +0.372m ICC +35m city sub 5.359m cash 9.744m JUMP PnL +0.127m; "
        "FOI ready not sent; next rq_1260 residual dual L5 VL + every-10 refresh"
    ),
}
rq_spawn = {
    "task_id": "rq_1260",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg not yet mined "
        "(Gent dual AGB cluster done ticks 1255-1259: K&D / Erfgoed / IVA HH / "
        "District09 / sogent; prefer next unmined AGB/zorg with direct PDF; "
        "skip Mobil-O/AG EOS inactive; skip Woonzorgnetwerk Edegem / "
        "Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat unpublished). "
        "Tick 1260 is a *0 tick: also refresh progress_every_10_ticks.md + "
        "doge_waste_top10_current.md."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1259 after AGB sogent JR2025 dual residual; next residual dual L5 VL + every-10 refresh",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1259", rq_new, rq_spawn)
print("research_queue 1259", found, "spawned_1260", spawned)

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
            "last_unit_id": "rq_1259",
            "ticks_completed": "1259",
            "paused": "no",
            "notes": (
                "tick1259 AGB sogent JR2025 dual residual; KBO 0367.300.594 160p text; "
                "assets 329.980m fin debt 96.310m AFM -3.901m gecorr -10.107m BBR +10.455m "
                "avail +0.372m ICC +35m city sub 5.359m cash 9.744m PnL +0.127m; FOI ready; "
                "next rq_1260 residual dual L5 VL + every-10 refresh; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1259 - 2026-08-17 - rq_1259 AGB sogent dual residual
- Unit: AGB sogent (Stadsontwikkelingsbedrijf Gent) JR2025 Entity II after city Gent stub tick101 + culture/IT AGBs ticks 1255–1258 (KBO 0367.300.594; 160p BBC text + VOL-kap; RVB 28.05.2026 / GR 2026_GR_00692 23.06.2026). Distinct from AGB Kunsten en Design / Erfgoed / IVA Historische Huizen / District09. Urban development / real estate vehicle; seat Voldersstraat 1.
- EUR strong: assets **329.980m** JUMP (was 289.619m); EV **204.821m** (inbreng **191.817m** +35m ICC); cash **9.744m** JUMP; voorraad te koop **73.561m**; fin debt **96.310m** (LT **86.666m** achtergesteld **58.393m** + bank **28.273m**; ST **8.152m**); expl rec **34.456m** / exp **36.922m** / saldo **−2.465m**; invest **−37.526m** (uitg **38.337m**); BBR **+10.455m** / avail **+0.372m**; AFM **−3.901m** / gecorr **−10.107m**; city werkingssub **5.359m** (alg **3.501m** + spec **1.858m**) + VL spec **1.282m**; ICC kapitaal **35.000m** off-MJP; new loans andere entiteiten **18.771m**; PnL **+0.127m**; personnel **7.173m** / **61 personen** (geen FTE); city borg **16.884m**; sogent borg Modest **18.720m** + The Loop **5.000m**.
- CSVs: sources+2/entities(+city note)/budgets+45/commitments+7/leaderboard+7 + FOI ready `gap_sogent_afm_neg_3_90m_icc_35m_fin_debt_96_31m_l5` (not sent); rq_1259=done; spawn rq_1260.
- Next: rq_1260 residual dual L5 VL JR2025 hole_fill + **every-10 progress refresh** (tick 1260 is a *0 tick). Gent dual AGB cluster 1255–1259 mapped.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
