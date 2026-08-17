# -*- coding: utf-8 -*-
"""Tick 1270 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 AGB MAC Mechelen JR2025 dual residual + every-10 progress refresh."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T08:55:00Z"
TICK = 1270
SRC = "src_mac_jr2025_bbc"
SRC2 = "src_mac_jr2025_portal"
SRC3 = "src_mac_rvb_20260608"
SRC4 = "src_kbo_mac_0546688337"
SRC5 = "src_nbb_mac_consult_0546688337"
ENT = "agb_mac_mechelen"
CITY = "city_mechelen"
SRC_URL = "https://www.mechelen.be/sites/default/files/agb-mac/files/2026-06/AGB%20MAC%20-%20JAARREKENING%202025%20BBC.pdf"
SRC2_URL = "https://www.mechelen.be/stad-en-bestuur/stadsbestuur-en-organisatie/bekendmakingen-verslagen-en-documenten/agb-mac-documenten"
SRC3_URL = "https://www.mechelen.be/sites/default/files/agb-mac/files/2026-06/Raad%20van%20Bestuur%20Beslissingslijst%2008-06-2026%20AGB%20MAC.pdf"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0546688337"
SRC5_URL = "https://consult.cbso.nbb.be/consult-enterprise/0546688337"
GAP = "gap_mac_gecorr_afm_neg_0_68m_fin_debt_40_33m_venb_l5"
HIER = "Vlaanderen>Gemeenten>Mechelen>AGB_MAC"

ASSETS = 45594748.00
CASH = 1282480.00
FIN_DEBT = 40334859.00
LT_DEBT = 38266166.00
ST_DUE = 2068693.00
NETTO = 3434806.00
CUM_PNL = 29653.00
AFM = 663363.00
GECORR = -677089.00
BBR = 382400.00
BBR_AVAIL = 607569.00
EXPL_UIT = 4179659.00
EXPL_ONT = 6893388.00
EXPL_SALDO = 2713729.00
INV_UIT = 283175.00
INV_SALDO = -280963.00
FIN_AFL = 2050366.00
PNL = 654722.00
DIV = 400000.00
PRIJS = 4519358.00
CITY_TOT = 4824439.00
BTW_PRIJS = 305081.00
LEASING = 40783387.00
WERKSUB_T2 = 167635.00
VL_WERKSUB = 156008.00
CITY_WERKSUB_T2 = 11627.00
MVA = 43442671.00
KAPSUB = 3405152.00
AANGEWEZEN = 3390818.00


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
            "title": "AGB MAC Mechelen JR2025 BBC 56p text PDF",
            "url": SRC_URL,
            "publisher": "AGB Mechelen Actief in Cultuur / Stad Mechelen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1270; published 2026-06-15; 5.05MB text PDF; assets 45.595m; "
                "fin debt 40.335m; AFM +0.663m gecorr -0.677m; city prijssub 4.519m; "
                "PnL 0.655m dividend 0.400m; leasing MVA 40.783m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGB MAC documenten portal (JR2025 BBC + MJP2026)",
            "url": SRC2_URL,
            "publisher": "Stad Mechelen",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1270; JR2025 BBC downloadable; VenB 2025 not listed (2024 VenW only); "
                "MJP 2026 bundel present"
            ),
        },
        {
            "source_id": SRC3,
            "title": "AGB MAC RvB beslissingslijst 08.06.2026 JR2025 vaststelling",
            "url": SRC3_URL,
            "publisher": "AGB MAC",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1270; voorzitter Kristof Calvo; BBC+VenB+resultaat goedgekeurd; "
                "agbmac@mechelen.be; BTW BE 0546.688.337"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO AGB MAC 0546.688.337",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1270; Autonoom gemeentebedrijf since 01.01.2014; seat Grote Markt 21 "
                "2800 Mechelen; 0 VE; bestuurder Kristof Calvo y Castaner since 17.02.2025; "
                "NACE 90.311/91.110/91.210/56.301; tel 015 29 40 13; financials empty"
            ),
        },
        {
            "source_id": SRC5,
            "title": "NBB Consult AGB MAC 0546688337 JR filings",
            "url": SRC5_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1270; consult SPA/empty this box; VenB 2025 not on org portal; "
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
            "name_nl": "AGB Mechelen Actief in Cultuur (MAC)",
            "name_fr": "AGB Malines Actif en Culture (MAC)",
            "name_en": "Mechelen Active in Culture municipal company (MAC)",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC2_URL,
            "foi_email": "agbmac@mechelen.be",
            "foi_postal": "Grote Markt 21 2800 Mechelen",
            "notes": (
                "tick1270 JR2025 dual residual; KBO 0546.688.337 AGB since 01.01.2014; "
                "assets 45.595m fin debt 40.335m AFM +0.663m gecorr -0.677m BBR 0.382m "
                "avail 0.608m city prijssub 4.519m PnL 0.655m dividend 0.400m leasing "
                "40.783m cash 1.282m; VenB 2025 unpublished; FOI " + GAP
            ),
        }
    ],
)
print("entity mac", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "AGB MAC dual residual tick1270 (KBO 0546.688.337; assets 45.595m; "
        "fin debt 40.335m; gecorr AFM -0.677m; city prijssub 4.519m; VenB FOI)"
    ),
)
print("city_mechelen notes", ok)

bud_rows = [
    ("bud_mac_assets_2025", "2025", ASSETS, SRC, "executed", "JR2025 J4 assets 45.594748m (was 49.255025m)"),
    ("bud_mac_cash_2025", "2025", CASH, SRC, "executed", "JR2025 J4 cash 1.282480m JUMP vs 0.671205m"),
    ("bud_mac_fin_debt_2025", "2025", FIN_DEBT, SRC, "executed", "JR2025 T4 fin debt 40.334859m (LT 38.266166 + ST due 2.068693) declining vs 42.385225m"),
    ("bud_mac_lt_debt_2025", "2025", LT_DEBT, SRC, "executed", "JR2025 T4/J4 LT fin debt 38.266166m"),
    ("bud_mac_st_due_2025", "2025", ST_DUE, SRC, "executed", "JR2025 T4 ST due within year 2.068693m"),
    ("bud_mac_netto_2025", "2025", NETTO, SRC, "executed", "JR2025 J4 nettoactief 3.434806m (kapsub 3.405152 + cum 0.029653)"),
    ("bud_mac_cum_pnl_2025", "2025", CUM_PNL, SRC, "executed", "JR2025 J4 cum P&L +0.029653m FLIP vs -0.225069m"),
    ("bud_mac_afm_2025", "2025", AFM, SRC, "executed", "JR2025 J2 AFM +0.663363m"),
    ("bud_mac_gecorr_afm_2025", "2025", GECORR, SRC, "executed", "JR2025 J2 gecorr AFM -0.677089m NEG (aangewezen 3.390818 vs periodiek 2.050366)"),
    ("bud_mac_bbr_2025", "2025", BBR, SRC, "executed", "JR2025 J2 BBR year +0.382400m"),
    ("bud_mac_bbr_avail_2025", "2025", BBR_AVAIL, SRC, "executed", "JR2025 J2 beschikbaar BBR 0.607569m"),
    ("bud_mac_expl_uit_2025", "2025", EXPL_UIT, SRC, "executed", "JR2025 J2/J3 expl uitgaven 4.179659m"),
    ("bud_mac_expl_ont_2025", "2025", EXPL_ONT, SRC, "executed", "JR2025 J2/J3 expl ontvangsten 6.893388m"),
    ("bud_mac_expl_saldo_2025", "2025", EXPL_SALDO, SRC, "executed", "JR2025 J2 expl saldo +2.713729m"),
    ("bud_mac_inv_uit_2025", "2025", INV_UIT, SRC, "executed", "JR2025 J2 invest uitgaven 0.283175m (credit 1.870811)"),
    ("bud_mac_inv_saldo_2025", "2025", INV_SALDO, SRC, "executed", "JR2025 J2 invest saldo -0.280963m"),
    ("bud_mac_fin_afl_2025", "2025", FIN_AFL, SRC, "executed", "JR2025 J2/T4 periodieke aflossingen 2.050366m; new loans 0"),
    ("bud_mac_pnl_2025", "2025", PNL, SRC, "executed", "JR2025 J5 surplus 0.654722m (opbr 7.557339 / kost 6.902617)"),
    ("bud_mac_dividend_2025", "2025", DIV, SRC, "executed", "JR2025 J5 rechthebbenden/dividend to city 0.400000m"),
    ("bud_mac_prijssub_2025", "2025", PRIJS, SRC, "executed", "JR2025 annex city prijssubsidie 4.519358m exe (budget 4.046001)"),
    ("bud_mac_city_sub_tot_2025", "2025", CITY_TOT, SRC, "executed", "JR2025 annex city prijssub+BTW 4.824439m (BTW 0.305081); invest-toelage 0"),
    ("bud_mac_leasing_mva_2025", "2025", LEASING, SRC, "executed", "JR2025 J4 leasing/soortgelijke rechten MVA 40.783387m (was 42.508402)"),
    ("bud_mac_werksub_t2_2025", "2025", WERKSUB_T2, SRC, "executed", "JR2025 T2 specifieke werkingssubsidies cash 0.167635m (VL 0.156008 + city 0.011627)"),
    ("bud_mac_mva_2025", "2025", MVA, SRC, "executed", "JR2025 J4 MVA 43.442671m"),
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
        "comm_mac_city_prijssub_4_52m_2025",
        "AGB MAC 2025 city prijssubsidie 4.519m",
        "4519358",
        "Annex exe 4.519358m vs budget 4.046001m (+0.473m visitors); +BTW 0.305m = 4.824m",
        "Publish 2026-2031 nominative lock + venue split FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mac_fin_debt_40_33m_2025",
        "AGB MAC YE2025 fin debt 40.335m",
        "40334859",
        "T4 LT 38.266m + ST due 2.069m; declining vs 42.385m; new loans 0; leasing MVA 40.783m",
        "Creditor split city vs bank vs Predikheren erfpacht FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mac_gecorr_afm_neg_0_68m_2025",
        "AGB MAC 2025 gecorr AFM -0.677m NEG",
        "677089",
        "Headline AFM +0.663m; aangewezen aflossing 3.391m vs periodiek 2.050m",
        "Explain NEG gecorr vs dividend 0.400m FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mac_leasing_mva_40_78m_2025",
        "AGB MAC leasing/erfpacht MVA 40.783m",
        "40783387",
        "J4 leasing 40.783m of MVA 43.443m; 2024 Predikheren 7.9m loan year",
        "Contract + remaining canon Predikheren FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mac_dividend_0_40m_2025",
        "AGB MAC 2025 dividend to city 0.400m",
        "400000",
        "J5 rechthebbenden 0.400m of surplus 0.655m; retained 0.255m; cum flip to +0.030m",
        "Why full 0.400m while gecorr AFM NEG FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mac_venb_2025_unpublished",
        "AGB MAC VenB/NBB JR2025 not on portal",
        "",
        "RvB 08.06.2026 approved VenB; portal has 2024 VenW only; NBB SPA this box",
        "Publish working VenB+NBB JR2025 PDF FOI",
        SRC5,
        SRC5_URL,
    ),
    (
        "comm_mac_2026_lock_unknown",
        "AGB MAC 2026 city prijssubsidie lock not extracted",
        "",
        "MJP 2026 bundel on portal; this tick used JR2025 BBC only",
        "Publish 2026 nominative MAC lock FOI",
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
            "beneficiary": "AGB Mechelen Actief in Cultuur (MAC)",
            "legal_basis": "Decreet Lokaal Bestuur + AGB MAC + beheersovereenkomst prijssubsidie + JR2025 BBC",
            "decision_date": "2026-06-08",
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
    ("lb_mac_fin_debt_40_33m_2025", "AGB MAC YE2025 fin debt 40.33m", "40334859", "7.0", "8.0", "3.0"),
    ("lb_mac_leasing_mva_40_78m_2025", "AGB MAC leasing/erfpacht MVA 40.78m", "40783387", "7.0", "8.0", "3.0"),
    ("lb_mac_gecorr_afm_neg_0_68m_2025", "AGB MAC 2025 gecorr AFM -0.68m NEG", "677089", "8.0", "5.0", "3.0"),
    ("lb_mac_city_prijssub_4_52m_2025", "AGB MAC 2025 city prijssubsidie 4.52m", "4519358", "6.0", "6.5", "3.0"),
    ("lb_mac_dividend_0_40m_2025", "AGB MAC 2025 dividend to city 0.40m vs gecorr NEG", "400000", "7.0", "4.5", "2.0"),
    ("lb_mac_pnl_0_65m_2025", "AGB MAC 2025 P&L surplus 0.65m", "654722", "5.5", "5.0", "3.0"),
    ("lb_mac_venb_2025_unpublished", "AGB MAC VenB/NBB JR2025 not retrieved", "4519358", "6.5", "6.0", "3.0"),
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
            "tco_notes": "AGB MAC Mechelen JR2025 Entity II culture AGB; fin debt/leasing are stock not TCO; VenB internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "CCM / Hof van Busleyden / Predikheren / De Garage / Extern Mechelen",
            "stated_goal": "Local dual residual culture-AGB map VL JR2025 Mechelen",
            "measured_outcome": "assets 45.595m / fin debt 40.335m / gecorr AFM -0.677m / city prijssub 4.519m / VenB unpublished",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish VenB 2025 + T4 creditor split + 2026 lock + city FTE FOI",
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
                "VenB/NBB JR2025 working URL (RvB 08.06.2026 approved; portal 2024 VenW only) "
                "+ T4 creditor split of fin debt 40.334859m (city vs bank vs Predikheren "
                "erfpacht) vs leasing MVA 40.783387m + aangewezen aflossing 3.390818m; "
                "2026-2031 city prijssubsidie lock + venue split of 4.519358m; city-payroll "
                "FTE/VTE/kost for MAC venues (BBC personeel N/A); why dividend 0.400m while "
                "gecorr AFM -0.677m NEG"
            ),
            "why_it_matters": (
                "Remaining Mechelen Entity II culture AGB after Energiepunt 1162 / SAM 1173 / "
                "Rivierenland 1247: city prijssub 4.52m sits beside a 40.33m leasing/erfpacht "
                "debt shell and a NEG gecorr AFM while the AGB pays 0.40m dividend back to the "
                "city. BBC JR2025 is public; VenB 2025 is not. Distinct from SAM and Energiepunt."
            ),
            "priority": "8",
            "recipient_body": "AGB MAC / Stad Mechelen",
            "recipient_email": "agbmac@mechelen.be",
            "recipient_postal": "Grote Markt 21 2800 Mechelen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_mac_fin_debt_40_33m_2025",
            "linked_leaderboard_id": "lb_mac_fin_debt_40_33m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1270",
    "title": "AGB MAC Mechelen JR2025 dual residual + every-10 progress",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB MAC JR2025 BBC 56p text + KBO; KBO 0546.688.337; "
        "assets 45.595m / fin debt 40.335m / gecorr AFM -0.677m / city prijssub 4.519m; "
        "every-10 refresh done"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:40:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1270 AGB MAC JR2025 dual residual + every-10; KBO 0546.688.337 56p BBC; "
        "assets 45.595m fin debt 40.335m AFM +0.663m gecorr -0.677m BBR +0.382m "
        "avail 0.608m city prijssub 4.519m cash 1.282m PnL 0.655m dividend 0.400m "
        "leasing 40.783m; VenB unpublished; FOI ready not sent; next rq_1271 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1271",
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
        "+ AGB MAC Mechelen 1270 done; prefer other unmined AGB/zorg/EVA with direct "
        "PDF/NBB/city HTML; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat "
        "unpublished; ebesluit TLS — prefer org sites / NBB / city HTML; Brugge SAS / "
        "Blauwe Lelie / SPOOR / WOK only if they have a separate downloadable JR)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1270 after AGB MAC Mechelen JR2025 dual residual + every-10; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1270", rq_new, rq_spawn)
print("research_queue 1270", found, "spawned_1271", spawned)

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
            "last_unit_id": "rq_1270",
            "ticks_completed": "1270",
            "paused": "no",
            "notes": (
                "tick1270 AGB MAC Mechelen JR2025 dual residual + every-10; KBO 0546.688.337; "
                "assets 45.595m fin debt 40.335m AFM +0.663m gecorr -0.677m city prijssub 4.519m; "
                "VenB unpublished; FOI ready; next rq_1271 residual dual L5 VL "
                "(prefer unmined AGB/zorg/EVA JR2025); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

# --- every-10 progress files ---
prog_snap = """# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## How to read the % figures

