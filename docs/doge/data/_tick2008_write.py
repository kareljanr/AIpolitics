# ephemeral tick2008 — AZ Oostende YE2025 Medium (leftover dual after Werken Glorieux)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T06:25:00Z"
ENTITY = "vzw_az_oostende"
GAP = "gap_az_oostende_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_az_oostende_jr2025_cw"
SRC_EN = "src_az_oostende_jr2025_cw_en"
SRC_FR = "src_az_oostende_jr2025_cw_fr"
SRC_KBO = "src_az_oostende_kbo_2008"
SRC_SITE = "src_az_oostende_site_2008"

OMZET = "308721709"
PNL = "2031443"
EQUITY = "165930443"
BRUTO = "159965423"
FTE = "1670.5"
OMZET24 = "304410200"
PNL24 = "1798471"
EQUITY24 = "152086573"
BRUTO24 = "157127060"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2008")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZ Oostende YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0800023336/algemeen-ziekenhuis-oostende",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2008; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 26.06.2026; assets/debt Unknown; Damiaan 0464.564.177 dual shell 0 FTE not double-counted; raw docs/doge/data/raw/tick2008/azo_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZ Oostende YE2025 statutory",
        "url": "https://www.companyweb.be/en/0800023336/algemeen-ziekenhuis-oostende",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2008; EN mirror YE2025 Medium; filed 26-06-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2008/azo_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZ Oostende YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0800023336/algemeen-ziekenhuis-oostende",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2008; FR mirror YE2025 Medium; deposés le 26-06-2026; raw docs/doge/data/raw/tick2008/azo_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZ Oostende 0800.023.336 Actief VZW Oostende",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0800023336",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2008; Actief VZW since 28.03.2023; Algemeen Ziekenhuis Oostende / AZ Oostende; Gouwelozestraat 100 8400 Oostende; no KBO email; 2 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azoostende.be AZ Oostende (Damiaan + Serruys)",
        "url": "https://www.azoostende.be/",
        "publisher": "AZ Oostende",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2008; campus Damiaan + Serruys; info@azoostende.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_az_oostende_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2008; omzet JUMP {OMZET} +1.42pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_az_oostende_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2008; pnl JUMP {PNL} +12.95pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_az_oostende_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2008; equity JUMP {EQUITY} +9.10pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_az_oostende_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2008; bruto JUMP {BRUTO} +1.81pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_az_oostende_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2008; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_az_oostende_jr2025_statutory_hospital",
    "title": "AZ Oostende YE2025 leftover hospital dual (omzet JUMP 308.72m / pnl JUMP 2.03m / equity JUMP 165.93m)",
    "entity_id": ENTITY,
    "beneficiary": "Oostende-region hospital patients / AZ Oostende",
    "legal_basis": "VZW/ASBL hospital (KBO 0800.023.336)",
    "decision_date": "2026-06-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0800023336/algemeen-ziekenhuis-oostende",
    "stated_goal": "Regional hospital care (Oostende / Damiaan+Serruys)",
    "cut_option": "Publish NBB PDF assets/debt FOI; avoid Damiaan shell double-count",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>AZ_Oostende>JR2025_statutory_L5",
    "notes": "tick2008; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Damiaan 0464.564.177 0-FTE dual not mined separately; Werken Glorieux already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_az_oostende_omzet_jump_308_72m_pnl_jump_2_03m_equity_jump_jr2025",
    "name": "AZ Oostende omzet JUMP 308.72m / pnl JUMP 2.03m / equity JUMP 165.93m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "WestVlaanderen>AZ_Oostende>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Oostende patients via AZ Oostende VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 308.72m omzet JUMP +1.42pct with pnl JUMP +12.95pct and equity JUMP +9.10pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.0",
    "difficulty": "4.0",
    "priority_index": "5.525",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon vs Glorieux/Alma; do not double-count Damiaan shell",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2008 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZ Oostende / Algemeen Ziekenhuis Oostende",
    "name_fr": "AZ Oostende / Algemeen Ziekenhuis Oostende",
    "name_en": "AZ Oostende (Damiaan + Serruys campuses)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.azoostende.be/",
    "foi_email": "info@azoostende.be",
    "foi_postal": "Gouwelozestraat 100, 8400 Oostende",
    "notes": "tick2008 YE2025 Medium CW NL+EN+FR + Strong KBO 0800.023.336 Actief VZW; omzet JUMP 308.72m pnl JUMP 2.03m equity JUMP 165.93m bruto JUMP 159.97m FTE 1670.5; assets/debt Unknown; neerlegging 26.06.2026; 2 VE; FOI "
    + GAP
    + "; Damiaan 0464.564.177 dual shell 0 FTE not double-counted; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "WestVlaanderen>AZ_Oostende>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); Damiaan shell dual map",
    "why_it_matters": "Medium CW shows 308.72m omzet Oostende fusion hospital VZW without balance sheet; Damiaan 0-FTE dual risk",
    "priority": "7",
    "recipient_body": "Algemeen Ziekenhuis Oostende VZW / AZ Oostende",
    "recipient_email": "info@azoostende.be",
    "recipient_postal": "Gouwelozestraat 100, 8400 Oostende",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_az_oostende_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_az_oostende_omzet_jump_308_72m_pnl_jump_2_03m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2008; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZ Oostende (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Algemeen Ziekenhuis Oostende VZW / AZ Oostende — KBO **0800.023.336**  
**recipient:** info@azoostende.be · Gouwelozestraat 100, 8400 Oostende  
**sources:** [CW NL](https://www.companyweb.be/nl/0800023336/algemeen-ziekenhuis-oostende) · [CW EN](https://www.companyweb.be/en/0800023336/algemeen-ziekenhuis-oostende) · [CW FR](https://www.companyweb.be/fr/0800023336/algemeen-ziekenhuis-oostende) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0800023336) · [site](https://www.azoostende.be/)  
**tick:** 2008  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **26.06.2026**): omzet **EUR308,721,709** JUMP +1.42%; pnl **EUR2,031,443** JUMP +12.95%; equity **EUR165,930,443** JUMP +9.10%; bruto **EUR159,965,423** JUMP +1.81%; FTE **1670.5**; assets/debt **Unknown**.
- Oostende VZW hospital (Damiaan + Serruys). Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Damiaan VZW **0464.564.177** 0-FTE dual — do not double-count. Werken Glorieux already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Algemeen Ziekenhuis Oostende VZW / AZ Oostende — Gouwelozestraat 100, 8400 Oostende
info@azoostende.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZ Oostende + balans (KBO 0800.023.336)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 26.06.2026).
2. Assets / schulden LT-ST / cash.
3. Dual-kaart t.o.v. Damiaan VZW 0464.564.177 (0 FTE shell) indien relevant.
4. Recon vs Glorieux / Alma indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2008":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Werken Glorieux — AZ Oostende YE2025 Medium"
        x["notes"] = (
            "tick2008 AZ Oostende Medium omzet JUMP 308.72m pnl JUMP 2.03m equity JUMP 165.93m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Damiaan shell not double-counted; next rq_2009; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover AZ Oostende YE2025 Medium CW; KBO 0800.023.336; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2009" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2009",
            "title": "leftover dual hole-fill after AZ Oostende",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2008 after AZ Oostende YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Sint-Elisabeth Zottegem / Jan Palfijn / AZ Turnhout / Waregem / other unused YE2025 if live). "
                "Do NOT redo AZ Oostende, Damiaan Oostende shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Maria Middelares/Imelda/Monica CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2008 AZ Oostende; next every-10 2010; AGB/FARO/AIESH/REW still YE2024",
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
        "last_unit_id": "rq_2008",
        "ticks_completed": "2008",
        "paused": "no",
        "notes": (
            "tick2008 leftover AZ Oostende 0800.023.336 Medium CW (omzet JUMP 308.72m pnl JUMP 2.03m equity JUMP 165.93m bruto JUMP 159.97m FTE 1670.5; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Damiaan shell dual not double-counted; next rq_2009; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2008 - {UTC} - rq_2008 AZ Oostende (omzet JUMP 308.72m / pnl JUMP 2.03m / Medium)

- Unit: **rq_2008** leftover dual after **rq_2007 Werken Glorieux**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Damiaan Oostende **0464.564.177** YE2025 but **0 FTE** shell — not double-counted. Took preferred leftover **AZ Oostende** YE2025 (KBO **0800.023.336**; Gouwelozestraat 100 Oostende; West-Vlaanderen **hospital VZW** Damiaan+Serruys). Do not redo Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR308,721,709** JUMP +1.42%; pnl **EUR2,031,443** JUMP +12.95%; equity **EUR165,930,443** JUMP +9.10%; bruto **EUR159,965,423** JUMP +1.81%; FTE **1670.5**; neerlegging **26.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 2 VE; email info@azoostende.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_az_oostende); foi + draft {GAP}; rq_2008=done + rq_2009 open; loop_state ticks=2008; raw under docs/doge/data/raw/tick2008/.
- FOI: **ready not sent** (human-gated; info@azoostende.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2009 (AGB/FARO-if-YE2025 / AIESH-REW / Zottegem-Palfijn-Turnhout / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
