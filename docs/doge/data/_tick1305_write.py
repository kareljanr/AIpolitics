# -*- coding: utf-8 -*-
"""Tick 1305 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Pepingen JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
sys.path.insert(0, str(DATA))
from _tick1305_hdr import *  # noqa: F401,F403


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


def patch_entity_notes(path, entity_id, new_notes):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines(keepends=True)
    header = lines[0]
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    found = False
    for i, line in enumerate(lines[1:], start=1):
        if not line.startswith(entity_id + ","):
            continue
        row = next(csv.DictReader([header, line], fieldnames=fields))
        # DictReader with fieldnames uses first data line; rebuild
        parsed = next(csv.reader([line.strip("\n").strip("\r")]))
        row = {fields[j]: (parsed[j] if j < len(parsed) else "") for j in range(len(fields))}
        row["notes"] = new_notes
        ending = "\n" if line.endswith("\n") else ""
        lines[i] = csv_line(fields, row) + ending
        found = True
        break
    if not found:
        raise SystemExit("entity %s not found" % entity_id)
    path.write_bytes("".join(lines).encode("utf-8"))
    return True


print("body follows")

assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((EVA + IGS + OCMW_VER + OTHER_FVA) - FVA) <= 2
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQ) - EQUITY) <= 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) <= 2
assert abs((CUM_PREV + BBR) - CUM_BBR) <= 1
assert abs((AFM + 21985) - GECORR) <= 1
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Pepingen BBC jaarrekening 2025 deel 1.1 (official PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Pepingen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1305; BBC scan PDF 104p / 14.8MB pepingen.be; GR 29.06.2026; "
                "College 08.06.2026; pub Jul 2026; Jnl Budg 349418 Alg 14974; "
                "KBO 0207.512.197/0212.208.086; assets 26871731 AFM 750871 "
                "PnL -471624 fin debt 3467023 pension 2689464"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Gemeenteraad Pepingen 29.06.2026 vaststelling jaarrekening 2025",
            "url": SRC2_URL,
            "publisher": "Gemeente Pepingen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1305; uittreksel GR 29.06.2026 8-7; College 08.06.2026; "
                "AD Leen Deneyer / FD Liesbet Kestens / burgemeester Peter Van Cutsem; not sent FOI"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Pepingen 0207.512.197",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1305; city KBO 0207.512.197 / OCMW 0212.208.086; "
                "seat Ninoofsesteenweg 116 1670; NIS 23064; AD Deneyer / FD Kestens / "
                "burgemeester Van Cutsem"
            ),
        },
    ],
)
print("sources", n)

patch_entity_notes(
    DATA / "entities.csv",
    ENT,
    (
        "tick1305 JR2025 GE residual after AGB 1304 stub; KBO 0207.512.197; NIS 23064; "
        "AD Leen Deneyer / FD Liesbet Kestens / burgemeester Peter Van Cutsem; "
        "assets 26871731 pension 2689464 JUMP fin debt 3467023 PnL -471624; "
        "has AGB (EVA 2500 already 1304); FOI ready"
    ),
)
print("entities city patched")

patch_entity_notes(
    DATA / "entities.csv",
    AGB,
    (
        "tick1304 JR2025 Entity II residual; KBO 0839.927.156; 0 VE; "
        "sportaccommodaties; assets 180707 AFM -3219 PnL -3685 cash 1492 DROP; "
        "fin debt 0; city GE mined 1305; FOI ready"
    ),
)
print("entities agb patched")

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Pepingen",
            "name_fr": "CPAS de Pepingen",
            "name_en": "OCMW Pepingen",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.pepingen.be",
            "foi_email": "info@pepingen.be",
            "foi_postal": "Kerkstraat 2 1670 Pepingen",
            "notes": (
                "tick1305 JR2025 GE residual; KBO 0212.208.086; J3 expl -489839 / "
                "tussenkomst 738928; cash 128901; openstaande leningen 546616; FOI ready"
            ),
        },
    ],
)
print("entities ocmw", n)

bud_rows = [
    ("bud_pepge_assets_2025", "2025", ASSETS, "J4 assets 26871730.96 vs 26966446.46"),
    ("bud_pepge_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 26966446.46"),
    ("bud_pepge_cash_2025", "2025", CASH, "J4/kengetallen cash 3097407.38 vs 3093410.06"),
    ("bud_pepge_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 3093410.06"),
    ("bud_pepge_fva_2025", "2025", FVA, "J4 FVA 3917667.61; EVA 2500 + IGS 2692364 + OCMW-ver 3758 + other 1219046"),
    ("bud_pepge_eva_2025", "2025", EVA, "T5 EVA AGB Pepingen kapitaal 2500 — AGB already mined 1304"),
    ("bud_pepge_igs_2025", "2025", IGS, "J4 IGS FVA 2692363.82"),
    ("bud_pepge_mva_2025", "2025", MVA, "J4 MVA 17696965.28; leasing 691229.16"),
    ("bud_pepge_leasing_2025", "2025", LEASING, "J4 leasing MVA 691229.16 vs 467135.16"),
    ("bud_pepge_iva_2025", "2025", IVA, "J4 IVA 336585.29"),
    ("bud_pepge_equity_2025", "2025", EQUITY, "J4 nettoactief 19420060.36"),
    ("bud_pepge_cap_subs_2025", "2025", CAP_SUBS, "J4 kapitaalsubsidies 3933605.15"),
    ("bud_pepge_cum_pnl_2025", "2025", CUM_PNL, "J4 cum PnL 2666261.73"),
    ("bud_pepge_schulden_2025", "2025", SCHULDEN, "J4 schulden 7451670.60"),
    ("bud_pepge_fin_debt_2025", "2025", FIN_DEBT, "J4 fin debt 3467022.95 (LT 3127590 + ST due 339433) vs 3768536"),
    ("bud_pepge_fin_debt_2024", "2024", FIN_DEBT_2024, "J4 YE2024 fin debt 3768535.67"),
    ("bud_pepge_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4 LT fin debt 3127590.11"),
    ("bud_pepge_fin_debt_st_2025", "2025", FIN_DEBT_ST, "J4 ST due 339432.84"),
    ("bud_pepge_new_loans_2025", "2025", NEW_LOANS, "J2/kengetallen new loans 247078 city"),
    ("bud_pepge_pension_2025", "2025", PENSION, "J4 pension LT 2689464.03 JUMP vs 2067101.13"),
    ("bud_pepge_pension_2024", "2024", PENSION_2024, "J4 YE2024 pension LT 2067101.13"),
    ("bud_pepge_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +1071093"),
    ("bud_pepge_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 8974852"),
    ("bud_pepge_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 7903758"),
    ("bud_pepge_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +1560932 (ontv 7836953 / uitg 6276020)"),
    ("bud_pepge_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -489839 (ontv 1137899 / uitg 1627738)"),
    ("bud_pepge_invest_2025", "2025", INVEST, "J2 invest -941530 vs MJP -2394650"),
    ("bud_pepge_invest_ontv_2025", "2025", INVEST_ONTV, "J2 invest ontv 394243"),
    ("bud_pepge_invest_uitg_2025", "2025", INVEST_UITG, "J2 invest uitg 1335773"),
    ("bud_pepge_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar -98241"),
    ("bud_pepge_cum_bbr_2025", "2025", CUM_BBR, "J2 gecumuleerd BBR 3338441 (prev 3436682)"),
    ("bud_pepge_afm_2025", "2025", AFM, "J2 AFM +750871 (city 539923 / OCMW 210948)"),
    ("bud_pepge_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +772856 (correctie 21985)"),
    ("bud_pepge_pnl_2025", "2025", PNL, "J5 PnL -471624 (ops -902458 / fin +430834)"),
    ("bud_pepge_tussen_2025", "2025", TUSSEN, "kengetallen tussenkomst gemeente-OCMW 738928"),
    ("bud_pepge_pers_2025", "2025", PERS, "J5 bezoldigingen 3670991; VTE unpublished"),
    ("bud_pepge_fiscal_2025", "2025", FISCAL, "J5 fiscale 5193620"),
    ("bud_pepge_agb_bbr_2025", "2025", AGB_BBR, "J2 consol extra AGB BBR 747 — AGB already 1304"),
    ("bud_pepge_agb_afm_2025", "2025", AGB_AFM, "J2 consol extra AGB AFM -3219 — AGB already 1304"),
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
        "comm_pepge_fin_debt_3_47m_2025",
        "Pepingen YE2025 fin debt 3.467m",
        "3467023",
        "J4 3467023 (LT 3127590 + ST due 339433) vs 3768536; new loans 247078 city; periodieke afl 323468; OCMW vervroegde afl 225123",
        "Publish T4 per-loan creditors + amort 2026-2031 FOI",
    ),
    (
        "comm_pepge_pension_2_69m_2025",
        "Pepingen YE2025 pension LT 2.689m JUMP",
        "2689464",
        "J4 pension LT 2689464 vs 2067101 JUMP; city/OCMW split + responsabilisering unpublished",
        "Publish actuarial note + respo city/OCMW split + pad 2026-2031 FOI",
    ),
    (
        "comm_pepge_tussen_0_74m_2025",
        "Pepingen YE2025 OCMW tussenkomst 0.739m",
        "738928",
        "kengetallen tussenkomst 738928; OCMW expl -489839; city expl +1560932; consol PnL -471624 split unpublished",
        "Publish cash vs book + city/OCMW PnL split + pad 2026-2031 FOI",
    ),
    (
        "comm_pepge_igs_2_69m_2025",
        "Pepingen YE2025 IGS FVA 2.692m",
        "2692364",
        "J4 IGS 2692364; EVA AGB 2500 already 1304; OCMW-ver 3758; other FVA 1219046",
        "Publish per-IGS aanschaf vs boekwaarde FOI",
    ),
    (
        "comm_pepge_pers_3_67m_2025",
        "Pepingen 2025 pers 3.671m / VTE unpublished",
        "3670991",
        "J5 bezoldigingen 3670991; VTE unpublished; politiezone/HVZ unpublished in extract",
        "Publish paid VTE city vs OCMW + politie/HVZ FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Pepingen / OCMW / AGB Pepingen",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Pepingen vastgesteld 29.06.2026",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Pepingen",
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
        "lb_pepge_fin_debt_3_47m_2025",
        "Pepingen YE2025 fin debt 3.47m",
        "3467023",
        "6.0",
        "6.0",
        "Publish T4 per-loan creditors + amort 2026-2031",
        "fin debt 3467023 vs 3768536; new loans 247078; OCMW early repay 225123",
    ),
    (
        "lb_pepge_pension_2_69m_2025",
        "Pepingen YE2025 pension LT 2.69m JUMP",
        "2689464",
        "8.0",
        "7.0",
        "Publish actuarial note + respo city/OCMW split + pad 2026-2031",
        "pension LT 2689464 vs 2067101 JUMP; city/OCMW split unpublished",
    ),
    (
        "lb_pepge_tussen_0_74m_2025",
        "Pepingen YE2025 OCMW tussenkomst 0.74m",
        "738928",
        "7.0",
        "6.0",
        "Publish cash vs book + city/OCMW PnL split + pad 2026-2031",
        "tussenkomst 738928; OCMW expl -489839; consol PnL -471624",
    ),
    (
        "lb_pepge_igs_2_69m_2025",
        "Pepingen YE2025 IGS FVA 2.69m",
        "2692364",
        "5.5",
        "6.5",
        "Publish per-IGS aanschaf vs boekwaarde",
        "IGS 2692364; EVA AGB 2500 already 1304; other FVA 1219046",
    ),
    (
        "lb_pepge_pers_3_67m_vte_unpub_2025",
        "Pepingen 2025 pers 3.67m / VTE unpublished",
        "3670991",
        "6.0",
        "6.5",
        "Publish paid VTE city vs OCMW + politie/HVZ",
        "pers 3670991; VTE unpublished; politie/HVZ unpublished in extract",
    ),
    (
        "lb_pepge_pnl_neg_0_47m_2025",
        "Pepingen YE2025 PnL -0.47m NEG",
        "471624",
        "7.0",
        "6.0",
        "Publish city/OCMW PnL split + provision note",
        "PnL -471624 (ops -902458 / fin +430834); BBR year -98241; AFM +750871",
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
            "beneficiaries": "Inwoners Pepingen / OCMW / AGB Pepingen",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Pepingen",
            "measured_outcome": (
                "assets 26871731 / fin debt 3467023 / pension 2689464 JUMP / "
                "PnL -471624 / IGS 2692364 / AFM +750871 / cum BBR 3338441"
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
                "T4 per-loan creditors for fin debt 3467023 (new loans 247078 + "
                "OCMW early repay 225123) + J4 pension LT 2689464 JUMP vs 2067101 "
                "city/OCMW split + responsabilisering + OCMW tussenkomst 738928 vs "
                "expl -489839 + city/OCMW PnL split behind consol -471624 + IGS FVA "
                "2692364 inventory (EVA AGB 2500 already 1304) + VTE vs pers 3670991 "
                "+ politiezone/HVZ unpublished + T2 fiscal split behind 5193620 + "
                "gemeentefonds inside algemene werkingssubsidies 2090913"
            ),
            "why_it_matters": (
                "Unmined leftover city+OCMW Pepingen GE after AGB 1304 left the "
                "city package unmined. Official BBC PDF now downloads on pepingen.be. "
                "Fin debt 3.467m declining. Pension LT 2.689m JUMP. OCMW expl -0.490m "
                "with tussen 0.739m. Consol PnL -0.472m. AFM +0.751m / cum BBR 3.338m. "
                "Politie/VTE unpublished in extract."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Pepingen (gemeente + OCMW)",
            "recipient_email": "info@pepingen.be",
            "recipient_postal": "Ninoofsesteenweg 116 1670 Pepingen",
            "draft_letter_path": "docs/doge/foi/drafts/gap_pepge_fin_debt_3_47m_pension_2_69m_ocmw_tussen_0_74m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_pepge_fin_debt_3_47m_2025",
            "linked_leaderboard_id": "lb_pepge_fin_debt_3_47m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1305",
    "title": "Stad+OCMW Pepingen JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Pepingen JR2025 BBC scan + GR + KBO; "
        "KBO 0207.512.197 / 0212.208.086; assets 26871731 / fin debt 3467023 / "
        "pension 2689464 JUMP / PnL -471624 / IGS 2692364 / AFM +750871; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T14:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1305 Stad+OCMW Pepingen JR2025 GE residual; KBO 0207.512.197/0212.208.086; "
        "assets 26871731 fin debt 3467023 pension 2689464 JUMP PnL -471624 "
        "IGS 2692364 AFM +750871 gecorr +772856 BBR -98241 cum 3338441 cash 3097407 "
        "tussen 738928 pers 3670991 new loans 247078; AGB EVA 2500 already 1304; "
        "FOI ready not sent; next rq_1306 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1306",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1305 done including Stad+OCMW Pepingen 1305 / AGB Pepingen 1304 / "
        "Stad+OCMW Edegem 1303 / Stad+OCMW Wommelgem 1302 / Stad+OCMW Zonhoven 1301 / "
        "Stad+OCMW Kortenaken 1300 / AGB Kortenaken 1299); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined city Pepingen 1305 / AGB Pepingen 1304 / city Edegem 1303 / "
        "AGB Edegem 1239 / city Wommelgem 1302 / city Zonhoven 1301 / city Kortenaken 1300 / "
        "AGB Kortenaken 1299 / city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / "
        "city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / "
        "Deerlijk 981 / Zonnebeke 963 / AGB MMP1917 964 / Lochristi 927 / Tervuren 1226 / "
        "AGB Bexit 1225; leftover Maarkedal/Meulebeke still unmined — take only if PDF fetches; "
        "Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem still no PDF; "
        "Vleteren JR2025 PDF was live on vleteren.be — take only if still downloads; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "skip AGB Kapellen / Nieuwerkerken 1102 already mined; "
        "skip AGB Sport Hulshout JR2024-only; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1305 after Stad+OCMW Pepingen JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1305", rq_new, rq_spawn)
print("research_queue 1305", found, "spawned_1306", spawned)

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
            "last_unit_id": "rq_1305",
            "ticks_completed": "1305",
            "paused": "no",
            "notes": (
                "tick1305 Stad+OCMW Pepingen JR2025 GE residual; KBO 0207.512.197/0212.208.086; "
                "assets 26871731 fin debt 3467023 pension 2689464 JUMP PnL -471624; "
                "FOI ready; next rq_1306 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1305_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
