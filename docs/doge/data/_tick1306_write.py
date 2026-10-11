# -*- coding: utf-8 -*-
"""Tick 1306 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Vleteren JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
sys.path.insert(0, str(DATA))
from _tick1306_hdr import *  # noqa: F401,F403


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


print("body follows")

assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((EVA + IGS + OCMW_VER + OTHER_FVA) - FVA) <= 2
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((CAP_SUBS + CUM_PNL + HERW + OTHER_EQ) - EQUITY) <= 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) <= 2
assert abs((CUM_PREV + BBR) - CUM_BBR) <= 1
assert abs((AFM + 402779) - GECORR) <= 1
assert abs((CITY_PNL + OCMW_PNL) - PNL) <= 1
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Vleteren BBC jaarrekening 2025 (official PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Vleteren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1306; BBC text PDF 95p / 4.74MB vleteren.be; pub 16.06.2026; "
                "print 25.05.2026; Jnl Budg 260541 Alg 16570; "
                "KBO 0216.770.452/0216.770.551; assets 25154213 AFM 949439 "
                "PnL -621430 fin debt 3323559 pension 825138 JUMP"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Jaarrekeningen Gemeente en OCMW Vleteren (official page)",
            "url": SRC_PAGE,
            "publisher": "Gemeente Vleteren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1306; official page lists JR2025 gepubliceerd 16/06/2026; "
                "AD Nele Vanderhaeghe / FD Joost Sampers / burgemeester Bram Coppein; not sent FOI"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Vleteren 0216.770.452",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1306; city KBO 0216.770.452 / OCMW 0216.770.551; "
                "seat Veurnestraat 4 / 4A 8640; NIS 33041; AD Vanderhaeghe / FD Sampers / "
                "burgemeester Coppein / OCMW-voorzitter Gouwy"
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
            "name_nl": "Gemeente Vleteren",
            "name_fr": "Commune de Vleteren",
            "name_en": "Municipality of Vleteren",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.vleteren.be",
            "foi_email": "info@vleteren.be",
            "foi_postal": "Veurnestraat 4 8640 Vleteren",
            "notes": (
                "tick1306 JR2025 GE residual; KBO 0216.770.452; NIS 33041; "
                "AD Nele Vanderhaeghe / FD Joost Sampers / burgemeester Bram Coppein; "
                "assets 25154213 pension 825138 JUMP fin debt 3323559 PnL -621430; "
                "no AGB (EVA 0); FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Vleteren",
            "name_fr": "CPAS de Vleteren",
            "name_en": "OCMW Vleteren",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.vleteren.be",
            "foi_email": "info@vleteren.be",
            "foi_postal": "Veurnestraat 4A 8640 Vleteren",
            "notes": (
                "tick1306 JR2025 GE residual; KBO 0216.770.551; voorzitter Patrick Gouwy; "
                "J3 expl -51374 / T5 PnL -401541 / cum -262503 NEG / equity 4045091; "
                "tussenkomst 0; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_vlet_assets_2025", "2025", ASSETS, "J4 assets 25154213 vs 25411712"),
    ("bud_vlet_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 25411712"),
    ("bud_vlet_cash_2025", "2025", CASH, "J4 cash 1679443 vs 1731235 DROP"),
    ("bud_vlet_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 1731235"),
    ("bud_vlet_fva_2025", "2025", FVA, "J4 FVA 3638582; EVA 0 + IGS 1983012 + other 1655569"),
    ("bud_vlet_eva_2025", "2025", EVA, "T5 EVA 0 — no AGB"),
    ("bud_vlet_igs_2025", "2025", IGS, "J4/T5 IGS FVA 1983012; reval +39852"),
    ("bud_vlet_mva_2025", "2025", MVA, "J4 MVA 19278543; leasing 278528"),
    ("bud_vlet_leasing_2025", "2025", LEASING, "J4 leasing MVA 278528 vs 248532"),
    ("bud_vlet_iva_2025", "2025", IVA, "T5 IVA 0"),
    ("bud_vlet_equity_2025", "2025", EQUITY, "J4 nettoactief 20248190"),
    ("bud_vlet_cap_subs_2025", "2025", CAP_SUBS, "J4 kapitaalsubsidies 3077678"),
    ("bud_vlet_cum_pnl_2025", "2025", CUM_PNL, "J4 cum PnL 3115125"),
    ("bud_vlet_schulden_2025", "2025", SCHULDEN, "J4 schulden 4906022"),
    ("bud_vlet_fin_debt_2025", "2025", FIN_DEBT, "J4/T4 fin debt 3323559 (LT 2606571 + ST due 716988) vs 3986228"),
    ("bud_vlet_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 3986228"),
    ("bud_vlet_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4 LT fin debt 2606571"),
    ("bud_vlet_fin_debt_st_2025", "2025", FIN_DEBT_ST, "J4 ST due 716988"),
    ("bud_vlet_new_loans_2025", "2025", NEW_LOANS, "T2/T4 new loans 59007 leasing only; bank 0"),
    ("bud_vlet_pension_2025", "2025", PENSION, "J4 pension LT 825138 JUMP vs 0"),
    ("bud_vlet_pension_2024", "2024", PENSION_2024, "J4 YE2024 pension LT 0"),
    ("bud_vlet_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +1669971"),
    ("bud_vlet_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 6273917"),
    ("bud_vlet_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 4603946"),
    ("bud_vlet_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +1721346 (ontv 5572150 / uitg 3850804)"),
    ("bud_vlet_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -51374 (ontv 701767 / uitg 753141)"),
    ("bud_vlet_invest_2025", "2025", INVEST, "J2 invest -668624 vs MJP -1203785"),
    ("bud_vlet_invest_ontv_2025", "2025", INVEST_ONTV, "J2 invest ontv 634708"),
    ("bud_vlet_invest_uitg_2025", "2025", INVEST_UITG, "J2 invest uitg 1303331"),
    ("bud_vlet_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +91990"),
    ("bud_vlet_cum_bbr_2025", "2025", CUM_BBR, "J2 gecumuleerd BBR 1490732 (prev 1398742)"),
    ("bud_vlet_afm_2025", "2025", AFM, "J2 AFM +949439"),
    ("bud_vlet_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +1352218 (correctie 402779)"),
    ("bud_vlet_pnl_2025", "2025", PNL, "J5 PnL -621430 (city -219889 / OCMW -401541)"),
    ("bud_vlet_tussen_2025", "2025", TUSSEN, "T5 tussenkomst gemeente-OCMW 0"),
    ("bud_vlet_pers_2025", "2025", PERS, "J5/T2 bezoldigingen 2320878; VTE unpublished"),
    ("bud_vlet_fiscal_2025", "2025", FISCAL, "T2 fiscale 3220418 (OV 1631870 + APB 1131034)"),
    ("bud_vlet_politie_2025", "2025", POLITIE, "T2 politiezone 263004 + invest 31122; name unpublished"),
    ("bud_vlet_hvz_2025", "2025", HVZ, "T2 HVZ Westhoek 136924 + invest 29494"),
    ("bud_vlet_ocmw_pnl_2025", "2025", OCMW_PNL, "T5 OCMW PnL -401541 / cum -262503 NEG / equity 4045091"),
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
        "comm_vlet_fin_debt_3_32m_2025",
        "Vleteren YE2025 fin debt 3.324m",
        "3323559",
        "J4/T4 3323559 (LT 2606571 + ST due 716988) vs 3986228; new loans 59007 leasing; periodieke afl 721677; kerkfabriek doorgeef 247833",
        "Publish T4 per-loan creditors + amort 2026-2031 FOI",
    ),
    (
        "comm_vlet_pension_0_83m_2025",
        "Vleteren YE2025 pension LT 0.825m JUMP",
        "825138",
        "J4 pension LT 825138 vs 0 JUMP; city/OCMW split + responsabilisering unpublished",
        "Publish actuarial note + respo city/OCMW split + pad 2026-2031 FOI",
    ),
    (
        "comm_vlet_ocmw_pnl_neg_0_40m_2025",
        "Vleteren YE2025 OCMW PnL -0.402m / tussen 0",
        "401541",
        "T5 OCMW PnL -401541 / cum -262503 NEG / equity 4045091; tussenkomst 0; OCMW expl -51374; consol PnL -621430",
        "Publish cash vs book + why tussen 0 with OCMW PnL -401541 FOI",
    ),
    (
        "comm_vlet_igs_1_98m_2025",
        "Vleteren YE2025 IGS FVA 1.983m",
        "1983012",
        "J4/T5 IGS 1983012; reval +39852; EVA 0; other FVA 1655569",
        "Publish per-IGS aanschaf vs boekwaarde FOI",
    ),
    (
        "comm_vlet_pers_2_32m_2025",
        "Vleteren 2025 pers 2.321m / VTE unpublished",
        "2320878",
        "J5/T2 bezoldigingen 2320878; VTE unpublished; politie 263004 name unpublished; HVZ Westhoek 136924",
        "Publish paid VTE city vs OCMW + politiezone name FOI",
    ),
    (
        "comm_vlet_politie_0_26m_2025",
        "Vleteren 2025 politiezone 0.263m",
        "263004",
        "T2 politiezone 263004 + invest 31122; HVZ Westhoek 136924 + invest 29494; zone name unpublished",
        "Publish politiezone name + 2026-2031 verdeelsleutel FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Vleteren / OCMW Vleteren",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Vleteren gepubliceerd 16.06.2026",
            "decision_date": "2026-06-16",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Vleteren",
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
        "lb_vlet_fin_debt_3_32m_2025",
        "Vleteren YE2025 fin debt 3.32m",
        "3323559",
        "6.0",
        "6.0",
        "Publish T4 per-loan creditors + amort 2026-2031",
        "fin debt 3323559 vs 3986228; new loans 59007 leasing; afl 721677",
    ),
    (
        "lb_vlet_pension_0_83m_2025",
        "Vleteren YE2025 pension LT 0.83m JUMP",
        "825138",
        "8.0",
        "6.5",
        "Publish actuarial note + respo city/OCMW split + pad 2026-2031",
        "pension LT 825138 vs 0 JUMP; city/OCMW split unpublished",
    ),
    (
        "lb_vlet_ocmw_pnl_neg_0_40m_2025",
        "Vleteren YE2025 OCMW PnL -0.40m / tussen 0",
        "401541",
        "7.0",
        "6.0",
        "Publish why tussen 0 with OCMW PnL -401541 / cum -262503 NEG",
        "OCMW PnL -401541 / cum -262503 NEG; tussenkomst 0; consol PnL -621430",
    ),
    (
        "lb_vlet_igs_1_98m_2025",
        "Vleteren YE2025 IGS FVA 1.98m",
        "1983012",
        "5.5",
        "6.0",
        "Publish per-IGS aanschaf vs boekwaarde",
        "IGS 1983012; reval +39852; EVA 0; other FVA 1655569",
    ),
    (
        "lb_vlet_pers_2_32m_vte_unpub_2025",
        "Vleteren 2025 pers 2.32m / VTE unpublished",
        "2320878",
        "6.0",
        "6.0",
        "Publish paid VTE city vs OCMW + politiezone name",
        "pers 2320878; VTE unpublished; politie 263004 name unpublished",
    ),
    (
        "lb_vlet_pnl_neg_0_62m_2025",
        "Vleteren YE2025 PnL -0.62m NEG",
        "621430",
        "7.0",
        "6.0",
        "Publish city/OCMW PnL split + pension provision note",
        "PnL -621430 (ops -758508 / fin +137078); BBR year +91990; AFM +949439",
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
            "beneficiaries": "Inwoners Vleteren / OCMW Vleteren",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Vleteren",
            "measured_outcome": (
                "assets 25154213 / fin debt 3323559 / pension 825138 JUMP / "
                "PnL -621430 / IGS 1983012 / AFM +949439 / cum BBR 1490732"
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
                "T4 per-loan creditors for fin debt 3323559 (new loans 59007 leasing; "
                "kerkfabriek doorgeef 247833) + J4 pension LT 825138 JUMP vs 0 "
                "city/OCMW split + responsabilisering + OCMW tussenkomst 0 vs "
                "expl -51374 / PnL -401541 / cum -262503 NEG + IGS FVA 1983012 "
                "inventory (reval +39852; EVA 0) + other FVA 1655569 + VTE vs pers "
                "2320878 + politiezone name behind 263004 / HVZ Westhoek 136924 pad "
                "+ GR vaststellingsdatum (pub 16.06.2026)"
            ),
            "why_it_matters": (
                "Unmined leftover city+OCMW Vleteren GE after tick 1305 found the "
                "live PDF. Official BBC now downloads on vleteren.be. No AGB (EVA 0). "
                "Fin debt 3.324m declining. Pension LT 0.825m JUMP from 0. OCMW PnL "
                "-0.402m / cum -0.263m NEG with tussenkomst 0. Consol PnL -0.621m. "
                "AFM +0.949m / cum BBR 1.491m. VTE/politiezone-naam unpublished."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Vleteren (gemeente + OCMW)",
            "recipient_email": "info@vleteren.be",
            "recipient_postal": "Veurnestraat 4 8640 Vleteren",
            "draft_letter_path": "docs/doge/foi/drafts/gap_vlet_fin_debt_3_32m_pension_0_83m_ocmw_pnl_neg_0_40m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_vlet_fin_debt_3_32m_2025",
            "linked_leaderboard_id": "lb_vlet_fin_debt_3_32m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1306",
    "title": "Stad+OCMW Vleteren JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Vleteren JR2025 BBC text + KBO; "
        "KBO 0216.770.452 / 0216.770.551; assets 25154213 / fin debt 3323559 / "
        "pension 825138 JUMP / PnL -621430 / IGS 1983012 / AFM +949439; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T14:45:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1306 Stad+OCMW Vleteren JR2025 GE residual; KBO 0216.770.452/0216.770.551; "
        "assets 25154213 fin debt 3323559 pension 825138 JUMP PnL -621430 "
        "IGS 1983012 AFM +949439 gecorr +1352218 BBR +91990 cum 1490732 cash 1679443 "
        "tussen 0 pers 2320878 new loans 59007 leasing; no AGB EVA 0; "
        "FOI ready not sent; next rq_1307 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1307",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1306 done including Stad+OCMW Vleteren 1306 / Stad+OCMW Pepingen 1305 / "
        "AGB Pepingen 1304 / Stad+OCMW Edegem 1303 / Stad+OCMW Wommelgem 1302 / "
        "Stad+OCMW Zonhoven 1301 / Stad+OCMW Kortenaken 1300 / AGB Kortenaken 1299); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined city Vleteren 1306 / city Pepingen 1305 / AGB Pepingen 1304 / "
        "city Edegem 1303 / AGB Edegem 1239 / city Wommelgem 1302 / city Zonhoven 1301 / "
        "city Kortenaken 1300 / AGB Kortenaken 1299 / city Steenokkerzeel 1298 / "
        "AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / AGB Diepenbeek 1296 / "
        "Voeren 1295 / Heusden-Zolder 1294 / Deerlijk 981 / Zonnebeke 963 / "
        "AGB MMP1917 964 / Lochristi 927 / Tervuren 1226 / AGB Bexit 1225; "
        "leftover Maarkedal/Meulebeke still unmined — take only if PDF fetches; "
        "Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem still no PDF; "
        "AGB Kinrooi / AGB Vilvoorde — take only if unmined and PDF downloads; "
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
    "notes": "spawned tick1306 after Stad+OCMW Vleteren JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1306", rq_new, rq_spawn)
print("research_queue 1306", found, "spawned_1307", spawned)

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
            "last_unit_id": "rq_1306",
            "ticks_completed": "1306",
            "paused": "no",
            "notes": (
                "tick1306 Stad+OCMW Vleteren JR2025 GE residual; KBO 0216.770.452/0216.770.551; "
                "assets 25154213 fin debt 3323559 pension 825138 JUMP PnL -621430; "
                "FOI ready; next rq_1307 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1306_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
