import csv
from pathlib import Path

csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
now = "2026-08-26T03:05:00Z"
tick = 1862
eid = "digipolis_antwerpen"
pdf_url = "https://ebesluit.antwerpen.be/document/6a4509e83247ef1f6b6f4718"
src = "src_digipolis_jr2025_gr00616_pdf"
EQUITY_NEG = 4114715
ASSETS = 73605124
SURPLUS = 109871
gap = "gap_digipolis_equity_neg_4_11m_continuity_j2_l5"


def read_csv(name):
    with (DATA / name).open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), list(r.fieldnames)


def write_csv(name, rows, fieldnames):
    with (DATA / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


sources, scols = read_csv("sources.csv")
sources.append(
    {
        "source_id": src,
        "title": "AG Digipolis Antwerpen JR2025 GR 2026_GR_00616 full PDF (74p)",
        "url": pdf_url,
        "publisher": "Stad Antwerpen ebesluit / AG Digipolis",
        "accessed_date": "2026-08-26",
        "source_class": "primary_pdf",
        "notes": (
            "tick1862; 3968982 bytes / 74p; assets 73605124 surplus 109871; "
            "commissaris equity NEG 4114715 continuity emphasis; J2 tables image-only residual"
        ),
    }
)
write_csv("sources.csv", sources, scols)

budgets, bcols = read_csv("budgets.csv")
for bid, amt, basis in [
    ("bud_digipolis_assets_73_61m_jr2025_pdf", ASSETS, "JR2025 GR PDF balanstotaal"),
    ("bud_digipolis_surplus_0_11m_jr2025_pdf", SURPLUS, "JR2025 GR PDF overschot boekjaar"),
    ("bud_digipolis_equity_neg_4_11m_jr2025_pdf", -EQUITY_NEG, "JR2025 commissaris EV NEG continuity"),
]:
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": eid,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": src,
            "confidence": "strong",
            "notes": f"tick{tick}; {basis}; not TE-additive; dual ICT cost-share",
        }
    )
write_csv("budgets.csv", budgets, bcols)

ents, ecols = read_csv("entities.csv")
for e in ents:
    if e.get("entity_id") == eid:
        e["notes"] = (
            "tick1862 JR2025 GR PDF LIVE: assets 73.605m surplus 0.110m equity NEG 4.115m "
            "continuity emphasis (commissaris); KBO 0751.541.350; Generaal Armstrongweg 1; "
            "J2 AFM/BBR/pers/debt image FOI residual; prior MJP 245.6m / member omzet 221.9m"
        )
        e["website"] = pdf_url
        e["foi_postal"] = "Generaal Armstrongweg 1 2020 Antwerpen"
        break
write_csv("entities.csv", ents, ecols)

comms, ccols = read_csv("commitments.csv")
comms += [
    {
        "commitment_id": "comm_digipolis_equity_neg_4_11m_jr2025",
        "title": "Digipolis JR2025 equity NEG 4.115m + continuity emphasis",
        "entity_id": eid,
        "beneficiary": "AG Digipolis / Stad Antwerpen ICT cost-share members",
        "legal_basis": "Decreet Lokaal Bestuur AGB; BBC JR2025; ISA commissaris",
        "decision_date": "2026-06-29",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(EQUITY_NEG),
        "cash_by_year": "",
        "remaining_eur": str(EQUITY_NEG),
        "status": "active",
        "evaluation_url": pdf_url,
        "stated_goal": "Municipal ICT cost-sharing continuity",
        "cut_option": "FOI EV recovery path + city guarantee + J2 full text",
        "source_id": src,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Antwerpen>AG_Digipolis>JR2025_L5",
        "notes": (
            "tick1862; commissaris PDF: EV NEG 4114715 despite PnL +109871; "
            "successive losses; AG part of Stad Antwerpen financing support"
        ),
    },
    {
        "commitment_id": "comm_digipolis_jr2025_pdf_assets_surplus",
        "title": "Digipolis JR2025 primary PDF assets 73.605m / surplus 0.110m",
        "entity_id": eid,
        "beneficiary": "Groep stad Antwerpen ICT members",
        "legal_basis": "BBC JR2025 GR 2026_GR_00616",
        "decision_date": "2026-06-29",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(ASSETS),
        "cash_by_year": f"{{2025_surplus:{SURPLUS}}}",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": pdf_url,
        "stated_goal": "Kostendelende ICT vereniging YE2025 close",
        "cut_option": "FOI J2 AFM/BBR/pers/debt text layer",
        "source_id": src,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Antwerpen>AG_Digipolis>JR2025_L5",
        "notes": "tick1862; closes prior PDF-opaque FOI for headline BS+PnL; residual J2 image-only",
    },
]
write_csv("commitments.csv", comms, ccols)

