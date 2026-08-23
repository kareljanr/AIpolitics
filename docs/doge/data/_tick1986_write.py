# ephemeral tick1986 — CHU UCL Namur YE2025 (deferred from 1985 race)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T00:10:00Z"
ENTITY = "vzw_chu_ucl_namur"
GAP = "gap_chu_ucl_namur_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_chu_ucl_namur_jr2025_cw"
SRC_EN = "src_chu_ucl_namur_jr2025_cw_en"
SRC_KBO = "src_chu_ucl_namur_kbo_1986"
SRC_SITE = "src_chu_ucl_namur_site_1986"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1986")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHU UCL Namur YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0641733885/centre-hospitalier-universitaire-dinant-godinne-sainte-elisabeth-ucl-namur",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1986; YE2025 omzet JUMP 637526612 pnl DROP 4182729 equity JUMP 141955644 bruto JUMP 351668788 FTE 3597.6; neerlegging 21.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1985/chu_ucl_namur_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHU UCL Namur YE2025 statutory",
        "url": "https://www.companyweb.be/en/0641733885/centre-hospitalier-universitaire-dinant-godinne-sainte-elisabeth-ucl-namur",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1986; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1985/chu_ucl_namur_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHU-UCL-NAMUR 0641.733.885 Actief VZW Yvoir",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0641733885",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1986; Actief VZW; Av Dr-Gaston-Therasse Godinne 1 5530 Yvoir; 8 VE; Aanbestedende overheid; NACE 86.101; no KBO email/web",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chuuclnamur.be Dinant Godinne Sainte-Elisabeth",
        "url": "https://www.chuuclnamur.be/",
        "publisher": "CHU UCL Namur",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": "tick1986; Namur province university hospital dual of CHwapi/Vivalia/HELORA/Epicura",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_chu_ucl_namur_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "637526612",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1986; omzet JUMP 637526612 +3.07pct vs YE2024 618538266",
    },
    {
        "budget_id": "bud_chu_ucl_namur_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "4182729",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1986; pnl DROP 4182729 -28.82pct vs YE2024 5876517",
    },
    {
        "budget_id": "bud_chu_ucl_namur_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "141955644",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1986; equity JUMP 141955644 +1.93pct vs YE2024 139265474",
    },
    {
        "budget_id": "bud_chu_ucl_namur_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "351668788",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1986; bruto JUMP 351668788 +2.15pct vs YE2024 344279642",
    },
    {
        "budget_id": "bud_chu_ucl_namur_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "3597.6",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1986; YE2025 FTE 3597.6 vs YE2024 3599.7",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_chu_ucl_namur_jr2025_statutory_hospital",
    "title": "CHU UCL Namur YE2025 leftover university hospital dual (omzet JUMP 637.53m / pnl DROP 4.18m)",
    "entity_id": ENTITY,
    "beneficiary": "Namur province patients / UCLouvain dual",
    "legal_basis": "WVV VZW / university hospital Wallonie",
    "decision_date": "2026-07-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "637526612",
    "cash_by_year": '{"2025_omzet":637526612,"2025_pnl":4182729,"2025_equity":141955644,"2025_bruto":351668788,"2025_fte":3597.6}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0641733885/centre-hospitalier-universitaire-dinant-godinne-sainte-elisabeth-ucl-namur",
    "stated_goal": "University hospital care Dinant Godinne Sainte-Elisabeth Namur",
    "cut_option": "Publish NBB PDF assets/debt + dual vs CHwapi/Vivalia/HELORA/Epicura FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Namur>CHU_UCL_Namur>JR2025_statutory_L5",
    "notes": "tick1986; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; ISoSL deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_chu_ucl_namur_omzet_jump_637_53m_pnl_drop_4_18m_jr2025",
    "name": "CHU UCL Namur omzet JUMP 637.53m / pnl DROP 4.18m / equity JUMP 141.96m (Namur university hospital YE2025)",
    "level": "L5",
    "type": "walloon_hospital_vzw_dual",
    "hierarchy_path": "Wallonie>Namur>CHU_UCL_Namur>JR2025_statutory_L5",
    "annual_cost_eur": "637526612",
    "total_cost_eur": "141955644",
    "tco_notes": "statutory omzet JUMP 637526612 pnl DROP 4182729 equity JUMP 141955644 bruto JUMP 351668788 FTE 3597.6; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Namur patients via university hospital VZW",
    "stated_goal": "University hospital care network",
    "measured_outcome": "Medium CW YE2025; 638m omzet with pnl DROP; NBB PDF residual",
    "absurdity_score": "4.0",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "5.725",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; dual vs CHwapi/Vivalia/HELORA/Epicura hospital opacity",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1986 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 1990",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHU UCL Namur (Dinant Godinne Sainte-Elisabeth)",
    "name_fr": "CHU UCL Namur (Dinant Godinne Sainte-Elisabeth)",
    "name_en": "CHU UCL Namur (Namur university hospital VZW)",
    "level": "other",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.chuuclnamur.be/",
    "foi_email": "",
    "foi_postal": "Av. Dr-Gaston-Therasse Godinne 1, 5530 Yvoir",
    "notes": "tick1986 YE2025 Medium CW NL+EN + Strong KBO 0641.733.885 Actief VZW; omzet JUMP 637.53m pnl DROP 4.18m equity JUMP 141.96m bruto JUMP 351.67m FTE 3597.6; assets/debt Unknown; neerlegging 21.07.2026; 8 VE; FOI gap_chu_ucl_namur_nbb_pdf_assets_debt_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; ISoSL deferred; do not redo Epicura/CHwapi/Vivalia/HELORA/IDETA/SPI",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Namur>CHU_UCL_Namur>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); dual vs CHwapi/Vivalia/HELORA/Epicura hospital path",
    "why_it_matters": "Medium CW shows 638m omzet university hospital without balance sheet; material TE-adjacent opacity",
    "priority": "7",
    "recipient_body": "CHU UCL Namur",
    "recipient_email": "",
    "recipient_postal": "https://www.chuuclnamur.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_chu_ucl_namur_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_chu_ucl_namur_omzet_jump_637_53m_pnl_drop_4_18m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1986; human-send only; Medium CW; KBO no email — route via chuuclnamur.be; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHU UCL Namur (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CHU-UCL-NAMUR VZW — KBO **0641.733.885**  
