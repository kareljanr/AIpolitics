# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T12:00:00Z"
TICK = 2125
RQ = "rq_2125"
NEXT_RQ = "rq_2126"
ENTITY = "nv_famifamenne"
GAP = "gap_famifamenne_nbb_pdf_assets_debt_omzet_jump_fte_jump_matrix_l5"
COMM = "comm_famifamenne_jr2025_statutory_wzc"
LB = "lb_famifamenne_omzet_jump_12_04m_fte_jump_jr2025"
SRC_EN = "src_famifamenne_jr2025_cw_en"
KBO = "0475.400.760"
KBO_DIGITS = "0475400760"
OMZET = "12041781"
OMZET_YOY = "+151.2%"
BRUTO = "8969927"
BRUTO_YOY = "+110.47%"
PNL = "368075"
PNL_YOY = "+135.18%"
EQUITY = "1172453"
EQUITY_YOY = "+45.76%"
FTE = "122"
FTE_PRIOR = "66"
ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_famifamenne_jr2025_cw",
        "title": "Companyweb NL Famifamenne YE2025 statutory",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/famifamenne",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; YE2025 omzet JUMP {OMZET} ({OMZET_YOY}) bruto JUMP {BRUTO} ({BRUTO_YOY}) "
            f"pnl JUMP {PNL} ({PNL_YOY}) equity JUMP {EQUITY} ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); "
            f"neerlegging 14.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2125/fami_nl.html"
        ),
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Famifamenne YE2025 statutory",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/famifamenne",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 14-07-2026; Last balance sheet year 2025; "
            f"Turnover {OMZET}; Gross margin {BRUTO}; FTE {FTE}; raw docs/doge/data/raw/tick2125/fami_en.html"
        ),
    },
    {
        "source_id": "src_famifamenne_jr2025_cw_fr",
        "title": "Companyweb FR Famifamenne YE2025 statutory",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/famifamenne",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2125/fami_fr.html",
    },
    {
        "source_id": f"src_famifamenne_kbo_{TICK}",
        "title": f"KBO Famifamenne {KBO} Actief Mechelen Armonea-seat path",
        "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Actief NV/SA; Stationsstraat 102 2800 Mechelen (same seat as Armonea/Home Sebrechts); "
            f"2 VE; NACE 87.301 ROB; kapitaal 462126.77; bestuurder 0723.858.144 Remy Yves; email/web empty in KBO"
        ),
    },
    {
        "source_id": f"src_famifamenne_armonea_{TICK}",
        "title": "Armonea site / Famifamenne FOI contact info@armonea.be",
        "url": "https://www.armonea.be",
        "publisher": "Armonea / Colisee",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; NV WZC at Armonea Mechelen seat; FOI info@armonea.be; "
            "DISTINCT Armonea holding / Home Sebrechts not retaken"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Famifamenne (Mechelen / Armonea-seat WZC)",
        "name_fr": "Famifamenne SA (Malines / MRS Armonea-siege)",
        "name_en": "Famifamenne nursing-home NV (Mechelen; Armonea seat path)",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.armonea.be",
        "foi_email": "info@armonea.be",
        "foi_postal": "Stationsstraat 102, 2800 Mechelen",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV/SA 2 VE NACE 87.301; "
            f"omzet JUMP 12.04m ({OMZET_YOY}) bruto JUMP 8.97m ({BRUTO_YOY}) pnl JUMP 0.37m ({PNL_YOY}) "
            f"equity JUMP 1.17m ({EQUITY_YOY}) FTE JUMP {FTE} (vs {FTE_PRIOR}); assets/debt Unknown; "
            f"filed 14.07.2026; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Home Sebrechts / Armonea holding / Le Castel / RSW"
        ),
    },
)

