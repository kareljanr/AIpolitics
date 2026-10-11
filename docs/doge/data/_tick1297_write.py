# -*- coding: utf-8 -*-
"""Tick 1297 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Diepenbeek JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T12:50:00Z"
TICK = 1297
SRC = "src_diepbk_jr2025_bbc"
SRC2 = "src_diepbk_jr2025_gr"
SRC3 = "src_kbo_diepbk_0207465974"
ENT = "city_diepenbeek"
OCMW = "ocmw_diepenbeek"
SRC_URL = "https://www.diepenbeek.be/file_uploads/42819.pdf?sc=F808981DD9F273563DAD49F3E75B762A"
SRC2_URL = "https://www.diepenbeek.be/file_uploads/42816.pdf?sc=DB6EB9B961D2402B1084C068852A8E92"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207465974"
GAP = "gap_diepbk_fin_debt_13_59m_igs_reval_19_43m_ocmw_equity_neg_0_71m_l5"
HIER = "Vlaanderen>Gemeenten>Diepenbeek"

ASSETS = 190495607
ASSETS_2024 = 169323416
CASH = 25046685
CASH_2024 = 25039786
CURRENT = 31474081
FIXED = 159021527
FVA = 55152635
EVA = 7010000
IGS = 45774081
IGS_REVAL = 19425066
OTHER_FVA = 2368555
MVA = 99220970
LEASING = 7812713
IVA = 343831
SCHULDEN = 23602460
EQUITY = 166893147
CAP_SUBS = 10977432
CUM_PNL = 26993831
REVAL = 19445051
OTHER_EQ = 109476833
FIN_DEBT = 13592179
FIN_DEBT_LT = 11712103
FIN_DEBT_ST = 1880077
FIN_DEBT_2024 = 14915568
NEW_LOANS = 576680
PENSION = 3093433
PENSION_2024 = 3292983
EXPL = 6222031
EXPL_ONTV = 45425962
EXPL_UITG = 39203931
CITY_EXPL = 7776203
OCMW_EXPL = -1554171
INVEST = -5231327
INVEST_UITG = 7093325
INVEST_ONTV = 1861997
BBR = 364399
CUM_PREV = 24852110
AVAIL = 21858004
AFM = 5047040
GECORR = 5784304
AFL = 1930509
PNL = 3153685
CITY_PNL = 4983251
OCMW_PNL = -1829566
TUSSEN = 0
PERS = 24853856
FISCAL = 18601363
OV = 7334841
APB = 9372059
GEMFONDS = 7009148
POLITIE = 2765711
HVZ = 952387
AGB_WERKSUB = 698706
OCMW_EQUITY = -708459
OCMW_CUM = -7385064


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
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:120]))
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
    # keep original line ending
    ending = b"\n"
    if end > start and raw[end - 1 : end] == b"\r":
        ending = b"\r\n"
        end = end  # end is at \n; include it by replacing up to end
    new = raw[:start] + payload + ending + raw[end + 1 :]
    path.write_bytes(new)
    return True


assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - (CUM_PREV + BBR)) < 2
assert abs((24852110 + 364399) - 25216509) < 2
assert abs((25216509 - 3358505) - AVAIL) < 2
assert abs((CITY_PNL + OCMW_PNL) - PNL) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((OV + APB + 336893 + 1557571) - FISCAL) < 3
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Lokaal Bestuur Diepenbeek BBC jaarrekening 2025 (PDF 122p)",
            "url": SRC_URL,
            "publisher": "Gemeente en OCMW Diepenbeek",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1297; 7.98MB BBC PDF diepenbeek.be file_uploads/42819; GR 22.06.2026; "
                "KBO 0207.465.974/0212.246.787; assets 190.496m fin debt 13.592m "
                "IGS reval 19.425m OCMW equity -0.708m NEG AFM +5.047m avail 21.858m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Diepenbeek GR 22.06.2026 vaststelling JR2025 deel gemeente",
            "url": SRC2_URL,
            "publisher": "Gemeenteraad Diepenbeek",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1297; JR2025 vaststelling GR 22.06.2026 2026_GR_00085; pub 24.06.2026; "
                "unanimiteit; AD Jan Dreesen; burgemeester Rik Kriekels"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Diepenbeek 0207.465.974",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1297; city since 01.01.1968; seat Dorpsstraat 14 3590; 14 VE; "
                "burgemeester Rik Kriekels since 01.01.2019; AD Jan Dreesen since 15.04.2024 / "
                "FD Monique Aerts; OCMW sibling 0212.246.787 (4 VE; voorzitter Kriekels); "
                "email info@diepenbeek.be; NIS 71011"
            ),
        },
    ],
)
print("sources", n)

city_row = {
    "entity_id": ENT,
    "name_nl": "Gemeente Diepenbeek",
    "name_fr": "Commune de Diepenbeek",
    "name_en": "Municipality of Diepenbeek",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.diepenbeek.be",
    "foi_email": "info@diepenbeek.be",
    "foi_postal": "Dorpsstraat 14 3590 Diepenbeek",
    "notes": (
        "tick1297 JR2025 GE residual (updated from tick1296 stub); KBO 0207.465.974; "
        "NIS 71011; 14 VE; AD Jan Dreesen / FD Monique Aerts / burgemeester Rik Kriekels; "
        "assets 190.496m fin debt 13.592m IGS reval 19.425m OCMW equity -0.708m NEG; "
        "AGB sibling agb_diepenbeek 0885.640.088 already 1296; FOI ready"
    ),
}
patch_id_line(DATA / "entities.csv", ENT, city_row)
print("entities city patched")

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Diepenbeek",
            "name_fr": "CPAS de Diepenbeek",
            "name_en": "OCMW Diepenbeek",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.diepenbeek.be",
            "foi_email": "info@diepenbeek.be",
            "foi_postal": "Dorpsstraat 14 3590 Diepenbeek",
            "notes": (
                "tick1297 JR2025 GE residual; KBO 0212.246.787; 4 VE; "
                "voorzitter Rik Kriekels; J3 expl -1.554m / T5 cum PnL -7.385m NEG / "
                "equity -0.708m NEG; tussenkomst 0; FOI ready"
            ),
        },
    ],
)
print("entities ocmw", n)

bud_rows = [
    ("bud_diepbk_assets_2025", "2025", ASSETS, "J4 assets 190.495607m vs 169.323416m"),
    ("bud_diepbk_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 169.323416m"),
    ("bud_diepbk_cash_2025", "2025", CASH, "J4 cash+beleg 25.046685m vs 25.039786m"),
    ("bud_diepbk_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 25.039786m"),
    ("bud_diepbk_fva_2025", "2025", FVA, "J4/T5 FVA 55.152635m (EVA 7.010 + IGS 45.774 + other 2.369)"),
    ("bud_diepbk_eva_2025", "2025", EVA, "T5 EVA AGBD kapitaal 7.010000m frozen"),
    ("bud_diepbk_igs_2025", "2025", IGS, "T5 IGS 45.774081m vs 26.349014m"),
    ("bud_diepbk_igs_reval_2025", "2025", IGS_REVAL, "T5 IGS herwaardering +19.425066m no cash"),
    ("bud_diepbk_mva_2025", "2025", MVA, "J4/T5 MVA 99.220970m; leasing 7.812713m"),
    ("bud_diepbk_leasing_2025", "2025", LEASING, "T5 leasing MVA 1.727+6.085=7.813m"),
    ("bud_diepbk_equity_2025", "2025", EQUITY, "J4 nettoactief 166.893147m vs 144.225242m"),
    ("bud_diepbk_cap_subs_2025", "2025", CAP_SUBS, "J4/T5 cap subs 10.977432m"),
    ("bud_diepbk_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL 26.993831m"),
    ("bud_diepbk_reval_2025", "2025", REVAL, "J4/T5 herwaardering 19.445051m vs 0.020m"),
    ("bud_diepbk_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 13.592179m (LT 11.712 + ST due 1.850 + ST 0.030)"),
    ("bud_diepbk_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 14.915568m"),
    ("bud_diepbk_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4 LT fin debt 11.712103m"),
    ("bud_diepbk_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4 ST due 1.849636m + ST 0.030441m"),
    ("bud_diepbk_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.576680m leasing; no new bank loans"),
    ("bud_diepbk_pension_2025", "2025", PENSION, "J4 LT pension 3.093433m vs 3.292983m"),
    ("bud_diepbk_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +6.222031m"),
    ("bud_diepbk_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 45.425962m"),
    ("bud_diepbk_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 39.203931m"),
    ("bud_diepbk_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +7.776203m"),
    ("bud_diepbk_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -1.554171m"),
    ("bud_diepbk_invest_2025", "2025", INVEST, "J2 invest -5.231327m vs MJP -8.476m"),
    ("bud_diepbk_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +0.364399m"),
    ("bud_diepbk_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 21.858004m"),
    ("bud_diepbk_afm_2025", "2025", AFM, "J2 AFM +5.047040m"),
    ("bud_diepbk_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +5.784304m"),
    ("bud_diepbk_pnl_2025", "2025", PNL, "J5 PnL +3.153685m (city +4.983 / OCMW -1.830)"),
    ("bud_diepbk_pers_2025", "2025", PERS, "J5/T2 bezoldigingen 24.853856m; VTE unpublished"),
    ("bud_diepbk_fiscal_2025", "2025", FISCAL, "T2 fiscale 18.601363m (OV 7.335 + APB 9.372)"),
    ("bud_diepbk_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 7.009148m"),
    ("bud_diepbk_politie_2025", "2025", POLITIE, "T2 politiezone Limburg regio Hoofdstad 2.765711m"),
    ("bud_diepbk_hvz_2025", "2025", HVZ, "T2 HVZ Zuid-West-Limburg 0.952387m"),
    ("bud_diepbk_agb_werksub_2025", "2025", AGB_WERKSUB, "T2 city werksub aan AGB 0.698706m vs AGBD 0.385m"),
    ("bud_diepbk_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity -0.708459m NEG"),
    ("bud_diepbk_afl_2025", "2025", AFL, "T4/J2 periodieke aflossingen 1.930509m"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT if "ocmw_equity" not in bid and "ocmw_expl" not in bid else OCMW,
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
        "comm_diepbk_fin_debt_13_59m_2025",
        "Diepenbeek YE2025 fin debt 13.592m",
        "13592179",
        "T4 13.592179m (LT 11.712 + ST due 1.850 + ST 0.030) declining vs 14.916m; new loans 0.577m leasing; no new bank loans; afl 1.931m",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_diepbk_igs_reval_19_43m_2025",
        "Diepenbeek YE2025 IGS reval 19.425m",
        "19425066",
        "T5 IGS 45.774m vs 26.349m; herwaardering +19.425m no cash; EVA AGBD 7.010m frozen",
        "Publish per-IGS aanschaf vs herwaardering FOI",
    ),
    (
        "comm_diepbk_ocmw_equity_neg_0_71m_2025",
        "Diepenbeek YE2025 OCMW equity -0.708m NEG",
        "708459",
        "T5 OCMW equity -0.708m NEG / cum PnL -7.385m NEG; J3 expl -1.554m; tussenkomst 0",
        "Publish tussenkomst pad 2026-2031 FOI",
    ),
    (
        "comm_diepbk_pension_3_09m_2025",
        "Diepenbeek YE2025 pension LT 3.093m",
        "3093433",
        "J4 LT pension 3.093m declining vs 3.293m; T2 pensioenkost 0.197m",
        "Publish city vs OCMW pension split FOI",
    ),
    (
        "comm_diepbk_avail_21_86m_2025",
        "Diepenbeek YE2025 avail BBR 21.858m",
        "21858004",
        "avail 21.858m; BBR year +0.364m; AFM +5.047m; cash 25.047m; onbeschikbaar 3.359m (2e pijler + Boost BOA)",
        "Publish uncommitted overschot vs onbeschikbaar lock FOI",
    ),
    (
        "comm_diepbk_agb_werksub_0_70m_2025",
        "Diepenbeek 2025 city AGB werksub 0.699m",
        "698706",
        "T2 city werksub aan AGB 0.699m vs AGBD JR2025 algemene 0.385m (tick 1296); dual lock",
        "Publish 2026-2031 beheersovereenkomst + reconciliatie FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Diepenbeek / OCMW / AGBD",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Diepenbeek GR 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Diepenbeek",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": note + f"; tick{TICK}",
        }
        for cid, title, env, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_diepbk_fin_debt_13_59m_2025",
        "Diepenbeek YE2025 fin debt 13.59m",
        "13592179",
        "6.0",
        "7.0",
        "Publish per-loan amort 2026-2031",
        "fin debt 13.592m declining vs 14.916m; new loans 0.577m leasing only",
    ),
    (
        "lb_diepbk_igs_reval_19_43m_2025",
        "Diepenbeek YE2025 IGS reval 19.43m no cash",
        "19425066",
        "5.5",
        "7.5",
        "Publish per-IGS aanschaf vs herwaardering",
        "IGS 45.774m; reval +19.425m no cash; EVA AGBD 7.010m frozen",
    ),
    (
        "lb_diepbk_ocmw_equity_neg_0_71m_2025",
        "Diepenbeek YE2025 OCMW equity -0.71m NEG",
        "708459",
        "7.0",
        "5.5",
        "Publish tussenkomst pad 2026-2031",
        "OCMW equity -0.708m NEG / cum -7.385m; expl -1.554m; tussen 0",
    ),
    (
        "lb_diepbk_pension_3_09m_2025",
        "Diepenbeek YE2025 pension LT 3.09m",
        "3093433",
        "6.0",
        "6.0",
        "Publish city vs OCMW pension split",
        "pension 3.093m declining vs 3.293m; T2 kost 0.197m",
    ),
    (
        "lb_diepbk_avail_21_86m_2025",
        "Diepenbeek YE2025 avail BBR 21.86m",
        "21858004",
        "5.0",
        "7.5",
        "Publish uncommitted overschot vs 2e pijler/BOA lock",
        "avail 21.858m; BBR +0.364m; AFM +5.047m; cash 25.047m",
    ),
    (
        "lb_diepbk_agb_werksub_0_70m_2025",
        "Diepenbeek 2025 city AGB werksub 0.70m dual",
        "698706",
        "6.5",
        "5.5",
        "Publish beheersovereenkomst + reconciliatie vs AGBD 0.385m",
        "city T2 0.699m vs AGBD algemene 0.385m tick1296",
    ),
    (
        "lb_diepbk_pers_24_85m_vte_unpub_2025",
        "Diepenbeek 2025 pers 24.85m / VTE unpublished",
        "24853856",
        "6.0",
        "7.0",
        "Publish paid VTE city vs OCMW",
        "pers 24.854m; VTE unpublished; onderwijs andere ov 2.505m",
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
            "beneficiaries": "Inwoners Diepenbeek / OCMW / AGBD",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Diepenbeek",
            "measured_outcome": (
                "assets 190.496m / fin debt 13.592m / IGS reval 19.425m / "
                "OCMW equity -0.708m NEG / AFM +5.047m / avail 21.858m"
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
                "T4/LT-S per-loan creditors for fin debt 13.592179m (new loans 0.576680 "
                "leasing only; no new bank loans) + IGS FVA 45.774081 inventory "
                "(reval +19.425066 no cash) + OCMW tussenkomst 0 vs expl -1.554171 / "
                "equity -0.708459 NEG / cum -7.385064 + VTE vs pers 24.853856 + "
                "AGB dual lock city T2 0.698706 vs AGBD 0.384720 + politiezone LRH "
                "2.765711 / HVZ 0.952387 pad"
            ),
            "why_it_matters": (
                "Unmined city+OCMW Diepenbeek GE after AGB 1296 left this live PDF. "
                "Has AGB (EVA 7.010m). Fin debt 13.592m declining; new loans 0.577m leasing. "
                "IGS reval 19.425m no cash. OCMW equity -0.708m NEG; tussen 0. "
                "Avail 21.858m with BBR year +0.364m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Diepenbeek (gemeente + OCMW)",
            "recipient_email": "info@diepenbeek.be",
            "recipient_postal": "Dorpsstraat 14 3590 Diepenbeek",
            "draft_letter_path": "docs/doge/foi/drafts/gap_diepbk_fin_debt_13_59m_igs_reval_19_43m_ocmw_equity_neg_0_71m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_diepbk_fin_debt_13_59m_2025",
            "linked_leaderboard_id": "lb_diepbk_fin_debt_13_59m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1297",
    "title": "Stad+OCMW Diepenbeek JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Diepenbeek JR2025 BBC text + KBO; "
        "KBO 0207.465.974 / 0212.246.787; assets 190.496m / fin debt 13.592m / "
        "IGS reval 19.425m / OCMW equity -0.708m NEG / AFM +5.047m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T12:45:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1297 Stad+OCMW Diepenbeek JR2025 GE residual; KBO 0207.465.974/0212.246.787; "
        "assets 190.496m fin debt 13.592m IGS reval 19.425m AFM +5.047m gecorr +5.784m "
        "BBR +0.364m avail 21.858m cash 25.047m OCMW equity -0.708m NEG tussen 0 "
        "pers 24.854m politie 2.766m new loans 0.577m leasing; AGB EVA 7.010m already 1296; "
        "FOI ready not sent; next rq_1298 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1298",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1297 done including Stad+OCMW Diepenbeek 1297 / AGB Diepenbeek 1296); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / "
        "Heusden-Zolder 1294 / Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / "
        "Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / "
        "AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Steenokkerzeel/Pepingen/Zwalm/Wortegem-Petegem "
        "city+OCMW JR2025 only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1297 after Stad+OCMW Diepenbeek JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1297", rq_new, rq_spawn)
print("research_queue 1297", found, "spawned_1298", spawned)

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
            "last_unit_id": "rq_1297",
            "ticks_completed": "1297",
            "paused": "no",
            "notes": (
                "tick1297 Stad+OCMW Diepenbeek JR2025 GE residual; KBO 0207.465.974/0212.246.787; "
                "assets 190.496m fin debt 13.592m IGS reval 19.425m OCMW equity -0.708m NEG; "
                "FOI ready; next rq_1298 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1297_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
