# ephemeral tick2063 — WZC Sint-Antonius Sint-Pieters-Leeuw YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T20:50:00Z"
ENTITY = "vzw_wzc_sint_antonius"
GAP = "gap_sint_antonius_nbb_pdf_assets_debt_pnl_flip_loss_matrix_l5"
SRC = "src_sint_antonius_jr2025_cw"
SRC_EN = "src_sint_antonius_jr2025_cw_en"
SRC_FR = "src_sint_antonius_jr2025_cw_fr"
SRC_KBO = "src_sint_antonius_kbo_2063"
SRC_SITE = "src_sint_antonius_site_2063"

OMZET = "7455500"
PNL = "-243742"
EQUITY = "12773930"
BRUTO = "7042846"
FTE = "88.1"
OMZET24 = "7446250"
PNL24 = "4317"
EQUITY24 = "13310521"
BRUTO24 = "6759745"
# pi = 0.55*4.8 + 0.35*5.5 + 0.10*(10-4) = 2.64 + 1.925 + 0.6 = 5.165 → 5.2
PI = "5.2"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2063")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Sint-Antonius YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0424236725/woon-en-zorgcentrum-sint-antonius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2063; YE2025 omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 12.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2063/antonius_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Antonius YE2025 statutory",
        "url": "https://www.companyweb.be/en/0424236725/woon-en-zorgcentrum-sint-antonius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2063; EN mirror YE2025 Medium; filed 12-06-2026; Last balance sheet year 2025; FTE 88.1; raw docs/doge/data/raw/tick2063/antonius_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Sint-Antonius YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0424236725/woon-en-zorgcentrum-sint-antonius",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2063; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2063/antonius_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Sint-Antonius 0424.236.725 Actief VZW Sint-Pieters-Leeuw",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424236725",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2063; Actief VZW; Jules Sermonstraat 17 1600 Sint-Pieters-Leeuw (since 07.09.1999); 1 VE; NACE 87.101; KBO email empty; not marked aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "WZC Sint-Antonius site www.stantonius.be (info@stantonius.be)",
        "url": "https://www.stantonius.be/",
        "publisher": "Woon- en Zorgcentrum Sint-Antonius vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2063; Jules Sermonstraat 17 1600 Sint-Pieters-Leeuw; Tel 02 377 18 90; email info@stantonius.be; raw docs/doge/data/raw/tick2063/antonius_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_sint_antonius_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2063; omzet JUMP {OMZET} +0.12pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_sint_antonius_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2063; pnl FLIP LOSS {PNL} vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_sint_antonius_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2063; equity DROP {EQUITY} -4.03pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_sint_antonius_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2063; bruto JUMP {BRUTO} +4.19pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_sint_antonius_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2063; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_sint_antonius_jr2025_statutory_wzc",
    "title": "WZC Sint-Antonius YE2025 leftover dual (omzet JUMP 7.46m / pnl FLIP LOSS 0.24m)",
    "entity_id": ENTITY,
    "beneficiary": "Sint-Pieters-Leeuw elderly residents (WZC Sint-Antonius)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0424.236.725)",
    "decision_date": "2026-06-12",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0424236725/woon-en-zorgcentrum-sint-antonius",
    "stated_goal": "WZC residential elderly care Sint-Pieters-Leeuw Jules Sermonstraat",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl FLIP LOSS despite flat omzet JUMP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>SintPietersLeeuw>WZCSintAntonius>JR2025_statutory_L5",
    "notes": "tick2063; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nlb = {
    **{k: "" for k in lfields},
    "item_id": "lb_sint_antonius_omzet_jump_7_46m_pnl_flip_loss_jr2025",
    "name": "WZC Sint-Antonius omzet JUMP 7.46m / pnl FLIP LOSS 0.24m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>SintPietersLeeuw>WZCSintAntonius>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Sint-Pieters-Leeuw elderly residents via WZC Sint-Antonius",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.46m omzet JUMP +0.12pct with pnl FLIP LOSS -0.24m vs YE2024 profit 4k; equity DROP -4.03pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS despite flat omzet; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2063 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nlb["item_id"] for x in lrows):
    lrows.append(nlb)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "WZC Sint-Antonius (VZW, Sint-Pieters-Leeuw)",
    "name_fr": "MRS Saint-Antoine (ASBL, Sint-Pieters-Leeuw)",
    "name_en": "WZC Sint-Antonius (VZW nursing home Sint-Pieters-Leeuw)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.stantonius.be/",
    "foi_email": "info@stantonius.be",
    "foi_postal": "Jules Sermonstraat 17, 1600 Sint-Pieters-Leeuw",
    "notes": (
        "tick2063 YE2025 Medium CW NL+EN+FR + Strong KBO 0424.236.725 Actief VZW 1 VE; omzet JUMP 7.46m pnl FLIP LOSS 0.24m equity DROP 12.77m bruto JUMP 7.04m FTE 88.1; "
        "assets/debt Unknown; neerlegging 12.06.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo OLV Wezembeek/Ter Burg/Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>SintPietersLeeuw>WZCSintAntonius>NBB_PDF_assets_debt_pnl_flip_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl FLIP LOSS YE2025 despite flat omzet JUMP",
    "why_it_matters": "Medium CW shows 7.46m omzet WZC VZW with pnl FLIP LOSS -0.24m and equity DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Woon- en Zorgcentrum Sint-Antonius vzw",
    "recipient_email": "info@stantonius.be",
    "recipient_postal": "Jules Sermonstraat 17, 1600 Sint-Pieters-Leeuw",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_sint_antonius_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_sint_antonius_omzet_jump_7_46m_pnl_flip_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2063; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Antonius (NBB PDF / assets-debt / pnl-flip-loss)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en Zorgcentrum Sint-Antonius VZW — KBO **0424.236.725**  
**recipient:** info@stantonius.be · Jules Sermonstraat 17, 1600 Sint-Pieters-Leeuw  
**sources:** [CW NL](https://www.companyweb.be/nl/0424236725/woon-en-zorgcentrum-sint-antonius) · [CW EN](https://www.companyweb.be/en/0424236725/woon-en-zorgcentrum-sint-antonius) · [CW FR](https://www.companyweb.be/fr/0424236725/woon-en-zorgcentrum-sint-antonius) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424236725) · [site](https://www.stantonius.be/)  
**tick:** 2063  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **12.06.2026**): omzet **EUR7,455,500** JUMP +0.12%; pnl **LOSS EUR-243,742** FLIP vs YE2024 profit EUR4,317; equity **EUR12,773,930** DROP −4.03%; bruto **EUR7,042,846** JUMP +4.19%; FTE **88.1**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Jules Sermonstraat 17 Sint-Pieters-Leeuw; NACE 87.101; niet gemarkeerd als aanbestedende overheid.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en Zorgcentrum Sint-Antonius vzw — Jules Sermonstraat 17, 1600 Sint-Pieters-Leeuw
info@stantonius.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Antonius + subsidiematrix (KBO 0424.236.725)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 12.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting omslag van winst EUR4.317 (YE2024) naar verlies EUR-243.742 (YE2025) bij vrijwel vlakke omzet JUMP +0,12%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo WZC Sint-Antonius, WZC OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, "
    "Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, "
    "Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Zusterhof, Veilige Have, "
    "Witte Meren, Sint-Jozef Rumst, Werken Glorieux, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, "
    "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
    "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2063":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after OLV Wezembeek — Sint-Antonius YE2025 Medium"
        x["notes"] = (
            "tick2063 Sint-Antonius Medium omzet JUMP 7.46m pnl FLIP LOSS 0.24m equity DROP 12.77m bruto JUMP 7.04m; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2064; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover WZC Sint-Antonius YE2025 Medium CW; KBO 0424.236.725; "
            f"omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2064" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2064",
            "title": "leftover dual hole-fill after WZC Sint-Antonius",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2063 after Sint-Antonius YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2063 Sint-Antonius; next every-10 2070",
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
        "last_unit_id": "rq_2063",
        "ticks_completed": "2063",
        "paused": "no",
        "notes": (
            "tick2063 leftover Sint-Antonius 0424.236.725 Medium CW (omzet JUMP 7.46m pnl FLIP LOSS 0.24m equity DROP 12.77m bruto JUMP 7.04m FTE 88.1; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2064; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("loop_state ok")

log = Path("docs/doge/loop_log.md")
block = f"""


## Tick 2063 - 2026-08-24T20:50:00Z - rq_2063 Sint-Antonius (omzet JUMP 7.46m / pnl FLIP LOSS 0.24m / Medium)

- Unit: **rq_2063** leftover dual after **rq_2062 OLV Wezembeek**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC Sint-Antonius** YE2025 (KBO **0424.236.725**; Jules Sermonstraat 17 Sint-Pieters-Leeuw; Vlaams-Brabant **VZW** WZC / **1 VE**). Do not redo OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR7,455,500** JUMP +0.12%; pnl **LOSS EUR-243,742** FLIP vs YE2024 profit EUR4,317; equity **EUR12,773,930** DROP −4.03%; bruto **EUR7,042,846** JUMP +4.19%; FTE **88.1**; neerlegging **12.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@stantonius.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.2); entities (+1 vzw_wzc_sint_antonius); foi + draft {GAP}; rq_2063=done + rq_2064 open; loop_state ticks=2063; raw under docs/doge/data/raw/tick2063/.
- FOI: **ready not sent** (human-gated; info@stantonius.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2064 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log.write_text(log.read_text(encoding="utf-8") + block, encoding="utf-8")
print("log ok")
print("DONE tick2063")
