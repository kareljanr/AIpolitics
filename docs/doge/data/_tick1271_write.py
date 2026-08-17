# -*- coding: utf-8 -*-
"""Tick 1271 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AGB Kruibeke/BKZ sport JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T09:30:00Z"
TICK = 1271
SRC = "src_agb_kruibeke_jr2025_bbc"
SRC2 = "src_agb_kruibeke_mjp2026"
SRC3 = "src_agb_kruibeke_amjp2025"
SRC4 = "src_kbo_agb_kruibeke_0878836925"
SRC5 = "src_nbb_agb_kruibeke_0878836925"
ENT = "agb_kruibeke_sport"
CITY = "city_bkz"
SRC_URL = "https://www.gemeentebkz.be/file/download/3e7222fa-4ea7-4ad5-8305-5e2c89cf14ee/BPrxsVy97SQFGmwC6fp0JdnImBSjnyli8mLJt9zSUHM3d.pdf"
SRC2_URL = "https://www.gemeentebkz.be/meerjarenplan-budget-agb-sport-cultuur-en-recreatie-kruibeke"
SRC3_URL = "https://www.gemeentebkz.be/file/download/c83a4d01-c380-4ab0-9f38-9643a7c36886/Fr51mktUEfi7pPQS7SUsyDrREZXuxqPDhD8oooP03d.pdf"
SRC2_PDF = "https://www.gemeentebkz.be/file/download/183aba0c-aacb-4381-b312-e12c90341efb/jGYG78oqnrE6A5bEkHkrapp7UUsIT2rEkYq4jIq9GE3d.pdf"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0878836925"
SRC5_URL = "https://consult.cbso.nbb.be/consult-enterprise/0878836925"
GAP = "gap_kruibeke_agb_thin_equity_0_01m_fin_debt_1_71m_prijssub_0_42m_l5"
HIER = "Vlaanderen>Gemeenten>BKZ>AGB_Kruibeke_Sport"

ASSETS = 1883844.00
CASH = 76768.00
CASH_2024 = 179924.00
FIN_DEBT = 1709928.00
LT_DEBT = 1417651.00
ST_DUE = 292277.00
NETTO = 11244.00
CUM_PNL = 10629.00
AFM = 11972.00
GECORR = 163355.00
BBR = 12859.00
BBR_AVAIL = 233774.00
EXPL_UIT = 229013.00
EXPL_ONT = 545222.00
EXPL_SALDO = 316209.00
INV_UIT = 102600.00
INV_SALDO = -102600.00
FIN_AFL = 304237.00
NEW_LOAN = 103487.00
PNL = 35215.00
PRIJS = 423059.40
MVA = 1482889.00
ST_RECV = 319677.00
DEBT_2024 = 1910678.00
MJP_EXPL_2026 = 328988.00
MJP_BBR_2026 = 10000.00
MJP_INV_2026 = 345000.00


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


def patch_entity_notes_line(path, entity_id, extra, extra_fields=None):
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
            if extra_fields:
                row.update(extra_fields)
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
            "title": "AGB Kruibeke sport/cultuur/recreatie JR2025 BBC text PDF",
            "url": SRC_URL,
            "publisher": "AGB Sport Cultuur Recreatie Kruibeke / Gemeente BKZ",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1271; RvB 30.06.2026; KBO 0878.836.925; assets 1.884m; "
                "fin debt 1.710m city renteloos; AFM +0.012m gecorr +0.163m; "
                "city prijssub 0.423m; PnL 0.035m full to rechthebbenden; "
                "nettoactief 0.011m; cash 0.077m DROP vs 0.180m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGB Kruibeke MJP 2026-2031 + portal (JR2025 BBC download)",
            "url": SRC2_URL,
            "publisher": "Gemeente Beveren-Kruibeke-Zwijndrecht",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1271; MJP PDF "
                + SRC2_PDF
                + "; RvB 16.12.2025; BBR 10k/yr AFM 10k/yr expl 2026 0.329m; "
                "prijssub factor no nominative 2026 lock"
            ),
        },
        {
            "source_id": SRC3,
            "title": "AGB Kruibeke AMJP 2025/1",
            "url": SRC3_URL,
            "publisher": "AGB Kruibeke / Gemeente BKZ",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1271; AMJP 2025/1 prijssub 416000 vs JR exe 423059; "
                "BBR AMJP 900 vs exe 12859"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO AGB Kruibeke / AGB BKZ 0878.836.925",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1271; AGB since 25.07.2005; renamed AGB Beveren-Kruibeke-"
                "Zwijndrecht 30.06.2026; seat Gravenplein 8 9120 Beveren; "
                "0 VE; NACE 84.120; tel 03 750 15 11; info@gemeentebkz.be; "
                "voorzitter Marc Van de Vijver since 23.06.2025"
            ),
        },
        {
            "source_id": SRC5,
            "title": "NBB Consult AGB Kruibeke 0878836925 JR filings",
            "url": SRC5_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1271; consult SPA/empty this box; VenB 2025 not retrieved; "
                "do not use Belscope/Companyweb"
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
            "name_nl": "AGB Sport, Cultuur & Recreatie Kruibeke (AGB BKZ)",
            "name_fr": "AGB Sport, Culture et Recreation Kruibeke (AGB BKZ)",
            "name_en": "Kruibeke sport/culture/recreation municipal company (AGB BKZ)",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC2_URL,
            "foi_email": "info@gemeentebkz.be",
            "foi_postal": "Gravenplein 8 9120 Beveren",
            "notes": (
                "tick1271 JR2025 dual residual; KBO 0878.836.925 AGB since 25.07.2005; "
                "renamed AGB Beveren-Kruibeke-Zwijndrecht 30.06.2026; assets 1.884m "
                "fin debt 1.710m city renteloos AFM +0.012m gecorr +0.163m BBR 0.013m "
                "avail 0.234m city prijssub 0.423m PnL 0.035m full strip cash 0.077m "
                "nettoactief 0.011m; VenB unpublished; FOI " + GAP
            ),
        }
    ],
)
print("entity kruibeke", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "AGB Kruibeke sport dual residual tick1271 (KBO 0878.836.925; "
        "assets 1.884m; fin debt 1.710m city renteloos; city prijssub 0.423m; "
        "thin equity 0.011m; VenB FOI)"
    ),
)
print("city_bkz notes", ok)

bud_rows = [
    ("bud_kruibeke_agb_assets_2025", "2025", ASSETS, SRC, "executed", "JR2025 J4 assets 1.883844m"),
    ("bud_kruibeke_agb_cash_2025", "2025", CASH, SRC, "executed", "JR2025 J4 cash 0.076768m DROP vs 0.179924m"),
    ("bud_kruibeke_agb_fin_debt_2025", "2025", FIN_DEBT, SRC, "executed", "JR2025 T3 fin debt 1.709928m (LT 1.417651 + ST due 0.292277) vs 1.910678m; all city renteloos; 0 bank 0 leasing"),
    ("bud_kruibeke_agb_lt_debt_2025", "2025", LT_DEBT, SRC, "executed", "JR2025 T3/J4 LT fin debt 1.417651m andere leningen"),
    ("bud_kruibeke_agb_st_due_2025", "2025", ST_DUE, SRC, "executed", "JR2025 T3 ST due within year 0.292277m"),
    ("bud_kruibeke_agb_netto_2025", "2025", NETTO, SRC, "executed", "JR2025 J4 nettoactief thin 0.011244m (kapsub 615 + cum 10629)"),
    ("bud_kruibeke_agb_cum_pnl_2025", "2025", CUM_PNL, SRC, "executed", "JR2025 J4 cum P&L +0.010629m"),
    ("bud_kruibeke_agb_afm_2025", "2025", AFM, SRC, "executed", "JR2025 J2 AFM +0.011972m (AMJP 900)"),
    ("bud_kruibeke_agb_gecorr_afm_2025", "2025", GECORR, SRC, "executed", "JR2025 J2 gecorr AFM +0.163355m (aangewezen 0.152854 vs periodiek 0.304237)"),
    ("bud_kruibeke_agb_bbr_2025", "2025", BBR, SRC, "executed", "JR2025 J2 BBR year +0.012859m (AMJP 900)"),
    ("bud_kruibeke_agb_bbr_avail_2025", "2025", BBR_AVAIL, SRC, "executed", "JR2025 J2 beschikbaar BBR 0.233774m (cum prev 0.220915)"),
    ("bud_kruibeke_agb_expl_uit_2025", "2025", EXPL_UIT, SRC, "executed", "JR2025 J2 expl uitgaven 0.229013m (AMJP 0.222939)"),
    ("bud_kruibeke_agb_expl_ont_2025", "2025", EXPL_ONT, SRC, "executed", "JR2025 J2 expl ontvangsten 0.545222m (AMJP 0.522808)"),
    ("bud_kruibeke_agb_expl_saldo_2025", "2025", EXPL_SALDO, SRC, "executed", "JR2025 J2 expl saldo +0.316209m"),
    ("bud_kruibeke_agb_inv_uit_2025", "2025", INV_UIT, SRC, "executed", "JR2025 J2 invest uitgaven 0.102600m (AMJP 0.158000)"),
    ("bud_kruibeke_agb_inv_saldo_2025", "2025", INV_SALDO, SRC, "executed", "JR2025 J2 invest saldo -0.102600m"),
    ("bud_kruibeke_agb_fin_afl_2025", "2025", FIN_AFL, SRC, "executed", "JR2025 J2/T3 periodieke aflossingen 0.304237m"),
    ("bud_kruibeke_agb_new_loan_2025", "2025", NEW_LOAN, SRC, "executed", "JR2025 T3 new city renteloos 0.103487m (invest 0.102600 + 887 prior-loan correction)"),
    ("bud_kruibeke_agb_pnl_2025", "2025", PNL, SRC, "executed", "JR2025 J5 surplus 0.035215m (opbr 0.545435 / kost 0.510220) full to rechthebbenden"),
    ("bud_kruibeke_agb_prijssub_2025", "2025", PRIJS, SRC, "executed", "JR2025 city prijssubsidie 423059.40 excl BTW exe (AMJP 416000)"),
    ("bud_kruibeke_agb_mva_2025", "2025", MVA, SRC, "executed", "JR2025 J4 MVA 1.482889m (gebouwen 1.380363 + install 0.099292 + meubilair 0.003233)"),
    ("bud_kruibeke_agb_st_recv_2025", "2025", ST_RECV, SRC, "executed", "JR2025 J4 ST recv 0.319677m (ruil 0.151483 + niet-ruil 0.168194)"),
    ("bud_kruibeke_agb_mjp_expl_2026", "2026", MJP_EXPL_2026, SRC2, "budget", "MJP 2026-2031 expl saldo 0.328988m; BBR 10000 AFM 10000"),
    ("bud_kruibeke_agb_mjp_inv_2026", "2026", MJP_INV_2026, SRC2, "budget", "MJP 2026 invest uitgaven 0.345000m city-loan financed"),
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
            "basis": basis,
            "source_id": src,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, year, amt, src, basis, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_kruibeke_agb_city_prijssub_0_42m_2025",
        "AGB Kruibeke 2025 city prijssubsidie 0.423m",
        "423059.40",
        "JR exe 423059.40 excl BTW vs AMJP 416000; needed for VAT-rendabel AGB",
        "Publish 2026-2031 nominative prijssub lock FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_kruibeke_agb_fin_debt_1_71m_2025",
        "AGB Kruibeke YE2025 fin debt 1.710m city renteloos",
        "1709928",
        "T3 LT 1.418m + ST due 0.292m; vs 1.911m 2024; 0 bank 0 leasing; new 0.103m + 887 correction",
        "T3 creditor schedule of city renteloos loans FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_kruibeke_agb_thin_equity_0_01m_2025",
        "AGB Kruibeke YE2025 nettoactief thin 0.011m",
        "11244",
        "J4 nettoactief 11244 vs fin debt 1.710m; full J5 surplus 35215 to rechthebbenden",
        "Why full surplus strip vs thin equity FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_kruibeke_agb_surplus_strip_0_04m_2025",
        "AGB Kruibeke 2025 J5 surplus 0.035m full to rechthebbenden",
        "35215",
        "J5 overschot 35215 entirely A. Rechthebbenden; retained 0",
        "Confirm beneficiary is city + why 0 retained FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_kruibeke_agb_venb_2025_unpublished",
        "AGB Kruibeke VenB/NBB JR2025 not retrieved",
        "",
        "BBC JR2025 public; NBB consult SPA this box; do not invent VenB",
        "Publish working VenB+NBB JR2025 PDF FOI",
        SRC5,
        SRC5_URL,
    ),
    (
        "comm_kruibeke_agb_2026_prijssub_lock_unknown",
        "AGB Kruibeke 2026 city prijssubsidie lock not extracted",
        "",
        "MJP 2026-2031 has evenwicht BBR 10k/yr but no nominative prijssub line",
        "Publish 2026 nominative prijssub lock FOI",
        SRC2,
        SRC2_URL,
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AGB Sport Cultuur Recreatie Kruibeke / AGB BKZ",
            "legal_basis": "Decreet Lokaal Bestuur + AGB Kruibeke + prijssubsidie + JR2025 BBC",
            "decision_date": "2026-06-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}" if env else "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": evurl,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": src,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF + KBO; VenB 2025 unpublished",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_kruibeke_agb_fin_debt_1_71m_2025", "AGB Kruibeke YE2025 fin debt 1.71m city renteloos", "1709928", "7.0", "4.0", "3.0"),
    ("lb_kruibeke_agb_thin_equity_0_01m_2025", "AGB Kruibeke YE2025 nettoactief thin 0.01m vs 1.71m debt", "11244", "8.0", "2.0", "3.0"),
    ("lb_kruibeke_agb_city_prijssub_0_42m_2025", "AGB Kruibeke 2025 city prijssubsidie 0.42m", "423059", "6.0", "3.5", "3.0"),
    ("lb_kruibeke_agb_surplus_strip_0_04m_2025", "AGB Kruibeke 2025 full surplus strip 0.04m to rechthebbenden", "35215", "7.0", "2.0", "2.0"),
    ("lb_kruibeke_agb_cash_drop_0_10m_2025", "AGB Kruibeke cash DROP 0.180m to 0.077m", "103156", "6.5", "2.5", "3.0"),
    ("lb_kruibeke_agb_venb_2025_unpublished", "AGB Kruibeke VenB/NBB JR2025 not retrieved", "423059", "6.0", "3.5", "3.0"),
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
            "tco_notes": "AGB Kruibeke/BKZ JR2025 Entity II sport AGB; fin debt is stock not TCO; VenB internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Sporthal De Dulpop / scheeps-demonstratieloods Rupelmonde / Gemeente BKZ",
            "stated_goal": "Local dual residual sport-AGB map VL JR2025 BKZ",
            "measured_outcome": "assets 1.884m / fin debt 1.710m city renteloos / thin equity 0.011m / city prijssub 0.423m / VenB unpublished",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish VenB 2025 + T3 city-loan schedule + 2026 prijssub lock + city FTE FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive without city GE; VenB unknown",
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
                "VenB/NBB JR2025 working URL (NBB SPA this box) + T3 creditor "
                "schedule of fin debt 1.709928m city renteloos (incl 887 prior-loan "
                "correction) + why cash DROP 179924 to 76768 + why full J5 surplus "
                "35215 to rechthebbenden while nettoactief only 11244 + 2026-2031 "
                "nominative prijssub lock (exe 423059.40 excl BTW) + city-payroll "
                "FTE for De Dulpop / Rupelmonde (BBC geen personeel)"
            ),
            "why_it_matters": (
                "Remaining BKZ Entity II sport AGB after city GE tick883 + Zorgpunt "
                "Waasland 1240: city prijssub 0.42m sits beside a 1.71m renteloos "
                "city-loan shell and thin equity 0.01m while the full 0.035m surplus "
                "is stripped to rechthebbenden. BBC JR2025 is public; VenB 2025 is "
                "not. Distinct from IBOGEM and Zorgpunt Waasland."
            ),
            "priority": "8",
            "recipient_body": "AGB BKZ / Gemeente Beveren-Kruibeke-Zwijndrecht",
            "recipient_email": "info@gemeentebkz.be",
            "recipient_postal": "Gravenplein 8 9120 Beveren",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_kruibeke_agb_fin_debt_1_71m_2025",
            "linked_leaderboard_id": "lb_kruibeke_agb_fin_debt_1_71m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1271",
    "title": "AGB Kruibeke/BKZ sport JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Kruibeke sport JR2025 BBC text + KBO; KBO 0878.836.925; "
        "assets 1.884m / fin debt 1.710m city renteloos / thin equity 0.011m / "
        "city prijssub 0.423m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:55:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1271 AGB Kruibeke/BKZ sport JR2025 dual residual; KBO 0878.836.925; "
        "assets 1.884m fin debt 1.710m city renteloos AFM +0.012m gecorr +0.163m "
        "BBR +0.013m avail 0.234m city prijssub 0.423m cash 0.077m DROP PnL 0.035m "
        "full strip nettoactief 0.011m; VenB unpublished; FOI ready not sent; "
        "next rq_1272 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1272",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa 1260 + AGSO 1261 + AG CIA Erfgoed 1262 "
        "+ AG CIA Kunsten 1263 + AG Energiebesparingsfonds 1264 + AG Digipolis 1265 + Atlas "
        "Antwerpen 1266 + Amal Gent 1267 + Fietsambassade Gent 1268 + Mintus Brugge 1269 "
        "+ AGB MAC Mechelen 1270 + AGB Kruibeke/BKZ sport 1271 done; prefer other unmined "
        "AGB/zorg/EVA with direct PDF/NBB/city HTML — leftover AGB IBOGEM waste if JR2025 "
        "becomes downloadable; skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; "
        "WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; skip Woonzorgnetwerk "
        "Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat unpublished; ebesluit "
        "TLS — prefer org sites / NBB / city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK "
        "only if they have a separate downloadable JR)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1271 after AGB Kruibeke/BKZ sport JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1271", rq_new, rq_spawn)
print("research_queue 1271", found, "spawned_1272", spawned)

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
            "last_unit_id": "rq_1271",
            "ticks_completed": "1271",
            "paused": "no",
            "notes": (
                "tick1271 AGB Kruibeke/BKZ sport JR2025 dual residual; KBO 0878.836.925; "
                "assets 1.884m fin debt 1.710m city renteloos AFM +0.012m gecorr +0.163m "
                "city prijssub 0.423m thin equity 0.011m; VenB unpublished; FOI ready; "
                "next rq_1272 residual dual L5 VL (prefer unmined AGB/zorg/EVA JR2025; "
                "IBOGEM if PDF); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1271 - 2026-08-17 - rq_1271 AGB Kruibeke/BKZ sport dual residual
- Unit: AGB Sport, Cultuur & Recreatie Kruibeke JR2025 Entity II after city BKZ GE tick883 + Zorgpunt Waasland tick1240 (KBO 0878.836.925; AGB since 25.07.2005; renamed AGB Beveren-Kruibeke-Zwijndrecht 30.06.2026; BBC text PDF; RvB 30.06.2026). **Distinct from** IBOGEM (waste AGB, JR2025 unpublished) and Zorgpunt Waasland. Seat JR Onze-Lieve-Vrouwplein 18 9150; KBO seat Gravenplein 8 9120. Venues De Dulpop + Rupelmonde loods. AGSO Knokke already mined 1217 — not redone.
- EUR strong (primary BBC text PDF): assets **1.884m**; cash **0.077m** DROP vs **0.180m**; MVA **1.483m**; fin debt **1.710m** (LT **1.418m** + ST due **0.292m**) all city renteloos, 0 bank/0 leasing, declining vs **1.911m**; new loans **0.103m** (+887 correction); expl **+0.316m** (ontv **0.545m** / uitg **0.229m**); invest **−0.103m**; BBR **+0.013m** / avail **+0.234m**; AFM **+0.012m** / gecorr **+0.163m**; city prijssub **0.423m** exe (AMJP 0.416m); PnL **+0.035m** full to rechthebbenden; **nettoactief thin 0.011m**. Personeel 0 (city payroll). VenB 2025 not retrieved; NBB SPA this box.
- CSVs: sources+5/entities(new+city_bkz note)/budgets+24/commitments+6/leaderboard+6 + FOI ready `gap_kruibeke_agb_thin_equity_0_01m_fin_debt_1_71m_prijssub_0_42m_l5` (not sent); rq_1271=done; spawn rq_1272; ticks=1271. Not a *0 tick — no progress refresh.
- Next: rq_1272 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; IBOGEM only if JR2025 downloadable).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