for bid, amt, basis in [
    ("bud_famifamenne_omzet_jr2025_statutory", OMZET, "CW YE2025 omzet / Turnover (primary envelope)"),
    ("bud_famifamenne_bruto_jr2025_statutory", BRUTO, "CW YE2025 Brutomarge / Gross margin"),
    ("bud_famifamenne_pnl_jr2025_statutory", PNL, "CW YE2025 Profit/Loss"),
    ("bud_famifamenne_equity_jr2025_statutory", EQUITY, "CW YE2025 Eigen vermogen / Equity"),
    ("bud_famifamenne_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees"),
]:
    append_csv(
        DATA / "budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Famifamenne YE2025 leftover dual (omzet JUMP 12.04m / FTE JUMP 66→122)",
        "entity_id": ENTITY,
        "beneficiary": "WZC/ROB residents (2 VE; Armonea-seat path Mechelen)",
        "legal_basis": f"NV/SA woonzorgcentrum ROB (KBO {KBO}; NACE 87.301; 2 VE)",
        "decision_date": "2026-07-14",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": (
            f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
            f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_fte":{FTE_PRIOR}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/famifamenne",
        "stated_goal": "Public-interest nursing-home care (Vlaanderen WZC / Armonea-path)",
        "cut_option": (
            "Publish NBB PDF assets/debt; explain omzet +151% / FTE nearly-double path "
            "(merger/absorption vs organic); VAPH/INAMI vs fees split"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>Famifamenne>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
            "DISTINCT Home Sebrechts / Armonea holding"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Famifamenne omzet JUMP 12.04m (+151%) / FTE JUMP 66→122 (YE2025)",
        "level": "L5",
        "type": "wzc_statutory_nv",
        "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>Famifamenne>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": (
            f"CW YE2025 omzet {OMZET} JUMP {OMZET_YOY} (primary); bruto {BRUTO} JUMP {BRUTO_YOY}; "
            f"pnl {PNL} JUMP {PNL_YOY}; equity {EQUITY} JUMP {EQUITY_YOY}; FTE {FTE} JUMP vs {FTE_PRIOR}; "
            "assets/debt Unknown pending NBB PDF; 2 VE Armonea-seat"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "WZC/ROB residents (2 VE Armonea-seat path)",
        "stated_goal": "Public-interest nursing-home care (Vlaanderen)",
        "measured_outcome": (
            f"omzet JUMP {OMZET_YOY}; bruto JUMP {BRUTO_YOY}; pnl JUMP {PNL_YOY}; "
            f"equity JUMP {EQUITY_YOY}; FTE JUMP {FTE_PRIOR}→{FTE}"
        ),
        "absurdity_score": "7.6",
        "cost_score": "5.0",
        "difficulty": "3.5",
        "priority_index": "6.4",
        "cut_proposal": (
            "FOI NBB PDF + explain scale jump (merger/absorption vs organic) + assets/debt; "
            "map public care flows vs private operator"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
            "DISTINCT Home Sebrechts / Armonea holding / Le Castel / RSW"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>Famifamenne>NBB_PDF_assets_debt_omzet_fte_jump",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet +151% / FTE 66→122 "
            "path (merger/absorption detail); VAPH/INAMI vs fee split; VE addresses"
        ),
        "why_it_matters": (
            "Medium CW shows Armonea-seat WZC NV with omzet JUMP 12.04m (+151%) and FTE nearly-doubled "
            "while assets/debt opaque — scale-jump / care-margin transparency gap"
        ),
        "priority": "8",
        "recipient_body": "Famifamenne NV (via Armonea)",
        "recipient_email": "info@armonea.be",
        "recipient_postal": "Stationsstraat 102, 2800 Mechelen",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"tick{TICK}; human-send only; Medium CW; info@armonea.be; next every-10 2130",
    },
)

rq_path = DATA / "research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

have_next = any(row["task_id"] == NEXT_RQ for row in rows)
for row in rows:
    if row["task_id"] == RQ:
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed: leftover dual Famifamenne after Castel+RSW; preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
            f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; omzet JUMP 12.04m bruto JUMP 8.97m pnl JUMP 0.37m "
            f"equity JUMP 1.17m FTE JUMP {FTE} (vs {FTE_PRIOR}); FOI ready NBB PDF; "
            "DISTINCT Home Sebrechts/Armonea holding/Le Castel/RSW"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            f"tick{TICK} Famifamenne YE2025 Medium CW; FOI ready not sent; next {NEXT_RQ}; next every-10 2130"
        )

