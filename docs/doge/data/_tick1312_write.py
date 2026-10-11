# -*- coding: utf-8 -*-
"""Tick 1312 — surgical append/patch only. AGBIM Maaseik JR2025 Entity II residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1312"
UTC = "2026-08-17T18:45:00Z"
ENT = "agb_infrastructuur_maaseik"
CITY = "city_maaseik"
HIER = "Vlaanderen>Gemeenten>Maaseik>AGBIM"
GAP = "gap_agbim_prijssub_cult_0_69m_sport_0_93m_ccao_8_91m_l5"
SRC = "src_agbim_jr2025_pdf"
SRC2 = "src_agbim_jr2025_doc"
SRC3 = "src_agbim_portal_2026"
SRC4 = "src_kbo_agbim_0828259640"
SRC_URL = "https://www.maaseik.be/sites/default/files/2026-08/BBC-jaarrekening-AGBI-2025.pdf"
SRC2_URL = "https://www.maaseik.be/sites/default/files/2026-08/Documentatie-bij-jaarrekening-2025_0.pdf"
SRC3_URL = "https://www.maaseik.be/autonome-gemeentebedrijven"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0828259640"

# nearest-euro from primary BBC (exact cents in notes)
ASSETS = 20412570
ASSETS_2024 = 19603266
CASH = 1948363
CASH_2024 = 1079757
FVA = 155
MVA = 16462954
BUILDINGS = 16069960
IVA = 77425
FIXED = 16540534
CURRENT = 3872036
RECV = 1784794
SCHULDEN = 2036216
EQUITY = 18376353
CAP_SUBS = 726328
CUM_PNL = 855894
OTHER_EQ = 16794132
FIN_DEBT = 0
NEW_LOANS = 0
CITY_INJECT_2025 = 0
CITY_INJECT_2024 = 4000000
CITY_INJECT_2023 = 1000000
EXPL = 1463736
EXPL_ONTV = 2994248
EXPL_UITG = 1530513
INVEST = 186673
INVEST_ONTV = 582531
INVEST_UITG = 395858
FIN_SALDO = 0
BBR = 1650408
CUM_PREV = 765727
CUM_BBR = 2416136
AFM = 1463736
GECORR = 1463736
PNL = 367651
DIVIDEND = 36765
CARRY = 330886
PERS = 0
WERKSUB = 12958
COSTS = 2444748
REV = 2812399
DEPR = 940680
PRIJSSUB_CULT_BOOK = 880397
PRIJSSUB_CULT_EFF = 692456
PRIJSSUB_CULT_2024 = 329895
PRIJSSUB_SPORT_BOOK = 930770
PRIJSSUB_MUSEUM = 64187
PRIJSSUB_BIB = 25954
PRIJSSUB_CS_BOOK = 1811167  # 880397+930770
CCAO = 8908328
VL_CCAO = 500000
BTW_RECU = 1616112


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
    """Replace notes on one entity row without rewriting the whole file."""
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    header, *lines = text.splitlines()
    fields = next(csv.reader([header]))
    out_lines = [header]
    found = False
    for line in lines:
        if not line.startswith(entity_id + ","):
            out_lines.append(line)
            continue
        row = next(csv.DictReader(io.StringIO(header + "\n" + line)))
        row["notes"] = new_notes
        out_lines.append(csv_line(fields, row))
        found = True
    if not found:
        raise SystemExit("entity %s not found" % entity_id)
    ending = b"\n" if raw.endswith(b"\n") else b""
    path.write_bytes(("\n".join(out_lines)).encode("utf-8") + ending)
    return True


assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((FVA + MVA + IVA) - FIXED) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CUM_PREV + BBR) - CUM_BBR) <= 1
assert abs((EXPL + INVEST + FIN_SALDO) - BBR) <= 1
assert abs((PRIJSSUB_CULT_BOOK + PRIJSSUB_SPORT_BOOK) - PRIJSSUB_CS_BOOK) == 0
assert FIN_DEBT == 0 and NEW_LOANS == 0 and CITY_INJECT_2025 == 0 and PERS == 0
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AGB Infrastructuur Maaseik BBC jaarrekening 2025 (official PDF)",
            "url": SRC_URL,
            "publisher": "Autonoom Gemeentebedrijf Infrastructuur Maaseik",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1312; BBC text PDF 61p / 2.26MB maaseik.be; pub 21.05.2026; "
                "created 21.04.2026; Jnl Budg 19435 Alg 2025010577; KBO 0828.259.640; "
                "assets 20412569.50 prijssub cult+sport booked 1811167 CCAO 8908328 AFM +1463736"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGB Infrastructuur Maaseik documentatie jaarrekening 2025",
            "url": SRC2_URL,
            "publisher": "Autonoom Gemeentebedrijf Infrastructuur Maaseik",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1312; documentatie PDF 1.40MB; geen personeel; geen fiscale opbrengsten; "
                "geen verbonden entiteiten (stad is moeder); Jnl Budg 19435 Alg 2025010577"
            ),
        },
        {
            "source_id": SRC3,
            "title": "Stad Maaseik autonome gemeentebedrijven portal",
            "url": SRC3_URL,
            "publisher": "Stad Maaseik",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1312; lists JR2025 AGBI 2.26MB pub 21.05.2026 + AGBM already mined 1311; "
                "city+OCMW GE still unmined; not sent FOI"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO AGB Infrastructuur Maaseik 0828.259.640",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1312; KBO 0828.259.640; AGB since 31.08.2009; 6 VE; seat Markt 1 3680; "
                "NACE 93.110; aanbestedende overheid; BTW since 01.08.2010; "
                "bestuurder Gunter Haeldermans since 10.03.2025; info@maaseik.be"
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
            "name_nl": "Autonoom Gemeentebedrijf Infrastructuur Maaseik (AGBIM)",
            "name_fr": "Regie communale autonome Infrastructure Maaseik (AGBIM)",
            "name_en": "Maaseik infrastructure autonomous municipal company (AGBIM)",
            "level": "agb",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.maaseik.be/autonome-gemeentebedrijven",
            "foi_email": "peter.graux@maaseik.be",
            "foi_postal": "Markt 1 3680 Maaseik",
            "notes": (
                "tick1312 JR2025 Entity II residual; KBO 0828.259.640; assets 20412570 "
                "fin debt 0 prijssub cult+sport booked 1811167 CCAO 8908328 AFM +1463736 "
                "PnL +367651 pers 0; FOI ready"
            ),
        },
    ],
)
print("entities", n)

patch_entity_notes(
    DATA / "entities.csv",
    CITY,
    (
        "tick1312 stub update; city+OCMW GE JR2025 still unmined; "
        "AGB Maaseik mined 1311; sister AGBIM mined this tick"
    ),
)
print("city_maaseik notes patched")

bud_rows = [
    ("bud_agbim_assets_2025", "2025", ASSETS, "J4 assets 20412569.50 vs 19603265.77"),
    ("bud_agbim_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 19603265.77"),
    ("bud_agbim_cash_2025", "2025", CASH, "J4 cash 1948362.77 vs 1079756.89 JUMP"),
    ("bud_agbim_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 1079756.89"),
    ("bud_agbim_fva_2025", "2025", FVA, "J4/T5 FVA 155; EVA 0 IGS 0"),
    ("bud_agbim_mva_2025", "2025", MVA, "J4 MVA 16462953.58; leasing 0"),
    ("bud_agbim_buildings_2025", "2025", BUILDINGS, "J4 terreinen/gebouwen 16069960.19"),
    ("bud_agbim_iva_2025", "2025", IVA, "J4 IVA 77425.37"),
    ("bud_agbim_recv_2025", "2025", RECV, "J4 ST vorderingen 1784793.74"),
    ("bud_agbim_schulden_2025", "2025", SCHULDEN, "J4 schulden 2036216.47 all ST; no LT/fin debt"),
    ("bud_agbim_equity_2025", "2025", EQUITY, "J4 nettoactief 18376353.03"),
    ("bud_agbim_cap_subs_2025", "2025", CAP_SUBS, "J4 kapitaalssubsidies 726327.76"),
    ("bud_agbim_cum_pnl_2025", "2025", CUM_PNL, "J4 cum overschot 855893.57"),
    ("bud_agbim_other_eq_2025", "2025", OTHER_EQ, "J4 overig nettoactief 16794131.70; city inject 2025 0"),
    ("bud_agbim_fin_debt_2025", "2025", FIN_DEBT, "T4 empty; toelichting geen leningen; fin saldo 0"),
    ("bud_agbim_new_loans_2025", "2025", NEW_LOANS, "T2/J2 new loans 0"),
    ("bud_agbim_city_inject_2025", "2025", CITY_INJECT_2025, "T2 kapitaalsvermeerderingen 0 (was 4m 2024 / 1m 2023)"),
    ("bud_agbim_city_inject_2024", "2024", CITY_INJECT_2024, "T2 kapitaalsvermeerderingen 4000000"),
    ("bud_agbim_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +1463735.52"),
    ("bud_agbim_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 2994248.25"),
    ("bud_agbim_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 1530512.73"),
    ("bud_agbim_invest_2025", "2025", INVEST, "J2 invest +186672.73 vs MJP -1605280.87"),
    ("bud_agbim_invest_ontv_2025", "2025", INVEST_ONTV, "J2 invest ontv 582530.80 (VL CCAO 500000)"),
    ("bud_agbim_invest_uitg_2025", "2025", INVEST_UITG, "J2 invest uitg 395858.07"),
    ("bud_agbim_bbr_2025", "2025", BBR, "J2 BBR boekjaar +1650408.25"),
    ("bud_agbim_cum_bbr_2025", "2025", CUM_BBR, "J2 gecumuleerd BBR 2416135.50 (prev 765727.25)"),
    ("bud_agbim_afm_2025", "2025", AFM, "J2 AFM +1463735.52 = expl (no loans)"),
    ("bud_agbim_afm_corr_2025", "2025", GECORR, "J2 gecorr AFM +1463735.52"),
    ("bud_agbim_pnl_2025", "2025", PNL, "J5 PnL +367651.47; dividend 10pct 36765.15"),
    ("bud_agbim_dividend_2025", "2025", DIVIDEND, "J5/statuten art.39 10pct winstuitkering stad 36765.15"),
    ("bud_agbim_pers_2025", "2025", PERS, "T2 bezoldigingen 0; documentatie geen personeel"),
    ("bud_agbim_werksub_2025", "2025", WERKSUB, "J5/T2 specifieke VL werksub 12957.80 (casula/velamen)"),
    ("bud_agbim_prijssub_cult_eff_2025", "2025", PRIJSSUB_CULT_EFF, "toelichting effectieve cultuur prijssub 692456 (2024 329895)"),
    ("bud_agbim_prijssub_cult_book_2025", "2025", PRIJSSUB_CULT_BOOK, "T1/toelichting cultuur ARK 707 geboekt 880397"),
    ("bud_agbim_prijssub_sport_book_2025", "2025", PRIJSSUB_SPORT_BOOK, "toelichting sport ARK 707 geboekt 930770"),
    ("bud_agbim_prijssub_cs_book_2025", "2025", PRIJSSUB_CS_BOOK, "cultuur+sport ARK 707 booked 1811167"),
    ("bud_agbim_ccao_t3_2025", "2025", CCAO, "T3 CCAO+BIB IP-AC000182 8908327.96"),
    ("bud_agbim_costs_2025", "2025", COSTS, "J5 kosten 2444747.73; depr 940679.62"),
    ("bud_agbim_rev_2025", "2025", REV, "J5 opbrengsten 2812399.20"),
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
        "comm_agbim_prijssub_cs_1_81m_2025",
        "AGBIM 2025 prijssubsidie cultuur+sport booked 1.811m",
        "1811167",
        "cultuur ARK 707 880397 / effectief 692456; sport ARK 707 930770; factor 2to9 from 11/2025; museum 64187 BIB 25954",
        "Publish prijssub ledger + factorbesluit + city dual GE",
    ),
    (
        "comm_agbim_ccao_8_91m_2025",
        "AGBIM CCAO+BIB T3 8.908m",
        "8908328",
        "T3 IP-AC000182 8908327.96; VL sub 500000; BTW recup 1616112; BIB under AGBI since 03/2025",
        "Publish CCAO final account + VAT ruling + remaining 2026 carry",
    ),
    (
        "comm_agbim_prijssub_cult_0_69m_2025",
        "AGBIM 2025 effectieve cultuur prijssub 0.692m",
        "692456",
        "effectief 692456 vs 2024 329895; booked 880397; defer 417596 to 2026; from 2024 229655; factor 2to9",
        "Publish factor 2to9 besluit + recon +367470 vs +362561",
    ),
    (
        "comm_agbim_city_inject_hist_5_00m_2023_2024",
        "AGBIM city capital inject 5.000m 2023-2024",
        "5000000",
        "T2 kapitaalsvermeerderingen 1000000 (2023) + 4000000 (2024); 2025 0; overig nettoactief 16794132",
        "Publish GR besluiten 2023/2024 inject + city dual GE",
    ),
    (
        "comm_agbim_bbr_2_42m_2025",
        "AGBIM YE2025 cum BBR 2.416m / cash 1.948m",
        "2416136",
        "J2 BBR year +1650408.25 / cum 2416135.50; cash 1948362.77 JUMP; fin debt 0; AFM +1463736",
        "Publish why cash pile vs city prijssub dependence",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Lokale besturen Limburg / Stad Maaseik",
            "legal_basis": "Decreet lokaal bestuur / BBC; AGBI JR2025 pub 21.05.2026; statuten art.39 10pct",
            "decision_date": "2026-05-21",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": amt,
            "cash_by_year": "",
            "remaining_eur": amt,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB residual map VL JR2025 Maaseik AGBIM",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": f"tick{TICK}; {note}; primary BBC",
        }
        for cid, title, amt, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_agbim_prijssub_cs_1_81m_2025",
        "AGBIM 2025 prijssubsidie cultuur+sport booked 1.81m",
        "1811167",
        "7.0",
        "3.5",
        "Publish prijssub ledger + factor 2to9 besluit + city dual",
        "cultuur booked 880397 / effectief 692456; sport booked 930770; factor hiked 2to9",
    ),
    (
        "lb_agbim_ccao_8_91m_2025",
        "AGBIM CCAO+BIB renovation T3 8.91m",
        "8908328",
        "6.5",
        "5.0",
        "Publish CCAO final account + VAT ruling + 2026 carry",
        "T3 8.908m; VL sub 0.500m; BTW recup 1.616m; BIB under AGBI since 03/2025",
    ),
    (
        "lb_agbim_prijssub_cult_0_69m_2025",
        "AGBIM 2025 effectieve cultuur prijssub 0.69m + factor 9",
        "692456",
        "7.5",
        "2.5",
        "Publish factor 2to9 besluit + recon YoY +367470 vs +362561",
        "effectief 692456 vs 2024 329895; booked 880397; defer 417596; factor 2to9 from 11/2025 too high",
    ),
    (
        "lb_agbim_city_inject_hist_5_00m_2023_2024",
        "AGBIM city capital inject 5.00m 2023-2024",
        "5000000",
        "6.0",
        "4.0",
        "Publish GR 2023/2024 inject besluiten + city dual GE",
        "1.000m (2023) + 4.000m (2024); 2025 inject 0; overig nettoactief 16.794m",
    ),
    (
        "lb_agbim_bbr_2_42m_2025",
        "AGBIM YE2025 cum BBR 2.42m / cash 1.95m",
        "2416136",
        "5.0",
        "3.5",
        "Publish cash-pile vs city prijssub dependence",
        "BBR year +1.650m / cum 2.416m; cash 1.948m JUMP; fin debt 0; AFM +1.464m",
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
            "beneficiaries": "Lokale besturen Limburg / Stad Maaseik",
            "stated_goal": "Local AGB residual map VL JR2025 Maaseik AGBIM",
            "measured_outcome": (
                "assets 20.413m / fin debt 0 / prijssub cult+sport booked 1.811m / "
                "CCAO 8.908m / AFM +1.464m / PnL +0.368m / pers 0"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "5.4",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC text; not TE-additive of 348bn; AGB FOI; leftover city GE still unmined",
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
                "Full prijssubsidie ledger 2025 per sector cash vs accrual vs factor "
                "(cultuur booked 880397 / effectief 692456; sport booked 930770; "
                "museum 64187; BIB 25954) + RVB/GR besluit factor 2to9 from 11/2025 + "
                "recon cultuur YoY +367470 vs 692456-329895=+362561 + Stad Maaseik dual "
                "GE prijssub lines + GR besluiten city inject 1000000 (2023) / 4000000 "
                "(2024) + RVB/GR vaststelling JR2025 PDF + kasstroom dividend 36765.15"
            ),
            "why_it_matters": (
                "Unmined leftover sister AGBIM after AGBM 1311. Official JR2025 BBC now "
                "downloads on maaseik.be. Fin debt 0. Prijssub cultuur+sport booked 1.811m "
                "with factor hiked 2to9. CCAO+BIB T3 8.908m. City inject 0 in 2025 after "
                "5.000m 2023-2024. AFM +1.464m / cum BBR 2.416m / cash 1.948m JUMP. "
                "Pers 0. City+OCMW Maaseik GE still unmined."
            ),
            "priority": "8",
            "recipient_body": "AGB Infrastructuur Maaseik / Stad Maaseik",
            "recipient_email": "peter.graux@maaseik.be",
            "recipient_postal": "Markt 1 3680 Maaseik",
            "draft_letter_path": "docs/doge/foi/drafts/gap_agbim_prijssub_cult_0_69m_sport_0_93m_ccao_8_91m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbim_prijssub_cs_1_81m_2025",
            "linked_leaderboard_id": "lb_agbim_prijssub_cs_1_81m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; BBC text strong; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1312",
    "title": "AGBIM Maaseik JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGBIM Maaseik JR2025 BBC text + KBO; KBO 0828.259.640; "
        "assets 20.413m / fin debt 0 / prijssub cult+sport booked 1.811m / "
        "CCAO 8.908m / AFM +1.464m / PnL +0.368m / pers 0 / BBR +1.650m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T18:20:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1312 AGBIM Maaseik JR2025 Entity II residual; KBO 0828.259.640; "
        "assets 20412570 fin debt 0 prijssub cult+sport booked 1811167 cult eff 692456 "
        "sport booked 930770 CCAO 8908328 AFM +1463736 PnL +367651 pers 0 BBR +1650408 "
        "cum BBR 2416136 cash 1948363 JUMP city inject 2025 0; FOI ready not sent; "
        "next rq_1313 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1313",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1312 done including AGBIM Maaseik 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
        "Stad+OCMW Vleteren 1306 / Stad+OCMW Pepingen 1305 / AGB Pepingen 1304 / "
        "Stad+OCMW Edegem 1303 / Stad+OCMW Wommelgem 1302 / Stad+OCMW Zonhoven 1301); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(AGB Merchtem / AGB Galmaarden / AGB Sport Hulshout only if a PDF actually downloads); "
        "leftover Maarkedal/Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem still unmined — take only if PDF fetches; "
        "leftover city Linkebeek GE still JR2024-only; leftover Ranst official still JR2024; "
        "leftover Kapellen city GE not published; leftover Drogenbos/Boutersem/Schelle city GE JR2024-only; "
        "leftover Oosterzele no BBC PDF; leftover Stad+OCMW Maaseik GE unmined; "
        "skip already-mined AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / EVA Hoeve Holleken 1309 / "
        "Stad+OCMW Beerse 1308 / AGB Beerse 1307 / city Vleteren 1306 / city Pepingen 1305 / "
        "AGB Pepingen 1304 / city Edegem 1303 / AGB Edegem 1239 / city Wommelgem 1302 / "
        "city Zonhoven 1301 / city Kortenaken 1300 / AGB Kortenaken 1299 / city Steenokkerzeel 1298 / "
        "AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGB Kapellen / AGB Lokeren 1200 / EVA Gezinswelzijn 1253 / AGB Genk / ZOG Genk 1242; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF + "
        "vlaamsbrabant.be TLS unexpected-EOF (vera.be OK); not every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1312 after AGBIM Maaseik JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1312", rq_new, rq_spawn)
print("research_queue 1312", found, "spawned_1313", spawned)

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
        lineterminator="\r\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1312",
            "ticks_completed": "1312",
            "paused": "no",
            "notes": (
                "tick1312 AGBIM Maaseik JR2025 residual; KBO 0828.259.640; "
                "fin debt 0 prijssub cult+sport 1.811m CCAO 8.908m AFM +1.464m; "
                "FOI ready; next rq_1313 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1312 - 2026-08-17 - rq_1312 AGBIM Maaseik dual residual
- Unit: Autonoom Gemeentebedrijf Infrastructuur Maaseik (AGBIM / AGBI) JR2025 Entity II after residual dual hunt (KBO **0828.259.640**; BBC text PDF on maaseik.be 2.26MB / 61p; pub **21.05.2026**; Jnl. Budg. **19435** / Alg. **2025010577**). PREFER NEXT after AGBM 1311: sister AGB, JR2025 still live. Distinct from already-mined AGBM (KBO 0887.694.015) and from unmined Stad+OCMW Maaseik GE. Seat Markt 1 3680 Maaseik. Voorzitter Gunter Haeldermans / secretaris Kristel Croonen. NACE 93.110; 6 VE; aanbestedende overheid. Hunt skipped already-mined AGB Maaseik 1311 / APB VERA 1310 / EVA Hoeve Holleken 1309 / city+AGB Beerse 1308-1307 + Motena / Trupark / PATRI / Zorgbedrijf ST TLS / Woonzorgnetwerk Edegem TLS. Leftover city GE Londerzeel / Holsbeek / Merchtem / Zwalm / Wortegem-Petegem / Maarkedal / Ranst / Linkebeek / Kapellen / Drogenbos / Boutersem still no fetchable JR2025 PDF. Official AGBI PDF still downloads. Not an every-10 tick.
- EUR strong (primary BBC text PDF): assets **20.413m** (was 19.603m); cash **1.948m** JUMP vs **1.080m**; MVA **16.463m** (gebouwen **16.070m**; leasing **0**); fin debt T4 **0**; new loans **0**; city inject 2025 **0** (was **4.000m** 2024 + **1.000m** 2023); nettoactief **18.376m**; cum PnL **+0.856m**; PnL J5 **+0.368m**; 10pct dividend stad **0.037m**; pers **0** / VTE **0**; werksub VL **0.013m**; expl **+1.464m** (ontv **2.994m** / uitg **1.531m**); invest **+0.187m**; BBR **+1.650m**; cum BBR **2.416m**; AFM **+1.464m**; gecorr AFM **+1.464m**. Prijssub cultuur ARK 707 geboekt **0.880m** / effectief **0.692m** (2024 **0.330m**); sport ARK 707 **0.931m**; museum **0.064m**; BIB **0.026m**; factor cultuur 2→9 vanaf 11/2025; CCAO+BIB T3 **8.908m**; VL invest-sub CCAO **0.500m**; BTW-recup CCAO **1.616m**.
- CSVs: sources+4/entities+1 (city stub patched)/budgets+39/commitments+5/leaderboard+5 + FOI ready `gap_agbim_prijssub_cult_0_69m_sport_0_93m_ccao_8_91m_l5` (not sent); rq_1312=done; spawn rq_1313; ticks=1312. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (AGBIM Maaseik). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1313 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; leftover Londerzeel/Holsbeek/Merchtem/Zwalm/Wortegem-Petegem / city Linkebeek GE / Stad+OCMW Maaseik GE only if a PDF now downloads; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1312 write done")
