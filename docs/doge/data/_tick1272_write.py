# -*- coding: utf-8 -*-
"""Tick 1272 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AGB Tienen JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T10:05:00Z"
TICK = 1272
SRC = "src_agb_tienen_jr2025_bbc"
SRC2 = "src_agb_tienen_mjp2026"
SRC3 = "src_kbo_agb_tienen_0872382861"
SRC4 = "src_nbb_agb_tienen_0872382861"
SRC5 = "src_agb_tienen_jr2025_portal"
ENT = "agb_tienen"
CITY = "city_tienen"
SRC_URL = "https://www.tienen.be/sites/default/files/2026-06/Jaarrekening-2025-AGB.pdf"
SRC2_URL = "https://www.tienen.be/sites/default/files/2025-12/AGB-Tienen-MJP-2026-2031-Beleidsrapport.pdf"
SRC2_PAGE = "https://www.tienen.be/menu/stad-en-bestuur/beleidsplannen-en-jaarrekening/beleidsplan-agb-tienen-2026-2031"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0872382861"
SRC4_URL = "https://consult.cbso.nbb.be/consult-enterprise/0872382861"
SRC5_URL = "https://www.tienen.be/menu/stad-en-bestuur/beleidsplannen-en-jaarrekening/jaarrekening-agb-2025"
GAP = "gap_tienen_agb_fin_debt_16_93m_city_loan_10_5m_prijssub_1_99m_l5"
HIER = "Vlaanderen>Gemeenten>Tienen>AGB_Tienen"

ASSETS = 24283259.00
CASH = 344130.00
CASH_2024 = 763759.00
FIN_DEBT = 16925793.00
LT_DEBT = 15463778.00
ST_DUE = 1462014.00
DEBT_2024 = 16262406.00
CITY_LOAN = 10500000.00
NETTO = 5353696.00
CUM_PNL = 275634.00
AFM = 73379.00
GECORR = 161656.00
BBR = -448190.00
BBR_AVAIL = 438914.00
EXPL_UIT = 2459953.00
EXPL_ONT = 3922601.00
EXPL_SALDO = 1462649.00
INV_UIT = 2583701.00
INV_SALDO = -2574226.00
FIN_AFL = 1389270.00
NEW_LOAN = 2052657.00
PNL = 94813.00
DIV = 25000.00
PRIJS = 1993499.00
MVA = 22693627.00
ST_RECV = 1122601.00
PERS = 37591.00
INT = 298099.00
MJP_EXPL_2026 = 1384799.00
MJP_AFM_2026 = -189291.00
MJP_GECORR_2026 = -59535.00
MJP_BBR_2026 = 467397.00
MJP_INV_2026 = 3975688.00
MJP_LOAN_2026 = 3975688.00
MJP_PRIJS_MY = 14400000.00
MJP_CITY_LOAN_MY = 12100000.00


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
            "title": "AGB Tienen JR2025 BBC text PDF",
            "url": SRC_URL,
            "publisher": "AGB Tienen / Stad Tienen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1272; RvB 01.06.2026; print 29.04.2026; KBO 0872.382.861; "
                "assets 24.283m; fin debt 16.926m (city renteloos ~10.5m + bank); "
                "AFM +0.073m gecorr +0.162m; city prijssub 1.993m; cash 0.344m DROP; "
                "PnL 0.095m of which dividend 0.025m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGB Tienen MJP 2026-2031 beleidsrapport",
            "url": SRC2_URL,
            "publisher": "AGB Tienen / Stad Tienen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1272; GR 11.12.2025; print 24.11.2025; page "
                + SRC2_PAGE
                + "; 2026 AFM -0.189m gecorr -0.060m BBR 0.467m; MY prijssub 14.4m "
                "city loan 12.1m; profit objective 35k/yr"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB Tienen 0872.382.861",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1272; AGB since 17.09.2004; seat Grote Markt 27 3300 Tienen; "
                "8 VE; NACE 68.201+84.114; RSZ since 01.01.2022; bestuurder "
                "Jonathan Holslag since 05.12.2024; KBO dump 16.08.2026"
            ),
        },
        {
            "source_id": SRC4,
            "title": "NBB Consult AGB Tienen 0872382861 JR filings",
            "url": SRC4_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1272; consult SPA/empty this box; VenB 2025 not retrieved; "
                "do not use Belscope/Companyweb"
            ),
        },
        {
            "source_id": SRC5,
            "title": "Stad Tienen portal Jaarrekening AGB 2025",
            "url": SRC5_URL,
            "publisher": "Stad Tienen",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1272; portal lists JR2025 AGB + city/OCMW 2025; city GE not mined this tick"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": CITY,
            "name_nl": "Stad Tienen",
            "name_fr": "Ville de Tirlemont",
            "name_en": "City of Tienen",
            "level": "local",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.tienen.be",
            "foi_email": "info@tienen.be",
            "foi_postal": "Grote Markt 27 3300 Tienen",
            "notes": (
                "stub parent tick1272; NIS 24107; GE+OCMW JR2025 published "
                "https://www.tienen.be/sites/default/files/2026-06/Jaarrekening-2025-Stad-en-OCMW.pdf "
                "not mined this tick; AGB dual residual tick1272"
            ),
        },
        {
            "entity_id": ENT,
            "name_nl": "Autonoom Gemeentebedrijf Tienen",
            "name_fr": "Regie communale autonome Tirlemont",
            "name_en": "Autonomous municipal company Tienen",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC5_URL,
            "foi_email": "info@tienen.be",
            "foi_postal": "Grote Markt 27 3300 Tienen",
            "notes": (
                "tick1272 JR2025 dual residual; KBO 0872.382.861 AGB since 17.09.2004; "
                "assets 24.283m fin debt 16.926m (city renteloos ~10.5m + bank) AFM +0.073m "
                "gecorr +0.162m BBR -0.448m avail 0.439m city prijssub 1.993m cash 0.344m DROP "
                "PnL 0.095m div 0.025m; VenB unpublished; FOI " + GAP
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_tienen_agb_assets_2025", "2025", ASSETS, SRC, "executed", "JR2025 J4 assets 24.283259m vs 23.088024m"),
    ("bud_tienen_agb_cash_2025", "2025", CASH, SRC, "executed", "JR2025 J4 cash 0.344130m DROP vs 0.763759m"),
    ("bud_tienen_agb_fin_debt_2025", "2025", FIN_DEBT, SRC, "executed", "JR2025 T4 fin debt 16.925793m (LT 15.463778 + ST due 1.462014) vs 16.262406m; city renteloos ~10.5m + bank; 0 leasing"),
    ("bud_tienen_agb_lt_debt_2025", "2025", LT_DEBT, SRC, "executed", "JR2025 J4/T4 LT fin debt 15.463778m"),
    ("bud_tienen_agb_st_due_2025", "2025", ST_DUE, SRC, "executed", "JR2025 J4/T4 ST due within year 1.462014m"),
    ("bud_tienen_agb_city_loan_2025", "2025", CITY_LOAN, SRC, "executed", "JR2025 verslag city renteloos stock ~10.5m of 16.926m; exact T4 creditor split FOI"),
    ("bud_tienen_agb_netto_2025", "2025", NETTO, SRC, "executed", "JR2025 J4 nettoactief 5.353696m (kapsub 1.117 + cum 0.276 + herw 0.945 + overig 3.016)"),
    ("bud_tienen_agb_cum_pnl_2025", "2025", CUM_PNL, SRC, "executed", "JR2025 J4 cum P&L +0.275634m"),
    ("bud_tienen_agb_afm_2025", "2025", AFM, SRC, "executed", "JR2025 J2 AFM +0.073379m vs MJP -0.230417m"),
    ("bud_tienen_agb_gecorr_afm_2025", "2025", GECORR, SRC, "executed", "JR2025 J2 gecorr AFM +0.161656m (aangewezen 1.300992 vs periodiek 1.389270)"),
    ("bud_tienen_agb_bbr_2025", "2025", BBR, SRC, "executed", "JR2025 J2 BBR year -0.448190m vs MJP -0.230417m"),
    ("bud_tienen_agb_bbr_avail_2025", "2025", BBR_AVAIL, SRC, "executed", "JR2025 J2 beschikbaar BBR 0.438914m (cum prev 0.887105)"),
    ("bud_tienen_agb_expl_uit_2025", "2025", EXPL_UIT, SRC, "executed", "JR2025 J2 expl uitgaven 2.459953m"),
    ("bud_tienen_agb_expl_ont_2025", "2025", EXPL_ONT, SRC, "executed", "JR2025 J2 expl ontvangsten 3.922601m"),
    ("bud_tienen_agb_expl_saldo_2025", "2025", EXPL_SALDO, SRC, "executed", "JR2025 J2 expl saldo +1.462649m"),
    ("bud_tienen_agb_inv_uit_2025", "2025", INV_UIT, SRC, "executed", "JR2025 J2 invest uitgaven 2.583701m (Houtemveld/zwembad/CC)"),
    ("bud_tienen_agb_inv_saldo_2025", "2025", INV_SALDO, SRC, "executed", "JR2025 J2 invest saldo -2.574226m (ontv 9475 VL/Cultuurconnect)"),
    ("bud_tienen_agb_fin_afl_2025", "2025", FIN_AFL, SRC, "executed", "JR2025 J2/T4 periodieke aflossingen 1.389270m (bank ~0.865 + city 0.324)"),
    ("bud_tienen_agb_new_loan_2025", "2025", NEW_LOAN, SRC, "executed", "JR2025 T4 new city renteloos 2.052657m (vs MJP 3.240914m underspend)"),
    ("bud_tienen_agb_pnl_2025", "2025", PNL, SRC, "executed", "JR2025 J5 surplus 0.094813m (opbr 3.762 / kost 3.667)"),
    ("bud_tienen_agb_div_2025", "2025", DIV, SRC, "executed", "JR2025 J5 rechthebbenden 0.025000m; retained 0.069813m; MJP profit objective 0.035m"),
    ("bud_tienen_agb_prijssub_2025", "2025", PRIJS, SRC, "executed", "JR2025 city prijssubsidie 1.993499m exe (~51pct of werking; vs 2024 1.600841m)"),
    ("bud_tienen_agb_mva_2025", "2025", MVA, SRC, "executed", "JR2025 J4 MVA 22.693627m; leasing 0"),
    ("bud_tienen_agb_st_recv_2025", "2025", ST_RECV, SRC, "executed", "JR2025 J4 ST recv 1.122601m (ruil 0.434 + niet-ruil 0.689)"),
    ("bud_tienen_agb_pers_2025", "2025", PERS, SRC, "executed", "JR2025 J5 personeel 0.037591m DROP vs 0.085775m; city-payroll FTE FOI"),
    ("bud_tienen_agb_int_2025", "2025", INT, SRC, "executed", "JR2025 T2 intrestlasten 0.298099m declining"),
    ("bud_tienen_agb_mjp_expl_2026", "2026", MJP_EXPL_2026, SRC2, "budgeted", "MJP 2026-2031 expl saldo 1.384799m; AFM -0.189291m"),
    ("bud_tienen_agb_mjp_afm_2026", "2026", MJP_AFM_2026, SRC2, "budgeted", "MJP 2026 AFM -0.189291m / gecorr -0.059535m / BBR avail 0.467397m"),
    ("bud_tienen_agb_mjp_inv_2026", "2026", MJP_INV_2026, SRC2, "budgeted", "MJP 2026 invest saldo -3.975688m city-loan financed 3.975688m"),
    ("bud_tienen_agb_mjp_prijs_my", "2026", MJP_PRIJS_MY, SRC2, "budgeted", "MJP 2026-2031 city prijssub 14.4m + city loan 12.1m + zakelijke rechten 1.6m"),
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
        "comm_tienen_agb_city_prijssub_1_99m_2025",
        "AGB Tienen 2025 city prijssubsidie 1.993m",
        "1993499",
        "JR exe 1.993499m vs 2024 1.600841m; ~51pct of werking; MJP MY 14.4m",
        "Publish 2026 nominative prijssub lock + factor FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_tienen_agb_fin_debt_16_93m_2025",
        "AGB Tienen YE2025 fin debt 16.926m city+bank",
        "16925793",
        "T4 LT 15.464m + ST due 1.462m; city renteloos ~10.5m + bank; new city 2.053m; 0 leasing",
        "T4 creditor schedule city vs bank FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_tienen_agb_city_loan_10_5m_2025",
        "AGB Tienen YE2025 city renteloos stock ~10.5m",
        "10500000",
        "Verslag ~10.5m of 16.926m; since 2015 city on-lend; repay 0.324m 2025; exact split FOI",
        "Per-loan restant + rate 0 city FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_tienen_agb_new_loan_2_05m_2025",
        "AGB Tienen 2025 new city renteloos 2.053m",
        "2052657",
        "T4 new 2.052657m vs MJP 3.240914m; invest underspend + VL Hal1 sub delayed",
        "Confirm 2026 draw vs MJP 3.976m FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_tienen_agb_mjp_prijs_14_4m_2026_2031",
        "AGB Tienen MJP 2026-2031 city prijssub 14.4m",
        "14400000",
        "MJP beleidsrapport 14.4m prijssub + 12.1m city loan + 1.6m zakelijke rechten; AFM NEG path",
        "Year-split nominative prijssub 2026-2031 FOI",
        SRC2,
        SRC2_URL,
    ),
    (
        "comm_tienen_agb_venb_2025_unpublished",
        "AGB Tienen VenB/NBB JR2025 not retrieved",
        "",
        "BBC JR2025 public; NBB consult SPA this box; do not invent VenB",
        "Publish working VenB+NBB JR2025 PDF FOI",
        SRC4,
        SRC4_URL,
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AGB Tienen / Stad Tienen",
            "legal_basis": "Decreet Lokaal Bestuur + AGB Tienen + prijssubsidie + JR2025 BBC",
            "decision_date": "2026-06-01",
            "start_year": "2025",
            "end_year": "2025" if "mjp" not in cid else "2031",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}" if env and "mjp" not in cid else (f"2026-2031:{env}" if env else ""),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": evurl,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": src,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF + MJP + KBO; VenB 2025 unpublished",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_tienen_agb_fin_debt_16_93m_2025", "AGB Tienen YE2025 fin debt 16.93m city+bank", "16925793", "7.0", "6.5", "3.0"),
    ("lb_tienen_agb_city_loan_10_5m_2025", "AGB Tienen YE2025 city renteloos ~10.5m", "10500000", "7.0", "6.0", "3.0"),
    ("lb_tienen_agb_city_prijssub_1_99m_2025", "AGB Tienen 2025 city prijssubsidie 1.99m", "1993499", "6.5", "5.0", "3.0"),
    ("lb_tienen_agb_new_loan_2_05m_2025", "AGB Tienen 2025 new city renteloos 2.05m", "2052657", "6.0", "5.0", "3.0"),
    ("lb_tienen_agb_cash_drop_0_42m_2025", "AGB Tienen cash DROP 0.764m to 0.344m", "419629", "6.5", "3.5", "3.0"),
    ("lb_tienen_agb_mjp_afm_neg_0_19m_2026", "AGB Tienen MJP 2026 AFM NEG 0.19m path", "189291", "7.0", "3.5", "3.0"),
    ("lb_tienen_agb_venb_2025_unpublished", "AGB Tienen VenB/NBB JR2025 not retrieved", "1993499", "6.0", "5.0", "3.0"),
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
            "tco_notes": "AGB Tienen JR2025 Entity II culture/sport/patrimonium AGB; fin debt is stock not TCO; VenB internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "CC De Kruisboog / stedelijk zwembad / Houtemveld / Stad Tienen",
            "stated_goal": "Local dual residual culture-sport-patrimonium AGB map VL JR2025 Tienen",
            "measured_outcome": "assets 24.283m / fin debt 16.926m city+bank / city prijssub 1.993m / AFM +0.073m / MJP AFM NEG / VenB unpublished",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish VenB 2025 + T4 city-vs-bank schedule + 2026 prijssub lock + city FTE FOI",
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
                "VenB/NBB JR2025 working URL (NBB SPA this box) + T4 creditor "
                "schedule of fin debt 16.925793m split city renteloos ~10.5m vs bank "
                "+ why cash DROP 763759 to 344130 + nominative 2026-2031 prijssub "
                "year-split (exe 2025 1.993499m; MJP MY 14.4m) + city-payroll FTE "
                "for CC De Kruisboog / zwembad / Houtemveld (BBC personeel only 37591) "
                "+ why MJP start debt 18.054m vs JR YE2025 16.926m"
            ),
            "why_it_matters": (
                "Unmined Tienen Entity II culture/sport/patrimonium AGB: city "
                "prijssub 1.99m sits beside a 16.93m city+bank debt shell "
                "(~10.5m renteloos city on-lend since 2015) while cash drops "
                "0.42m and MJP 2026-2031 locks AFM NEG. BBC JR2025 is public; "
                "VenB 2025 is not. Distinct from IBOGEM and AGB Kruibeke/BKZ."
            ),
            "priority": "8",
            "recipient_body": "AGB Tienen / Stad Tienen",
            "recipient_email": "info@tienen.be",
            "recipient_postal": "Grote Markt 27 3300 Tienen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_tienen_agb_fin_debt_16_93m_2025",
            "linked_leaderboard_id": "lb_tienen_agb_fin_debt_16_93m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1272",
    "title": "AGB Tienen JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Tienen JR2025 BBC text + MJP + KBO; KBO 0872.382.861; "
        "assets 24.283m / fin debt 16.926m city+bank / city prijssub 1.993m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T09:30:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1272 AGB Tienen JR2025 dual residual; KBO 0872.382.861; "
        "assets 24.283m fin debt 16.926m city renteloos ~10.5m + bank AFM +0.073m "
        "gecorr +0.162m BBR -0.448m avail 0.439m city prijssub 1.993m cash 0.344m DROP "
        "PnL 0.095m div 0.025m; VenB unpublished; FOI ready not sent; "
        "next rq_1273 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1273",
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
        "+ AGB MAC Mechelen 1270 + AGB Kruibeke/BKZ sport 1271 + AGB Tienen 1272 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML — leftover AGB "
        "IBOGEM waste if JR2025 becomes downloadable; skip AGSO Knokke-Heist already 1217; "
        "skip AGB Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat "
        "unpublished; ebesluit TLS — prefer org sites / NBB / city HTML; Brugge SAS / "
        "Blauwe Lelie / SPOOR / WOK only if they have a separate downloadable JR)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1272 after AGB Tienen JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1272", rq_new, rq_spawn)
print("research_queue 1272", found, "spawned_1273", spawned)

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
            "last_unit_id": "rq_1272",
            "ticks_completed": "1272",
            "paused": "no",
            "notes": (
                "tick1272 AGB Tienen JR2025 dual residual; KBO 0872.382.861; "
                "assets 24.283m fin debt 16.926m city renteloos ~10.5m + bank AFM +0.073m "
                "gecorr +0.162m city prijssub 1.993m cash 0.344m DROP; VenB unpublished; "
                "FOI ready; next rq_1273 residual dual L5 VL (prefer unmined AGB/zorg/EVA "
                "JR2025; IBOGEM if PDF); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1272 - 2026-08-17 - rq_1272 AGB Tienen dual residual
- Unit: Autonoom Gemeentebedrijf Tienen JR2025 Entity II after AGB Kruibeke/BKZ sport tick1271 (KBO 0872.382.861; AGB since 17.09.2004; BBC text PDF; RvB 01.06.2026). **Distinct from** IBOGEM (waste AGB, JR2025 unpublished) and AGB Kruibeke/BKZ. Seat Grote Markt 27 3300. Venues CC De Kruisboog + stedelijk zwembad + Houtemveld. AD Patricia Willems / FD Ans Aerts. City Tienen GE+OCMW JR2025 published but not mined this tick. AGSO Knokke already mined 1217 — not redone.
- EUR strong (primary BBC text PDF): assets **24.283m** (was 23.088m); cash **0.344m** DROP vs **0.764m**; MVA **22.694m** leasing **0**; fin debt **16.926m** (LT **15.464m** + ST due **1.462m**) city renteloos **~10.5m** + bank, rising vs **16.262m**; new city loans **2.053m** (vs MJP 3.241m); expl **+1.463m** (ontv **3.923m** / uitg **2.460m**); invest **−2.574m** (uitg **2.584m**); BBR **−0.448m** / avail **+0.439m**; AFM **+0.073m** / gecorr **+0.162m**; city prijssub **1.993m** exe (was 1.601m); PnL **+0.095m** of which dividend **0.025m**; personeel **0.038m**. MJP 2026–2031: AFM **−0.189m** / gecorr **−0.060m** / BBR **0.467m**; MY prijssub **14.4m** + city loan **12.1m**. VenB 2025 not retrieved; NBB SPA this box.
- CSVs: sources+5/entities(new city stub + AGB)/budgets+30/commitments+6/leaderboard+7 + FOI ready `gap_tienen_agb_fin_debt_16_93m_city_loan_10_5m_prijssub_1_99m_l5` (not sent); rq_1272=done; spawn rq_1273; ticks=1272. Not a *0 tick — no progress refresh.
- Next: rq_1273 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; IBOGEM only if JR2025 downloadable).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