| Layer | Meaning | “End stop of money”? |
|-------|---------|----------------------|
| **A. L0 total** | Official GG TE known | No — single top line |
| **B. L1 subsector** | TE split federal / SS / state / local | No — still aggregates |
| **C. L2 entity totals** | Named institutions with primary budget totals (De Lijn, FOREM, ORES, …) | **Partial** — who holds the money |
| **D. L5 end-receivers** | Named third party / project / ASBL / firm with € | **Yes** — where possible |
| **E. FOI residual** | Known gap, draft ready for human send | Tracked, not yet answered |

**Honest claim:** A+B are essentially complete. C is large but incomplete. **D is still a small share of €348 bn** — that is structural (payroll, pensions, debt interest, formula grants are not “projects”).

---

## Snapshot at **tick 1270** (2026-08-17)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1261-1270: AGSO · CIA Erfgoed · CIA Kunsten · EBF · Digipolis · Atlas · Amal · Fietsambassade · Mintus · **AGB MAC Mechelen** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1261-1270 is VL residual dual L5 (not near-complete of 348bn):** **AGB MAC** assets **45.6m** fin debt **40.3m** leasing **40.8m** gecorr AFM **−0.68m** city prijssub **4.52m** PnL **0.65m** dividend **0.40m** · **Mintus** city dual **26.36m** deelneming **56.96m** · Digipolis assets **73.61m** member omzet **221.9m** · Atlas city dual **21.85m** · AGSO / CIA / Amal / Fietsambassade stack retained |
| **E. FOI-ready gaps** | **~913** drafts ready | Human send only; answered **~9**; partial **~27**; total FOI rows **~961** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM shells** (**NEW AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** gecorr AFM **−EUR0.68m** city prijssub **EUR4.52m** · **Mintus** dual **EUR26.36m** deelneming **EUR56.96m** · Digipolis assets **EUR73.61m** · prior **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1270)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | ~33918 |
| commitments.csv | ~4663 |
| leaderboard.csv | ~6817 |
| entities.csv | ~992 |
| sources.csv | ~2229 |
| FOI ready | ~913 |
| FOI answered | ~9 |
| FOI partial | ~27 |
| FOI total rows | ~961 |
| research_queue open | rq_116 deferred + rq_1271 hole-fill after progress |

