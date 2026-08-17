# -*- coding: utf-8 -*-
"""Tick 1275 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AGB IBOGEM JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T09:25:00Z"
TICK = 1275
SRC = "src_ibogem_jr2025_jaarverslag"
SRC2 = "src_ibogem_portal_verslagen"
SRC3 = "src_kbo_ibogem_1023770068"
SRC4 = "src_nbb_ibogem_1023770068"
SRC5 = "src_ibogem_beleidsplan_2025_2030"
ENT = "agb_ibogem"
CITY = "city_bkz"
SRC_URL = "https://www.ibogem.be/wp-content/uploads/2026/07/Jaarverslag-2025_def-XLR.pdf"
SRC2_URL = "https://www.ibogem.be/over/verslagen/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=1023770068"
SRC4_URL = "https://consult.cbso.nbb.be/consult-enterprise/1023770068"
SRC5_URL = "https://www.ibogem.be/wp-content/uploads/2026/01/Beleidsplan-2025-2030_DEF_LR.pdf"
GAP = "gap_ibogem_pension_4_95m_bbc_opaque_city_dual_6_20m_l5"
HIER = "Vlaanderen>Gemeenten>BKZ>AGB_Ibogem"

ASSETS = 11773383.30
ASSETS_2024 = 13368869.61
CASH = 488587.16
INVEST = 3907267.73
EQUITY = 3577976.59
EQUITY_2024 = 3384302.62
PENSION = 4950069.22
SCHULDEN = 3245337.49
ST_DEBT = 3142212.84
TRADE = 1445582.00
PREPAY = 1400324.88
MVA = 6737126.66
BUILDINGS = 4340272.71
FIXED = 6791699.26
CURRENT = 4981684.04
OMZET = 5148030.22
OTHER_REV = 6969334.17
OPBR = 12129796.53
KOST = 12230866.83
EBIT = -101070.30
FIN_INC = 239898.89
FIN_COST = 14151.11
FIN_RESULT = 225747.78
PNL = 93700.94
PNL_2024 = 62326.66
RETAINED = 182262.42
CITY_LOCK = 6197950.61
KW_OMZET = 595432.62
RP_OMZET = 493225.89
KW_LOSS = 352007.76
RP_LOSS = 797022.26
PERS = 2804574.06
KAPSUB = 955165.47
INBR = 1914189.90
VTE = 39.7


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
            "title": "AGB Ibogem Jaarverslag 2025 + NBB VOL-inb JR",
            "url": SRC_URL,
            "publisher": "AGB Ibogem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1275; published July 2026; AV 30.06.2026; KBO 1023.770.068; "
                "assets 11.773m vs IGS 13.369m; pension 4.950m; fin debt 0; "
                "city dual vennoten 6.198m; PnL 0.094m; cash 0.489m + invest 3.907m; "
                "BBC J2 not in this PDF"
            ),
        },
        {
            "source_id": SRC2,
            "title": "IBOGEM portal verslagen (JR2025 jaarverslag link)",
            "url": SRC2_URL,
            "publisher": "AGB Ibogem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1275; 30.06.2026 jaarverslag row; prior ticks said JR unpublished",
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB Ibogem 1023.770.068",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1275; AGB since 19.09.2025; seat Schaarbeekstraat 27 9120; "
                "7 VE; NACE 38.110; RSZ+BTW; bestuurders Beeldens + Van Hove; "
                "successor of IGS 0213.384.063"
            ),
        },
        {
            "source_id": SRC4,
            "title": "NBB Consult AGB Ibogem 1023770068 JR filings",
            "url": SRC4_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1275; VenB 2025 is inside org jaarverslag PDF (VOL-inb); "
                "NBB consult often 403/SPA this box; do not use Belscope/Companyweb"
            ),
        },
        {
            "source_id": SRC5,
            "title": "AGB Ibogem Beleidsplan 2025-2030",
            "url": SRC5_URL,
            "publisher": "AGB Ibogem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1275; policy plan Jan 2026; action budgets mostly 'regulier budget'; "
                "not a BBC J2 substitute; no invented AFM/BBR"
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
            "name_nl": "AGB Ibogem (Autonoom Gemeentebedrijf duurzaam afvalbeheer BKZ)",
            "name_fr": "Regie communale autonome Ibogem",
            "name_en": "Autonomous municipal company Ibogem waste BKZ",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC2_URL,
            "foi_email": "info@ibogem.be",
            "foi_postal": "Schaarbeekstraat 27 9120 Beveren",
            "notes": (
                "tick1275 JR2025 dual residual; KBO 1023.770.068 AGB since 19.09.2025 "
                "(ops 01.01.2025 after IGS 0213.384.063 dissolution); assets 11.773m "
                "pension 4.950m fin debt 0 city dual 6.198m cash 0.489m invest 3.907m "
                "PnL 0.094m pers 2.805m / 39.7 VTE; BBC J2 unpublished; FOI " + GAP
            ),
        },
    ],
)
print("entities", n)
print(
    "city_bkz patched",
    patch_entity_notes_line(
        DATA / "entities.csv",
        CITY,
        "tick1275 AGB Ibogem JR2025 dual residual (KBO 1023.770.068; pension 4.950m + city dual 6.198m; fin debt 0); distinct from AGB Kruibeke/BKZ sport",
    ),
)

bud_rows = [
    ("bud_ibogem_assets_2025", "2025", ASSETS, SRC, "executed", "NBB 20/58 assets 11.773383m vs IGS YE2024 13.368870m drop 1.595m"),
    ("bud_ibogem_assets_igs_2024", "2024", ASSETS_2024, SRC, "executed", "IGS predecessor YE2024 assets 13.368870m cited in AGB jaarverslag"),
    ("bud_ibogem_cash_2025", "2025", CASH, SRC, "executed", "NBB 54/58 cash 0.488587m + beleggingen 3.907268m = liquid-ish 4.396m"),
    ("bud_ibogem_invest_2025", "2025", INVEST, SRC, "executed", "NBB 50/53 overige beleggingen 3.907268m"),
    ("bud_ibogem_equity_2025", "2025", EQUITY, SRC, "executed", "NBB 10/15 EV 3.577977m vs IGS 3.384303m; inbreng 1.914 + kapsub 0.955 + retained 0.182"),
    ("bud_ibogem_pension_2025", "2025", PENSION, SRC, "executed", "NBB 160 pension provision 4.950069m = 42pct assets; actuarial basis FOI"),
    ("bud_ibogem_schulden_2025", "2025", SCHULDEN, SRC, "executed", "NBB 17/49 debts 3.245337m; LT fin 170/4 = 0; ST 3.142213m"),
    ("bud_ibogem_fin_debt_2025", "2025", 0, SRC, "executed", "NBB 170/4 and 43 empty; Verrebroek 2015 loan prepaid; fin cost drop 0.029 to 0.014m"),
    ("bud_ibogem_st_debt_2025", "2025", ST_DEBT, SRC, "executed", "NBB 42/48 ST 3.142213m (trade 1.446 + prepay 1.400 + tax/soc 0.296)"),
    ("bud_ibogem_trade_2025", "2025", TRADE, SRC, "executed", "NBB 44 trade 1.445582m"),
    ("bud_ibogem_prepay_2025", "2025", PREPAY, SRC, "executed", "NBB 46 vooruitbetalingen 1.400325m"),
    ("bud_ibogem_mva_2025", "2025", MVA, SRC, "executed", "NBB 22/27 MVA 6.737127m; buildings 4.340273; machines 1.540581; leasing 0"),
    ("bud_ibogem_buildings_2025", "2025", BUILDINGS, SRC, "executed", "NBB 22 terreinen en gebouwen 4.340273m"),
    ("bud_ibogem_omzet_2025", "2025", OMZET, SRC, "executed", "NBB 70 omzet 5.148030m; andere bedrijfsopbr 6.969334m"),
    ("bud_ibogem_opbr_2025", "2025", OPBR, SRC, "executed", "NBB 70/76A bedrijfsopbrengsten 12.129797m vs IGS 12.034664m"),
    ("bud_ibogem_kost_2025", "2025", KOST, SRC, "executed", "NBB 60/66A bedrijfskosten 12.230867m vs IGS 12.180426m"),
    ("bud_ibogem_ebit_2025", "2025", EBIT, SRC, "executed", "NBB 9901 EBIT -0.101070m"),
    ("bud_ibogem_fin_result_2025", "2025", FIN_RESULT, SRC, "executed", "fin opbr 0.239899 - fin kost 0.014151 = +0.225748m"),
    ("bud_ibogem_pnl_2025", "2025", PNL, SRC, "executed", "NBB 9904/9905 surplus 0.093701m vs IGS 0.062327m; full retain"),
    ("bud_ibogem_city_dual_2025", "2025", CITY_LOCK, SRC, "executed", "management table omzet vennoten-oprichters 6.197951m; BBC/nominative split FOI"),
    ("bud_ibogem_kw_omzet_2025", "2025", KW_OMZET, SRC, "executed", "Kringwinkel omzet 0.595433m vs 0.578993m; resultaat -0.352008m"),
    ("bud_ibogem_rp_omzet_2025", "2025", RP_OMZET, SRC, "executed", "recyclageparken 0.493226m vs 0.498731m; resultaat -0.797022m"),
    ("bud_ibogem_pers_2025", "2025", PERS, SRC, "executed", "NBB 62 personeel 2.804574m / 39.7 VTE; narrative 32.44 intern + 9.98 extern"),
    ("bud_ibogem_kapsub_2025", "2025", KAPSUB, SRC, "executed", "NBB 15 kapitaalsubsidies stock 0.955165m; 2025 income 0.158256m"),
    ("bud_ibogem_retained_2025", "2025", RETAINED, SRC, "executed", "NBB 14 over te dragen winst 0.182262m (prior 0.088561 + year 0.093701)"),
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
        "comm_ibogem_city_dual_6_20m_2025",
        "AGB Ibogem 2025 city/vennoot omzet 6.198m",
        "6197950.61",
        "Management table vennoten-oprichters 6.197951m; NBB andere opbr 6.969m; BBC lock FOI",
        "Publish nominative 2026-2031 city dual lock + werk vs prijs split FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ibogem_pension_4_95m_2025",
        "AGB Ibogem YE2025 pension provision 4.950m",
        "4950069.22",
        "NBB 160 4.950069m = 42pct assets; fin debt 0 after Verrebroek prepay",
        "Actuarial note + annual cash outflow FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ibogem_kw_loss_0_35m_2025",
        "AGB Ibogem 2025 Kringwinkel resultaat NEG 0.352m",
        "352007.76",
        "KW omzet 0.595m vs resultaat -0.352m; 2 new shops 2025",
        "Publish KW P&L vs city cover FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ibogem_rp_loss_0_80m_2025",
        "AGB Ibogem 2025 recyclageparken resultaat NEG 0.797m",
        "797022.26",
        "RP omzet 0.493m / resultaat -0.797m; 3 parks",
        "Publish RP cost recovery vs city cover FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ibogem_igs_transfer_2025",
        "IGS Ibogem 0213.384.063 to AGB 1023.770.068 2025 transfer",
        "1595486.31",
        "Assets drop 13.369m to 11.773m; first AGB year after BKZ fusion",
        "Publish vereffeningsrekening + transfer inventory FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_ibogem_bbc_j2_opaque_2025",
        "AGB Ibogem BBC J2 AFM/BBR 2025 unpublished",
        "",
        "Org PDF is NBB VOL-inb only; beleidsplan is policy not J2; do not invent AFM/BBR",
        "Publish BBC JR2025 J1-J5 FOI",
        SRC,
        SRC_URL,
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "AGB Ibogem / Gemeente BKZ / inwoners BKZ",
            "legal_basis": "Decreet Lokaal Bestuur + AGB statuten 2025 + IGS ontbinding + NBB VOL-inb JR2025 AV 30.06.2026",
            "decision_date": "2026-06-30",
            "start_year": "2025",
            "end_year": "2025" if "bbc" not in cid and "transfer" not in cid else "2031",
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
            "notes": f"tick{TICK}; primary NBB JR2025 in jaarverslag PDF; BBC J2 unpublished; NBB consult often SPA",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_ibogem_pension_4_95m_2025", "AGB Ibogem YE2025 pension provision 4.95m", "4950069", "8.0", "7.5", "3.0"),
    ("lb_ibogem_city_dual_6_20m_2025", "AGB Ibogem 2025 city/vennoot omzet 6.20m", "6197951", "7.0", "7.0", "3.0"),
    ("lb_ibogem_rp_loss_0_80m_2025", "AGB Ibogem 2025 recyclageparken NEG 0.80m", "797022", "6.5", "5.0", "3.0"),
    ("lb_ibogem_kw_loss_0_35m_2025", "AGB Ibogem 2025 Kringwinkel NEG 0.35m", "352008", "6.0", "4.5", "3.0"),
    ("lb_ibogem_pers_2_80m_40vte_2025", "AGB Ibogem personnel 2.80m / 39.7 VTE", "2804574", "5.5", "6.0", "3.0"),
    ("lb_ibogem_assets_drop_1_60m_2025", "AGB Ibogem assets drop 1.60m IGS to AGB", "1595486", "6.5", "5.5", "3.0"),
    ("lb_ibogem_bbc_j2_opaque_2025", "AGB Ibogem BBC J2 AFM/BBR unpublished", "6197951", "6.0", "5.0", "3.0"),
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
            "tco_notes": "AGB Ibogem JR2025 Entity II waste AGB; pension is stock not TCO; city dual is flow; BBC J2 unpublished",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "inwoners BKZ / Kringwinkel / recyclageparken / AGB staff",
            "stated_goal": "Local dual residual waste AGB map VL JR2025 BKZ after IGS-to-AGB conversion",
            "measured_outcome": "assets 11.773m / pension 4.950m / fin debt 0 / city dual 6.198m / PnL 0.094m / pers 2.805m 39.7 VTE / BBC J2 unpublished",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish BBC J2 AFM/BBR + pension actuarial note + nominative city dual 2026-2031 + IGS transfer inventory FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary NBB JR2025 in jaarverslag PDF; not TE-additive without city GE; BBC J2 unpublished",
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
                "BBC J2 AFM/gecorr AFM/BBR/avail BBR (org PDF is NBB VOL-inb only) "
                "+ pension 4.950069m actuarial basis/cash outflow "
                "+ city dual 6.197951m werk vs prijs vs verwerking split and 2026-2031 lock "
                "+ IGS 0213.384.063 to AGB transfer inventory (assets drop 1.595m) "
                "+ Verrebroek 2015 early-repay proof fin debt 0 "
                "+ NBB Consult working URL (VenB is in org PDF; consult often SPA this box)"
            ),
            "why_it_matters": (
                "Unmined BKZ Entity II waste AGB after IGS-to-AGB conversion: city dual "
                "6.20m sits beside a 4.95m pension provision (42pct of assets) while "
                "financial debt is 0. NBB JR2025 is public in the jaarverslag; BBC J2 "
                "is not. Distinct from AGB Kruibeke/BKZ sport."
            ),
            "priority": "8",
            "recipient_body": "AGB Ibogem / Gemeente Beveren-Kruibeke-Zwijndrecht",
            "recipient_email": "info@ibogem.be",
            "recipient_postal": "Schaarbeekstraat 27 9120 Beveren",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_ibogem_pension_4_95m_2025",
            "linked_leaderboard_id": "lb_ibogem_pension_4_95m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1275",
    "title": "AGB IBOGEM JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Ibogem JR2025 NBB VOL-inb inside jaarverslag + KBO; "
        "KBO 1023.770.068; assets 11.773m / pension 4.950m / city dual 6.198m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:15:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1275 AGB IBOGEM JR2025 dual residual; KBO 1023.770.068; "
        "assets 11.773m pension 4.950m fin debt 0 city dual 6.198m cash 0.489m "
        "invest 3.907m PnL 0.094m pers 2.805m / 39.7 VTE; BBC J2 unpublished; "
        "FOI ready not sent; next rq_1276 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1276",
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
        "+ AGB IBOGEM 1275 done; prefer other unmined AGB/zorg/EVA with direct "
        "PDF/NBB/city HTML; skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; "
        "WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; skip "
        "Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat "
        "unpublished; ebesluit TLS + Leuven besluitvorming TLS — prefer org sites / "
        "NBB / city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have "
        "a separate downloadable JR)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1275 after AGB IBOGEM JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1275", rq_new, rq_spawn)
print("research_queue 1275", found, "spawned_1276", spawned)

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
            "last_unit_id": "rq_1275",
            "ticks_completed": "1275",
            "paused": "no",
            "notes": (
                "tick1275 AGB IBOGEM JR2025 dual residual; KBO 1023.770.068; "
                "assets 11.773m pension 4.950m fin debt 0 city dual 6.198m cash 0.489m "
                "invest 3.907m PnL 0.094m pers 2.805m; BBC J2 unpublished; FOI ready; "
                "next rq_1276 residual dual L5 VL (prefer unmined AGB/zorg/EVA JR2025); "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1275 - 2026-08-17 - rq_1275 AGB IBOGEM dual residual
- Unit: AGB Ibogem (duurzaam afvalbeheer BKZ) JR2025 Entity II after AGB Kruibeke/BKZ sport tick1271 + city BKZ GE tick883 + Zorgpunt Waasland tick1240 (KBO **1023.770.068**; AGB since 19.09.2025 / ops 01.01.2025 after IGS/CV Ibogem **0213.384.063** dissolution on BKZ fusion; NBB VOL-inb inside org jaarverslag PDF published July 2026; AV 30.06.2026). **Distinct from** AGB Sport/Cultuur/Recreatie Kruibeke (0878.836.925). Seat Schaarbeekstraat 27 9120. AD Wim Beeldens / voorzitter Danny Van Hove. 3 recyclageparken + 3 kringwinkels; 88.302 inwoners. Prior ticks skipped IBOGEM because JR2025 was unpublished — now public.
- EUR strong (primary NBB text PDF; **BBC J2 not in this file**): assets **11.773m** (was IGS **13.369m**, drop **1.596m**); cash **0.489m** + beleggingen **3.907m**; MVA **6.737m** leasing **0** buildings **4.340m**; **fin debt 0** (Verrebroek 2015 loan prepaid; fin cost **0.014m** vs **0.029m**); **pension provision 4.950m** (42pct assets); schulden **3.245m** (ST **3.142m** of which trade **1.446m** + prepay **1.400m**); EV **3.578m** (was 3.384m); bedrijfsopbr **12.130m** / kost **12.231m**; EBIT **−0.101m**; fin resultaat **+0.226m**; PnL **+0.094m** (was 0.062m) full retain; city/vennoot omzet **6.198m**; KW **0.595m** / resultaat **−0.352m**; RP **0.493m** / resultaat **−0.797m**; pers **2.805m** / **39.7 VTE**. Beleidsplan 2025–2030 is policy, not J2. NBB consult often 403/SPA this box.
- CSVs: sources+5/entities(new AGB + city_bkz note)/budgets+25/commitments+6/leaderboard+7 + FOI ready `gap_ibogem_pension_4_95m_bbc_opaque_city_dual_6_20m_l5` (not sent); rq_1275=done; spawn rq_1276; ticks=1275. Not a *0 tick — no progress refresh.
- Next: rq_1276 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
