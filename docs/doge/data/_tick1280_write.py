# -*- coding: utf-8 -*-
"""Tick 1280 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Stad+OCMW Gingelom JR2025 GE residual + every-10 progress."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T10:20:00Z"
TICK = 1280
SRC = "src_gingelom_jr2025_bbc"
SRC2 = "src_gingelom_jr2025_portal"
SRC3 = "src_kbo_gingelom_0207466469"
SRC4 = "src_kbo_ocmw_gingelom_0212213630"
SRC5 = "src_gingelom_jr2025_doc"
ENT = "city_gingelom"
OCMW = "ocmw_gingelom"
SRC_URL = "https://www.gingelom.be/file/download/4894e14b-9562-46c0-aa19-ca3ec95b44d7/kSpKHcN7afM6L9YIBiQnQeUoCNcNh2BCXxlw0AhOvk3d.pdf"
SRC2_URL = "https://www.gingelom.be/jaarrekening"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207466469"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0212213630"
SRC5_URL = "https://www.gingelom.be/file/download/94090906-50a2-4f0f-bbb8-cf825ccbd447/Fuail4AlehfEFUzC5RydupxamQp0QFTpR9qGsEzHk3d.pdf"
GAP = "gap_gingelom_fin_debt_3_86m_pension_3_56m_fluvius_reval_9_75m_l5"
HIER = "Vlaanderen>Gemeenten>Gingelom"

ASSETS = 57638905
ASSETS_2024 = 45826398
CASH = 10084079
CASH_2024 = 7852020
FVA = 19438543
IGS = 18047617
OTHER_FVA = 1390926
MVA = 26195586
LEASING = 851304
FIN_DEBT = 3857607
FIN_DEBT_2024 = 4381746
FIN_DEBT_LT = 3218526
FIN_DEBT_ST = 639081
PENSION = 3560536
PENSION_2024 = 4857297
EQUITY = 48459631
CUM_PNL = 15074868
REVAL = 9746903
FLUVIUS_REVAL = 9735233
LIMBURGNET = 11670
EXPL = 3627439
EXPL_ONTV = 15934982
EXPL_UITG = 12307543
INVEST = -909244
INVEST_ONTV = 518192
INVEST_UITG = 1427436
BBR = 2233359
AVAIL = 10621212
AFM = 2999236
GECORR = 3316202
NEW_LOANS = 143367
PNL = 3737352
CITY_PNL = 4524335
OCMW_PNL = -786983
PERS = 7340424
FISCAL = 7690496
OV = 2116584
APB = 4532742
GEMFONDS = 3254319
POLICE = 872955
HVZ = 334030
IGS_SUB = 619356
KERK = 98764


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


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Gingelom BBC jaarrekening 2025 (text PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal bestuur Gingelom",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1280; 0.73MB text PDF; GR+RVMW 19.05.2026; pub 22.05.2026; "
                "KBO 0207.466.469 / 0212.213.630; assets 57.639m fin debt 3.858m "
                "pension 3.561m AFM +2.999m gecorr +3.316m BBR +2.233m Fluvius "
                "reval 9.735m AGB 0"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Gingelom jaarrekening portal (JR2025 + documentatie)",
            "url": SRC2_URL,
            "publisher": "Lokaal bestuur Gingelom",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1280; JR2025 approved 19.05.2026 published 22.05.2026; no AGB",
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Gingelom 0207.466.469",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1280; Stad/gemeente since 01.01.1968; seat Sint-Pieterstraat 1 3890; "
                "6 VE; AD Kim Peters since 01.04.2019; burgemeester Patrick Lismont "
                "since 01.01.2016; NACE 84.114"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO OCMW Gingelom 0212.213.630",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1280; OCMW Gingelom; seat Sint-Pieterstraat 1 3890; 2 VE; voorzitter Lismont; AD Peters",
        },
        {
            "source_id": SRC5,
            "title": "Documentatie bij jaarrekening 2025 Stad+OCMW Gingelom",
            "url": SRC5_URL,
            "publisher": "Lokaal bestuur Gingelom",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": "tick1280; 0.77MB documentation companion; euros taken from main BBC text PDF",
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "Gemeente Gingelom",
            "name_fr": "Commune de Gingelom",
            "name_en": "Municipality of Gingelom",
            "level": "municipality",
            "parent_id": "sec_local",
            "community_language": "nl",
            "website": "https://www.gingelom.be/",
            "foi_email": "financien@gingelom.be",
            "foi_postal": "Sint-Pieterstraat 1 3890 Gingelom",
            "notes": (
                "tick1280 JR2025 GE residual; KBO 0207.466.469 / OCMW 0212.213.630; "
                "assets 57.639m fin debt 3.858m pension 3.561m AFM +2.999m "
                "gecorr +3.316m BBR +2.233m avail 10.621m Fluvius reval 9.735m "
                "AGB 0; AD Peters FD Forier burgemeester Lismont; FOI " + GAP
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Gingelom",
            "name_fr": "CPAS de Gingelom",
            "name_en": "OCMW Gingelom",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.gingelom.be/",
            "foi_email": "financien@gingelom.be",
            "foi_postal": "Sint-Pieterstraat 1 3890 Gingelom",
            "notes": (
                "tick1280; KBO 0212.213.630; consol in city JR2025; OCMW PnL "
                "-0.787m vs city +4.524m; nettoactief -2.710m; no own loans; split FOI"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_gingelom_assets_2025", "2025", ASSETS, "J4 assets 57.638905m vs 45.826398m jump 11.813m (Fluvius reval)"),
    ("bud_gingelom_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 45.826398m"),
    ("bud_gingelom_cash_2025", "2025", CASH, "J4 cash 10.084079m JUMP vs 7.852020m"),
    ("bud_gingelom_fva_2025", "2025", FVA, "J4 FVA 19.438543m (EVA 0 + IGS 18.047617m + other 1.390926m)"),
    ("bud_gingelom_igs_2025", "2025", IGS, "J4 IGS FVA 18.047617m vs 8.300714m; Fluvius EV-reval"),
    ("bud_gingelom_mva_2025", "2025", MVA, "J4 MVA 26.195586m; gemeenschapsgoederen 21.881m"),
    ("bud_gingelom_leasing_2025", "2025", LEASING, "J4 leasing 0.851304m vs 0.779012m; new 0.143367m"),
    ("bud_gingelom_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 3.857607m (LT 3.219 + ST due 0.639) vs 4.382m"),
    ("bud_gingelom_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4/T4 LT fin debt 3.218526m"),
    ("bud_gingelom_pension_2025", "2025", PENSION, "J4 pension LT 3.560536m vs 4.857297m drop 1.297m"),
    ("bud_gingelom_equity_2025", "2025", EQUITY, "J4 nettoactief 48.459631m (city 51.169 / OCMW -2.710)"),
    ("bud_gingelom_cum_pnl_2025", "2025", CUM_PNL, "J4 cum P&L 15.074868m (city 18.988 / OCMW -3.913)"),
    ("bud_gingelom_reval_2025", "2025", REVAL, "J4/T5 herwaarderingsreserve 9.746903m (Fluvius 9.735 + Limburg.net 0.012)"),
    ("bud_gingelom_expl_2025", "2025", EXPL, "J2 expl +3.627439m (ontv 15.935 / uitg 12.308)"),
    ("bud_gingelom_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 15.934982m"),
    ("bud_gingelom_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 12.307543m"),
    ("bud_gingelom_invest_2025", "2025", INVEST, "J2 invest -0.909244m (ontv 0.518 / uitg 1.427) vs MJP -2.716m"),
    ("bud_gingelom_invest_uitg_2025", "2025", INVEST_UITG, "J2 invest uitg 1.427436m; realisatie 28pct vs eindkrediet"),
    ("bud_gingelom_bbr_2025", "2025", BBR, "J2 BBR year +2.233359m vs MJP -0.627m"),
    ("bud_gingelom_avail_2025", "2025", AVAIL, "J2 avail BBR 10.621212m; onbeschikbaar 0"),
    ("bud_gingelom_afm_2025", "2025", AFM, "J2 AFM +2.999236m vs MJP +1.455m"),
    ("bud_gingelom_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +3.316202m vs MJP +1.774m"),
    ("bud_gingelom_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.143367m leasing only; planned bank 0.500m not drawn"),
    ("bud_gingelom_pnl_2025", "2025", PNL, "J5 PnL +3.737352m (city +4.524 / OCMW -0.787)"),
    ("bud_gingelom_pers_2025", "2025", PERS, "J5/T2 personeel 7.340424m; VTE unpublished"),
    ("bud_gingelom_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 7.690496m (OV 2.117 + APB 4.533)"),
    ("bud_gingelom_apb_2025", "2025", APB, "T2 APB 4.532742m vs FOD init 4.140m / +20pct vs 2024"),
    ("bud_gingelom_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 3.254319m"),
    ("bud_gingelom_police_2025", "2025", POLICE, "T2 politiezone Zuid-West Limburg 0.872955m"),
    ("bud_gingelom_hvz_2025", "2025", HVZ, "T2 HVZ 0.334030m"),
    ("bud_gingelom_igs_sub_2025", "2025", IGS_SUB, "T2 IGS werksub 0.619356m"),
    ("bud_gingelom_fluvius_reval_2025", "2025", FLUVIUS_REVAL, "verslag Fluvius EV-herwaardering 9.735233m (AE+AG+niet-gereguleerd)"),
    ("bud_gingelom_agb_sub_2025", "2025", 0, "J4 EVA FVA 0; no AGB; consol = GE+OCMW"),
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
            "notes": note + f"; tick{TICK}",
        }
        for bid, year, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_gingelom_fin_debt_3_86m_2025",
        "Stad+OCMW Gingelom YE2025 fin debt 3.858m",
        "3857607",
        "T4 3.857607m declining vs 4.382m; new 0.143m leasing; planned bank 0.500m not drawn; 37 loans avg 3.43pct",
        "Publish T4 creditor schedule + 7 kerkfabriek pass-through + narrative 3.01m vs T4 3.86m FOI",
    ),
    (
        "comm_gingelom_pension_3_56m_2025",
        "Stad+OCMW Gingelom YE2025 pension LT 3.561m",
        "3560536",
        "J4 pension 3.560536m drop vs 4.857m; actuarial basis FOI",
        "Publish wettelijk vs extra-wettelijk + why drop 1.297m FOI",
    ),
    (
        "comm_gingelom_fluvius_reval_9_75m_2025",
        "Gingelom Fluvius Limburg EV-reval 9.735m + Limburg.net 0.012m",
        "9746903",
        "IGS FVA 8.301m to 18.048m; Fluvius AE 4.594 + AG 0.456 + niet-gereguleerd 10.839",
        "Publish ABB note + dividend vs EV booking FOI",
    ),
    (
        "comm_gingelom_police_hvz_1_21m_2025",
        "Gingelom 2025 politiezone 0.873m + HVZ 0.334m",
        "1206985",
        "T2 dual 1.207m; IGS extra 0.619m; eredienst 0.099m; AGB 0",
        "Keep nominative 2026-2031 lock public",
    ),
    (
        "comm_gingelom_invest_underspend_2025",
        "Gingelom 2025 invest uitg 1.427m vs MJP 4.417m (28pct)",
        "1427436",
        "realisatie 28pct; planned 0.500m loan skipped; BBR still +2.233m",
        "Publish 2026 carry + centrum/riolering/sportcomplex pad FOI",
    ),
    (
        "comm_gingelom_ocmw_pnl_0_79m_2025",
        "OCMW Gingelom 2025 PnL -0.787m / equity -2.710m",
        "786983",
        "city PnL +4.524m; OCMW no own loans; Maribel clawback 0.032m",
        "Publish city/OCMW J2/J5 split + VTE FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Gingelom / Fluvius / politiezone ZWL / HVZ / eredienst",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 GR+RVMW 19.05.2026",
            "decision_date": "2026-05-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Gingelom (no AGB)",
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
        "lb_gingelom_fin_debt_3_86m_2025",
        "Stad+OCMW Gingelom YE2025 fin debt 3.86m",
        "3857607",
        "6.0",
        "5.5",
        "Publish T4 creditor + 7 kerkfabriek pass-through; keep no-new-bank-loan path public",
        "fin debt 3.858m declining; planned 0.50m bank not drawn; stock not TCO",
    ),
    (
        "lb_gingelom_pension_3_56m_2025",
        "Stad+OCMW Gingelom YE2025 pension 3.56m (drop 1.30m)",
        "3560536",
        "6.5",
        "5.5",
        "Publish actuarial note + why drop vs 4.857m",
        "pension LT 3.561m drop vs 4.857m; stock not TCO",
    ),
    (
        "lb_gingelom_fluvius_reval_9_75m_2025",
        "Gingelom Fluvius EV-reval jump 9.75m (assets +11.81m)",
        "9746903",
        "7.0",
        "6.5",
        "Publish ABB EV-methode note + Fluvius AE/AG/niet-gereguleerd split vs dividend",
        "one-off IGS reval 9.747m; cash/AFM unchanged by book entry",
    ),
    (
        "lb_gingelom_ocmw_equity_neg_2_71m_2025",
        "OCMW Gingelom YE2025 equity -2.71m / PnL -0.79m",
        "2709559",
        "7.0",
        "5.5",
        "Publish city/OCMW J2/J5 split + Maribel 0.032m clawback",
        "OCMW nettoactief -2.710m; city 51.169m; no OCMW loans",
    ),
    (
        "lb_gingelom_igs_fva_18_05m_2025",
        "Gingelom IGS FVA 18.05m + IGS werksub 0.62m (no AGB)",
        "18047617",
        "5.5",
        "6.5",
        "Publish IGS holdings list vs Fluvius EV stock",
        "EVA/AGB 0; IGS stock 18.048m after reval; IGS werksub 0.619m",
    ),
    (
        "lb_gingelom_invest_underspend_1_43m_2025",
        "Gingelom 2025 invest 1.43m vs MJP 4.42m (28pct)",
        "1427436",
        "6.0",
        "5.5",
        "Publish 2026 carry of centrum/riolering/sportcomplex envelopes",
        "underspend lets skip 0.50m loan; BBR still +2.233m / AFM +2.999m",
    ),
    (
        "lb_gingelom_police_hvz_1_21m_2025",
        "Gingelom 2025 politiezone 0.87m + HVZ 0.33m",
        "1206985",
        "5.5",
        "5.5",
        "Keep PZ Zuid-West Limburg + HVZ nominative lock public",
        "T2 dual 1.207m; eredienst 0.099m; AGB 0",
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
            "beneficiaries": "inwoners Gingelom / Fluvius / politiezone ZWL / HVZ / eredienst",
            "stated_goal": "Local GE residual map VL JR2025 Gingelom after Machelen 1279",
            "measured_outcome": (
                "assets 57.639m / fin debt 3.858m / pension 3.561m / "
                "AFM +2.999m / Fluvius reval 9.735m / AGB 0"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive of 348bn; city/OCMW split FOI",
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
                "City vs OCMW split of J2/J4/J5 (BBR/AFM/gecorr/assets/cash/"
                "fin debt/pension/pers/VTE) + T4 per-loan creditors for "
                "3.857607m incl 7 kerkfabriek pass-through + Fluvius EV-reval "
                "note 9.735233m + pension drop 4.857 to 3.561m + narrative "
                "3.01m vs T4 3.86m"
            ),
            "why_it_matters": (
                "Unmined Gingelom GE after neighbouring Sint-Truiden AGOST/"
                "Trupark/PATRI and Landen. No AGB. Fluvius EV-reval jumps "
                "assets +11.8m without cash. Distinct from AGB MAC Mechelen."
            ),
            "priority": "8",
            "recipient_body": "Lokaal bestuur Gingelom / OCMW Gingelom",
            "recipient_email": "financien@gingelom.be",
            "recipient_postal": "Sint-Pieterstraat 1 3890 Gingelom",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_gingelom_fin_debt_3_86m_2025",
            "linked_leaderboard_id": "lb_gingelom_fin_debt_3_86m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1280",
    "title": "Stad+OCMW Gingelom JR2025 GE residual + every-10 progress",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Gingelom JR2025 BBC text + KBO; "
        "KBO 0207.466.469 / 0212.213.630; assets 57.639m / fin debt 3.858m / "
        "pension 3.561m / Fluvius reval 9.735m / AGB 0; every-10 refresh; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T09:58:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1280 Stad+OCMW Gingelom JR2025 GE residual + every-10; KBO 0207.466.469/"
        "0212.213.630; assets 57.639m fin debt 3.858m pension 3.561m "
        "AFM +2.999m gecorr +3.316m BBR +2.233m avail 10.621m Fluvius reval "
        "9.735m cash 10.084m JUMP PnL +3.737m AGB 0; FOI ready not sent; "
        "next rq_1281 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1281",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(Gent dual AGB cluster 1255-1259 + Antwerp AG 1260-1265 + Atlas 1266 + Amal 1267 "
        "+ Fietsambassade 1268 + Mintus 1269 + MAC 1270 + AGB Kruibeke/BKZ sport 1271 "
        "+ AGB Tienen 1272 + AG Museum Leuven 1273 + Stad+OCMW Tienen 1274 "
        "+ AGB IBOGEM 1275 + Motena Roeselare 1276 + AGBPB Bonheiden 1277 "
        "+ AGB Trupark 1278 + Stad+OCMW Machelen 1279 + Stad+OCMW Gingelom 1280 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; AGB PATRI "
        "Sint-Truiden (0635.564.190) only if JR2025 downloadable; skip Motena / Trupark / "
        "Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST unless a fetchable "
        "JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; skip AGB "
        "Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "ebesluit TLS + Leuven besluitvorming TLS + Roeselare.be Cloudflare + "
        "zorgbedrijfsinttruiden.be TLS unexpected-EOF — prefer org sites / NBB / "
        "city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a "
        "separate downloadable JR"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1280 after Stad+OCMW Gingelom JR2025 GE residual + every-10; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1280", rq_new, rq_spawn)
print("research_queue 1280", found, "spawned_1281", spawned)

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
            "last_unit_id": "rq_1280",
            "ticks_completed": "1280",
            "paused": "no",
            "notes": (
                "tick1280 Stad+OCMW Gingelom JR2025 GE residual + every-10; KBO 0207.466.469/"
                "0212.213.630; assets 57.639m fin debt 3.858m pension 3.561m "
                "Fluvius reval 9.735m AGB 0; FOI ready; next rq_1281 residual dual L5 VL; "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1280 - 2026-08-17 - rq_1280 Stad+OCMW Gingelom GE residual + progress@1280
- Unit: Stad + OCMW Gingelom JR2025 GE package after Stad+OCMW Machelen tick1279 (KBO **0207.466.469** / **0212.213.630**; BBC text PDF on city site; GR+RVMW 19.05.2026; pub 22.05.2026). **No AGB** (J4 EVA FVA **0**; consol = GE+OCMW). Seat Sint-Pieterstraat 1 3890. AD Kim Peters / FD Frank Forier / burgemeester Patrick Lismont. NIS 71017. 6+2 VE. **Distinct from** neighbouring Sint-Truiden AGOST/Trupark/PATRI and Landen GE. PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare — not redone.
- EUR strong (primary BBC text PDF): assets **57.639m** (was 45.826m, jump **11.813m**); cash **10.084m** JUMP vs **7.852m**; FVA **19.439m** (EVA **0** + IGS **18.048m**); MVA **26.196m** leasing **0.851m**; fin debt **3.858m** (LT **3.219m** + ST due **0.639m**) declining vs **4.382m**; new loans **0.143m** (leasing; planned bank **0.500m** not drawn); pension LT **3.561m** (was 4.857m, drop **1.297m**); expl **+3.627m** (ontv **15.935m** / uitg **12.308m**); invest **−0.909m** (ontv **0.518m** / uitg **1.427m**, 28pct vs MJP); BBR **+2.233m** / avail **10.621m**; AFM **+2.999m** / gecorr **+3.316m**; PnL **+3.737m** (city **+4.524m** / OCMW **−0.787m**); pers **7.340m**; fiscal **7.690m** (OV **2.117m** + APB **4.533m**); gemeentefonds **3.254m**; politiezone **0.873m** + HVZ **0.334m** + IGS **0.619m**. Fluvius EV-reval **9.735m** + Limburg.net **0.012m**. VTE + city/OCMW J2 split unpublished.
- CSVs: sources+5/entities(new city+OCMW)/budgets+33/commitments+6/leaderboard+7 + FOI ready `gap_gingelom_fin_debt_3_86m_pension_3_56m_fluvius_reval_9_75m_l5` (not sent); rq_1280=done; spawn rq_1281; ticks=1280.
- Progress@1280: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E recounted ready. Pure annual waste top10 **stable** vs 1270 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds Tienen city 59.73m / Machelen 26.37m / AGB Tienen 16.93m / Museum Leuven 14.51m + Gingelom Fluvius reval 9.75m / fin debt 3.86m.
- Coverage: 1271–1280 is residual dual L5 (Kruibeke sport · AGB Tienen · Museum Leuven · Stad+OCMW Tienen · Ibogem · Motena · AGBPB · Trupark · Machelen · **Gingelom**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1281 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
