# ephemeral tick2029 — Karus psych YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T11:55:00Z"
ENTITY = "vzw_karus"
GAP = "gap_karus_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_karus_jr2025_cw"
SRC_EN = "src_karus_jr2025_cw_en"
SRC_FR = "src_karus_jr2025_cw_fr"
SRC_KBO = "src_karus_kbo_2025"
SRC_SITE = "src_karus_site_2025"

OMZET = "70079391"
PNL = "1756084"
EQUITY = "92800700"
BRUTO = "56053974"
FTE = "639.3"
OMZET24 = "66786071"
PNL24 = "1399527"
EQUITY24 = "91665733"
BRUTO24 = "56759855"
FTE24 = "639.6"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2029")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

# claim in_progress early
for x in qrows:
    if x.get("task_id") == "rq_2029":
        x["status"] = "in_progress"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
save("docs/doge/data/research_queue.csv", qrows, qfields)

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Karus Merelbeke-Melle YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0861314369/karus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2029; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 27.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2029/karus_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Karus Merelbeke-Melle YE2025 statutory",
        "url": "https://www.companyweb.be/en/0861314369/karus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2029; EN mirror YE2025 Medium; filed 27-06-2026; Last balance sheet year 2025; FTE 639.3; raw docs/doge/data/raw/tick2029/karus_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Karus Merelbeke-Melle YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0861314369/karus",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2029; FR mirror YE2025 Medium; déposés le 27-06-2026; raw docs/doge/data/raw/tick2029/karus_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Karus 0861.314.369 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0861314369",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2029; Actief VZW; Caritasstraat 76 9090 Merelbeke-Melle; 8 VE; sinds 27.10.2003; raw docs/doge/data/raw/tick2029/karus_kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "karus.be Psychiatrisch ziekenhuis Karus",
        "url": "https://www.karus.be/",
        "publisher": "Karus VZW",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2029; info@karus.be; +32 9 210 69 69; Caritasstraat 76 Merelbeke-Melle + campus Gent Beukenlaan 20; erkenning 959",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_karus_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2029; omzet JUMP {OMZET} +4.93pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_karus_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2029; pnl JUMP {PNL} +25.48pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_karus_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2029; equity JUMP {EQUITY} +1.24pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_karus_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2029; bruto DROP {BRUTO} -1.24pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_karus_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2029; YE2025 FTE {FTE} vs YE2024 {FTE24}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_karus_jr2025_statutory",
    "title": "Karus YE2025 leftover dual (omzet JUMP 70.08m / pnl JUMP 1.76m / equity JUMP 92.80m)",
    "entity_id": ENTITY,
    "beneficiary": "Oost-Vlaanderen psych patients via Karus VZW (Merelbeke-Melle + Gent)",
    "legal_basis": "VZW/ASBL psychiatrisch ziekenhuis (KBO 0861.314.369)",
    "decision_date": "2026-06-27",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0861314369/karus",
    "stated_goal": "Psychiatric hospital / mental-health care Merelbeke-Melle + Gent",
    "cut_option": "Publish NBB PDF assets/debt FOI; map RIZIV/public vs private revenue",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>MerelbekeMelle>Karus>JR2025_statutory_L5",
    "notes": "tick2029; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*6.0 + 0.10*(10-4) = 3.025 + 2.1 + 0.6 = 5.725 ~ round 5.7
# larger psych hospital ~70m omzet → cost_score 6.0; pnl JUMP +25pct absurdity 5.5
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_karus_omzet_jump_70_08m_pnl_jump_1_76m_jr2025",
    "name": "Karus omzet JUMP 70.08m / pnl JUMP 1.76m (+25pct) / equity JUMP 92.80m (YE2025)",
    "level": "L5",
    "type": "flemish_psych_hospital_vzw_dual",
    "hierarchy_path": "OostVlaanderen>MerelbekeMelle>Karus>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Oost-Vlaanderen psych patients via Karus VZW",
    "stated_goal": "Psychiatric hospital / mental-health care",
    "measured_outcome": "Medium CW YE2025; 70.08m omzet JUMP +4.93pct with pnl JUMP +25.48pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.0",
    "difficulty": "4.0",
    "priority_index": "5.7",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map RIZIV/public vs private revenue mix",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2029 leftover psych dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Karus (psychiatrisch ziekenhuis)",
    "name_fr": "Karus (hôpital psychiatrique)",
    "name_en": "Karus (psychiatric hospital)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.karus.be/",
    "foi_email": "info@karus.be",
    "foi_postal": "Caritasstraat 76, 9090 Merelbeke-Melle",
    "notes": "tick2029 YE2025 Medium CW NL+EN+FR + Strong KBO 0861.314.369 Actief VZW; omzet JUMP 70.08m pnl JUMP 1.76m (+25.48pct) equity JUMP 92.80m bruto DROP 56.05m FTE 639.3; assets/debt Unknown; neerlegging 27.06.2026; 8 VE; campuses Merelbeke-Melle + Gent; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo WZC De Foyer Gent/WZC Sint-Carolus Ternat/WZC Zilverbos/Sint Carolus Mayerhof/Evara/Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge",
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
    "hierarchy_path": "OostVlaanderen>MerelbekeMelle>Karus>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); RIZIV/public vs private revenue split; pnl JUMP +25.48pct recon vs omzet +4.93pct",
    "why_it_matters": "Medium CW shows 70.08m omzet psych hospital with pnl JUMP without balance sheet or public/private revenue mix",
    "priority": "7",
    "recipient_body": "Karus VZW",
    "recipient_email": "info@karus.be",
    "recipient_postal": "Caritasstraat 76, 9090 Merelbeke-Melle",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_karus_jr2025_statutory",
    "linked_leaderboard_id": "lb_karus_omzet_jump_70_08m_pnl_jump_1_76m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2029; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Karus (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Karus VZW — KBO **0861.314.369**  
