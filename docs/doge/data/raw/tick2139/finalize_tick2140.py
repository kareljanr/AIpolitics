# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T16:40:00Z"
TICK = 2140
RQ = "rq_2140"
NEXT_RQ = "rq_2141"
ENTITY = "vzw_zorgcampus_denderrust_aalst"
GAP = "gap_denderrust_nbb_pdf_assets_debt_pnl_drop_omzet_jump_merger_dienstengroep_matrix_l5"
DATA = Path("docs/doge/data")
ROOT = Path("docs/doge")

# research_queue
path = DATA / "research_queue.csv"
with open(path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
found = False
for r in rows:
    if r.get("task_id") == RQ and r.get("status") == "open":
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["title"] = (
            "EVERY-10 + leftover dual — Zorgcampus Denderrust Aalst YE2025 Medium "
            "(omzet JUMP 11.14m / pnl DROP / bruto JUMP 12.10m)"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick2140 EVERY-10 Denderrust Medium omzet JUMP 11.14m (+3.66%) bruto JUMP 12.10m "
            "(+5.90%) pnl DROP 48k (-68.86%) equity JUMP 8.53m FTE 139.9; KBO Actief VZW "
            "aanbestedende overheid; Dienstengroep absorbed; FOI ready; progress+top10 refreshed; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2141; next every-10 2150"
        )
        r["instructions"] = (
            "Completed EVERY-10 + leftover Denderrust YE2025 Medium CW after En Famille; "
            "preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; race-recover "
            "(concurrent took rq_2139 En Famille); FOI " + GAP
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2140 open not found")
if not any(r.get("task_id") == NEXT_RQ for r in rows):
    rows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual hole-fill after Denderrust EVERY-10 — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2141 after Denderrust EVERY-10 YE2025 Medium (omzet JUMP / pnl DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
                "AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/"
                "creche/disability/thuiszorg. Do NOT redo Zorgcampus Denderrust Aalst, "
                "Maison De Repos En Famille Vaux, Residence Prestige Chaudfontaine, Les Corolles "
                "Tournai, l'Esplanade Ath, Residence Les Peupliers Seneffe, MRS Comte d'Egmont, "
                "C.I.G.B. Menen, Maagd Der Armen / Ten Rozen, L'Orchidée Ittre, Care-Support, "
                "MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, Le Château Vert, SLG Wallonie, "
                "Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, "
                "Le Bosquet, Strebo, Entraide, La Charmille, Charmilles, Sittelles, Les Buissons, "
                "Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, "
                "IDELUX*, INTRADEL, Korian*, Always Home, AREWAL, AGB Bornem, Armonea holding, "
                "emeis holding, Prinsenhof, Akapella, Familiehof, La Moisson (absorbed), "
                "Denderrust Dienstengroep (absorbed)."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                "spawned after tick2140 Denderrust EVERY-10; FARO/AIESH/REW still YE2024; "
                "next every-10 2150"
            ),
        }
    )
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# loop_state
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
                "tick2140 EVERY-10 + leftover Denderrust 0419.333.572 Medium CW "
                "(omzet JUMP 11.14m bruto JUMP 12.10m pnl DROP 48k equity JUMP 8.53m FTE 139.9; "
                "Actief VZW 1 VE aanbestedende overheid; Dienstengroep absorbed; assets/debt Unknown); "
                "progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2141; "
                "next every-10 2150; continuous hole_fill"
            ),
        }
    )

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} EVERY-10 Zorgcampus Denderrust Aalst (omzet JUMP 11.14m / pnl DROP / bruto JUMP 12.10m / Medium)

- Unit: **{RQ}** EVERY-10 + leftover dual after **rq_2139 Maison De Repos En Famille** (race: this agent researched Denderrust while concurrent closed 2139 as En Famille). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024 / filed 24-11-2025); AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Zorgcampus Denderrust VZW** YE2025 (KBO **0419.333.572**; Alfons De Cockstraat 12A Aalst; **VZW** NACE **87.101/87.301/88.102** / **1 VE**; **aanbestedende overheid**; absorbed **Denderrust Dienstengroep 0409.698.009** 17.12.2025). Do not redo En Famille/Residence Prestige/Les Corolles/l'Esplanade/Les Peupliers/Comte d'Egmont/CIGB Menen/Ten Rozen/L'Orchidée/Care-Support/Prinsenhof.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR11135834** JUMP +3.66% vs YE2024 EUR10742203; bruto **EUR12099041** JUMP +5.90% vs YE2024 EUR11424596; pnl **EUR47586** DROP -68.86% vs YE2024 EUR152817; equity **EUR8526706** JUMP +0.52%; FTE **139.9**; neerlegging **03.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via administratie@denderrust.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.2); entities (+1 {ENTITY}); foi + draft {GAP}; progress_every_10_ticks.md + doge_waste_top10_current.md refreshed; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2139/ (shared with En Famille race).
- FOI: **ready not sent** (human-gated).
- **EVERY-10@2140** (last was 2130; **next 2150**). Pure annual top10 stable (GIP/fossil/cars/cheque). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK finalize tick", TICK, ENTITY)