**recipient:** CHU UCL Namur (KBO has no email; route via https://www.chuuclnamur.be/ contact)  
**sources:** [CW NL](https://www.companyweb.be/nl/0641733885/centre-hospitalier-universitaire-dinant-godinne-sainte-elisabeth-ucl-namur) · [CW EN](https://www.companyweb.be/en/0641733885/centre-hospitalier-universitaire-dinant-godinne-sainte-elisabeth-ucl-namur) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0641733885) · [site](https://www.chuuclnamur.be/)  
**tick:** 1986  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **21.07.2026**): omzet **EUR637,526,612** JUMP +3.07%; pnl **EUR4,182,729** DROP -28.82%; equity **EUR141,955,644** JUMP +1.93%; bruto **EUR351,668,788** JUMP +2.15%; FTE **3597.6**; assets/debt **Unknown**.
- Namur university hospital (Dinant / Godinne / Sainte-Elisabeth). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. ISoSL deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CHU UCL Namur — Av. Dr-Gaston-Therasse Godinne 1, 5530 Yvoir
cc: SPW sante / UCLouvain transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHU UCL Namur + balans (KBO 0641.733.885)
Geachte, op grond van decret wallon / CDLD / openbaarheid vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 21.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl DROP (-29pct vs YE2024 5.88m) vs omzet JUMP.
4. Dual vs CHwapi / Vivalia / HELORA / Epicura indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1986":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Epicura — CHU UCL Namur YE2025 Medium"
        x["notes"] = "tick1986 CHU UCL Namur Medium omzet JUMP 637.53m pnl DROP 4.18m; FOI ready; next rq_1987; next every-10 1990"
        x["instructions"] = (
            "Completed leftover CHU UCL Namur YE2025 Medium CW; KBO 0641.733.885; "
            "omzet JUMP 637526612 pnl DROP 4182729 equity JUMP 141955644 bruto JUMP 351668788 FTE 3597.6; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1987" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1987",
            "title": "leftover dual hole-fill after CHU UCL Namur",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1986 after CHU UCL Namur YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (ISoSL if YE2025 / other). Do NOT redo CHU UCL Namur, Epicura, CHwapi, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau, IDEA.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1986 CHU UCL Namur; ISoSL deferred; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1986",
        "ticks_completed": "1986",
        "paused": "no",
        "notes": "tick1986 leftover CHU UCL Namur 0641.733.885 Medium CW (omzet JUMP 637.53m pnl DROP 4.18m equity JUMP 141.96m bruto JUMP 351.67m FTE 3597.6; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; ISoSL deferred; next rq_1987; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1986 - 2026-08-24T00:10:00Z - rq_1986 CHU UCL Namur (omzet JUMP 637.53m / pnl DROP 4.18m / Medium)

- Unit: **rq_1986** leftover dual after **rq_1985 Epicura**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **CHU UCL Namur** YE2025 (KBO **0641.733.885**; Godinne Yvoir; Namur **university hospital VZW**). ISoSL deferred. Do not redo Epicura/CHwapi/Vivalia/HELORA/IDETA/SPI/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC/IPFBW/IDEA.
- Found: Companyweb NL+EN YE2025 - omzet **EUR637,526,612** JUMP +3.07%; pnl **EUR4,182,729** DROP -28.82%; equity **EUR141,955,644** JUMP +1.93%; bruto **EUR351,668,788** JUMP +2.15%; FTE **3597.6**; neerlegging **21.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 8 VE; no KBO email.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_chu_ucl_namur); foi + draft gap_chu_ucl_namur_nbb_pdf_assets_debt_matrix_l5; rq_1986=done + rq_1987 open; loop_state ticks=1986.
- FOI: **ready not sent** (human-gated; route via chuuclnamur.be).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1987 (AGB/FARO-if-YE2025 / AIESH-REW / ISoSL / unused DSO-IGS-HVZ-hospital).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1986" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1986")
