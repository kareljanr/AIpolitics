# ephemeral tick2001 — Z.org KU Leuven YE2025 Medium (leftover UZ Leuven dual after AZ Delta EVERY-10)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T04:05:00Z"
ENTITY = "vzw_zorg_kul"
GAP = "gap_zorg_kul_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_zorg_kul_jr2025_cw"
SRC_EN = "src_zorg_kul_jr2025_cw_en"
SRC_FR = "src_zorg_kul_jr2025_cw_fr"
SRC_KBO = "src_zorg_kul_kbo_2001"
SRC_SITE = "src_uzleuven_site_2001"

OMZET = "111242745"
PNL = "9476550"
EQUITY = "109376202"
BRUTO = "91376305"
FTE = "940.6"
OMZET24 = "106869067"
PNL24 = "5199390"
EQUITY24 = "100920757"
BRUTO24 = "86616854"
FTE24 = "927.3"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2001")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Z.org KU Leuven YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0558906971/z-org-ku-leuven",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2001; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 30.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2001/zorg_kul_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Z.org KU Leuven YE2025 statutory",
        "url": "https://www.companyweb.be/en/0558906971/z-org-ku-leuven",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2001; EN mirror YE2025 Medium; filed 30-06-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2001/zorg_kul_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Z.org KU Leuven YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0558906971/z-org-ku-leuven",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2001; FR mirror YE2025 Medium; déposés le 30-06-2026; raw docs/doge/data/raw/tick2001/zorg_kul_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Z.org KU Leuven 0558.906.971 Actief VZW Leuven",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0558906971",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2001; Actief VZW since 10.07.2014; Herestraat 49 3000 Leuven; 5 VE; 17 functiehouders; Aanbestedende overheid; NACE 86.104 psychiatrische ziekenhuizen; no KBO email/web",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "uzleuven.be UZ Leuven (Z.org campus host)",
        "url": "https://www.uzleuven.be/",
        "publisher": "UZ Leuven",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2001; Herestraat 49 campus; FOI route via uzleuven.be contact (+32 16 33 22 11); no public generic info@ in crawl",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_zorg_kul_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2001; omzet JUMP {OMZET} +4.09pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_zorg_kul_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2001; pnl JUMP {PNL} +82.26pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_zorg_kul_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2001; equity JUMP {EQUITY} +8.38pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_zorg_kul_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2001; bruto JUMP {BRUTO} +5.49pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_zorg_kul_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2001; YE2025 FTE {FTE} vs YE2024 {FTE24}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_zorg_kul_jr2025_statutory_hospital",
    "title": "Z.org KU Leuven YE2025 leftover UZ Leuven dual (omzet JUMP 111.24m / pnl JUMP 9.48m / equity JUMP 109.38m)",
    "entity_id": ENTITY,
    "beneficiary": "Leuven psychiatric / UZ Leuven campus patients via Z.org KU Leuven",
    "legal_basis": "VZW / ASBL psychiatric hospital (KBO 0558.906.971)",
    "decision_date": "2026-06-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0558906971/z-org-ku-leuven",
    "stated_goal": "Psychiatric hospital care on UZ Leuven / KU Leuven campus",
    "cut_option": "Publish NBB PDF assets/debt + pnl JUMP recon vs omzet FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>Z_org_KU_Leuven>JR2025_statutory_L5",
    "notes": "tick2001; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Erasme/UZB opaque; AZ Delta already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*6.0 + 0.10*6.0 = 3.025+2.1+0.6 = 5.725
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_zorg_kul_omzet_jump_111_24m_pnl_jump_9_48m_equity_jump_jr2025",
    "name": "Z.org KU Leuven omzet JUMP 111.24m / pnl JUMP 9.48m / equity JUMP 109.38m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>Z_org_KU_Leuven>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Leuven psychiatric patients via Z.org KU Leuven VZW (UZ Leuven campus)",
    "stated_goal": "Psychiatric hospital care",
    "measured_outcome": "Medium CW YE2025; 111.24m omzet with pnl JUMP +82pct and equity JUMP +8.4pct; NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.725",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl JUMP +82pct vs modest omzet +4pct path",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2001 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Z.org KU Leuven",
    "name_fr": "Z.org KU Leuven",
    "name_en": "Z.org KU Leuven (UZ Leuven psychiatric ASBL)",
    "level": "asbl",
    "parent_id": "prov_vlaams_brabant",
    "community_language": "nl",
    "website": "https://www.uzleuven.be/",
    "foi_email": "",
    "foi_postal": "Herestraat 49, 3000 Leuven",
    "notes": "tick2001 YE2025 Medium CW NL+EN+FR + Strong KBO 0558.906.971 Actief VZW; omzet JUMP 111.24m pnl JUMP 9.48m equity JUMP 109.38m bruto JUMP 91.38m FTE 940.6; assets/debt Unknown; neerlegging 30.06.2026; 5 VE; NACE 86.104; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Erasme/UZB opaque; do not redo AZ Delta/AZJP/ZAS/Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "VlaamsBrabant>Z_org_KU_Leuven>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl JUMP +82pct recon vs YE2024; equity JUMP recon",
    "why_it_matters": "Medium CW shows 111.24m omzet UZ Leuven campus psychiatric VZW with pnl JUMP +82pct and equity JUMP without balance sheet",
    "priority": "7",
    "recipient_body": "Z.org KU Leuven VZW / UZ Leuven",
    "recipient_email": "",
    "recipient_postal": "Herestraat 49, 3000 Leuven",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_zorg_kul_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_zorg_kul_omzet_jump_111_24m_pnl_jump_9_48m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2001; human-send only; Medium CW; no KBO email — route via uzleuven.be (+32 16 33 22 11); next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Z.org KU Leuven (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Z.org KU Leuven VZW — KBO **0558.906.971**  
**recipient:** UZ Leuven / Z.org KU Leuven — Herestraat 49, 3000 Leuven · route via [uzleuven.be](https://www.uzleuven.be/) (+32 16 33 22 11)  
**sources:** [CW NL](https://www.companyweb.be/nl/0558906971/z-org-ku-leuven) · [CW EN](https://www.companyweb.be/en/0558906971/z-org-ku-leuven) · [CW FR](https://www.companyweb.be/fr/0558906971/z-org-ku-leuven) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0558906971) · [UZ Leuven](https://www.uzleuven.be/)  
**tick:** 2001  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **30.06.2026**): omzet **EUR111,242,745** JUMP +4.09%; pnl **EUR9,476,550** JUMP +82.26%; equity **EUR109,376,202** JUMP +8.38%; bruto **EUR91,376,305** JUMP +5.49%; FTE **940.6** (vs YE2024 927.3); assets/debt **Unknown**.
- Leuven VZW psychiatric hospital (NACE 86.104) on UZ Leuven / KU Leuven campus. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. Erasme / UZ Brussel CW opaque. AZ Delta already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Z.org KU Leuven VZW / UZ Leuven — Herestraat 49, 3000 Leuven
t.a.v. dienst openbaarheid / informatieambtenaar (via uzleuven.be contact)
cc: Agentschap Zorg en Gezondheid / Provincie Vlaams-Brabant indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Z.org KU Leuven + balans (KBO 0558.906.971)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 30.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl JUMP (EUR9.476.550 vs YE2024 EUR5.199.390; +82,26pct) en equity JUMP (+8,38pct).
4. Dual vs UZ Leuven / AZ Delta / AZJP / regionale VL ziekenhuizen indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2001":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZ Delta EVERY-10 — Z.org KU Leuven YE2025 Medium"
        x["notes"] = (
            "tick2001 Z.org KU Leuven Medium omzet JUMP 111.24m pnl JUMP 9.48m equity JUMP 109.38m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Erasme/UZB opaque; next rq_2002; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover Z.org KU Leuven YE2025 Medium CW; KBO 0558.906.971; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2002" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2002",
            "title": "leftover dual hole-fill after Z.org KU Leuven",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2001 after Z.org KU Leuven YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Sint-Jan Brugge / AZ Turnhout / other unused YE2025 if live). "
                "Do NOT redo Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Note: Erasme/UZ Brussel CW opaque; AZ Groeninge CW N/A omzet as of 2001. Next every-10 is 2010."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2001 Z.org KU Leuven; next every-10 2010; AGB/FARO/AIESH/REW still YE2024",
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
        "last_unit_id": "rq_2001",
        "ticks_completed": "2001",
        "paused": "no",
        "notes": (
            "tick2001 leftover Z.org KU Leuven 0558.906.971 Medium CW (omzet JUMP 111.24m pnl JUMP 9.48m equity JUMP 109.38m bruto JUMP 91.38m FTE 940.6; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Erasme/UZB opaque; next rq_2002; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2001 - {UTC} - rq_2001 Z.org KU Leuven (omzet JUMP 111.24m / pnl JUMP 9.48m / Medium)

- Unit: **rq_2001** leftover dual after **rq_2000 EVERY-10 + AZ Delta**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Erasme/UZ Brussel CW **opaque**. Took preferred leftover **Z.org KU Leuven** YE2025 (KBO **0558.906.971**; Herestraat 49 Leuven; Vlaams-Brabant **psychiatric hospital VZW** on UZ Leuven campus). Do not redo AZ Delta/AZJP/ZAS/Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR111,242,745** JUMP +4.09%; pnl **EUR9,476,550** JUMP +82.26%; equity **EUR109,376,202** JUMP +8.38%; bruto **EUR91,376,305** JUMP +5.49%; FTE **940.6** (+13.3 vs 927.3); neerlegging **30.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE; no KBO email (route via uzleuven.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_zorg_kul); foi + draft {GAP}; rq_2001=done + rq_2002 open; loop_state ticks=2001; raw under docs/doge/data/raw/tick2001/.
- FOI: **ready not sent** (human-gated; route via uzleuven.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2002 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
