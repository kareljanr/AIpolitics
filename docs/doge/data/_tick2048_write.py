# ephemeral tick2048 — Ter Kimme YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T17:10:00Z"
ENTITY = "vzw_ter_kimme"
GAP = "gap_ter_kimme_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_ter_kimme_jr2025_cw"
SRC_EN = "src_ter_kimme_jr2025_cw_en"
SRC_FR = "src_ter_kimme_jr2025_cw_fr"
SRC_KBO = "src_ter_kimme_kbo_2048"
SRC_SITE = "src_ter_kimme_site_2048"

OMZET = "8539894"
PNL = "602018"
EQUITY = "20458585"
BRUTO = "8022468"
FTE = "104.4"
OMZET24 = "8379241"
PNL24 = "574588"
EQUITY24 = "19880590"
BRUTO24 = "8142086"
# pi = 0.55*4.8 + 0.35*4.5 + 0.10*(10-4) = 2.64 + 1.575 + 0.6 = 4.815 → 4.8
PI = "4.8"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
        fields = [f.lstrip("\ufeff") for f in fields]
        for row in rows:
            if any(k.startswith("\ufeff") for k in row):
                for k in list(row):
                    if k.startswith("\ufeff"):
                        row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    fields = [f.lstrip("\ufeff") for f in fields]
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2048")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Ter Kimme YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0421535373/ter-kimme",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2048; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 17.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2048/ter_kimme_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Ter Kimme YE2025 statutory",
        "url": "https://www.companyweb.be/en/0421535373/ter-kimme",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2048; EN mirror YE2025 Medium; filed 17-07-2026; Last balance sheet year 2025; FTE 104.4; raw docs/doge/data/raw/tick2048/ter_kimme_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Ter Kimme YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0421535373/ter-kimme",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2048; FR mirror YE2025 Medium; depose le 17-07-2026; raw docs/doge/data/raw/tick2048/ter_kimme_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Ter Kimme 0421.535.373 Actief VZW aanbestedende overheid Sint-Lievens-Houtem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421535373",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2048; Actief VZW; Kloosterstraat 3 9520 Sint-Lievens-Houtem; 1 VE; aanbestedende overheid sinds 10.12.1980; NACE 87.101; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Ter Kimme site + contact info@terkimme.be",
        "url": "https://www.terkimme.be/contact",
        "publisher": "Ter Kimme vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2048; Cloudflare mailto decoded info@terkimme.be; WZC Sint-Lievens-Houtem; raw docs/doge/data/raw/tick2048/ter_kimme_contact.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ter_kimme_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2048; omzet JUMP {OMZET} +1.92pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ter_kimme_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2048; pnl JUMP {PNL} +4.77pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_ter_kimme_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2048; equity JUMP {EQUITY} +2.91pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ter_kimme_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2048; bruto DROP {BRUTO} -1.47pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_ter_kimme_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2048; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ter_kimme_jr2025_statutory_wzc",
    "title": "Ter Kimme YE2025 leftover dual (omzet JUMP 8.54m / pnl JUMP 0.60m)",
    "entity_id": ENTITY,
    "beneficiary": "Oost-Vlaanderen elderly-care residents (WZC Ter Kimme Sint-Lievens-Houtem)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0421.535.373)",
    "decision_date": "2026-07-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0421535373/ter-kimme",
    "stated_goal": "WZC Ter Kimme Sint-Lievens-Houtem",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>SintLievensHoutem>TerKimme>JR2025_statutory_L5",
    "notes": "tick2048; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Huize Vincent/Hof ter Waarbeek YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ter_kimme_omzet_jump_8_54m_pnl_jump_0_60m_jr2025",
    "name": "Ter Kimme omzet JUMP 8.54m / pnl JUMP 0.60m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>OostVlaanderen>SintLievensHoutem>TerKimme>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Oost-Vlaanderen elderly-care residents via Ter Kimme WZC",
    "stated_goal": "WZC Ter Kimme",
    "measured_outcome": "Medium CW YE2025; 8.54m omzet JUMP +1.92pct with pnl JUMP +4.77pct and bruto DROP -1.47pct; NBB PDF residual",
    "absurdity_score": "4.5",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2048 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Ter Kimme (VZW WZC Sint-Lievens-Houtem)",
    "name_fr": "Ter Kimme (ASBL MRS Sint-Lievens-Houtem)",
    "name_en": "Ter Kimme (VZW nursing home Sint-Lievens-Houtem)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.terkimme.be/",
    "foi_email": "info@terkimme.be",
    "foi_postal": "Kloosterstraat 3, 9520 Sint-Lievens-Houtem",
    "notes": (
        "tick2048 YE2025 Medium CW NL+EN+FR + Strong KBO 0421.535.373 Actief VZW aanbestedende overheid 1 VE; omzet JUMP 8.54m pnl JUMP 0.60m equity JUMP 20.46m bruto DROP 8.02m FTE 104.4; "
        "assets/debt Unknown; neerlegging 17.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Huize Vincent/Hof ter Waarbeek YE2025 deferred; do not redo Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hieronymus/Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren"
    ),
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>OostVlaanderen>SintLievensHoutem>TerKimme>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split (IFIC/Alivia/Vlaio/code73); bruto DROP vs omzet/pnl JUMP recon",
    "why_it_matters": "Medium CW shows 8.54m omzet VL aanbestedende-overheid WZC VZW without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Ter Kimme vzw",
    "recipient_email": "info@terkimme.be",
    "recipient_postal": "Kloosterstraat 3, 9520 Sint-Lievens-Houtem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ter_kimme_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_ter_kimme_omzet_jump_8_54m_pnl_jump_0_60m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2048; human-send only; Medium CW; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Ter Kimme (NBB PDF / assets-debt / pnl-jump matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ter Kimme VZW — KBO **0421.535.373**  
