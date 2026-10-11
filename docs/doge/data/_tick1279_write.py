# -*- coding: utf-8 -*-
"""Tick 1279 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Stad+OCMW Machelen JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T09:58:00Z"
TICK = 1279
SRC = "src_machelen_jr2025_bbc"
SRC2 = "src_machelen_jr2025_portal"
SRC3 = "src_kbo_machelen_0207539121"
SRC4 = "src_kbo_ocmw_machelen_0212195319"
SRC5 = "src_machelen_jr2025_doc"
ENT = "city_machelen"
OCMW = "ocmw_machelen"
SRC_URL = "https://www.machelen.be/file/download/19675/086DAB10639E47558708C7B75BD812C0"
SRC2_URL = "https://www.machelen.be/jaarrekening"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207539121"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0212195319"
SRC5_URL = "https://www.machelen.be/file/download/19674/6F20E83B29D5FCD70CAB0560D515CF34"
GAP = "gap_machelen_fin_debt_26_37m_pension_15_05m_farys_lease_16_90m_wzc_0_82m_l5"
HIER = "Vlaanderen>Gemeenten>Machelen"

ASSETS = 106034826
ASSETS_2024 = 125475946
CASH = 10388824
CASH_2024 = 12281688
FVA = 11831632
IGS = 11754130
MVA = 75928969
LEASING = 16899954
LEASING_2024 = 26665066
LEASE_SALE = 9662578
FIN_DEBT = 26368730
FIN_DEBT_2024 = 37886751
FIN_DEBT_LT = 23450805
FIN_DEBT_ST = 2917925
PENSION = 15054233
PENSION_2024 = 13394944
EQUITY = 55487380
CUM_PNL = -6254233
EXPL = 3929106
EXPL_ONTV = 46128626
EXPL_UITG = 42199520
INVEST = 7401106
INVEST_ONTV = 9958099
INVEST_UITG = 2556993
FIN_SALDO = -12106864
FIN_UITG = 12997982
BBR = -776652
AVAIL = 9181789
GECUM = 9368456
AFM = 1269876
GECORR = 1468188
NEW_LOANS = 398777
EARLY_REPAY = 8687720
PNL = -2371903
PERS = 21806089
FISCAL = 22541264
OV = 11918425
APB = 3652168
VERBLIJF = 2789599
GEMFONDS = 5938438
WERKSUB_REC = 13152615
WERKSUB_GRANT = 7474072
POLICE = 3396374
HVZ = 2398725
IGS_SUB = 1342806
FARYS_PRIJS = 402665.15
FARYS_BEHEER = 276646.04
FARYS_FIN = 375567.63
FARYS_REPAY = 1341688.32
WZC_EXPL = -749728
WZC_TOTAL = -819351
WZC_ONTV = 6654275
WZC_UITG = 7404002
WZC_EXT = 1408756.38
CITY_PNL = 4092084
OCMW_PNL = -6463988


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
            "title": "Stad+OCMW Machelen BBC jaarrekening 2025 (text PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal bestuur Machelen-Diegem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1279; 13.5MB text PDF; print 07.06.2026; GR+RVMW 24.06.2026; "
                "KBO 0207.539.121 / 0212.195.319; assets 106.035m fin debt 26.369m "
                "pension 15.054m AFM +1.270m gecorr +1.468m BBR -0.777m Farys lease "
                "16.900m WZC -0.819m; no AGB"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Machelen jaarrekening portal (JR2025 + documentatie)",
            "url": SRC2_URL,
            "publisher": "Lokaal bestuur Machelen-Diegem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1279; JR2025 12.9Mb + documentatie 2.0Mb listed as attachments",
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Machelen 0207.539.121",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1279; Stad/gemeente since 01.01.1968; seat Woluwestraat 1 1830; "
                "12 VE; AD Ellen De Boeck since 23.05.2025; burgemeester Jean De Groef "
                "since 01.01.2022; NACE 84.114"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO OCMW Machelen 0212.195.319",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1279; OCMW Machelen (Brab.); seat Woluwestraat 1 1830; WZC Parkhof in city GE",
        },
        {
            "source_id": SRC5,
            "title": "Documentatie bij jaarrekening 2025 Stad+OCMW Machelen",
            "url": SRC5_URL,
            "publisher": "Lokaal bestuur Machelen-Diegem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": "tick1279; 2.0MB documentation companion; euros taken from main BBC text PDF",
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "Gemeente Machelen-Diegem",
            "name_fr": "Commune de Machelen-Diegem",
            "name_en": "Municipality of Machelen-Diegem",
            "level": "municipality",
            "parent_id": "sec_local",
            "community_language": "nl",
            "website": "https://www.machelen.be/",
            "foi_email": "financien@machelen.be",
            "foi_postal": "Woluwestraat 1 1830 Machelen",
            "notes": (
                "tick1279 JR2025 GE residual; KBO 0207.539.121 / OCMW 0212.195.319; "
                "assets 106.035m fin debt 26.369m pension 15.054m AFM +1.270m "
                "gecorr +1.468m BBR -0.777m avail 9.182m Farys lease 16.900m "
                "WZC Parkhof -0.819m AGB 0; AD De Boeck FD Van Rijmenant "
                "burgemeester De Groef; FOI " + GAP
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Machelen",
            "name_fr": "CPAS de Machelen",
            "name_en": "OCMW Machelen",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.machelen.be/",
            "foi_email": "financien@machelen.be",
            "foi_postal": "Woluwestraat 1 1830 Machelen",
            "notes": (
                "tick1279; KBO 0212.195.319; consol in city JR2025; OCMW PnL "
                "-6.464m vs city +4.092m; WZC Parkhof inside GE; split FOI"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_machelen_assets_2025", "2025", ASSETS, "J4 assets 106.034826m vs 125.475946m drop 19.441m"),
    ("bud_machelen_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 125.475946m"),
    ("bud_machelen_cash_2025", "2025", CASH, "J4 cash 10.388824m DROP vs 12.281688m"),
    ("bud_machelen_fva_2025", "2025", FVA, "J4 FVA 11.831632m (EVA 0 + IGS 11.754130m)"),
    ("bud_machelen_igs_2025", "2025", IGS, "J4 IGS FVA 11.754130m; AGB/EVA 0"),
    ("bud_machelen_mva_2025", "2025", MVA, "J4 MVA 75.928969m; gemeenschapsgoederen 60.288m"),
    ("bud_machelen_leasing_2025", "2025", LEASING, "J4 leasing 16.899954m vs 26.665066m; Farys sale 9.662578m"),
    ("bud_machelen_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 26.368730m (LT 23.451 + ST due 2.918) vs 37.887m"),
    ("bud_machelen_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4/T4 LT fin debt 23.450805m"),
    ("bud_machelen_pension_2025", "2025", PENSION, "J4 pension LT 15.054233m vs 13.394944m"),
    ("bud_machelen_equity_2025", "2025", EQUITY, "J4 nettoactief 55.487380m (city 48.017 + OCMW 7.470)"),
    ("bud_machelen_cum_pnl_2025", "2025", CUM_PNL, "J4 cum P&L -6.254233m (city -1.274 + OCMW -4.980)"),
    ("bud_machelen_expl_2025", "2025", EXPL, "J2 expl +3.929106m (ontv 46.129 / uitg 42.200)"),
    ("bud_machelen_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 46.128626m"),
    ("bud_machelen_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 42.199520m"),
    ("bud_machelen_invest_2025", "2025", INVEST, "J2 invest +7.401106m (ontv 9.958 / uitg 2.557) sale-driven"),
    ("bud_machelen_invest_ontv_2025", "2025", INVEST_ONTV, "J2 invest ontv 9.958099m (Farys/lease sale)"),
    ("bud_machelen_bbr_2025", "2025", BBR, "J2 BBR year -0.776652m vs MJP +0.673m"),
    ("bud_machelen_avail_2025", "2025", AVAIL, "J2 avail BBR 9.181789m (gecum 9.368 - onbeschikbaar 0.187)"),
    ("bud_machelen_afm_2025", "2025", AFM, "J2 AFM +1.269876m vs MJP +3.149m"),
    ("bud_machelen_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +1.468188m"),
    ("bud_machelen_early_repay_2025", "2025", EARLY_REPAY, "T4 LT extra aflossingen 8.687720m (fin uitg 12.998m)"),
    ("bud_machelen_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.398777m = Farys lease 1721000"),
    ("bud_machelen_pnl_2025", "2025", PNL, "J5 PnL -2.371903m (city +4.092 / OCMW -6.464)"),
    ("bud_machelen_pers_2025", "2025", PERS, "J5/T2 personeel 21.806089m; VTE unpublished"),
    ("bud_machelen_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 22.541264m (OV 11.918 + APB 3.652 + verblijf 2.790)"),
    ("bud_machelen_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 5.938438m"),
    ("bud_machelen_police_2025", "2025", POLICE, "T2 politiezone 3.396374m"),
    ("bud_machelen_hvz_2025", "2025", HVZ, "T2 HVZ 2.398725m"),
    ("bud_machelen_igs_sub_2025", "2025", IGS_SUB, "T2 IGS werksub 1.342806m"),
    ("bud_machelen_farys_prijs_2025", "2025", FARYS_PRIJS, "verslag prijssub Farys clubs 0.402665m"),
    ("bud_machelen_wzc_total_2025", "2025", WZC_TOTAL, "WZC Parkhof eindtotaal -0.819351m (expl -0.750; 103 bewoners)"),
    ("bud_machelen_wzc_ext_2025", "2025", WZC_EXT, "externe tewerkstelling WZC 1.408756m vs AMJP 0.250m"),
    ("bud_machelen_agb_sub_2025", "2025", 0, "T2 werksub eigen AGB 0; J4 EVA FVA 0 — no AGB"),
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
        "comm_machelen_fin_debt_26_37m_2025",
        "Stad+OCMW Machelen YE2025 fin debt 26.369m",
        "26368730",
        "T4 26.368730m declining vs 37.887m; extra LT repay 8.688m; new 0.399m Farys lease",
        "Publish T4 creditor schedule + city/OCMW split FOI",
    ),
    (
        "comm_machelen_pension_15_05m_2025",
        "Stad+OCMW Machelen YE2025 pension LT 15.054m",
        "15054233",
        "J4 pension 15.054233m rising vs 13.395m; actuarial basis FOI",
        "Publish wettelijk vs extra-wettelijk + cash outflow FOI",
    ),
    (
        "comm_machelen_farys_lease_16_90m_2025",
        "Machelen Farys sport leasing MVA 16.900m after 9.663m sale",
        "16899954",
        "J4 leasing 16.900m; sale 9.663m; prijssub 0.403 + beheer 0.277 + Farys fin 0.376 + repay 1.342",
        "Publish Farys contract + remaining lease FOI",
    ),
    (
        "comm_machelen_wzc_parkhof_0_82m_2025",
        "WZC Parkhof 2025 city cover -0.819m",
        "819351",
        "expl -0.750m (ontv 6.654 / uitg 7.404); 103 bewoners €22/dag; interim 1.409m vs 0.250m",
        "Publish WZC VTE/interim + 2026 recovery path FOI",
    ),
    (
        "comm_machelen_early_repay_8_69m_2025",
        "Machelen 2025 extra LT debt repay 8.688m",
        "8687720",
        "T4 LT aflossingen 8.688m vs typical 0.2-0.7m; drives BBR -0.777m and fin -12.107m",
        "Publish which loans prepaid and source of cash FOI",
    ),
    (
        "comm_machelen_police_hvz_5_80m_2025",
        "Machelen 2025 politiezone 3.396m + HVZ 2.399m",
        "5795099",
        "T2 dual 5.795m; IGS extra 1.343m; AGB 0",
        "Keep nominative 2026-2031 lock public",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Machelen-Diegem / Farys / WZC Parkhof / politiezone / HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 GR+RVMW 24.06.2026",
            "decision_date": "2026-06-24",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Machelen (no AGB)",
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
        "lb_machelen_fin_debt_26_37m_2025",
        "Stad+OCMW Machelen YE2025 fin debt 26.37m",
        "26368730",
        "6.5",
        "7.5",
        "Publish T4 creditor + city/OCMW split; keep early-repay path public",
        "fin debt 26.369m declining after 8.688m extra repay; stock not TCO",
    ),
    (
        "lb_machelen_pension_15_05m_2025",
        "Stad+OCMW Machelen YE2025 pension 15.05m",
        "15054233",
        "6.0",
        "7.0",
        "Publish actuarial note + annual cash outflow",
        "pension LT 15.054m rising vs 13.395m; stock not TCO",
    ),
    (
        "lb_machelen_farys_lease_16_90m_2025",
        "Machelen Farys sport leasing shell 16.90m",
        "16899954",
        "7.0",
        "7.5",
        "Publish Farys contract + remaining lease after 9.66m 2025 sale",
        "leasing MVA 16.900m after sale 9.663m; dual prijs+beheer+fin 1.05m",
    ),
    (
        "lb_machelen_wzc_parkhof_0_82m_2025",
        "WZC Parkhof 2025 city cover -0.82m + interim 1.41m",
        "819351",
        "7.5",
        "6.5",
        "Publish WZC VTE vs interim 1.409m overrun (AMJP 0.250m)",
        "expl -0.750 / total -0.819; 103 bewoners €22/dag; OCMW PnL -6.464m",
    ),
    (
        "lb_machelen_early_repay_8_69m_2025",
        "Machelen 2025 extra LT repay 8.69m (BBR -0.78m)",
        "8687720",
        "6.0",
        "7.0",
        "Publish which loans prepaid and cash source (invest ontv 9.96m)",
        "drives financing -12.107m and BBR -0.777m while AFM stays +1.270m",
    ),
    (
        "lb_machelen_igs_fva_11_75m_2025",
        "Machelen IGS FVA 11.75m + IGS werksub 1.34m (no AGB)",
        "11754130",
        "5.5",
        "6.5",
        "Publish IGS holdings list vs Farys sport inbreng",
        "EVA/AGB 0; IGS stock 11.754m; IGS werksub 1.343m",
    ),
    (
        "lb_machelen_bbr_neg_0_78m_2025",
        "Stad+OCMW Machelen 2025 BBR -0.78m vs MJP +0.67m",
        "776652",
        "6.0",
        "5.5",
        "Keep AFM +1.27m / gecorr +1.47m vs BBR miss public",
        "BBR -0.777m after early repay; avail still 9.182m; PnL -2.372m",
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
            "beneficiaries": "inwoners Machelen-Diegem / Farys / WZC Parkhof / politiezone / HVZ",
            "stated_goal": "Local GE residual map VL JR2025 Machelen after Trupark 1278",
            "measured_outcome": (
                "assets 106.035m / fin debt 26.369m / pension 15.054m / "
                "AFM +1.270m / Farys lease 16.900m / WZC -0.819m / AGB 0"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.2",
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
                "26.368730m + Farys contract after 9.662578m leasing sale + "
                "Matexi PPS remaining + WZC Parkhof VTE/interim 1.408756 vs "
                "0.250m + pension actuarial 15.054233m"
            ),
            "why_it_matters": (
                "Unmined Machelen GE after neighbouring Vilvoorde/Zaventem/"
                "Steenokkerzeel. No AGB. Farys sport shell + WZC Parkhof "
                "deficit + 8.688m extra repay move the 2025 result. Distinct "
                "from AGB MAC Mechelen."
            ),
            "priority": "8",
            "recipient_body": "Lokaal bestuur Machelen-Diegem / OCMW Machelen",
            "recipient_email": "financien@machelen.be",
            "recipient_postal": "Woluwestraat 1 1830 Machelen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_machelen_fin_debt_26_37m_2025",
            "linked_leaderboard_id": "lb_machelen_fin_debt_26_37m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1279",
    "title": "Stad+OCMW Machelen JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Machelen JR2025 BBC text + KBO; "
        "KBO 0207.539.121 / 0212.195.319; assets 106.035m / fin debt 26.369m / "
        "pension 15.054m / Farys lease 16.900m / WZC -0.819m / AGB 0; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T09:48:13Z",
    "updated_utc": UTC,
    "notes": (
        "tick1279 Stad+OCMW Machelen JR2025 GE residual; KBO 0207.539.121/"
        "0212.195.319; assets 106.035m fin debt 26.369m pension 15.054m "
        "AFM +1.270m gecorr +1.468m BBR -0.777m avail 9.182m Farys lease "
        "16.900m sale 9.663m early repay 8.688m WZC -0.819m AGB 0; FOI ready "
        "not sent; next rq_1280 residual dual L5 VL + every-10"
    ),
}
rq_spawn = {
    "task_id": "rq_1280",
    "title": "Continuous FOI-adjacent public hole-fill batch + every-10 progress",
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
        "+ AGB Trupark 1278 + Stad+OCMW Machelen 1279 done; prefer other unmined "
        "AGB/zorg/EVA with direct PDF/NBB/city HTML; AGB PATRI Sint-Truiden "
        "(0635.564.190) only if JR2025 downloadable; skip Motena / Trupark / "
        "Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST unless a fetchable "
        "JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; skip AGB "
        "Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "ebesluit TLS + Leuven besluitvorming TLS + Roeselare.be Cloudflare + "
        "zorgbedrijfsinttruiden.be TLS unexpected-EOF — prefer org sites / NBB / "
        "city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a "
        "separate downloadable JR; tick 1280 is a *0 tick — do the every-10 "
        "progress refresh"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1279 after Stad+OCMW Machelen JR2025 GE residual; next residual dual L5 VL + every-10",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1279", rq_new, rq_spawn)
print("research_queue 1279", found, "spawned_1280", spawned)

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
            "last_unit_id": "rq_1279",
            "ticks_completed": "1279",
            "paused": "no",
            "notes": (
                "tick1279 Stad+OCMW Machelen JR2025 GE residual; KBO 0207.539.121/"
                "0212.195.319; assets 106.035m fin debt 26.369m pension 15.054m "
                "Farys lease 16.900m WZC -0.819m AGB 0; FOI ready; next rq_1280 "
                "residual dual L5 VL + every-10; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1279 - 2026-08-17 - rq_1279 Stad+OCMW Machelen GE residual
- Unit: Stad + OCMW Machelen-Diegem JR2025 GE package after AGB Trupark tick1278 (KBO **0207.539.121** / **0212.195.319**; BBC text PDF on city site; print 07.06.2026; GR+RVMW 24.06.2026). **No AGB** (J4 EVA FVA **0** / T2 eigen AGB **0**). Seat Woluwestraat 1 1830. AD Ellen De Boeck / FD Joeri Van Rijmenant / burgemeester Jean-Pierre De Groef. NIS 23047. 12 VE. **Distinct from** AGB MAC Mechelen (0546.688.337) and neighbouring Vilvoorde / Zaventem / Steenokkerzeel. PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare — not redone.
- EUR strong (primary BBC text PDF): assets **106.035m** (was 125.476m, drop **19.441m**); cash **10.389m** DROP vs **12.282m**; FVA **11.832m** (EVA **0** + IGS **11.754m**); MVA **75.929m** leasing **16.900m** (was **26.665m**; Farys sale **9.663m**); fin debt **26.369m** (LT **23.451m** + ST due **2.918m**) declining vs **37.887m**; new loans **0.399m** (Farys lease); extra LT repay **8.688m**; pension LT **15.054m** (was 13.395m); expl **+3.929m** (ontv **46.129m** / uitg **42.200m**); invest **+7.401m** (ontv **9.958m** / uitg **2.557m**); BBR **−0.777m** / avail **9.182m**; AFM **+1.270m** / gecorr **+1.468m**; PnL **−2.372m** (city **+4.092m** / OCMW **−6.464m**); pers **21.806m**; fiscal **22.541m** (OV **11.918m** + APB **3.652m** + verblijf **2.790m**); gemeentefonds **5.938m**; politiezone **3.396m** + HVZ **2.399m** + IGS **1.343m**. Farys dual: prijssub **0.403m** + beheer **0.277m** + Farys-loan fin **0.376m** + lease repay **1.342m**. WZC Parkhof expl **−0.750m** / total **−0.819m** (103 bewoners; **€22**/dag); externe tewerkstelling **1.409m** vs AMJP **0.250m**. VTE + city/OCMW J2 split unpublished.
- CSVs: sources+5/entities(new city+OCMW)/budgets+34/commitments+6/leaderboard+7 + FOI ready `gap_machelen_fin_debt_26_37m_pension_15_05m_farys_lease_16_90m_wzc_0_82m_l5` (not sent); rq_1279=done; spawn rq_1280; ticks=1279. Not a *0 tick — no progress refresh.
- Next: rq_1280 residual dual L5 VL JR2025 hole_fill + **every-10 progress refresh** (tick 1280 is a *0 tick). Prefer other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST unless a fetchable JR appears.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
