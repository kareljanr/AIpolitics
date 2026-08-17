# -*- coding: utf-8 -*-
"""Tick 1273 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AG Museum Leuven JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T10:25:00Z"
TICK = 1273
SRC = "src_agm_leuven_jr2025_bbc"
SRC2 = "src_agm_leuven_mjp2026"
SRC3 = "src_kbo_agm_leuven_0896728376"
SRC4 = "src_nbb_agm_leuven_0896728376"
SRC5 = "src_agm_leuven_jr2025_portal"
SRC6 = "src_agm_leuven_beheer2026"
ENT = "ag_museum_leuven"
CITY = "city_leuven"
SRC_URL = "https://www.mleuven.be/sites/default/files/2026-06/Jaarrekening_MLeuven_2025.pdf"
SRC2_URL = "https://www.mleuven.be/sites/default/files/2026-01/Meerjarenplan_AGM_2026_2031.pdf"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0896728376"
SRC4_URL = "https://consult.cbso.nbb.be/consult-enterprise/0896728376"
SRC5_URL = "https://www.mleuven.be/beleidsdocumenten"
SRC6_URL = "https://www.mleuven.be/sites/default/files/2026-06/Beheers_samenwerkingsovereenkomst_2026_2031.pdf"
GR_URL = "https://besluitvorming.leuven.be/zittingen/25.1003.1677.6034/agendapunten/26.0605.9940.1229"
GAP = "gap_agm_gecorr_afm_neg_0_13m_fin_debt_14_51m_prijssub_5_88m_l5"
HIER = "Vlaanderen>Gemeenten>Leuven>AG_Museum_Leuven"

ASSETS = 16900565.84
CASH = 689414.78
CASH_2024 = 589130.24
FIN_DEBT = 14505996.98
LT_DEBT = 13413791.55
ST_DUE = 1092205.43
DEBT_2024 = 15431978.11
NETTO = 989648.15
CUM_PNL = 841159.15
AFM = 6964.58
GECORR = -126051.67
BBR = 6964.58
BBR_AVAIL = 687438.49
EXPL_UIT = 8156039.15
EXPL_ONT = 9264545.73
EXPL_SALDO = 1108506.58
INV_UIT = 175560.87
INV_SALDO = -175560.87
FIN_AFL = 1101542.00
NEW_LOAN = 175560.87
PNL = 336062.29
DIV = 17826.65
PRIJS = 5880345.12
WERKSUB = 2645062.31
WERK_ALG = 2498199.84
MVA = 14603680.55
ST_RECV = 1015873.09
PERS = 4112312.47
GOODS = 3927240.39
MJP_AFM_2026 = -39250.88
MJP_GECORR_2026 = -133960.74
MJP_BBR_2026 = -39250.88
MJP_WERK_2026 = 2467120.00
MJP_LOAN_2026 = 330000.00
MJP_DEBT_START = 14984201.74


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
            "title": "AG Museum Leuven JR2025 BBC+NBB text PDF",
            "url": SRC_URL,
            "publisher": "AG Museum Leuven / M Leuven",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1273; print 22.05.2026; RvB 27.05.2026; GR 29.06.2026 2026_GR_00290; "
                "KBO 0896.728.376; assets 16.901m; fin debt 14.506m ALL city loans; "
                "AFM +0.007m gecorr -0.126m NEG; city prijssub 5.880m; cash 0.689m JUMP; "
                "PnL 0.336m of which inbreng 0.018m; VTE 52.7; VenB inside same PDF"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AG Museum Leuven MJP 2026-2031",
            "url": SRC2_URL,
            "publisher": "AG Museum Leuven / M Leuven",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1273; 17.12.2025; 2026 AFM -0.039m gecorr -0.134m BBR -0.039m; "
                "werkingssub 2.467m; new loans 0.330m/yr; MJP start debt 14.984m vs JR YE 14.506m"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AG Museum Leuven 0896.728.376",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1273; AGB since 25.06.2007; seat Professor Van Overstraetenplein 1 3000; "
                "3 VE; NACE 91.210+90.312+56.210; RSZ since 01.01.2022; kapitaal 20m statutory; "
                "12 bestuurders; voorzitter Bert Cornillie"
            ),
        },
        {
            "source_id": SRC4,
            "title": "NBB Consult AG Museum Leuven 0896728376 JR filings",
            "url": SRC4_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1273; consult SPA/empty this box; VenB 2025 is inside org-site JR PDF "
                "(verkort schema); do not use Belscope/Companyweb"
            ),
        },
        {
            "source_id": SRC5,
            "title": "M Leuven portal beleidsdocumenten JR2025",
            "url": SRC5_URL,
            "publisher": "M Leuven",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1273; org site lists JR2025 PDF dated 30.06.26 + MJP + beheersovereenkomst; "
                "Leuven besluitvorming portal TLS unexpected-EOF this box; GR HTML via isolated fetch"
            ),
        },
        {
            "source_id": SRC6,
            "title": "AGM-Stad Leuven beheers- en samenwerkingsovereenkomst 2026-2031",
            "url": SRC6_URL,
            "publisher": "AG Museum Leuven / Stad Leuven",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1273; GR 29.06.2026; looptijd 01.07.2026-30.06.2031; art.13 prijssubsidies "
                "no annual euro lock; collectie-aankoop 0.225m/yr + restauratie 0.100m/yr city"
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
            "name_nl": "Autonoom Gemeentebedrijf Museum Leuven (AGM / M Leuven)",
            "name_fr": "Regie communale autonome Musee Louvain",
            "name_en": "Autonomous municipal company Museum Leuven",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC5_URL,
            "foi_email": "info@leuven.be",
            "foi_postal": "Professor Van Overstraetenplein 1 3000 Leuven",
            "notes": (
                "tick1273 JR2025 dual residual; KBO 0896.728.376 AGB since 25.06.2007; "
                "assets 16.901m fin debt 14.506m ALL city loans AFM +0.007m "
                "gecorr -0.126m NEG BBR +0.007m avail 0.687m city prijssub 5.880m "
                "werkingssub 2.645m cash 0.689m JUMP PnL 0.336m inbreng 0.018m "
                "pers 4.112m / 52.7 VTE; VenB in org PDF; FOI " + GAP
            ),
        },
    ],
)
print("entities", n)
print("city_leuven patched", patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    "tick1273 AG Museum Leuven JR2025 dual residual (KBO 0896.728.376; city-loan shell 14.506m + prijssub 5.880m); distinct from AGSL + Zorg Leuven",
    extra_fields={"foi_email": "info@leuven.be"} if True else None,
))

bud_rows = [
    ("bud_agm_assets_2025", "2025", ASSETS, SRC, "executed", "JR2025 J4/NBB assets 16.900566m vs 17.571930m"),
    ("bud_agm_cash_2025", "2025", CASH, SRC, "executed", "JR2025 J4 cash 0.689415m JUMP vs 0.589130m"),
    ("bud_agm_fin_debt_2025", "2025", FIN_DEBT, SRC, "executed", "JR2025 T4 fin debt 14.505997m (LT 13.413792 + ST due 1.092205) vs 15.431978m; ALL city overige leningen; NBB 172/3 bank+leasing 0"),
    ("bud_agm_lt_debt_2025", "2025", LT_DEBT, SRC, "executed", "JR2025 J4/NBB 174 LT city loans 13.413792m"),
    ("bud_agm_st_due_2025", "2025", ST_DUE, SRC, "executed", "JR2025 J4/T4 ST due within year 1.092205m (4240000002 city)"),
    ("bud_agm_netto_2025", "2025", NETTO, SRC, "executed", "JR2025 J4/NBB EV 0.989648m (inbreng 0.100 + reserve 0.010 + retained 0.831 + kapsub 0.048)"),
    ("bud_agm_cum_pnl_2025", "2025", CUM_PNL, SRC, "executed", "JR2025 J4 cum P&L +0.841159m (NBB overgedragen 0.831159 after 0.018 inbreng)"),
    ("bud_agm_afm_2025", "2025", AFM, SRC, "executed", "JR2025 J2 AFM +0.006965m vs MJP -0.114886m"),
    ("bud_agm_gecorr_afm_2025", "2025", GECORR, SRC, "executed", "JR2025 J2 gecorr AFM -0.126052m NEG (aangewezen 1.234558 vs periodiek 1.101542)"),
    ("bud_agm_bbr_2025", "2025", BBR, SRC, "executed", "JR2025 J2 BBR year +0.006965m vs MJP -0.114886m"),
    ("bud_agm_bbr_avail_2025", "2025", BBR_AVAIL, SRC, "executed", "JR2025 J2 beschikbaar BBR 0.687438m (cum prev 0.680474)"),
    ("bud_agm_expl_uit_2025", "2025", EXPL_UIT, SRC, "executed", "JR2025 J2 expl uitgaven 8.156039m"),
    ("bud_agm_expl_ont_2025", "2025", EXPL_ONT, SRC, "executed", "JR2025 J2 expl ontvangsten 9.264546m"),
    ("bud_agm_expl_saldo_2025", "2025", EXPL_SALDO, SRC, "executed", "JR2025 J2 expl saldo +1.108507m"),
    ("bud_agm_inv_uit_2025", "2025", INV_UIT, SRC, "executed", "JR2025 J2 invest uitgaven 0.175561m vs MJP 0.709050m underspend 0.533489m"),
    ("bud_agm_inv_saldo_2025", "2025", INV_SALDO, SRC, "executed", "JR2025 J2 invest saldo -0.175561m (ontv 0)"),
    ("bud_agm_fin_afl_2025", "2025", FIN_AFL, SRC, "executed", "JR2025 J2/T4 periodieke aflossingen 1.101542m all city"),
    ("bud_agm_new_loan_2025", "2025", NEW_LOAN, SRC, "executed", "JR2025 T4 new city loans 0.175561m (= invest)"),
    ("bud_agm_pnl_2025", "2025", PNL, SRC, "executed", "JR2025 J5/NBB surplus 0.336062m (opbr 9.551 / kost 9.215)"),
    ("bud_agm_div_2025", "2025", DIV, SRC, "executed", "JR2025 J5/NBB vergoeding inbreng 0.017827m; retained 0.318236m"),
    ("bud_agm_prijssub_2025", "2025", PRIJS, SRC, "executed", "JR2025 city prijssubsidie 5.880345m exe (~63pct expl ontv; omzet 707); factor FOI"),
    ("bud_agm_werksub_2025", "2025", WERKSUB, SRC, "executed", "JR2025 werkingssub 2.645062m (alg 2.498200 + spec 0.146862); city vs VL split FOI"),
    ("bud_agm_mva_2025", "2025", MVA, SRC, "executed", "JR2025 J4 MVA 14.603681m; leasing 0; buildings 13.666286m; erfgoed 0.049394m"),
    ("bud_agm_st_recv_2025", "2025", ST_RECV, SRC, "executed", "JR2025 J4 ST recv 1.015873m (ruil 0.215400 + niet-ruil 0.800473)"),
    ("bud_agm_pers_2025", "2025", PERS, SRC, "executed", "JR2025 J5 personeel 4.112312m / NBB 52.7 VTE (own payroll; RSZ since 2022)"),
    ("bud_agm_goods_2025", "2025", GOODS, SRC, "executed", "JR2025 J5 goederen 3.927240m"),
    ("bud_agm_mjp_afm_2026", "2026", MJP_AFM_2026, SRC2, "budgeted", "MJP 2026 AFM -0.039251m / gecorr -0.133961m / BBR -0.039251m"),
    ("bud_agm_mjp_werk_2026", "2026", MJP_WERK_2026, SRC2, "budgeted", "MJP 2026 werkingssub 2.467120m (alg 2.317120 + spec 0.150000)"),
    ("bud_agm_mjp_loan_2026", "2026", MJP_LOAN_2026, SRC2, "budgeted", "MJP 2026-2031 new loans 0.330m/yr; repay ~1.10m/yr"),
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
        "comm_agm_prijssub_5_88m_2025",
        "AG Museum Leuven 2025 city prijssubsidie 5.880m",
        "5880345.12",
        "JR exe 5.880345m as omzet 707 ~63pct expl ontv; MJP factor unpublished; beheer art.13 no annual lock",
        "Publish 2026-2031 nominative prijssub lock + coefficient FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_agm_fin_debt_14_51m_2025",
        "AG Museum Leuven YE2025 fin debt 14.506m ALL city loans",
        "14505996.98",
        "T4 LT 13.414m + ST due 1.092m; NBB 174 only (bank+leasing 0); declining vs 15.432m",
        "T4 per-loan city schedule + rate FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_agm_werksub_2_65m_2025",
        "AG Museum Leuven 2025 werkingssubsidies 2.645m",
        "2645062.31",
        "Alg 2.498m + spec 0.147m; MJP cites VL Kunstendecreet/Erfgoeddecreet + city; split FOI",
        "Nominative city vs VL vs project split FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_agm_new_loan_0_18m_2025",
        "AG Museum Leuven 2025 new city loans 0.176m",
        "175560.87",
        "T4 new 0.175561m equals invest; MJP 2026-2031 0.330m/yr",
        "Confirm 2026 draw vs MJP 0.330m FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_agm_mjp_afm_neg_0_04m_2026",
        "AG Museum Leuven MJP 2026 AFM NEG 0.039m path",
        "39250.88",
        "MJP 2026 AFM -0.039m / gecorr -0.134m / BBR -0.039m; start debt 14.984m vs JR 14.506m",
        "Reconcile MJP start debt vs JR YE FOI",
        SRC2,
        SRC2_URL,
    ),
    (
        "comm_agm_nbb_consult_2025_spa",
        "AG Museum Leuven NBB Consult JR2025 SPA this box",
        "",
        "VenB 2025 is inside org-site PDF; NBB consult SPA; do not invent filing number",
        "Publish working NBB Consult URL / neerleggingsnummer FOI",
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
            "beneficiary": "AG Museum Leuven / Stad Leuven",
            "legal_basis": "Decreet Lokaal Bestuur + AGM statuten 25.06.2007 + prijssubsidie + JR2025 BBC/NBB + beheer 2026-2031",
            "decision_date": "2026-05-27",
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
            "notes": f"tick{TICK}; primary BBC+NBB JR2025 text PDF + MJP + KBO; NBB consult SPA",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_agm_prijssub_5_88m_2025", "AG Museum Leuven 2025 city prijssubsidie 5.88m", "5880345", "7.5", "7.0", "3.0"),
    ("lb_agm_fin_debt_14_51m_2025", "AG Museum Leuven YE2025 fin debt 14.51m ALL city loans", "14505997", "7.5", "6.5", "3.0"),
    ("lb_agm_gecorr_afm_neg_0_13m_2025", "AG Museum Leuven gecorr AFM NEG 0.13m", "126052", "7.5", "4.0", "3.0"),
    ("lb_agm_werksub_2_65m_2025", "AG Museum Leuven 2025 werkingssub 2.65m city+VL", "2645062", "6.0", "5.5", "3.0"),
    ("lb_agm_pers_4_11m_52vte_2025", "AG Museum Leuven personnel 4.11m / 52.7 VTE", "4112312", "5.5", "6.0", "3.0"),
    ("lb_agm_mjp_afm_neg_0_04m_2026", "AG Museum Leuven MJP 2026 AFM NEG 0.04m path", "39251", "7.0", "3.5", "3.0"),
    ("lb_agm_nbb_consult_2025_spa", "AG Museum Leuven NBB Consult JR2025 SPA this box", "5880345", "5.5", "5.0", "3.0"),
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
            "tco_notes": "AG Museum Leuven JR2025 Entity II museum AGB; fin debt is stock not TCO; city-loan shell; NBB consult SPA",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "M Leuven / Sint-Pieterskerk / Stad Leuven / visitors",
            "stated_goal": "Local dual residual museum AGB map VL JR2025 Leuven",
            "measured_outcome": "assets 16.901m / fin debt 14.506m ALL city / prijssub 5.880m / gecorr AFM -0.126m / pers 4.112m 52.7 VTE / VenB in org PDF",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish T4 city-loan schedule + prijssub factor 2026-2031 + werksub city/VL split + NBB Consult URL FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC+NBB JR2025 text PDF; not TE-additive without city GE; NBB consult SPA",
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
                "T4 per-loan schedule of fin debt 14.505997m (ALL city 174; bank+leasing 0) "
                "+ prijssubsidie coefficient/lock for 5.880345m (MJP unpublished factor; "
                "beheer art.13 no annual euro) + werkingssub 2.645062m city vs VL "
                "Kunstendecreet/Erfgoeddecreet split + why MJP start debt 14.984m vs JR YE "
                "14.506m + NBB Consult working URL (VenB is in org PDF; consult SPA this box) "
                "+ erfpacht 1 EUR/yr vs buildings 13.666m book"
            ),
            "why_it_matters": (
                "Unmined Leuven Entity II museum AGB: city prijssub 5.88m sits beside a "
                "14.51m all-city loan shell while gecorr AFM is NEG -0.13m and the AGB "
                "pays 0.018m inbreng. BBC+NBB JR2025 is public on the org site; NBB "
                "consult and the city-loan/prijssub factor internals are not. Distinct "
                "from AGSL Leuven and Zorg Leuven."
            ),
            "priority": "8",
            "recipient_body": "AG Museum Leuven / Stad Leuven",
            "recipient_email": "info@leuven.be",
            "recipient_postal": "Professor Van Overstraetenplein 1 3000 Leuven",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agm_fin_debt_14_51m_2025",
            "linked_leaderboard_id": "lb_agm_fin_debt_14_51m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1273",
    "title": "AG Museum Leuven JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AG Museum Leuven JR2025 BBC+NBB text + MJP + KBO; KBO 0896.728.376; "
        "assets 16.901m / fin debt 14.506m ALL city / city prijssub 5.880m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T10:05:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1273 AG Museum Leuven JR2025 dual residual; KBO 0896.728.376; "
        "assets 16.901m fin debt 14.506m ALL city AFM +0.007m gecorr -0.126m NEG "
        "BBR +0.007m avail 0.687m city prijssub 5.880m werksub 2.645m cash 0.689m JUMP "
        "PnL 0.336m inbreng 0.018m pers 4.112m / 52.7 VTE; VenB in org PDF; NBB consult SPA; "
        "FOI ready not sent; next rq_1274 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1274",
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
        "+ AGB MAC Mechelen 1270 + AGB Kruibeke/BKZ sport 1271 + AGB Tienen 1272 "
        "+ AG Museum Leuven 1273 done; prefer other unmined AGB/zorg/EVA with direct "
        "PDF/NBB/city HTML — leftover AGB IBOGEM waste if JR2025 becomes downloadable; "
        "City Tienen GE+OCMW JR2025 is published (different unit than AGB Tienen); "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; WAGSO already mined "
        "tick1199; skip Mobil-O/AG EOS inactive; skip Woonzorgnetwerk Edegem / "
        "Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat unpublished; ebesluit TLS + "
        "Leuven besluitvorming TLS — prefer org sites / NBB / city HTML; Brugge SAS / "
        "Blauwe Lelie / SPOOR / WOK only if they have a separate downloadable JR)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1273 after AG Museum Leuven JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1273", rq_new, rq_spawn)
print("research_queue 1273", found, "spawned_1274", spawned)

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
            "last_unit_id": "rq_1273",
            "ticks_completed": "1273",
            "paused": "no",
            "notes": (
                "tick1273 AG Museum Leuven JR2025 dual residual; KBO 0896.728.376; "
                "assets 16.901m fin debt 14.506m ALL city AFM +0.007m gecorr -0.126m NEG "
                "city prijssub 5.880m werksub 2.645m cash 0.689m JUMP; VenB in org PDF; "
                "NBB consult SPA; FOI ready; next rq_1274 residual dual L5 VL (prefer unmined "
                "AGB/zorg/EVA JR2025; IBOGEM if PDF; City Tienen GE+OCMW if picked); "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1273 - 2026-08-17 - rq_1273 AG Museum Leuven dual residual
- Unit: Autonoom Gemeentebedrijf Museum Leuven (AGM / M Leuven) JR2025 Entity II after AGSL Leuven tick1237 + Zorg Leuven tick1241 + AGB Tienen tick1272 (KBO 0896.728.376; AGB since 25.06.2007; BBC+NBB text PDF on org site; print 22.05.2026; RvB 27.05.2026 / GR 29.06.2026 `2026_GR_00290`). **Distinct from** AGSL (0870.310.526) and Zorg Leuven. Seat Professor Van Overstraetenplein 1 3000. Venues M Leuven + Sint-Pieterskerk. AD Peter Bary / voorzitter Bert Cornillie / commissaris Baker Tilly. IBOGEM JR2025 still unpublished — not redone. Leuven besluitvorming TLS unexpected-EOF this box; org-site PDF fetched.
- EUR strong (primary BBC+NBB text PDF): assets **16.901m** (was 17.572m); cash **0.689m** JUMP vs **0.589m**; MVA **14.604m** leasing **0** buildings **13.666m**; fin debt **14.506m** (LT **13.414m** + ST due **1.092m**) **ALL city overige leningen** (NBB 172/3 bank+leasing **0**), declining vs **15.432m**; new city loans **0.176m** (= invest); expl **+1.109m** (ontv **9.265m** / uitg **8.156m**); invest **−0.176m** (vs MJP 0.709m underspend **0.533m**); BBR **+0.007m** / avail **+0.687m**; AFM **+0.007m** / **gecorr −0.126m NEG**; city prijssub **5.880m** exe (~63pct expl ontv) + werksub **2.645m** (alg 2.498 + spec 0.147; city/VL split FOI); PnL **+0.336m** of which inbreng **0.018m**; personeel **4.112m** / **52.7 VTE**. MJP 2026–2031: AFM **−0.039m** / gecorr **−0.134m** / BBR **−0.039m**; new loans **0.330m**/yr; start debt **14.984m** vs JR YE **14.506m**. VenB 2025 is inside the org PDF; NBB consult SPA this box.
- CSVs: sources+6/entities(new AGM + city note)/budgets+29/commitments+6/leaderboard+7 + FOI ready `gap_agm_gecorr_afm_neg_0_13m_fin_debt_14_51m_prijssub_5_88m_l5` (not sent); rq_1273=done; spawn rq_1274; ticks=1273. Not a *0 tick — no progress refresh.
- Next: rq_1274 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; IBOGEM only if JR2025 downloadable; City Tienen GE+OCMW JR2025 published as a different unit).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