lbs, lcols = read_csv("leaderboard.csv")
lbs += [
    {
        "item_id": "lb_digipolis_equity_neg_4_11m_continuity_jr2025",
        "name": "Digipolis equity NEG 4.11m + continuity alarm (JR2025 PDF)",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Gemeenten>Antwerpen>AG_Digipolis>JR2025_L5",
        "annual_cost_eur": str(EQUITY_NEG),
        "total_cost_eur": str(ASSETS),
        "tco_notes": "EV NEG 4114715; assets 73605124; surplus 109871; successive losses; city-backed AG",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "Stad+PZA+AGSO+HVZ+VESPA+other Digipolis members",
        "stated_goal": "Cost-sharing ICT continuity",
        "measured_outcome": "Commissaris zonder voorbehoud + continuity emphasis of matter",
        "absurdity_score": "7.5",
        "cost_score": "5.5",
        "difficulty": "4.0",
        "priority_index": "6.05",
        "cut_proposal": "Publish EV recovery + J2 full; review member recharge vs thin surplus",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1862; primary GR PDF; not TE-additive; dual ICT",
    },
    {
        "item_id": "lb_digipolis_jr2025_pdf_assets_73_61m",
        "name": "Digipolis JR2025 PDF live: assets 73.61m / surplus 0.11m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Gemeenten>Antwerpen>AG_Digipolis>JR2025_L5",
        "annual_cost_eur": str(SURPLUS),
        "total_cost_eur": str(ASSETS),
        "tco_notes": "Confirms prior GR HTML; PDF now live; J2 residual FOI",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "Digipolis member entities",
        "stated_goal": "YE2025 BBC close",
        "measured_outcome": "GR advies + kwijting 29.06.2026",
        "absurdity_score": "4.0",
        "cost_score": "7.5",
        "difficulty": "3.0",
        "priority_index": "5.55",
        "cut_proposal": "Machine-readable J2/J4/J5",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1862; closes PDF-opaque path for headline; not TE-additive",
    },
]
write_csv("leaderboard.csv", lbs, lcols)

fois, fcols = read_csv("foi_queue.csv")
# mark old opaque gap partial
for row in fois:
    if row.get("gap_id") == "gap_digipolis_jr2025_pdf_opaque_assets_73_61m_surplus_0_11m_l5":
        row["status"] = "partial"
        row["date_answered"] = "2026-08-26"
        row["response_summary"] = (
            "tick1862: GR PDF now live at ebesluit document/6a4509e8…; assets 73.605m + surplus "
            "0.110m + NEW equity NEG 4.115m continuity confirmed; residual J2 text layer image-only"
        )
        row["updated_utc"] = now
        row["notes"] = (row.get("notes") or "") + "; tick1862 partial — PDF live, J2 residual new FOI"
fois.append(
    {
        "gap_id": gap,
        "hierarchy_path": "Vlaanderen>Gemeenten>Antwerpen>AG_Digipolis>equity_continuity_J2_L5",
        "entity_id": eid,
        "what_is_missing": (
            "Machine-readable J2/J4/J5 AFM/BBR/pers/VTE/cash/fin debt; EV NEG 4.115m recovery path "
            "+ city guarantees/treasury advances; recon surplus 0.110m vs successive losses; "
            "member omzet 2025 outturn vs 221.9m matrix"
        ),
        "why_it_matters": (
            "Largest Antwerp ICT AGB: NEG equity 4.11m + continuity emphasis despite thin surplus "
            "on ~222m member omzet — need J2 transparency beyond image annex"
        ),
        "priority": "8",
        "recipient_body": "AG Digipolis Antwerpen / Stad Antwerpen openbaarheid",
        "recipient_email": "info@digipolis.be",
        "recipient_postal": "Generaal Armstrongweg 1 2020 Antwerpen",
        "draft_letter_path": f"docs/doge/foi/drafts/{gap}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_digipolis_equity_neg_4_11m_jr2025",
        "linked_leaderboard_id": "lb_digipolis_equity_neg_4_11m_continuity_jr2025",
        "created_utc": now,
        "updated_utc": now,
        "notes": "tick1862 residual after PDF live; human-send only; prior opaque FOI marked partial",
    }
)
write_csv("foi_queue.csv", fois, fcols)

rq, rcols = read_csv("research_queue.csv")
for row in rq:
    if row.get("task_id") == "rq_1862":
        row["status"] = "done"
        row["entity_id"] = eid
        row["blocked_gap_id"] = gap
        row["updated_utc"] = now
        row["notes"] = (
            "tick1862 DONE Digipolis JR2025 GR PDF live; assets 73.605m surplus 0.110m "
            "NEW equity NEG 4.115m continuity; J2 image FOI residual; AGB Bornem JR2024; "
            "Dijk92 403; FARO YE2024; Bosgroep Houtland/IJzer no YE2025 deposit"
        )
rq.append(
    {
        "task_id": "rq_1863",
        "title": "Leftover dual residual hole-fill after Digipolis PDF (AGB/Dijk92/FARO/Bosgroep-if-CDN / other HVZ-IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1863 after 1862 Digipolis JR2025 PDF. Prefer leftover AGB/APB if PDF live, else "
            "Dijk92/Enebra if CDN 200, else FARO if TRUE NBB YE2025, else Bosgroep Houtland/IJzer "
            "if CDN 200, else other HVZ/IGS live JR2025 euros. Digipolis+BosgroepLimburgFOI+"
            "DiependaeleIOED+Audio taken. Skip done. Prefer NON-Eneco. Next every-10 1870."
        ),
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": now,
        "notes": "spawned after tick1862; next every-10 1870",
    }
)
write_csv("research_queue.csv", rq, rcols)

ls, lsc = read_csv("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = now
        row["last_unit_id"] = "rq_1862"
        row["ticks_completed"] = "1862"
        row["paused"] = "no"
        row["notes"] = (
            "tick1862 leftover Digipolis JR2025 GR PDF (assets 73.605m surplus 0.110m equity NEG "
            "4.115m continuity); J2 FOI residual; AGB Bornem JR2024; Dijk92 403; FARO YE2024; "
            "next rq_1863; next every-10 1870; continuous hole_fill"
        )
write_csv("loop_state.csv", ls, lsc)

print("OK", tick, "budgets", len(budgets), "foi", len(fois))