**recipient:** info@karus.be · Caritasstraat 76, 9090 Merelbeke-Melle  
**sources:** [CW NL](https://www.companyweb.be/nl/0861314369/karus) · [CW EN](https://www.companyweb.be/en/0861314369/karus) · [CW FR](https://www.companyweb.be/fr/0861314369/karus) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0861314369) · [karus.be](https://www.karus.be/)  
**tick:** 2029  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **27.06.2026**): omzet **EUR70,079,391** JUMP +4.93%; pnl **EUR1,756,084** JUMP +25.48%; equity **EUR92,800,700** JUMP +1.24%; bruto **EUR56,053,974** DROP -1.24%; FTE **639.3**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Karus VZW — Caritasstraat 76, 9090 Merelbeke-Melle
info@karus.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 Karus (KBO 0861.314.369)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 27.06.2026).
2. Assets / schulden LT-ST / cash.
3. Split RIZIV/publieke middelen vs private/andere inkomsten 2025.
4. Toelichting pnl JUMP (+25,48pct) t.o.v. omzet JUMP (+4,93pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

skip_list = (
    "Do NOT redo Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara/Multiversum, "
    "Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, "
    "PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, "
    "Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, "
    "AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, "
    "Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, "
    "IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, "
    "BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, "
    "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, "
    "Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

qrows, qfields = load("docs/doge/data/research_queue.csv")
for x in qrows:
    if x.get("task_id") == "rq_2029":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC De Foyer Gent — Karus YE2025 Medium"
        x["notes"] = (
            "tick2029 Karus Medium omzet JUMP 70.08m pnl JUMP 1.76m (+25.48pct) equity JUMP 92.80m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2030 EVERY-10; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover Karus YE2025 Medium CW; KBO 0861.314.369; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2030" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2030",
            "title": "EVERY-10 + leftover dual hole-fill after Karus",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2029 after Karus YE2025 Medium. FIRST: EVERY-10 mandatory — refresh progress_every_10_ticks.md (A–E % of €347.956bn TE) "
                "+ doge_waste_top10_current.md (top 10 by priority_index); note in log. THEN leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Bethanie / other unused YE2025 if live with omzet). "
                + skip_list
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2029 Karus; EVERY-10 due at 2030",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue updated")

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
for x in srows2:
    if x.get("state_id") == "main":
        x["mode"] = "continuous"
        x["current_sprint"] = "hole_fill"
        x["last_tick_utc"] = UTC
        x["last_unit_id"] = "rq_2029"
        x["ticks_completed"] = "2029"
        x["paused"] = "no"
        x["notes"] = (
            "tick2029 leftover Karus 0861.314.369 Medium CW (omzet JUMP 70.08m pnl JUMP 1.76m +25.48pct "
            "equity JUMP 92.80m bruto DROP 56.05m FTE 639.3; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2030 EVERY-10; next every-10 2030; continuous hole_fill"
        )
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state updated")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2029 - {UTC} - rq_2029 Karus (omzet JUMP 70.08m / pnl JUMP 1.76m / Medium)

- Unit: **rq_2029** leftover dual after **rq_2028 WZC De Foyer Gent**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024**. Took unused leftover **Karus** YE2025 (KBO **0861.314.369**; Caritasstraat 76 Merelbeke-Melle; Oost-Vlaanderen **psychiatrisch ziekenhuis VZW** / campuses Merelbeke-Melle + Gent). Do not redo De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR70,079,391** JUMP +4.93%; pnl **EUR1,756,084** JUMP +25.48%; equity **EUR92,800,700** JUMP +1.24%; bruto **EUR56,053,974** DROP -1.24%; FTE **639.3**; neerlegging **27.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 8 VE; email info@karus.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_karus); foi + draft gap_karus_nbb_pdf_assets_debt_pnl_jump_matrix_l5; rq_2029=done + rq_2030 open (EVERY-10); loop_state ticks=2029; raw under docs/doge/data/raw/tick2029/.
- FOI: **ready not sent** (human-gated; info@karus.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2030 EVERY-10 + (AGB/FARO-if-YE2025 / AIESH-REW / Bethanie / unused DSO-IGS-HVZ-hospital-psych-WZC).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log appended")
print("DONE tick2029")
