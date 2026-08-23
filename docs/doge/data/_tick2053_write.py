# ephemeral tick2053 — WZC Walfergem YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T18:20:00Z"
ENTITY = "vzw_wzc_walfergem"
GAP = "gap_walfergem_nbb_pdf_assets_debt_pnl_drop_equity_jump_matrix_l5"
SRC = "src_walfergem_jr2025_cw"
SRC_EN = "src_walfergem_jr2025_cw_en"
SRC_FR = "src_walfergem_jr2025_cw_fr"
SRC_KBO = "src_walfergem_kbo_2053"
SRC_SITE = "src_walfergem_site_2053"

OMZET = "8880682"
PNL = "947077"
EQUITY = "4258074"
BRUTO = "6540292"
FTE = "76"
OMZET24 = "8665802"
PNL24 = "1266012"
EQUITY24 = "3310998"
BRUTO24 = "6664407"
# pi = 0.55*4.0 + 0.35*5.0 + 0.10*(10-4) = 2.2 + 1.75 + 0.6 = 4.55
PI = "4.55"

do_not_redo = (
    "Do NOT redo Walfergem, Ter Berk Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, "
    "AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, "
    "OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, IPFBW, IGRETEC, "
    "Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, "
    "Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, "
    "Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear. "
    "Centrum Ganspoel YE2025 deferred (aanbestedende; bruto 20.57m / omzet 1.71m)."
)


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
r = next(x for x in qrows if x.get("task_id") == "rq_2053")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Walfergem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0633687439/woonzorgcentrum-walfergem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2053; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 28.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2053/walfergem_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Walfergem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0633687439/woonzorgcentrum-walfergem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2053; EN mirror YE2025 Medium; filed 28-07-2026; Last balance sheet year 2025; FTE 76; raw docs/doge/data/raw/tick2053/walfergem_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Walfergem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0633687439/woonzorgcentrum-walfergem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2053; FR mirror YE2025 Medium; deposés le 28-07-2026; raw docs/doge/data/raw/tick2053/walfergem_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Walfergem 0633.687.439 Actief VZW Asse",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0633687439",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2053; Actief VZW; Stevensveld 3 1730 Asse; 1 VE; NACE RVT; KBO email empty; aanbestedende overheid flag not present in KBO extract",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Walfergem website contact info@walfergem.be",
        "url": "https://www.walfergem.be/contact",
        "publisher": "WZC Walfergem",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2053; site mailto info@walfergem.be; FOI email sourced; raw docs/doge/data/raw/tick2053/site_walfergem_contact.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_walfergem_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2053; omzet JUMP {OMZET} +2.48pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_walfergem_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2053; pnl DROP {PNL} -25.19pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_walfergem_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2053; equity JUMP {EQUITY} +28.60pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_walfergem_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2053; bruto DROP {BRUTO} -1.86pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_walfergem_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2053; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_walfergem_jr2025_statutory_wzc",
    "title": "WZC Walfergem YE2025 leftover dual (omzet JUMP 8.88m / pnl DROP 0.95m)",
    "entity_id": ENTITY,
    "beneficiary": "Vlaams-Brabant elderly-care residents (WZC Walfergem Asse)",
    "legal_basis": "VZW WZC operator (KBO 0633.687.439)",
    "decision_date": "2026-07-28",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0633687439/woonzorgcentrum-walfergem",
    "stated_goal": "WZC Walfergem Asse",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>Walfergem>JR2025_statutory_L5",
    "notes": "tick2053; Medium CW; assets/debt Unknown; preferred FARO/AIESH/REW YE2024; Ganspoel YE2025 deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_walfergem_omzet_jump_8_88m_pnl_drop_jr2025",
    "name": "Walfergem omzet JUMP 8.88m / pnl DROP 0.95m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>Walfergem>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; VZW WZC dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Vlaams-Brabant elderly-care residents via Walfergem Asse",
    "stated_goal": "WZC Walfergem",
    "measured_outcome": "Medium CW YE2025; 8.88m omzet JUMP +2.48pct; pnl DROP -25.19pct; equity JUMP +28.60pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "4.0",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs split; explain pnl DROP vs equity JUMP",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2053 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Walfergem (Asse)",
    "name_fr": "Maison de repos et de soins Walfergem (Asse)",
    "name_en": "Walfergem nursing home (Asse)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.walfergem.be/",
    "foi_email": "info@walfergem.be",
    "foi_postal": "Stevensveld 3, 1730 Asse",
    "notes": (
        "tick2053 YE2025 Medium CW NL+EN+FR + Strong KBO 0633.687.439 Actief VZW 1 VE; omzet JUMP 8.88m pnl DROP 0.95m equity JUMP 4.26m bruto DROP 6.54m FTE 76; "
        "assets/debt Unknown; neerlegging 28.07.2026; FOI "
        + GAP
        + "; preferred FARO/AIESH/REW YE2024; Centrum Ganspoel YE2025 deferred; do not redo Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>Walfergem>NBB_PDF_assets_debt_pnl_drop_equity_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; pnl DROP -25.19pct path vs equity JUMP +28.60pct",
    "why_it_matters": "Medium CW shows 8.88m omzet VL WZC VZW with pnl DROP and equity JUMP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Woonzorgcentrum Walfergem vzw",
    "recipient_email": "info@walfergem.be",
    "recipient_postal": "Stevensveld 3, 1730 Asse",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_walfergem_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_walfergem_omzet_jump_8_88m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2053; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Walfergem (NBB PDF / assets-debt / pnl-drop + equity-jump matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Walfergem VZW — KBO **0633.687.439**  
**recipient:** info@walfergem.be · Stevensveld 3, 1730 Asse  
**sources:** [CW NL](https://www.companyweb.be/nl/0633687439/woonzorgcentrum-walfergem) · [CW EN](https://www.companyweb.be/en/0633687439/woonzorgcentrum-walfergem) · [CW FR](https://www.companyweb.be/fr/0633687439/woonzorgcentrum-walfergem) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0633687439) · [site contact](https://www.walfergem.be/contact)  
**tick:** 2052  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **28.07.2026**): omzet **EUR8,880,682** JUMP +2.48%; pnl **EUR947,077** DROP −25.19%; equity **EUR4,258,074** JUMP +28.60%; bruto **EUR6,540,292** DROP −1.86%; FTE **76**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Stevensveld 3 Asse; NACE RVT; aanbestedende-overheid flag not in KBO extract.
- Preferred stall: FARO/AIESH/REW still YE2024. Centrum Ganspoel YE2025 deferred.
- Email via official site contact mailto.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Walfergem vzw — Stevensveld 3, 1730 Asse
info@walfergem.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Walfergem + balanstotaal (KBO 0633.687.439)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 28.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting pnl DROP (~−25.2%) bij equity JUMP (~+28.6%) en milde omzet JUMP (~+2.5%).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2053":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Ter Berk Anzegem — WZC Walfergem YE2025 Medium"
        x["notes"] = (
            "tick2053 Walfergem Medium omzet JUMP 8.88m pnl DROP 0.95m equity JUMP 4.26m bruto DROP 6.54m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Ganspoel deferred; next rq_2054; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover WZC Walfergem YE2025 Medium CW; KBO 0633.687.439; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2054" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2054",
            "title": "leftover dual hole-fill after Walfergem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2053 after Walfergem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet; Centrum Ganspoel YE2025 deferred). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2053 Walfergem; next every-10 2060",
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
        "last_unit_id": "rq_2053",
        "ticks_completed": "2053",
        "paused": "no",
        "notes": (
            "tick2053 leftover Walfergem 0633.687.439 Medium CW (omzet JUMP 8.88m pnl DROP 0.95m equity JUMP 4.26m bruto DROP 6.54m FTE 76; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Ganspoel deferred; next rq_2054; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2053 - {UTC} - rq_2053 WZC Walfergem (omzet JUMP 8.88m / pnl DROP 0.95m / Medium)

- Unit: **rq_2053** leftover dual after **rq_2052 Ter Berk Anzegem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **WZC Walfergem** YE2025 (KBO **0633.687.439**; Stevensveld 3 Asse; Vlaams-Brabant **VZW** WZC / **1 VE**). Centrum Ganspoel YE2025 also live — deferred. Do not redo Ter Berk Anzegem/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hieronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren/Sint-Jozef Rumst.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR8,880,682** JUMP +2.48%; pnl **EUR947,077** DROP −25.19%; equity **EUR4,258,074** JUMP +28.60%; bruto **EUR6,540,292** DROP −1.86%; FTE **76**; neerlegging **28.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@walfergem.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2053=done + rq_2054 open; loop_state ticks=2053; raw under docs/doge/data/raw/tick2053/.
- FOI: **ready not sent** (human-gated; info@walfergem.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2054 (AGB/FARO-if-YE2025 / AIESH-REW / Ganspoel deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2053 Walfergem", OMZET, "pi", PI)