### What improved since tick 1260

- **VL residual dual JR2025 Entity II (tick1261-1269):** AGSO Antwerpen assets **725.2m** fin debt **82.7m** · CIA Erfgoed city dual **11.34m** · CIA Kunsten BBR **2.76m** city dual **0.19m** · EBF BBR cum **1.02m** · Digipolis assets **73.61m** member omzet **221.9m** · Atlas city dual **21.85m** · Amal city dual **7.37m** · Fietsambassade city dual **2.65m** · **Mintus Brugge** creditor **26.36m** deelneming **56.96m**.
- **NEW (tick1270):** **AGB MAC Mechelen** culture AGB (KBO 0546.688.337) assets **45.595m** · cash **1.282m** JUMP · **fin debt 40.335m** (leasing MVA **40.783m**) · AFM **+0.663m** / **gecorr AFM −0.677m NEG** · BBR **+0.382m** / avail **+0.608m** · city prijssub **4.519m** (+BTW **0.305m** = **4.824m**) · PnL **+0.655m** · dividend to city **0.400m** · cum P&L flip to **+0.030m** · VenB 2025 unpublished · FOI T4 split + 2026 lock ready.
- **Dual map themes:** **culture leasing/erfpacht shell + NEG gecorr AFM + city dividend** (MAC) · **zorg-EVA city dual + deelneming stock** (Mintus) · **ICT cost-recovery AGB** (Digipolis) · prior mega real-estate / care stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""

