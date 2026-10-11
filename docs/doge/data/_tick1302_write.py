# -*- coding: utf-8 -*-
"""Tick 1302 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Wommelgem JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
sys.path.insert(0, str(DATA))
from _tick1302_hdr import *  # noqa: F401,F403

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


def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True


assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((FVA + MVA + IVA) - FIXED) <= 2
assert abs((EVA + IGS + OCMW_VER + OTHER_FVA) - FVA) <= 2
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) <= 2
assert abs((CUM_PREV + BBR) - AVAIL) <= 1
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) <= 1
assert abs((CITY_PNL + OCMW_PNL) - PNL) <= 1
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Wommelgem BBC jaarrekening 2025 (Meeting Burger PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Wommelgem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1302; BBC text PDFs meetingburger GR 28.05.2026 Jnl 21030; "
                "deel0 3p / deel2 19p / deel3 58p / deel4 65p; afdruk 27.04.2026; "
                "KBO 0207.535.161/0212.185.025; assets 76.003m pension 10.479m "
                "politie MINOS 2.151m OCMW equity -1.094m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "KBO Gemeente Wommelgem 0207.535.161",
            "url": SRC2_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1302; city KBO 0207.535.161 / OCMW 0212.185.025; "
                "seat Kaakstraat 2 2160; OCMW Handboogstraat 36 2160; "
                "NIS 11052; AD Deroover / FD Augustyns / burgemeester Gys"
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
            "name_nl": "Gemeente Wommelgem",
            "name_fr": "Commune de Wommelgem",
            "name_en": "Municipality of Wommelgem",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.wommelgem.be",
            "foi_email": "info@wommelgem.be",
            "foi_postal": "Kaakstraat 2 2160 Wommelgem",
            "notes": (
                "tick1302 JR2025 GE residual; KBO 0207.535.161; NIS 11052; "
                "AD Marijke Deroover / FD Kris Augustyns / burgemeester Frank Gys; "
                "assets 76.003m pension 10.479m politie MINOS 2.151m "
                "OCMW equity -1.094m; no AGB (EVA 0); FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Wommelgem",
            "name_fr": "CPAS de Wommelgem",
            "name_en": "OCMW Wommelgem",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.wommelgem.be",
            "foi_email": "info@wommelgem.be",
            "foi_postal": "Handboogstraat 36 2160 Wommelgem",
            "notes": (
                "tick1302 JR2025 GE residual; KBO 0212.185.025; J3 expl -1.466m / "
                "T5 PnL -1.291m / cum -2.635m / equity -1.094m NEG; "
                "tussenkomst 1.536m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_wmmg_assets_2025", "2025", ASSETS, "J4 assets 76.002865m vs 73.228125m"),
    ("bud_wmmg_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 73.228125m"),
    ("bud_wmmg_cash_2025", "2025", CASH, "J4 cash+beleg 10.386815m vs 10.932304m DROP"),
    ("bud_wmmg_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 10.932304m"),
    ("bud_wmmg_fva_2025", "2025", FVA, "T5 FVA 8.128993m; EVA 0 + IGS 8.075m + OCMW-ver 124 + other 0.054m"),
    ("bud_wmmg_eva_2025", "2025", EVA, "T5 EVA AGB kapitaal 0 — no AGB Wommelgem"),
    ("bud_wmmg_igs_2025", "2025", IGS, "T5 IGS FVA 8.075072m; Fluvius reval +0.117403m"),
    ("bud_wmmg_mva_2025", "2025", MVA, "J4/T5 MVA 53.887175m; leasing 0.773566m"),
    ("bud_wmmg_leasing_2025", "2025", LEASING, "T5 leasing MVA 0.773566m Fluvius OV (aankoop 0.435m)"),
    ("bud_wmmg_iva_2025", "2025", IVA, "J4/T5 IVA 0.246635m"),
    ("bud_wmmg_equity_2025", "2025", EQUITY, "J4 nettoactief 60.215779m vs 57.861524m"),
    ("bud_wmmg_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL 10.992760m (city 13.628 / OCMW -2.635)"),
    ("bud_wmmg_reval_2025", "2025", REVAL, "J4 herwaarderingsreserves 2.489298m (Fluvius +0.117m)"),
    ("bud_wmmg_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 0.773566m (LT 0.711 + ST due 0.062) JUMP vs 0.380m"),
    ("bud_wmmg_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 0.379656m"),
    ("bud_wmmg_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin debt 0.711435m"),
    ("bud_wmmg_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4/J4 ST due 0.062130m"),
    ("bud_wmmg_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.435206m Fluvius leasing; no new bank"),
    ("bud_wmmg_pension_2025", "2025", PENSION, "J4 pension LT 10.479156m vs 10.640897m"),
    ("bud_wmmg_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +4.707647m"),
    ("bud_wmmg_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 24.605560m"),
    ("bud_wmmg_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 19.897914m"),
    ("bud_wmmg_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +6.173472m (ontv 21.350 / uitg 15.177)"),
    ("bud_wmmg_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -1.465825m (ontv 3.255 / uitg 4.721)"),
    ("bud_wmmg_invest_2025", "2025", INVEST, "J2 invest -5.171223m vs MJP -6.002m"),
    ("bud_wmmg_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar -0.069666m (GR omitted minus)"),
    ("bud_wmmg_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 10.527644m"),
    ("bud_wmmg_afm_2025", "2025", AFM, "J2 AFM +4.666351m"),
    ("bud_wmmg_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +4.677274m"),
    ("bud_wmmg_pnl_2025", "2025", PNL, "J5 PnL +2.436851m; city +3.728 / OCMW -1.291; tussen 1.536m"),
    ("bud_wmmg_tussen_2025", "2025", TUSSEN, "T5 tussenkomst gemeente-OCMW 1.536147m"),
    ("bud_wmmg_pers_2025", "2025", PERS, "J5/T2 bezoldigingen 8.862622m; VTE unpublished"),
    ("bud_wmmg_fiscal_2025", "2025", FISCAL, "J5/T2 fiscale 13.389553m (OV 5.649 + APB 4.206)"),
    ("bud_wmmg_ov_2025", "2025", OV, "T2 OV 5.648542m"),
    ("bud_wmmg_apb_2025", "2025", APB, "T2 APB 4.206222m JUMP vs 3.583m"),
    ("bud_wmmg_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 3.225990m"),
    ("bud_wmmg_politie_2025", "2025", POLITIE, "T2 PZ MINOS 2.150852m JUMP vs 1.925m"),
    ("bud_wmmg_hvz_2025", "2025", HVZ, "T2 HVZ Rand werk 0.497157m (+ invest 0.128325m)"),
    ("bud_wmmg_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity -1.094158m NEG"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": year,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "executed",
            "source_id": SRC,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}; primary BBC",
        }
        for bid, year, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_wmmg_pension_10_48m_2025",
        "Wommelgem YE2025 pension LT 10.479m",
        "10479156",
        "J4 pension LT 10.479156m vs 10.640897m; respo city 0.363290 + OCMW 0.084940; mandatarissen 0.167791; VL cover 0.297670",
        "Publish actuarial note + city/OCMW split + pad 2026-2031 FOI",
    ),
    (
        "comm_wmmg_politie_2_15m_2025",
        "Wommelgem 2025 PZ MINOS 2.151m",
        "2150852",
        "T2 PZ MINOS 2.150852m JUMP vs 1.925232m; invest 0.058525m; HVZ Rand werk 0.497157m + invest 0.128325m",
        "Publish 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_wmmg_tussen_1_54m_2025",
        "Wommelgem YE2025 OCMW tussenkomst 1.536m",
        "1536147",
        "T5 tussenkomst 1.536147m; OCMW expl -1.466m / PnL -1.291m / equity -1.094m NEG / cum -2.635m NEG",
        "Publish cash vs resultaatstoewijzing + pad 2026-2031 FOI",
    ),
    (
        "comm_wmmg_igs_8_08m_2025",
        "Wommelgem YE2025 IGS FVA 8.075m",
        "8075072",
        "T5 IGS 8.075072m; Fluvius reval +0.117403m; verkoop -0.023379m; verledding -0.045058m; EVA 0",
        "Publish per-IGS aanschaf vs boekwaarde FOI",
    ),
    (
        "comm_wmmg_fin_debt_0_77m_2025",
        "Wommelgem YE2025 fin debt 0.774m Fluvius lease",
        "773566",
        "T4 0.773566m (LT 0.711 + ST due 0.062) JUMP vs 0.380m; new loans 0.435m Fluvius leasing only",
        "Publish per-contract amort 2026-2031 FOI",
    ),
    (
        "comm_wmmg_pers_8_86m_2025",
        "Wommelgem 2025 pers 8.863m / VTE unpublished",
        "8862622",
        "pers 8.862622m; VTE unpublished; politiek 0.465 / vast 2.534 / niet-vast 5.292",
        "Publish paid VTE city vs OCMW FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Wommelgem / OCMW / PZ MINOS / HVZ Rand",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Wommelgem vastgesteld 28.05.2026",
            "decision_date": "2026-05-28",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Wommelgem",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": note + f"; tick{TICK}; primary BBC",
        }
        for cid, title, env, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_wmmg_pension_10_48m_2025",
        "Wommelgem YE2025 pension LT 10.48m",
        "10479156",
        "7.5",
        "8.0",
        "Publish actuarial note + city/OCMW split + pad 2026-2031",
        "pension LT 10.479m vs 10.641m; respo city 0.363 + OCMW 0.085; VL cover 0.298",
    ),
    (
        "lb_wmmg_politie_2_15m_2025",
        "Wommelgem 2025 PZ MINOS 2.15m",
        "2150852",
        "6.5",
        "6.5",
        "Publish 2026-2031 verdeelsleutel",
        "PZ MINOS 2.151m JUMP vs 1.925m; invest 0.059m; HVZ Rand 0.497+0.128m",
    ),
    (
        "lb_wmmg_tussen_1_54m_2025",
        "Wommelgem YE2025 OCMW tussenkomst 1.54m",
        "1536147",
        "7.0",
        "6.0",
        "Publish cash vs resultaatstoewijzing + pad 2026-2031",
        "tussenkomst 1.536m; OCMW expl -1.466m / PnL -1.291m / equity -1.094m NEG",
    ),
    (
        "lb_wmmg_igs_8_08m_2025",
        "Wommelgem YE2025 IGS FVA 8.08m",
        "8075072",
        "5.5",
        "7.5",
        "Publish per-IGS aanschaf vs boekwaarde",
        "IGS 8.075m; Fluvius reval +0.117m; EVA 0; no AGB",
    ),
    (
        "lb_wmmg_fin_debt_0_77m_2025",
        "Wommelgem YE2025 fin debt 0.77m Fluvius lease",
        "773566",
        "5.0",
        "5.0",
        "Publish per-contract amort 2026-2031",
        "fin debt 0.774m JUMP vs 0.380m; new loans 0.435m Fluvius leasing only",
    ),
    (
        "lb_wmmg_pers_8_86m_vte_unpub_2025",
        "Wommelgem 2025 pers 8.86m / VTE unpublished",
        "8862622",
        "6.0",
        "7.0",
        "Publish paid VTE city vs OCMW",
        "pers 8.863m; VTE unpublished; niet-vast 5.292m",
    ),
    (
        "lb_wmmg_ocmw_equity_neg_1_09m_2025",
        "Wommelgem YE2025 OCMW equity -1.09m NEG",
        "1094158",
        "6.5",
        "5.5",
        "Publish OCMW recovery pad 2026-2031",
        "OCMW equity -1.094m NEG / cum -2.635m NEG; tussen 1.536m vs expl -1.466m",
    ),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": amt,
            "total_cost_eur": amt,
            "tco_notes": tco,
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Inwoners Wommelgem / OCMW / PZ MINOS / HVZ Rand",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Wommelgem",
            "measured_outcome": (
                "assets 76.003m / pension 10.479m / politie 2.151m / "
                "OCMW equity -1.094m / IGS 8.075m / AFM +4.666m / avail 10.528m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "5.5",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; city GE FOI",
        }
        for iid, name, amt, absu, cost, cut, tco in lb_rows
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
                "J4 pension LT 10.479156m city/OCMW split + responsabilisering "
                "0.363290/0.084940 + T4 per-contract creditors for fin debt 0.773566m "
                "(new loans 0.435206 Fluvius leasing only) + IGS FVA 8.075072 inventory "
                "(Fluvius reval +0.117403; EVA 0) + OCMW tussenkomst 1.536147 vs expl "
                "-1.465825 / PnL -1.291089 / equity -1.094158 NEG + VTE vs pers 8.862622 "
                "+ politiezone MINOS 2.150852 / HVZ Rand 0.497157 pad"
            ),
            "why_it_matters": (
                "Unmined leftover city+OCMW Wommelgem GE after residual dual hunt found "
                "live Meeting Burger JR2025 PDFs. No AGB (EVA 0). Pension LT 10.479m. "
                "PZ MINOS 2.151m JUMP. OCMW equity -1.094m NEG; tussen 1.536m. "
                "Fin debt 0.774m all Fluvius leasing. Avail 10.528m with BBR year -0.070m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Wommelgem (gemeente + OCMW)",
            "recipient_email": "info@wommelgem.be",
            "recipient_postal": "Kaakstraat 2 2160 Wommelgem",
            "draft_letter_path": "docs/doge/foi/drafts/gap_wmmg_pension_10_48m_politie_2_15m_ocmw_equity_neg_1_09m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_wmmg_pension_10_48m_2025",
            "linked_leaderboard_id": "lb_wmmg_pension_10_48m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1302",
    "title": "Stad+OCMW Wommelgem JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Wommelgem JR2025 BBC text + KBO; "
        "KBO 0207.535.161 / 0212.185.025; assets 76.003m / pension 10.479m / "
        "politie MINOS 2.151m / OCMW equity -1.094m NEG / IGS 8.075m / AFM +4.666m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T15:30:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1302 Stad+OCMW Wommelgem JR2025 GE residual; KBO 0207.535.161/0212.185.025; "
        "assets 76.003m pension 10.479m politie MINOS 2.151m OCMW equity -1.094m NEG "
        "IGS 8.075m AFM +4.666m gecorr +4.677m BBR -0.070m avail 10.528m cash 10.387m "
        "tussen 1.536m pers 8.863m new loans 0.435m Fluvius leasing; no AGB EVA 0; "
        "FOI ready not sent; next rq_1303 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1303",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1302 done including Stad+OCMW Wommelgem 1302 / Stad+OCMW Zonhoven 1301 / "
        "Stad+OCMW Kortenaken 1300 / AGB Kortenaken 1299 / Stad+OCMW Steenokkerzeel 1298 / "
        "AGB Steenokkerzeel 1167 / Stad+OCMW Diepenbeek 1297 / AGB Diepenbeek 1296); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined city Wommelgem 1302 / city Zonhoven 1301 / city Kortenaken 1300 / "
        "AGB Kortenaken 1299 / city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / "
        "city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / "
        "Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / "
        "Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; "
        "leftover Maarkedal/Meulebeke still unmined — take only if PDF fetches; "
        "Londerzeel/Holsbeek/Merchtem/Pepingen/Zwalm/Wortegem-Petegem city+OCMW JR2025 only if PDF fetches; "
        "AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "skip AGB Kapellen / APB Mercator / Nieuwerkerken 1102 already mined; "
        "skip AGB Sport Hulshout JR2024-only; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1302 after Stad+OCMW Wommelgem JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1302", rq_new, rq_spawn)
print("research_queue 1302", found, "spawned_1303", spawned)

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
            "last_unit_id": "rq_1302",
            "ticks_completed": "1302",
            "paused": "no",
            "notes": (
                "tick1302 Stad+OCMW Wommelgem JR2025 GE residual; KBO 0207.535.161/0212.185.025; "
                "assets 76.003m pension 10.479m politie MINOS 2.151m OCMW equity -1.094m; "
                "FOI ready; next rq_1303 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1302_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
