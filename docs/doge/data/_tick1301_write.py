# -*- coding: utf-8 -*-
"""Tick 1301 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Zonhoven JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
UTC = "2026-08-17T15:30:00Z"
TICK = 1301
SRC = "src_znhv_jr2025_bbc"
SRC2 = "src_kbo_znhv_0207471221"
ENT = "city_zonhoven"
OCMW = "ocmw_zonhoven"
SRC_URL = "https://www.zonhoven.be/rapport-jaarrekening-2025"
SRC2_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207471221"
GAP = "gap_znhv_tussen_3_70m_politie_3_18m_igs_28_66m_l5"
HIER = "Vlaanderen>Gemeenten>Zonhoven"

ASSETS = 131804307
ASSETS_2024 = 125991416
CASH = 17571861
CASH_2024 = 17180201
CURRENT = 29047622
FIXED = 102756685
FVA = 31278074
EVA = 0
IGS = 28664104
OTHER_FVA = 2613969
MVA = 70733787
LEASING = 2050910
IVA = 562356
LT_RECV = 182469
SCHULDEN = 13942805
EQUITY = 117861502
CAP_SUBS = 6052173
CUM_PNL = 66263769
REVAL = 10930
OTHER_EQ = 45534630
FIN_DEBT = 2107093
FIN_DEBT_LT = 1716668
FIN_DEBT_ST = 390425
FIN_DEBT_2024 = 1981574
NEW_LOANS = 559448
PENSION = 1638259
PENSION_2024 = 1589966
EXPL = 6493674
EXPL_ONTV = 36830487
EXPL_UITG = 30336813
CITY_EXPL = 8158361
OCMW_EXPL = -1664688
INVEST = -6605687
INVEST_UITG = 7202987
INVEST_ONTV = 597300
BBR = 13506
CUM_PREV = 19773926
AVAIL = 16638411
AFM = 6059745
GECORR = 6335148
AFL = 433929
PNL = 4482626
CITY_PNL = 6131714
OCMW_PNL = -1649088
TUSSEN = 3700000
PERS = 16730063
FISCAL = 19812547
OV = 8234199
APB = 10347910
GEMFONDS = 5531416
POLITIE = 3177093
HVZ = 1103029
OCMW_EQUITY = 7168024
OCMW_CUM = 2499506


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
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) <= 2
assert abs((EVA + IGS + OTHER_FVA) - FVA) <= 2
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) <= 2
assert abs((CUM_PREV + BBR) - 19787432) <= 1
assert abs((19787432 - 3149021) - AVAIL) <= 1
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) <= 1
assert abs((CITY_PNL + OCMW_PNL) - PNL) <= 1
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Zonhoven BBC jaarrekening 2025 (PDF 390p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Zonhoven",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1301; 12.08MB BBC PDF zonhoven.be rapport-jaarrekening-2025; "
                "vastgesteld 29.06.2026 pub 03.07.2026; KBO 0207.471.221/0212.187.104; "
                "assets 131.804m fin debt 2.107m tussen 3.700m politie 3.177m IGS 28.664m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "KBO Gemeente Zonhoven 0207.471.221",
            "url": SRC2_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1301; city KBO 0207.471.221 / OCMW 0212.187.104; seat Kerkplein 1 3520; "
                "OCMW Kerkplein 60 3520; NIS 71066; AD Telen / FD Mommen / burgemeester De Raeve"
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
            "name_nl": "Gemeente Zonhoven",
            "name_fr": "Commune de Zonhoven",
            "name_en": "Municipality of Zonhoven",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.zonhoven.be",
            "foi_email": "info@zonhoven.be",
            "foi_postal": "Kerkplein 1 3520 Zonhoven",
            "notes": (
                "tick1301 JR2025 GE residual; KBO 0207.471.221; NIS 71066; "
                "AD Bart Telen / FD Stijn Mommen / burgemeester Bram De Raeve; "
                "assets 131.804m fin debt 2.107m tussen 3.700m politie 3.177m IGS 28.664m; "
                "no AGB (EVA 0); FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Zonhoven",
            "name_fr": "CPAS de Zonhoven",
            "name_en": "OCMW Zonhoven",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.zonhoven.be",
            "foi_email": "info@zonhoven.be",
            "foi_postal": "Kerkplein 60 3520 Zonhoven",
            "notes": (
                "tick1301 JR2025 GE residual; KBO 0212.187.104; J3 expl -1.665m / "
                "T5 PnL -1.649m / cum +2.500m / equity +7.168m; tussenkomst 3.700m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_znhv_assets_2025", "2025", ASSETS, "J4 assets 131.804307m vs 125.991416m"),
    ("bud_znhv_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 125.991416m"),
    ("bud_znhv_cash_2025", "2025", CASH, "J4 cash+beleg 17.571861m vs 17.180201m"),
    ("bud_znhv_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 17.180201m"),
    ("bud_znhv_fva_2025", "2025", FVA, "T5 FVA 31.278074m; EVA 0 + IGS 28.664m + other 2.614m"),
    ("bud_znhv_eva_2025", "2025", EVA, "T5 EVA AGB kapitaal 0 — no AGB Zonhoven"),
    ("bud_znhv_igs_2025", "2025", IGS, "T5 IGS FVA 28.664104m vs 28.644971m (+19.134 overboeking)"),
    ("bud_znhv_mva_2025", "2025", MVA, "J4/T5 MVA 70.733787m; leasing 2.050910m"),
    ("bud_znhv_leasing_2025", "2025", LEASING, "T5 leasing MVA 2.050910m (aankoop 0.559m)"),
    ("bud_znhv_iva_2025", "2025", IVA, "J4/T5 IVA 0.562356m"),
    ("bud_znhv_equity_2025", "2025", EQUITY, "J4 nettoactief 117.861502m vs 111.920210m"),
    ("bud_znhv_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL 66.263769m (city 63.764 / OCMW 2.500)"),
    ("bud_znhv_reval_2025", "2025", REVAL, "J4 herwaarderingsreserves 0.010930m frozen"),
    ("bud_znhv_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 2.107093m (LT 1.717 + ST due 0.390)"),
    ("bud_znhv_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 1.981574m"),
    ("bud_znhv_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin debt 1.716668m"),
    ("bud_znhv_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4/J4 ST due 0.390425m"),
    ("bud_znhv_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.559448m leasing; no new bank"),
    ("bud_znhv_pension_2025", "2025", PENSION, "J4 pension LT 1.638259m vs 1.589966m"),
    ("bud_znhv_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +6.493674m"),
    ("bud_znhv_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 36.830487m"),
    ("bud_znhv_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 30.336813m"),
    ("bud_znhv_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +8.158361m (ontv 31.062 / uitg 22.904)"),
    ("bud_znhv_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -1.664688m (ontv 5.769 / uitg 7.433)"),
    ("bud_znhv_invest_2025", "2025", INVEST, "J2 invest -6.605687m vs MJP -9.027m"),
    ("bud_znhv_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +0.013506m"),
    ("bud_znhv_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 16.638411m"),
    ("bud_znhv_afm_2025", "2025", AFM, "J2 AFM +6.059745m"),
    ("bud_znhv_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +6.335148m"),
    ("bud_znhv_pnl_2025", "2025", PNL, "J5 PnL +4.482626m; city +6.132 / OCMW -1.649; tussen 3.700m"),
    ("bud_znhv_tussen_2025", "2025", TUSSEN, "T5/3.13 tussenkomst gemeente-OCMW 3.700000m"),
    ("bud_znhv_pers_2025", "2025", PERS, "J5/T2 bezoldigingen 16.730063m; VTE unpublished"),
    ("bud_znhv_fiscal_2025", "2025", FISCAL, "J5/T2 fiscale 19.812547m (OV 8.234 + APB 10.348)"),
    ("bud_znhv_ov_2025", "2025", OV, "T2 OV 8.234199m"),
    ("bud_znhv_apb_2025", "2025", APB, "T2 APB 10.347910m JUMP vs 8.940m"),
    ("bud_znhv_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 5.531416m"),
    ("bud_znhv_politie_2025", "2025", POLITIE, "T2 PZ Limburg Regio Hoofdstad 3.177093m"),
    ("bud_znhv_hvz_2025", "2025", HVZ, "T2 HVZ Zuid-West Limburg 1.103029m"),
    ("bud_znhv_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity +7.168024m"),
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
        "comm_znhv_tussen_3_70m_2025",
        "Zonhoven YE2025 OCMW tussenkomst 3.700m",
        "3700000",
        "T5/3.13 tussenkomst 3.700000m (netto geldbewegingen gemeente-OCMW); OCMW expl -1.665m / PnL -1.649m / equity +7.168m",
        "Publish cash vs resultaatstoewijzing + pad 2026-2031 FOI",
    ),
    (
        "comm_znhv_politie_3_18m_2025",
        "Zonhoven 2025 PZ Limburg Regio Hoofdstad 3.177m",
        "3177093",
        "T2 PZ LRH 3.177093m; 2026 pad 3.270817m; HVZ Zuid-West Limburg 1.103029m",
        "Publish 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_znhv_igs_28_66m_2025",
        "Zonhoven YE2025 IGS FVA 28.664m",
        "28664104",
        "T5 IGS 28.664104m vs 28.644971m (+19.134); EVA 0; Fluvius/Nuhma dividend dependency; no 2025 reval",
        "Publish per-IGS aanschaf vs boekwaarde FOI",
    ),
    (
        "comm_znhv_fin_debt_2_11m_2025",
        "Zonhoven YE2025 fin debt 2.107m",
        "2107093",
        "T4 2.107093m (LT 1.717 + ST due 0.390) vs 1.982m; new loans 0.559m leasing",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_znhv_avail_16_64m_2025",
        "Zonhoven YE2025 avail BBR 16.638m",
        "16638411",
        "avail 16.638411m; BBR year +0.013506m; AFM +6.060m; cash 17.572m",
        "Publish uncommitted overschot vs 2e pijler/BOA lock FOI",
    ),
    (
        "comm_znhv_pers_16_73m_2025",
        "Zonhoven 2025 pers 16.730m / VTE unpublished",
        "16730063",
        "pers 16.730063m; VTE unpublished; politiek 0.714 / vast 3.361 / niet-vast 11.601",
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
            "beneficiary": "Inwoners Zonhoven / OCMW / PZ LRH / HVZ Zuid-West Limburg",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Zonhoven vastgesteld 29.06.2026",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Zonhoven",
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
        "lb_znhv_tussen_3_70m_2025",
        "Zonhoven YE2025 OCMW tussenkomst 3.70m",
        "3700000",
        "7.0",
        "6.0",
        "Publish cash vs resultaatstoewijzing + pad 2026-2031",
        "tussenkomst 3.700m; OCMW expl -1.665m / PnL -1.649m / equity +7.168m",
    ),
    (
        "lb_znhv_politie_3_18m_2025",
        "Zonhoven 2025 PZ Limburg Regio Hoofdstad 3.18m",
        "3177093",
        "6.5",
        "6.5",
        "Publish 2026-2031 verdeelsleutel",
        "PZ LRH 3.177m; 2026 pad 3.271m; HVZ Zuid-West Limburg 1.103m",
    ),
    (
        "lb_znhv_igs_28_66m_2025",
        "Zonhoven YE2025 IGS FVA 28.66m",
        "28664104",
        "5.5",
        "8.0",
        "Publish per-IGS aanschaf vs boekwaarde",
        "IGS 28.664m; EVA 0; no 2025 Fluvius reval; Fluvius/Nuhma dividend dependency",
    ),
    (
        "lb_znhv_fin_debt_2_11m_2025",
        "Zonhoven YE2025 fin debt 2.11m",
        "2107093",
        "5.0",
        "5.0",
        "Publish per-loan amort 2026-2031",
        "fin debt 2.107m vs 1.982m; new loans 0.559m leasing only",
    ),
    (
        "lb_znhv_avail_16_64m_2025",
        "Zonhoven YE2025 avail BBR 16.64m",
        "16638411",
        "5.0",
        "7.5",
        "Publish uncommitted overschot vs 2e pijler/BOA lock",
        "avail 16.638m; BBR year +0.014m; AFM +6.060m; cash 17.572m",
    ),
    (
        "lb_znhv_pers_16_73m_vte_unpub_2025",
        "Zonhoven 2025 pers 16.73m / VTE unpublished",
        "16730063",
        "6.0",
        "7.5",
        "Publish paid VTE city vs OCMW",
        "pers 16.730m; VTE unpublished; niet-vast 11.601m",
    ),
    (
        "lb_znhv_invest_gap_6_61m_2025",
        "Zonhoven 2025 invest -6.61m vs MJP -9.03m",
        "6605687",
        "5.5",
        "6.5",
        "Publish unrealised 2025 project list + 2026 carry",
        "invest -6.606m (uitg 7.203 vs MJP 14.017); wegennet/riolering carry",
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
            "beneficiaries": "Inwoners Zonhoven / OCMW / PZ LRH / HVZ Zuid-West Limburg",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Zonhoven",
            "measured_outcome": (
                "assets 131.804m / fin debt 2.107m / tussen 3.700m / "
                "politie 3.177m / IGS 28.664m / AFM +6.060m / avail 16.638m"
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
                "T4/LT-S per-loan creditors for fin debt 2.107093m (new loans 0.559448 "
                "leasing only) + IGS FVA 28.664104 inventory (EVA 0; +19.134 overboeking) "
                "+ OCMW tussenkomst 3.700000 vs expl -1.664688 / PnL -1.649088 / "
                "equity +7.168024 + VTE vs pers 16.730063 + politiezone LRH "
                "3.177093 / HVZ Zuid-West Limburg 1.103029 pad"
            ),
            "why_it_matters": (
                "Unmined city+OCMW Zonhoven GE after leftover-city hunt found a live 390p PDF. "
                "No AGB (EVA 0). Fin debt 2.107m; new loans 0.559m leasing. "
                "Tussenkomst 3.700m. IGS 28.664m no per-entity inventory. "
                "Avail 16.638m with BBR year +0.014m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Zonhoven (gemeente + OCMW)",
            "recipient_email": "info@zonhoven.be",
            "recipient_postal": "Kerkplein 1 3520 Zonhoven",
            "draft_letter_path": "docs/doge/foi/drafts/gap_znhv_tussen_3_70m_politie_3_18m_igs_28_66m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_znhv_tussen_3_70m_2025",
            "linked_leaderboard_id": "lb_znhv_tussen_3_70m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1301",
    "title": "Stad+OCMW Zonhoven JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Zonhoven JR2025 BBC text + KBO; "
        "KBO 0207.471.221 / 0212.187.104; assets 131.804m / fin debt 2.107m / "
        "tussen 3.700m / politie 3.177m / IGS 28.664m / AFM +6.060m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T14:15:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1301 Stad+OCMW Zonhoven JR2025 GE residual; KBO 0207.471.221/0212.187.104; "
        "assets 131.804m fin debt 2.107m tussen 3.700m politie 3.177m IGS 28.664m "
        "AFM +6.060m gecorr +6.335m BBR +0.014m avail 16.638m cash 17.572m "
        "OCMW equity +7.168m pers 16.730m new loans 0.559m leasing; no AGB EVA 0; "
        "FOI ready not sent; next rq_1302 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1302",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1301 done including Stad+OCMW Zonhoven 1301 / Stad+OCMW Kortenaken 1300 / "
        "AGB Kortenaken 1299 / Stad+OCMW Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / "
        "Stad+OCMW Diepenbeek 1297 / AGB Diepenbeek 1296); prefer other unmined AGB/zorg/EVA "
        "with direct PDF/NBB/city HTML; "
        "skip already-mined city Zonhoven 1301 / city Kortenaken 1300 / AGB Kortenaken 1299 / "
        "city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / "
        "AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / Oud-Heverlee 1293 / "
        "Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / "
        "Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Pepingen/Zwalm/Wortegem-Petegem "
        "city+OCMW JR2025 only if PDF fetches; "
        "AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "skip AGB Kapellen / APB Mercator / Nieuwerkerken 1102 already mined; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1301 after Stad+OCMW Zonhoven JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1301", rq_new, rq_spawn)
print("research_queue 1301", found, "spawned_1302", spawned)

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
            "last_unit_id": "rq_1301",
            "ticks_completed": "1301",
            "paused": "no",
            "notes": (
                "tick1301 Stad+OCMW Zonhoven JR2025 GE residual; KBO 0207.471.221/0212.187.104; "
                "assets 131.804m fin debt 2.107m tussen 3.700m politie 3.177m IGS 28.664m; "
                "FOI ready; next rq_1302 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1301_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
