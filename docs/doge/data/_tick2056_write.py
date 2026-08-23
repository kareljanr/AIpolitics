# ephemeral tick2056 — Huize Westerhauwe YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T19:05:00Z"
ENTITY = "vzw_huize_westerhauwe"
GAP = "gap_westerhauwe_nbb_pdf_assets_debt_pnl_flip_loss_matrix_l5"
SRC = "src_westerhauwe_jr2025_cw"
SRC_EN = "src_westerhauwe_jr2025_cw_en"
SRC_FR = "src_westerhauwe_jr2025_cw_fr"
SRC_KBO = "src_westerhauwe_kbo_2056"
SRC_SITE = "src_westerhauwe_site_2056"

OMZET = "1964040"
PNL = "-228705"
EQUITY = "1407861"
BRUTO = "3143282"
FTE = "37.8"
OMZET24 = "1880814"
PNL24 = "100423"
EQUITY24 = "1636786"
BRUTO24 = "2970116"
# pi = 0.55*3.8 + 0.35*5.8 + 0.10*(10-4) = 2.09 + 2.03 + 0.6 = 4.72 → 4.7
PI = "4.7"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2056")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Huize Westerhauwe YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0455080547/huize-westerhauwe",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2056; YE2025 omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 23.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2056/westerhauwe_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Huize Westerhauwe YE2025 statutory",
        "url": "https://www.companyweb.be/en/0455080547/huize-westerhauwe",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2056; EN mirror YE2025 Medium; filed 23-07-2026; Last balance sheet year 2025; FTE 37.8; raw docs/doge/data/raw/tick2056/westerhauwe_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Huize Westerhauwe YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0455080547/huize-westerhauwe",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2056; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2056/westerhauwe_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Huize Westerhauwe 0455.080.547 Actief VZW Bredene",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455080547",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2056; Actief VZW; Klemskerkestraat 19 8450 Bredene; 1 VE; NACE 87.302; KBO email empty; aanbestedende overheid flag not present in KBO extract",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Huize Westerhauwe site info@huize-westerhauwe.be",
        "url": "https://www.huize-westerhauwe.be/",
        "publisher": "Huize Westerhauwe vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2056; site+contact list info@huize-westerhauwe.be; raw docs/doge/data/raw/tick2056/westerhauwe_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_westerhauwe_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2056; omzet JUMP {OMZET} +4.42pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_westerhauwe_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2056; pnl FLIP LOSS {PNL} vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_westerhauwe_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2056; equity DROP {EQUITY} -13.99pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_westerhauwe_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2056; bruto JUMP {BRUTO} +5.83pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_westerhauwe_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2056; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_westerhauwe_jr2025_statutory_wzc",
    "title": "Huize Westerhauwe YE2025 leftover dual (omzet JUMP 1.96m / pnl FLIP LOSS 0.23m)",
    "entity_id": ENTITY,
    "beneficiary": "West-Vlaanderen elderly-care residents (Huize Westerhauwe Bredene)",
    "legal_basis": "VZW WZC/service-flat operator (KBO 0455.080.547)",
    "decision_date": "2026-07-23",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0455080547/huize-westerhauwe",
    "stated_goal": "WZC / service flats Huize Westerhauwe Bredene",
    "cut_option": "Publish NBB PDF assets/debt + explain FLIP to LOSS vs omzet JUMP FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Bredene>HuizeWesterhauwe>JR2025_statutory_L5",
    "notes": "tick2056; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_westerhauwe_omzet_jump_1_96m_pnl_flip_loss_jr2025",
    "name": "Huize Westerhauwe omzet JUMP 1.96m / pnl FLIP LOSS 0.23m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Bredene>HuizeWesterhauwe>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; VZW WZC dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "West-Vlaanderen elderly-care residents via Huize Westerhauwe Bredene",
    "stated_goal": "WZC / service flats Huize Westerhauwe",
    "measured_outcome": "Medium CW YE2025; 1.96m omzet JUMP +4.42pct with pnl FLIP to LOSS EUR-228k (was +100k); equity DROP -14pct; NBB PDF residual",
    "absurdity_score": "5.8",
    "cost_score": "3.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain FLIP to LOSS vs omzet JUMP; map subsidy stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2056 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Huize Westerhauwe (VZW WZC Bredene)",
    "name_fr": "Huize Westerhauwe (ASBL MRS Bredene)",
    "name_en": "Huize Westerhauwe (VZW nursing home Bredene)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.huize-westerhauwe.be/",
    "foi_email": "info@huize-westerhauwe.be",
    "foi_postal": "Klemskerkestraat 19, 8450 Bredene",
    "notes": (
        "tick2056 YE2025 Medium CW NL+EN+FR + Strong KBO 0455.080.547 Actief VZW 1 VE; omzet JUMP 1.96m pnl FLIP LOSS 0.23m equity DROP 1.41m bruto JUMP 3.14m FTE 37.8; "
        "assets/debt Unknown; neerlegging 23.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Bredene>HuizeWesterhauwe>NBB_PDF_assets_debt_pnl_flip_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of FLIP to LOSS (EUR-228k vs YE2024 profit EUR100k) despite omzet JUMP",
    "why_it_matters": "Medium CW shows 1.96m omzet VL WZC VZW with pnl FLIP to LOSS and equity DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Huize Westerhauwe vzw",
    "recipient_email": "info@huize-westerhauwe.be",
    "recipient_postal": "Klemskerkestraat 19, 8450 Bredene",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_westerhauwe_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_westerhauwe_omzet_jump_1_96m_pnl_flip_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2056; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Huize Westerhauwe (NBB PDF / assets-debt / pnl-flip-loss)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Huize Westerhauwe VZW — KBO **0455.080.547**  
**recipient:** info@huize-westerhauwe.be · Klemskerkestraat 19, 8450 Bredene  
**sources:** [CW NL](https://www.companyweb.be/nl/0455080547/huize-westerhauwe) · [CW EN](https://www.companyweb.be/en/0455080547/huize-westerhauwe) · [CW FR](https://www.companyweb.be/fr/0455080547/huize-westerhauwe) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455080547) · [site](https://www.huize-westerhauwe.be/)  
**tick:** 2056  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **23.07.2026**): omzet **EUR1,964,040** JUMP +4.42%; pnl **LOSS EUR-228,705** FLIP vs YE2024 profit EUR100,423; equity **EUR1,407,861** DROP −13.99%; bruto **EUR3,143,282** JUMP +5.83%; FTE **37.8**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Klemskerkestraat 19 Bredene; NACE 87.302.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Huize Westerhauwe vzw — Klemskerkestraat 19, 8450 Bredene
info@huize-westerhauwe.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Huize Westerhauwe + verliesverklaring (KBO 0455.080.547)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 23.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting omslag naar verlies (van winst EUR100.423 YE2024 naar verlies EUR-228.705 YE2025) bij omzet JUMP.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, "
    "Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, "
    "Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "Sint-Jozef Rumst, Veilige Have, Witte Meren, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
    "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
    "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2056":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Centrum Ganspoel — Huize Westerhauwe YE2025 Medium"
        x["notes"] = (
            "tick2056 Huize Westerhauwe Medium omzet JUMP 1.96m pnl FLIP LOSS 0.23m equity DROP 1.41m bruto JUMP 3.14m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2057; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover Huize Westerhauwe YE2025 Medium CW; KBO 0455.080.547; "
            f"omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2057" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2057",
            "title": "leftover dual hole-fill after Huize Westerhauwe",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2056 after Huize Westerhauwe YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2056 Huize Westerhauwe; next every-10 2060",
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
        "last_unit_id": "rq_2056",
        "ticks_completed": "2056",
        "paused": "no",
        "notes": (
            "tick2056 leftover Huize Westerhauwe 0455.080.547 Medium CW (omzet JUMP 1.96m pnl FLIP LOSS 0.23m equity DROP 1.41m bruto JUMP 3.14m FTE 37.8; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2057; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2056 - {UTC} - rq_2056 Huize Westerhauwe (omzet JUMP 1.96m / pnl FLIP LOSS 0.23m / Medium)

- Unit: **rq_2056** leftover dual after **rq_2055 Centrum Ganspoel**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Huize Westerhauwe** YE2025 (KBO **0455.080.547**; Klemskerkestraat 19 Bredene; West-Vlaanderen **VZW** WZC / **1 VE**). Do not redo Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR1,964,040** JUMP +4.42%; pnl **LOSS EUR-228,705** FLIP vs YE2024 profit EUR100,423; equity **EUR1,407,861** DROP −13.99%; bruto **EUR3,143,282** JUMP +5.83%; FTE **37.8**; neerlegging **23.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@huize-westerhauwe.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2056=done + rq_2057 open; loop_state ticks=2056; raw under docs/doge/data/raw/tick2056/.
- FOI: **ready not sent** (human-gated; info@huize-westerhauwe.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2057 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2056 Huize Westerhauwe", OMZET, "pi", PI)