**recipient:** info@terkimme.be · Kloosterstraat 3, 9520 Sint-Lievens-Houtem  
**sources:** [CW NL](https://www.companyweb.be/nl/0421535373/ter-kimme) · [CW EN](https://www.companyweb.be/en/0421535373/ter-kimme) · [CW FR](https://www.companyweb.be/fr/0421535373/ter-kimme) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421535373) · [site](https://www.terkimme.be/contact)  
**tick:** 2048  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **17.07.2026**): omzet **EUR8,539,894** JUMP +1.92%; pnl **EUR602,018** JUMP +4.77% vs YE2024 EUR574,588; equity **EUR20,458,585** JUMP +2.91%; bruto **EUR8,022,468** DROP −1.47%; FTE **104.4**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **1 VE**; zetel Kloosterstraat 3 Sint-Lievens-Houtem.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Huize Vincent / Hof ter Waarbeek YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ter Kimme vzw — Kloosterstraat 3, 9520 Sint-Lievens-Houtem
info@terkimme.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Ter Kimme + subsidiematrix (KBO 0421.535.373)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 17.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting bruto DROP (van EUR8.142.086 YE2024 naar EUR8.022.468 YE2025) bij omzet/pnl JUMP.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, "
    "Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, "
    "PC Sint-Hieronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, "
    "Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, "
    "AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaus, AZORG, "
    "Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, "
    "Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, Gravenkasteel, Armonea, Colisee Belgium, Prinsenhof, "
    "Vivalto Home BE, emeis Belgium / ORPEA. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2048":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Integro — Ter Kimme YE2025 Medium"
        x["notes"] = (
            "tick2048 Ter Kimme Medium omzet JUMP 8.54m pnl JUMP 0.60m equity JUMP 20.46m bruto DROP 8.02m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Huize Vincent/Hof Waarbeek deferred; next rq_2049; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover Ter Kimme YE2025 Medium CW; KBO 0421.535.373; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2049" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2049",
            "title": "leftover dual hole-fill after Ter Kimme",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2048 after Ter Kimme YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Huize Vincent YE2025 live deferred / Hof ter Waarbeek YE2025 / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2048 Ter Kimme; next every-10 2050; Huize Vincent/Hof Waarbeek YE2025 deferred",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2048",
        "ticks_completed": "2048",
        "paused": "no",
        "notes": (
            "tick2048 leftover Ter Kimme 0421.535.373 Medium CW (omzet JUMP 8.54m pnl JUMP 0.60m equity JUMP 20.46m bruto DROP 8.02m FTE 104.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Huize Vincent/Hof Waarbeek deferred; next rq_2049; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2048 - {UTC} - rq_2048 Ter Kimme (omzet JUMP 8.54m / pnl JUMP 0.60m / Medium)

- Unit: **rq_2048** leftover dual after **rq_2047 Integro**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Ter Kimme** YE2025 (KBO **0421.535.373**; Kloosterstraat 3 Sint-Lievens-Houtem; Oost-Vlaanderen **aanbestedende-overheid VZW** WZC / **1 VE**). Huize Vincent / Hof ter Waarbeek YE2025 also live — deferred. Do not redo Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hieronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR8,539,894** JUMP +1.92%; pnl **EUR602,018** JUMP +4.77%; equity **EUR20,458,585** JUMP +2.91%; bruto **EUR8,022,468** DROP −1.47%; FTE **104.4**; neerlegging **17.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email info@terkimme.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2048=done + rq_2049 open; loop_state ticks=2048; raw under docs/doge/data/raw/tick2048/.
- FOI: **ready not sent** (human-gated; info@terkimme.be).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2049 (AGB/FARO-if-YE2025 / AIESH-REW / Huize Vincent-Hof Waarbeek deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2048 Ter Kimme", OMZET, "pi", PI)
