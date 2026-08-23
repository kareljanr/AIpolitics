# ephemeral tick2059 — WZC Home Vrijzicht YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T19:50:00Z"
ENTITY = "vzw_wzc_home_vrijzicht"
GAP = "gap_vrijzicht_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_vrijzicht_jr2025_cw"
SRC_EN = "src_vrijzicht_jr2025_cw_en"
SRC_FR = "src_vrijzicht_jr2025_cw_fr"
SRC_KBO = "src_vrijzicht_kbo_2059"
SRC_SITE = "src_vrijzicht_site_2059"

OMZET = "8551479"
PNL = "195194"
EQUITY = "5953029"
BRUTO = "8173946"
FTE = "112.8"
OMZET24 = "8434905"
PNL24 = "140668"
EQUITY24 = "5779644"
BRUTO24 = "8107037"
# pi = 0.55*4.8 + 0.35*4.9 + 0.10*(10-4) = 2.64 + 1.715 + 0.6 = 4.955 → 5.0
PI = "5.0"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2059")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Home Vrijzicht YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2059; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2059/vrijzicht_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Home Vrijzicht YE2025 statutory",
        "url": "https://www.companyweb.be/en/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2059; EN mirror YE2025 Medium; filed 10-06-2026; Last balance sheet year 2025; FTE 112.8; raw docs/doge/data/raw/tick2059/vrijzicht_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Home Vrijzicht YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2059; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2059/vrijzicht_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Home Vrijzicht 0416.337.262 Actief VZW Ieper",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416337262",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2059; Actief VZW; Veurnseweg 538 8906 Ieper; 1 VE; NACE 87.101/87.301; KBO email empty; aanbestedende overheid flag not present",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Home Vrijzicht site info@homevrijzicht.be",
        "url": "https://www.homevrijzicht.be/",
        "publisher": "WZC Home Vrijzicht vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2059; site+contact info@homevrijzicht.be / socialedienst@homevrijzicht.be; raw docs/doge/data/raw/tick2059/vrijzicht_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_vrijzicht_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2059; omzet JUMP {OMZET} +1.38pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_vrijzicht_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2059; pnl JUMP {PNL} +38.76pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_vrijzicht_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2059; equity JUMP {EQUITY} +3.00pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_vrijzicht_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2059; bruto JUMP {BRUTO} +0.83pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_vrijzicht_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2059; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_vrijzicht_jr2025_statutory_wzc",
    "title": "Home Vrijzicht YE2025 leftover dual (omzet JUMP 8.55m / pnl JUMP 0.20m)",
    "entity_id": ENTITY,
    "beneficiary": "Ieper elderly residents (WZC Home Vrijzicht)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0416.337.262)",
    "decision_date": "2026-06-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw",
    "stated_goal": "WZC residential elderly care Ieper Veurnseweg",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl JUMP +38.76pct",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>HomeVrijzicht>JR2025_statutory_L5",
    "notes": "tick2059; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_vrijzicht_omzet_jump_8_55m_pnl_jump_jr2025",
    "name": "Home Vrijzicht omzet JUMP 8.55m / pnl JUMP 0.20m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>HomeVrijzicht>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Ieper elderly residents via WZC Home Vrijzicht",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 8.55m omzet JUMP +1.38pct with pnl JUMP +38.76pct; NBB PDF residual",
    "absurdity_score": "4.9",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl JUMP; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2059 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "WZC Home Vrijzicht (VZW, Ieper)",
    "name_fr": "WZC Home Vrijzicht (ASBL MRS, Ieper)",
    "name_en": "WZC Home Vrijzicht (VZW nursing home Ieper)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.homevrijzicht.be/",
    "foi_email": "info@homevrijzicht.be",
    "foi_postal": "Veurnseweg 538, 8906 Ieper",
    "notes": (
        "tick2059 YE2025 Medium CW NL+EN+FR + Strong KBO 0416.337.262 Actief VZW 1 VE; omzet JUMP 8.55m pnl JUMP 0.20m equity JUMP 5.95m bruto JUMP 8.17m FTE 112.8; "
        "assets/debt Unknown; neerlegging 10.06.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo 't Pandje/Groep Zorg H. Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>HomeVrijzicht>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl JUMP +38.76pct YE2025",
    "why_it_matters": "Medium CW shows 8.55m omzet WZC VZW with pnl JUMP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "WZC Home Vrijzicht vzw",
    "recipient_email": "info@homevrijzicht.be",
    "recipient_postal": "Veurnseweg 538, 8906 Ieper",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_vrijzicht_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_vrijzicht_omzet_jump_8_55m_pnl_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2059; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Home Vrijzicht (NBB PDF / assets-debt / pnl-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WZC Home Vrijzicht VZW — KBO **0416.337.262**  
**recipient:** info@homevrijzicht.be · Veurnseweg 538, 8906 Ieper  
**sources:** [CW NL](https://www.companyweb.be/nl/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw) · [CW EN](https://www.companyweb.be/en/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw) · [CW FR](https://www.companyweb.be/fr/0416337262/woon-en-zorgcentrum-home-vrijzicht-vzw) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416337262) · [site](https://www.homevrijzicht.be/)  
**tick:** 2059  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.06.2026**): omzet **EUR8,551,479** JUMP +1.38%; pnl **EUR195,194** JUMP +38.76% vs YE2024 EUR140,668; equity **EUR5,953,029** JUMP +3.00%; bruto **EUR8,173,946** JUMP +0.83%; FTE **112.8**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Veurnseweg 538 Ieper; NACE 87.101/87.301; niet gemarkeerd als aanbestedende overheid.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live YE2025: Christine / Ter Burg / OLV Wezembeek / Sint-Antonius.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WZC Home Vrijzicht vzw — Veurnseweg 538, 8906 Ieper
info@homevrijzicht.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Home Vrijzicht + subsidiematrix (KBO 0416.337.262)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting stijging winst van EUR140.668 (YE2024) naar EUR195.194 (YE2025; +38,76%).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, "
    "AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2059":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after 't Pandje Izegem — Home Vrijzicht YE2025 Medium"
        x["notes"] = (
            "tick2059 Home Vrijzicht Medium omzet JUMP 8.55m pnl JUMP 0.20m equity JUMP 5.95m bruto JUMP 8.17m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2060; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover Home Vrijzicht YE2025 Medium CW; KBO 0416.337.262; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2060" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2060",
            "title": "leftover dual hole-fill after Home Vrijzicht (EVERY-10)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2059 after Home Vrijzicht YE2025 Medium. EVERY-10 mandatory first (progress_every_10_ticks.md + doge_waste_top10_current.md). "
                "Then prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Christine / Ter Burg / OLV Wezembeek / Sint-Antonius YE2025 deferred if still live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2059 Home Vrijzicht; EVERY-10 at 2060",
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
        "last_unit_id": "rq_2059",
        "ticks_completed": "2059",
        "paused": "no",
        "notes": (
            "tick2059 leftover Home Vrijzicht 0416.337.262 Medium CW (omzet JUMP 8.55m pnl JUMP 0.20m equity JUMP 5.95m bruto JUMP 8.17m FTE 112.8; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2060 EVERY-10; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2059 - 2026-08-24T19:50:00Z - rq_2059 Home Vrijzicht (omzet JUMP 8.55m / pnl JUMP 0.20m / Medium)

- Unit: **rq_2059** leftover dual after **rq_2058 't Pandje**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **WZC Home Vrijzicht** YE2025 (KBO **0416.337.262**; Veurnseweg 538 Ieper; West-Vlaanderen **VZW** WZC / **1 VE**). Christine / Ter Burg / OLV Wezembeek / Sint-Antonius YE2025 also live - deferred. Do not redo 't Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR8,551,479** JUMP +1.38%; pnl **EUR195,194** JUMP +38.76%; equity **EUR5,953,029** JUMP +3.00%; bruto **EUR8,173,946** JUMP +0.83%; FTE **112.8**; neerlegging **10.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@homevrijzicht.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.0); entities (+1 vzw_wzc_home_vrijzicht); foi + draft {GAP}; rq_2059=done + rq_2060 open (EVERY-10); loop_state ticks=2059; raw under docs/doge/data/raw/tick2059/.
- FOI: **ready not sent** (human-gated; info@homevrijzicht.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2060 (EVERY-10 mandatory + AGB/FARO-if-YE2025 / AIESH-REW / Christine-TerBurg-Wezembeek-Antonius deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2059")