prog_path = DATA / "progress_every_10_ticks.md"
old = prog_path.read_text(encoding="utf-8")
# keep from the tick 1260 snapshot onward (drop old header/how-to already rewritten)
marker = "## Snapshot at **tick 1260**"
idx = old.find(marker)
if idx < 0:
    raise SystemExit("progress file missing tick 1260 marker")
# keep how-to is already in prog_snap; append old from 1260
# but old file starts with header+how-to then 1260 — we only keep from 1260
prog_path.write_text(prog_snap + old[idx:], encoding="utf-8")
print("progress_every_10_ticks ok")

waste = """# DOGE waste ranking — current top 10

**As-of:** tick **1270** (2026-08-17) · **~6817** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **WE consol €6.38bn** · **SOFICO €3.02bn** · **university/city balance sheets** · **AGB/zorg dual AFM NEG + debt + leasing/city-loan/DBFM shells** (**NEW AGB MAC** fin debt **€40.3m** leasing **€40.8m** gecorr AFM **−€0.68m** city prijssub **€4.52m** · **Mintus** dual **€26.36m** deelneming **€56.96m** · Digipolis assets **€73.61m** · **AG Vespa** fin debt **€179.6m** DBFM **€109.4m** gecorr AFM **−€1.86m** · **sogent** AFM **−€3.90m** debt **€96.3m** ICC **€35m** · AG-O cum loss **−€29.2m** · **Zorgbedrijf Antwerpen** AFM **−€18.87m** debt **€220m** city sub **€51.4m** · **Dodoens** equity **−€18.88m** · prior Waasland / AGSL / Hasselt ~€95–103m stack) · **LUWA PPP €590m** · private gambling stakes **€31.5bn** market.

**Change vs tick 1260:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). **Major NEW residual 1261–1270 (off pure top10 / dual):** **AGB MAC** assets **EUR45.6m** fin debt **EUR40.3m** leasing **EUR40.8m** gecorr AFM **−EUR0.68m** city prijssub **EUR4.52m** dividend **EUR0.40m** · **Mintus** city dual **EUR26.36m** deelneming **EUR56.96m** · Digipolis assets **EUR73.61m** member omzet **EUR221.9m** · Atlas city dual **EUR21.85m**. Gain is **culture leasing/erfpacht shell + NEG gecorr AFM + city dividend + zorg-EVA dual**.

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| — | `lb_metro3_overrun_477pct` | **stock** | **9.05** | STOCK filtered |
| — | `lb_owv_sub_snowball_27bn_2083` | **stock-as-ann** | **8.55** | STOCK filtered eoy2083 |
| — | `lb_vl_gsc_pv_legacy_7_078bn` | **~708 m** class | **8.05** | GSC PV legacy oversubsidy |
| — | `lb_fed_consultancy_2_5bn_coa` | **~842 m/yr** | **8.00** | CoA 2.525bn/3y |
| — | `lb_mac_fin_debt_40_33m_2025` | **40.3 m stock** | **~7.5 dual** | **NEW 1270** AGB MAC fin debt / leasing |
| — | `lb_mac_gecorr_afm_neg_0_68m_2025` | **0.68 m** | **~high dual** | **NEW 1270** gecorr AFM NEG vs dividend |
| — | `lb_vespa_fin_debt_179_63m_2025` | **179.6 m stock** | **~7.5 dual** | 1260 AG Vespa fin debt / DBFM |
| — | `lb_sogent_fin_debt_96_31m_2025` | **96.3 m stock** | **~7.5 dual** | 1259 sogent urban-dev debt |
| — | `lb_zba_fin_debt_220m_2025` | **220 m stock** | **~high dual** | 1246 mega care debt |
| — | `lb_zba_afm_neg_18_9m_2025` | **18.9 m** | **~high dual** | 1246 Zorgbedrijf Antwerpen AFM NEG |

### High-absurdity shortlist (not pure annual cost rank)

| ID | Abs | Note |
|----|----:|------|
| `lb_metro3_overrun_477pct` | **9.5** | Metro3 cost +477pct |
| `lb_vl_wassalon_podcast` | **9.5** | VL gelijke kansen vodcast |
| `lb_dodoens_equity_neg_18_9m_2025` | **8.5** | pension-shell equity DEEP NEG |
| `lb_zba_afm_neg_18_9m_2025` | **8.5** | mega city dual care AFM NEG |
| `lb_mac_gecorr_afm_neg_0_68m_2025` | **8.0** | **NEW** headline AFM +0.66m / gecorr −0.68m + city dividend 0.40m |
| `lb_vespa_gecorr_afm_neg_1_86m_2025` | **8.0** | headline AFM +7.3m / gecorr −1.86m |
| `lb_sogent_icc_capital_35m_2025` | **8.5** | 1259 ICC city capital off-MJP |
| `lb_zpw_cum_loss_12_3m_2025` | **8.5** | multi-muni zorg cum loss DEEP |
| `lb_agbvv_bbr_neg_0_45m_2025` | **8** | Vilvoorde BBR NEG + full div strip |
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("waste top10 ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1270 - 2026-08-17 - rq_1270 AGB MAC Mechelen dual residual + progress@1270
- Unit: AGB Mechelen Actief in Cultuur (MAC) JR2025 Entity II after city Mechelen GE tick829 + Energiepunt tick1162 + SAM tick1173 + Rivierenland tick1247 (KBO 0546.688.337; AGB since 01.01.2014; 56p BBC text PDF published 15.06.2026; RvB 08.06.2026). **Distinct from** SAM (0871.106.718) and Energiepunt (0843.922.170). Seat Grote Markt 21. Venues CCM / Hof van Busleyden / Predikheren / De Garage / Extern. WAGSO already mined tick1199. Brugge siblings SAS/Blauwe Lelie/SPOOR/WOK skipped (no separate JR).
- EUR strong (primary BBC text PDF): assets **45.595m** (was 49.255m); cash **1.282m** JUMP; MVA **43.443m** of which leasing **40.783m**; fin debt **40.335m** (LT **38.266m** + ST due **2.069m**) declining vs **42.385m**; new loans **0**; expl **+2.714m** (ontv **6.893m** / uitg **4.180m**); invest **−0.281m**; BBR **+0.382m** / avail **+0.608m**; AFM **+0.663m** / **gecorr −0.677m NEG**; city prijssub **4.519m** exe (budget 4.046m) + BTW **0.305m** = **4.824m**; PnL **+0.655m**; dividend to city **0.400m**; cum P&L flip **−0.225 → +0.030m**. Personeel N/A (city payroll). VenB 2025 not on portal; NBB SPA this box.
- CSVs: sources+5/entities(new+city note)/budgets+24/commitments+7/leaderboard+7 + FOI ready `gap_mac_gecorr_afm_neg_0_68m_fin_debt_40_33m_venb_l5` (not sent); rq_1270=done; spawn rq_1271; ticks=1270.
- Progress@1270: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E ~913 ready. Pure annual waste top10 **stable** vs 1260 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds MAC fin debt 40.33m / leasing 40.78m / gecorr AFM −0.68m + Mintus 26.36m / Digipolis 73.61m.
- Coverage: 1261–1270 is residual dual L5 (AGSO · CIA E/K · EBF · Digipolis · Atlas · Amal · Fietsambassade · Mintus · **MAC**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Inventory@1270: budgets ~33918 · commitments ~4663 · leaderboard ~6817 · entities ~992 · sources ~2229 · FOI ready ~913 / answered ~9 / partial ~27 / total ~961.
- Dual theme this decade: culture leasing/erfpacht shell + NEG gecorr AFM while paying city dividend; prior mega real-estate/care/ICT stack retained.
- Next: rq_1271 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; Brugge SAS/Lelie/SPOOR/WOK only if own JR).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
