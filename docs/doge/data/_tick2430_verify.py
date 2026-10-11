import csv
csv.field_size_limit(10_000_000)
for fn, key, expect in [
    ("sources.csv","source_id","src_beregoed_jr2025_nbb_pdf_2430"),
    ("entities.csv","entity_id","vzw_beregoed"),
    ("budgets.csv","budget_id","bud_beregoed_destin_jr2025_statutory"),
    ("commitments.csv","commitment_id","comm_beregoed_jr2025_statutory_omzet_2_98m_73_empty_pnl_jump_177k"),
    ("leaderboard.csv","item_id","lb_beregoed_omzet_2_98m_73_empty_pnl_jump_177k_destin_177k_jr2025"),
    ("foi_queue.csv","gap_id","gap_beregoed_opgroeien_matrix_omzet_2_98m_73_empty_pnl_jump_177k_destin_177k_l5"),
]:
    with open("docs/doge/data/"+fn, newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    last=rows[-1]
    ok = last.get(key)==expect or expect in (last.get(key) or "")
    print(fn, "nrows", len(rows), "last", last.get(key), "OK" if ok else "CHECK")
    if fn=="entities.csv":
        n=sum(1 for r in rows if r.get("entity_id")=="vzw_beregoed")
        print("  beregoed entity count", n)
        kbohits=sum(1 for r in rows if "0447.515.042" in " ".join(r.values()))
        print("  kbo mentions in entities", kbohits)
    if fn=="foi_queue.csv":
        print("  status", last.get("status"), "email", last.get("recipient_email"))
    if fn=="leaderboard.csv":
        print("  pi", last.get("priority_index"), "cost", last.get("annual_cost_eur"), "abs", last.get("absurdity_score"), "cs", last.get("cost_score"))
    if fn=="commitments.csv":
        print("  envelope", last.get("total_envelope_eur"), "status", last.get("status"))

with open("docs/doge/data/research_queue.csv", newline="", encoding="utf-8") as f:
    r=csv.DictReader(f)
    found={}
    for row in r:
        if row["task_id"] in ("rq_2429","rq_2430","rq_2431"):
            found[row["task_id"]]=row
print("RQ", {k: (v["status"], v["title"][:90], v.get("entity_id")) for k,v in found.items()})
print("rq_2430 every10 notes", "EVERY-10" in (found["rq_2430"]["notes"]))
print("rq_2431 next2440", "2440" in (found["rq_2431"]["instructions"]+found["rq_2431"]["notes"]))

with open("docs/doge/data/loop_state.csv", newline="", encoding="utf-8") as f:
    st=list(csv.DictReader(f))[0]
print("STATE", st["last_unit_id"], st["ticks_completed"], st["last_tick_utc"], st["paused"])
for tid in ("rq_2430","rq_2431"):
    row=found[tid]
    empty_keys=[k for k,v in row.items() if v is None]
    print(tid, "nfields", len(row), "nonevals", empty_keys)
    print("  notes[:80]", (row.get("notes") or "")[:80])

from pathlib import Path
assert Path("docs/doge/foi/drafts/gap_beregoed_opgroeien_matrix_omzet_2_98m_73_empty_pnl_jump_177k_destin_177k_l5.md").is_file()
prog = Path("docs/doge/data/progress_every_10_ticks.md").read_text()
waste = Path("docs/doge/data/doge_waste_top10_current.md").read_text()
assert "tick 2430" in prog and "Beregoed" in prog
assert "tick **2430**" in waste and "Beregoed" in waste
print("every10 files OK")
print("ALL VERIFY OK")