if not have_next:
    rows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual hole-fill after Famifamenne — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"Tick {TICK + 1} after Famifamenne YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche. Do NOT redo Famifamenne, "
                "Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, 't Buurthuis, Le Bosquet, Strebo, "
                "Entraide Fraternelle Jolimont, La Charmille, Les Charmilles Sambreville, Les Sittelles, "
                "Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, "
                "IDELUX*, INTRADEL, Korian Belgium, Comnexio, ORES*, SLG*, Always Home, AREWAL, AGB Bornem, "
                "Armonea holding, emeis holding."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Famifamenne; FARO/AIESH/REW still YE2024; next every-10 2130"
            ),
        }
    )

with open(rq_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
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
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover Famifamenne {KBO} Medium CW "
                f"(omzet JUMP 12.04m {OMZET_YOY} bruto JUMP 8.97m pnl JUMP 0.37m equity JUMP 1.17m "
                f"FTE JUMP {FTE} vs {FTE_PRIOR}; assets/debt Unknown; 2 VE NACE 87.301 Mechelen Armonea-seat); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Castel/RSW/Sebrechts taken; "
                f"next {NEXT_RQ}; next every-10 2130; continuous hole_fill"
            ),
        }
    )

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — Famifamenne (NBB PDF / assets-debt / omzet-jump / FTE-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Famifamenne NV/SA — KBO **{KBO}**  
**recipient:** info@armonea.be · Stationsstraat 102, 2800 Mechelen · cc Departement Zorg / bestuurder Remy Yves (0723.858.144)  
**sources:** [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/famifamenne) · [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/famifamenne) · [CW FR](https://www.companyweb.be/fr/{KBO_DIGITS}/famifamenne) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; KBO Strong)

## Context
- YE **2025** (filed **14.07.2026**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP vs {FTE_PRIOR}; assets/debt **Unknown**.
- KBO: Actief NV/SA; Stationsstraat 102 Mechelen (Armonea seat); **2 VE**; NACE **87.301** ROB; kapitaal EUR462126.77; bestuurder Remy Yves via 0723.858.144; email/web empty in KBO.
- DISTINCT from Home Sebrechts / Armonea holding / Le Castel / RSW. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Famifamenne NV — Stationsstraat 102, 2800 Mechelen
via info@armonea.be
t.a.v. Remy Yves (bestuurder / vaste vertegenwoordiger 0723.858.144)
cc: Departement Zorg
Betreft: Openbaarmaking jaarrekening NBB 2025 Famifamenne + balans/resultaat-matrix (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur (Bestuursdecreet e.a.)
vraag ik openbaarmaking van:

1. PDF NBB jaarrekening 2025 (neerlegging 14.07.2026) + neerleggingsreferentie.
2. Activa / schulden LT-KT / liquide middelen / balanstotaal.
3. Toelichting omzet JUMP EUR{OMZET} ({OMZET_YOY} vs YE2024 EUR4793736) en FTE JUMP {FTE_PRIOR}→{FTE}
   — fusie/absorptie vs organische groei; lijst VE-adressen.
4. Split publieke zorgstromen (VAPH/INAMI/Vlaamse WZC-financiering) vs residentenbijdragen
   (brutomarge EUR{BRUTO}).
5. Winst JUMP EUR{PNL} ({PNL_YOY}) met equity JUMP EUR{EQUITY} — dividend / herwaardering / extractie?

Periode 01.01.2025–31.12.2025. Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

log_path = ROOT / "loop_log.md"
log_entry = f"""

## Tick {TICK} - {UTC} - {RQ} Famifamenne Mechelen (omzet JUMP 12.04m / FTE JUMP 66→122 / Medium)

- Unit: **{RQ}** leftover dual after **rq_2124 Residence Le Castel + concurrent RSW**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Famifamenne NV** YE2025 (KBO **{KBO}**; Stationsstraat 102 Mechelen Armonea-seat; **NV/SA** NACE **87.301** / **2 VE**; bestuurder Remy Yves path). Do not redo Le Castel/RSW/Home Sebrechts/Unite Jolimont/'t Buurthuis/Le Bosquet/Strebo/Entraide/Armonea holding.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY} vs YE2024 EUR4793736; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; pnl **EUR{PNL}** JUMP {PNL_YOY}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; FTE **{FTE}** JUMP vs {FTE_PRIOR}; neerlegging **14.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@armonea.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.4); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2125/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2120**; next **2130**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
with open(log_path, "a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"OK tick{TICK} Famifamenne writes")
