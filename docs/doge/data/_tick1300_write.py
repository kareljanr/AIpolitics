# -*- coding: utf-8 -*-
"""Tick 1300 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Kortenaken JR2025 GE residual + every-10 progress."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T14:15:00Z"
TICK = 1300
SRC = "src_ktnk_jr2025_bbc"
SRC2 = "src_ktnk_jr2025_eval"
SRC3 = "src_kbo_ktnk_0207520711"
ENT = "city_kortenaken"
OCMW = "ocmw_kortenaken"
SRC_URL = "https://www.kortenaken.be/sites/default/files/2026-06/2025-Jaarrekening-LB-Kortenaken-Financiele-Nota-Toelichtingen-Documentatie-DEF.pdf"
SRC2_URL = "https://www.kortenaken.be/sites/default/files/2026-06/LB-2025-beleidsevaluatie-2025_20260527-DEF.pdf"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207520711"
GAP = "gap_ktnk_fin_debt_10_57m_igs_reval_8_90m_ocmw_equity_neg_5_41m_l5"
HIER = "Vlaanderen>Gemeenten>Kortenaken"

ASSETS = 62278271
ASSETS_2024 = 52966330
CASH = 11104602
CASH_2024 = 9915599
CURRENT = 13890946
FIXED = 48387326
FVA = 15034032
EVA = 25000
IGS = 14973101
IGS_REVAL = 8897132
OTHER_FVA = 35931
MVA = 28053996
LEASING = 960766
IVA = 579293
LT_RECV = 4720006
SCHULDEN = 17416762
EQUITY = 44861510
CAP_SUBS = 3071476
CUM_PNL = -1871840
REVAL = 8903034
OTHER_EQ = 34758840
FIN_DEBT = 10567781
FIN_DEBT_LT = 9730409
FIN_DEBT_ST = 837371
FIN_DEBT_2024 = 11402363
NEW_LOANS = 11389
PENSION = 4982275
PENSION_2024 = 4988429
EXPL = 2327713
EXPL_ONTV = 14975310
EXPL_UITG = 12647597
CITY_EXPL = 3377688
OCMW_EXPL = -1049974
INVEST = -217688
INVEST_UITG = 1225806
INVEST_ONTV = 1008118
BBR = 1405505
CUM_PREV = 11162217
AVAIL = 10480008
AFM = 1559190
GECORR = 1465145
AFL = 818145
AANGEWEZEN = 912189
PNL = 658102
CITY_PNL = 1815497
OCMW_PNL = -1157395
TUSSEN = 0
PERS = 6761879
FISCAL = 7709004
OV = 2927688
APB = 3850628
GEMFONDS = 2577124
POLITIE = 747132
HVZ = 393440
AGB_WERKSUB = 166116
OCMW_EQUITY = -5407194
OCMW_CUM = -6062316


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


def patch_id_line(path, id_value, new_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    payload = csv_line(fields, new_row).encode("utf-8")
    raw = path.read_bytes()
    needle = b"\n" + id_value.encode("utf-8") + b","
    idx = raw.find(needle)
    if idx == -1:
        raise SystemExit("id line not found: %s" % id_value)
    start = idx + 1
    end = raw.find(b"\n", start)
    if end == -1:
        end = len(raw)
    ending = b"\n"
    new = raw[:start] + payload + ending + raw[end + 1 :]
    path.write_bytes(new)
    return True


assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) <= 1
assert abs((EVA + IGS + OTHER_FVA) - FVA) <= 1
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CUM_PREV + BBR - 2087714) - AVAIL) <= 1
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) <= 1
assert abs((CITY_PNL + OCMW_PNL) - PNL) <= 1
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) <= 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Kortenaken BBC jaarrekening 2025 (PDF 118p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Kortenaken",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1300; 5.46MB BBC PDF kortenaken.be 2025-Jaarrekening-LB-Kortenaken-Financiele-Nota; "
                "Afdruk 27.05.2026 pub 22.06.2026; KBO 0207.520.711/0212.189.379; "
                "assets 62.278m fin debt 10.568m IGS reval 8.897m OCMW equity -5.407m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Stad+OCMW Kortenaken beleidsevaluatie JR2025",
            "url": SRC2_URL,
            "publisher": "Lokaal Bestuur Kortenaken",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1300; beleidsevaluatie 2.37MB pub 22.06.2026; companion to BBC 118p; "
                "BBR 1.405505 / avail 10.480008 / fin debt 10.567781"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Kortenaken 0207.520.711",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1300; city KBO 0207.520.711 / OCMW 0212.189.379; seat Dorpsplein 35 3470; "
                "OCMW Miskom-dorp 1 3472; NIS 24054; AD Hayen / FD Jacobs / burgemeester Mollu"
            ),
        },
    ],
)
print("sources", n)

before = (DATA / "entities.csv").stat().st_size
patch_id_line(
    DATA / "entities.csv",
    ENT,
    {
        "entity_id": ENT,
        "name_nl": "Gemeente Kortenaken",
        "name_fr": "Commune de Kortenaken",
        "name_en": "Municipality of Kortenaken",
        "level": "municipality",
        "parent_id": "vlaanderen_gov",
        "community_language": "nl",
        "website": "https://www.kortenaken.be",
        "foi_email": "financien@kortenaken.be",
        "foi_postal": "Dorpsplein 35 3470 Kortenaken",
        "notes": (
            "tick1300 JR2025 GE residual (updated from tick1299 stub); KBO 0207.520.711; "
            "NIS 24054; AD Dominique Hayen / FD Eddy Jacobs / burgemeester Kristof Mollu; "
            "assets 62.278m fin debt 10.568m IGS reval 8.897m OCMW equity -5.407m NEG; "
            "AGB sibling agb_kortenaken 0535.811.469 already 1299; FOI ready"
        ),
    },
)
after = (DATA / "entities.csv").stat().st_size
print("city patched", before, "->", after)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Kortenaken",
            "name_fr": "CPAS de Kortenaken",
            "name_en": "OCMW Kortenaken",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.kortenaken.be",
            "foi_email": "financien@kortenaken.be",
            "foi_postal": "Miskom-dorp 1 3472 Kortenaken",
            "notes": (
                "tick1300 JR2025 GE residual; KBO 0212.189.379; J3 expl -1.050m / "
                "T5 PnL -1.157m / cum -6.062m NEG / equity -5.407m NEG; tussenkomst 0; FOI ready"
            ),
        }
    ],
)
print("entities ocmw", n)

bud_rows = [
    ("bud_ktnk_assets_2025", "2025", ASSETS, "J4 assets 62.278271m vs 52.966330m jump 9.312m"),
    ("bud_ktnk_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 52.966330m"),
    ("bud_ktnk_cash_2025", "2025", CASH, "J4 cash+beleg 11.104602m JUMP vs 9.915599m"),
    ("bud_ktnk_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 9.915599m"),
    ("bud_ktnk_fva_2025", "2025", FVA, "T5 FVA 15.034032m; EVA 0.025m + IGS 14.973m"),
    ("bud_ktnk_eva_2025", "2025", EVA, "T5 EVA AGB kapitaal 0.025000m frozen"),
    ("bud_ktnk_igs_2025", "2025", IGS, "T5 IGS FVA 14.973101m vs 6.067991m"),
    ("bud_ktnk_igs_reval_2025", "2025", IGS_REVAL, "T5 Fluvius Zenne-Dijle reval +8.897132m no cash"),
    ("bud_ktnk_mva_2025", "2025", MVA, "J4/T5 MVA 28.053996m; leasing 0.960766m"),
    ("bud_ktnk_leasing_2025", "2025", LEASING, "T5 leasing MVA 0.960766m (Fluvius licht)"),
    ("bud_ktnk_iva_2025", "2025", IVA, "J4/T5 IVA 0.579293m"),
    ("bud_ktnk_equity_2025", "2025", EQUITY, "J4 nettoactief 44.861510m vs 34.729906m"),
    ("bud_ktnk_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL -1.871840m (city +4.190 / OCMW -6.062)"),
    ("bud_ktnk_reval_2025", "2025", REVAL, "J4 herwaarderingsreserves 8.903034m (was 5.902)"),
    ("bud_ktnk_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 10.567781m (LT 9.730 + ST due 0.837)"),
    ("bud_ktnk_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 11.402363m"),
    ("bud_ktnk_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin debt 9.730409m"),
    ("bud_ktnk_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4/J4 ST due 0.837371m; ST fin 0"),
    ("bud_ktnk_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.011389m leasing; no new bank"),
    ("bud_ktnk_pension_2025", "2025", PENSION, "J4 pension LT 4.982275m vs 4.988429m"),
    ("bud_ktnk_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +2.327713m"),
    ("bud_ktnk_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 14.975310m"),
    ("bud_ktnk_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 12.647597m"),
    ("bud_ktnk_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +3.377688m (ontv 13.379 / uitg 10.001)"),
    ("bud_ktnk_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -1.049974m (ontv 1.597 / uitg 2.647)"),
    ("bud_ktnk_invest_2025", "2025", INVEST, "J2 invest -0.217688m vs MJP -3.101m"),
    ("bud_ktnk_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +1.405505m"),
    ("bud_ktnk_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 10.480008m"),
    ("bud_ktnk_afm_2025", "2025", AFM, "J2 AFM +1.559190m"),
    ("bud_ktnk_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +1.465145m (aangewezen 0.912m)"),
    ("bud_ktnk_pnl_2025", "2025", PNL, "J5 PnL +0.658102m; city +1.815 / OCMW -1.157; tussen 0"),
    ("bud_ktnk_pers_2025", "2025", PERS, "J5/T2 bezoldigingen 6.761879m; VTE unpublished"),
    ("bud_ktnk_fiscal_2025", "2025", FISCAL, "J5/T2 fiscale 7.709004m (OV 2.928 + APB 3.851)"),
    ("bud_ktnk_ov_2025", "2025", OV, "T2 OV 2.927688m"),
    ("bud_ktnk_apb_2025", "2025", APB, "T2 APB 3.850628m JUMP vs 3.268m"),
    ("bud_ktnk_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.577124m"),
    ("bud_ktnk_politie_2025", "2025", POLITIE, "T2 PZ Hageland 0.747132m JUMP vs 0.592521m"),
    ("bud_ktnk_hvz_2025", "2025", HVZ, "T2 HVZ 0.393440m"),
    ("bud_ktnk_agb_werksub_2025", "2025", AGB_WERKSUB, "T2 AGB werksub 0.166116m vs AGB prijssub 0.157m tick1299"),
    ("bud_ktnk_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity -5.407194m NEG"),
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
        "comm_ktnk_fin_debt_10_57m_2025",
        "Kortenaken YE2025 fin debt 10.568m",
        "10567781",
        "T4 10.567781m (LT 9.730 + ST due 0.837) declining vs 11.402m; new loans 0.011m leasing; extra repay 0.028m",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_ktnk_igs_reval_8_90m_2025",
        "Kortenaken YE2025 Fluvius IGS reval 8.897m",
        "8897132",
        "T5 Fluvius Zenne-Dijle reval +8.897132m no cash; IGS FVA 6.068→14.973m; EV-schommeling -0.197m in reval",
        "Publish per-IGS aanschaf vs herwaardering FOI",
    ),
    (
        "comm_ktnk_ocmw_equity_neg_5_41m_2025",
        "Kortenaken YE2025 OCMW equity -5.407m NEG",
        "5407194",
        "OCMW equity -5.407m NEG / cum -6.062m; expl -1.050m; PnL -1.157m; tussen 0",
        "Publish tussenkomst pad 2026-2031 FOI",
    ),
    (
        "comm_ktnk_pension_4_98m_2025",
        "Kortenaken YE2025 pension LT 4.982m",
        "4982275",
        "pension 4.982275m vs 4.988429m; T2 kost 0.151m",
        "Publish city vs OCMW pension split FOI",
    ),
    (
        "comm_ktnk_avail_10_48m_2025",
        "Kortenaken YE2025 avail BBR 10.480m",
        "10480008",
        "avail 10.480008m; BBR +1.405505m; AFM +1.559m; cash 11.105m JUMP",
        "Publish uncommitted overschot vs 2e pijler/BOA lock FOI",
    ),
    (
        "comm_ktnk_politie_0_75m_2025",
        "Kortenaken 2025 PZ Hageland 0.747m JUMP",
        "747132",
        "T2 PZ Hageland 0.747132m JUMP vs 0.592521m; aandeel 20.745pct tot 2025; actualisatie 2026",
        "Publish 2026 verdeelsleutel + GAS-5 pad FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Kortenaken / OCMW / AGB / PZ Hageland",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Kortenaken pub 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Kortenaken",
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
        "lb_ktnk_fin_debt_10_57m_2025",
        "Kortenaken YE2025 fin debt 10.57m",
        "10567781",
        "6.0",
        "7.0",
        "Publish per-loan amort 2026-2031",
        "fin debt 10.568m declining vs 11.402m; new loans 0.011m leasing only",
    ),
    (
        "lb_ktnk_igs_reval_8_90m_2025",
        "Kortenaken YE2025 Fluvius IGS reval 8.90m no cash",
        "8897132",
        "5.5",
        "7.5",
        "Publish per-IGS aanschaf vs herwaardering",
        "IGS 14.973m; Fluvius Zenne-Dijle reval +8.897m no cash; EVA AGB 0.025m",
    ),
    (
        "lb_ktnk_ocmw_equity_neg_5_41m_2025",
        "Kortenaken YE2025 OCMW equity -5.41m NEG",
        "5407194",
        "7.0",
        "5.5",
        "Publish tussenkomst pad 2026-2031",
        "OCMW equity -5.407m NEG / cum -6.062m; expl -1.050m; tussen 0",
    ),
    (
        "lb_ktnk_pension_4_98m_2025",
        "Kortenaken YE2025 pension LT 4.98m",
        "4982275",
        "6.0",
        "6.0",
        "Publish city vs OCMW pension split",
        "pension 4.982m declining vs 4.988m; T2 kost 0.151m",
    ),
    (
        "lb_ktnk_avail_10_48m_2025",
        "Kortenaken YE2025 avail BBR 10.48m",
        "10480008",
        "5.0",
        "7.5",
        "Publish uncommitted overschot vs 2e pijler/BOA lock",
        "avail 10.480m; BBR +1.406m; AFM +1.559m; cash 11.105m JUMP",
    ),
    (
        "lb_ktnk_politie_0_75m_2025",
        "Kortenaken 2025 PZ Hageland 0.75m JUMP",
        "747132",
        "6.5",
        "5.5",
        "Publish 2026 verdeelsleutel + GAS-5 pad",
        "PZ Hageland 0.747m JUMP vs 0.593m; aandeel 20.745pct; HVZ 0.393m",
    ),
    (
        "lb_ktnk_pers_6_76m_vte_unpub_2025",
        "Kortenaken 2025 pers 6.76m / VTE unpublished",
        "6761879",
        "6.0",
        "7.0",
        "Publish paid VTE city vs OCMW",
        "pers 6.762m; VTE unpublished (image-only); onderwijs andere ov 0.220m",
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
            "beneficiaries": "Inwoners Kortenaken / OCMW / AGB / PZ Hageland",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Kortenaken",
            "measured_outcome": (
                "assets 62.278m / fin debt 10.568m / IGS reval 8.897m / "
                "OCMW equity -5.407m NEG / AFM +1.559m / avail 10.480m"
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
                "T4/LT-S per-loan creditors for fin debt 10.567781m (new loans 0.011389 "
                "leasing only; no new bank loans) + IGS FVA 14.973101 inventory "
                "(Fluvius Zenne-Dijle reval +8.897132 no cash) + OCMW tussenkomst 0 vs expl -1.049974 / "
                "equity -5.407194 NEG / cum -6.062316 + VTE vs pers 6.761879 + "
                "AGB dual lock city T2 0.166116 vs AGB 0.157062 + politiezone Hageland "
                "0.747132 JUMP / HVZ 0.393440 pad"
            ),
            "why_it_matters": (
                "Unmined city+OCMW Kortenaken GE after AGB 1299 left this live PDF. "
                "Has AGB (EVA 0.025m). Fin debt 10.568m declining; new loans 0.011m leasing. "
                "IGS reval 8.897m no cash. OCMW equity -5.407m NEG; tussen 0. "
                "Avail 10.480m with BBR year +1.406m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Kortenaken (gemeente + OCMW)",
            "recipient_email": "financien@kortenaken.be",
            "recipient_postal": "Dorpsplein 35 3470 Kortenaken",
            "draft_letter_path": "docs/doge/foi/drafts/gap_ktnk_fin_debt_10_57m_igs_reval_8_90m_ocmw_equity_neg_5_41m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_ktnk_fin_debt_10_57m_2025",
            "linked_leaderboard_id": "lb_ktnk_fin_debt_10_57m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1300",
    "title": "Stad+OCMW Kortenaken JR2025 GE residual + every-10 progress",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Kortenaken JR2025 BBC text + KBO; "
        "KBO 0207.520.711 / 0212.189.379; assets 62.278m / fin debt 10.568m / "
        "IGS reval 8.897m / OCMW equity -5.407m NEG / AFM +1.559m; every-10 refresh; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1300 Stad+OCMW Kortenaken JR2025 GE residual + every-10; KBO 0207.520.711/0212.189.379; "
        "assets 62.278m fin debt 10.568m IGS reval 8.897m AFM +1.559m gecorr +1.465m "
        "BBR +1.406m avail 10.480m cash 11.105m OCMW equity -5.407m NEG tussen 0 "
        "pers 6.762m politie 0.747m JUMP new loans 0.011m leasing; AGB EVA 0.025m already 1299; "
        "FOI ready not sent; next rq_1301 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1301",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1300 done including Stad+OCMW Kortenaken 1300 / AGB Kortenaken 1299 / "
        "Stad+OCMW Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / Stad+OCMW Diepenbeek 1297 / "
        "AGB Diepenbeek 1296); prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined city Kortenaken 1300 / AGB Kortenaken 1299 / city Steenokkerzeel 1298 / "
        "AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / "
        "Heusden-Zolder 1294 / Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / "
        "Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / "
        "AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Pepingen/Zwalm/Wortegem-Petegem "
        "city+OCMW JR2025 only if PDF fetches; "
        "AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1300 after Stad+OCMW Kortenaken JR2025 GE residual + every-10; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1300", rq_new, rq_spawn)
print("research_queue 1300", found, "spawned_1301", spawned)

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
            "last_unit_id": "rq_1300",
            "ticks_completed": "1300",
            "paused": "no",
            "notes": (
                "tick1300 Stad+OCMW Kortenaken JR2025 GE residual + every-10; KBO 0207.520.711/0212.189.379; "
                "assets 62.278m fin debt 10.568m IGS reval 8.897m OCMW equity -5.407m NEG; "
                "FOI ready; next rq_1301 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1300_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
