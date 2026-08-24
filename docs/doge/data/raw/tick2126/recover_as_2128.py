# -*- coding: utf-8 -*-
"""Race recovery: Fakkel CSV already on main via concurrent commit; assign as tick 2128 / rq_2128."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T12:55:00Z"
TICK = 2128
RQ = "rq_2128"
NEXT_RQ = "rq_2129"
ENTITY = "bv_zorghome_de_fakkel"
GAP = "gap_fakkel_nbb_pdf_assets_debt_omzet_jump_equity_jump_matrix_l5"
KBO = "0865.574.649"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"

rq_path = DATA / "research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

have_next = any(row["task_id"] == NEXT_RQ for row in rows)
for row in rows:
    if row["task_id"] == "rq_2126":
        # fix race corruption: SLG Wallonie title with Fakkel entity_id
        if row.get("entity_id") == ENTITY or "SLG Wallonie" in (row.get("title") or ""):
            row["entity_id"] = "srl_slg_wallonie"
            if "Fakkel" in (row.get("notes") or ""):
                row["notes"] = (
                    "tick2126 SLG Wallonie YE2025 Medium CW; FOI ready not sent; "
                    "entity fixed after Fakkel race collision; next every-10 2130"
                )
            row["updated_utc"] = UTC
    if row["task_id"] == RQ:
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["title"] = "leftover dual — Zorghome De Fakkel YE2025 Medium (race-recover)"
        row["instructions"] = (
            "Completed (race-recover after SLG Wallonie took rq_2126 + Chateau Vert rq_2127): "
            f"Zorghome De Fakkel BV YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
            "omzet JUMP 19.64m (+94.8%) bruto JUMP 13.38m pnl JUMP 0.41m equity JUMP 6.28m (+828%) "
            "FTE JUMP 212.7 (vs 119.2); FOI ready NBB PDF; CSV rows already present from race; "
            "DISTINCT Famifamenne/SLG Wallonie/Chateau Vert/Home Sebrechts/Armonea holding"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            f"tick{TICK} Fakkel YE2025 Medium CW race-recover; FOI ready not sent; "
            f"next {NEXT_RQ}; next every-10 2130"
        )

if not have_next:
    rows.append(
        {
            "task_id": NEXT_RQ,
            "title": (
                "leftover dual hole-fill after Zorghome De Fakkel — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"Tick {TICK + 1} after Zorghome De Fakkel YE2025 Medium (race-recover). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche "
                "(Restel Flats 0413.550.491 YE2025 live deferred; L'Orchidee 0458.352.318 YE2025 live deferred). "
                "Do NOT redo Zorghome De Fakkel, SLG Wallonie, Le Chateau Vert, Famifamenne, Residence Le Castel, "
                "R.S.W., Home Sebrechts, Unite Jolimont, 't Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                "Les Charmilles Sambreville, Les Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, "
                "Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, Korian Belgium, Comnexio, ORES*, SLG*, "
                "Always Home, AREWAL, AGB Bornem, Armonea holding, emeis holding, Gravenkasteel."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} Fakkel race-recover; FARO/AIESH/REW still YE2024; "
                "Restel Flats + Orchidee deferred live YE2025; next every-10 2130"
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
                f"tick{TICK} leftover Zorghome De Fakkel {KBO} Medium CW race-recover "
                "(omzet JUMP 19.64m +94.8% bruto JUMP 13.38m pnl JUMP 0.41m equity JUMP 6.28m +828.25% "
                "FTE JUMP 212.7 vs 119.2; assets/debt Unknown; 6 VE NACE 87.101/87.301 Roeselare Armonea-path); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; SLG Wallonie/Chateau Vert/Famifamenne taken; "
                f"Restel Flats deferred; next {NEXT_RQ}; next every-10 2130; continuous hole_fill"
            ),
        }
    )

# Update FOI draft tick label if present
foi = ROOT / "foi" / "drafts" / f"{GAP}.md"
if foi.exists():
    text = foi.read_text(encoding="utf-8")
    text = text.replace("**tick:** 2126", f"**tick:** {TICK} (race-recover from 2126 collision)")
    foi.write_text(text, encoding="utf-8")

log_path = ROOT / "loop_log.md"
log_entry = f"""

## Tick {TICK} - {UTC} - {RQ} Zorghome De Fakkel Roeselare RACE-RECOVER (omzet JUMP 19.64m / equity JUMP +828% / Medium)

- Unit: **{RQ}** race-recover after concurrent agents took **rq_2126 SLG Wallonie** + **rq_2127 Le Chateau Vert**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Recovered unused leftover **Zorghome De Fakkel BV** YE2025 (KBO **{KBO}**; Hoveniersstraat 15 Roeselare Rumbeke; **BV** NACE **87.101/87.301** / **6 VE**; Armonea/Colisee Remy Yves path). CSV/entity/leaderboard/FOI-queue rows already landed via race into tick2127 commit; this tick fixes queue ownership + FOI draft + raw + loop_state. Do not redo SLG Wallonie/Chateau Vert/Famifamenne/Le Castel/RSW/Sebrechts/Armonea holding. Restel Flats + L'Orchidee deferred live YE2025.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR19637342** JUMP +94.8% vs YE2024 EUR10080939; bruto **EUR13383296** JUMP +90.24%; pnl **EUR412463** JUMP +30.53%; equity **EUR6281446** JUMP +828.25% vs YE2024 EUR676698; FTE **212.7** JUMP vs 119.2; neerlegging **14.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@armonea.be.
- Wrote: fixed rq_2126 entity→srl_slg_wallonie; {RQ}=done Fakkel + {NEXT_RQ} open; loop_state ticks={TICK}; FOI draft + raw tick2126 restored; sources/budgets/commitments/leaderboard/entities already present.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2120**; next **2130**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Restel Flats / unused IGS-DSO-WZC-MRS).
"""
with open(log_path, "a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"OK tick{TICK} Fakkel race-recover")
