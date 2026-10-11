import csv
csv.field_size_limit(10_000_000)
for fn, key, expect in [
    ("sources.csv","source_id","src_windekind_jr2025_nbb_pdf_2429"),
    ("entities.csv","entity_id","vzw_windekind"),
    ("budgets.csv","budget_id","bud_windekind_destin_jr2025_statutory"),
    ("commitments.csv","commitment_id","comm_windekind_jr2025_statutory_bruto_1_18m_omzet73_empty_pnl_drop_61k"),
    ("leaderboard.csv","item_id","lb_windekind_bruto_1_18m_omzet73_empty_pnl_drop_61k_destin_61k_jr2025"),
    ("foi_queue.csv","gap_id","gap_windekind_opgroeien_matrix_bruto_1_18m_omzet73_empty_pnl_drop_61k_destin_61k_l5"),
]:
    with open("docs/doge/data/"+fn, newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    last=rows[-1]
    ok = last.get(key)==expect or expect in (last.get(key) or "")
    print(fn, "nrows", len(rows), "last", last.get(key), "OK" if ok else "CHECK")
    if fn=="entities.csv":
        n=sum(1 for r in rows if r.get("entity_id")=="vzw_windekind")
        print("  windekind entity count", n)
    if fn=="foi_queue.csv":
        print("  status", last.get("status"), "email", last.get("recipient_email"))
    if fn=="leaderboard.csv":
        print("  pi", last.get("priority_index"), "cost", last.get("annual_cost_eur"))
    if fn=="commitments.csv":
        print("  envelope", last.get("total_envelope_eur"), "status", last.get("status"))

with open("docs/doge/data/research_queue.csv", newline="", encoding="utf-8") as f:
    r=csv.DictReader(f)
    found={}
    for row in r:
        if row["task_id"] in ("rq_2428","rq_2429","rq_2430"):
            found[row["task_id"]]=row
print("RQ", {k: (v["status"], v["title"][:90], v.get("entity_id")) for k,v in found.items()})
print("rq_2430 every10", "EVERY-10" in (found["rq_2430"]["instructions"]+found["rq_2430"]["notes"]))
print("rq_2429 created", found["rq_2429"]["created_utc"], "updated", found["rq_2429"]["updated_utc"])

with open("docs/doge/data/loop_state.csv", newline="", encoding="utf-8") as f:
    st=list(csv.DictReader(f))[0]
print("STATE", st["last_unit_id"], st["ticks_completed"], st["last_tick_utc"], st["paused"])
for tid in ("rq_2429","rq_2430"):
    row=found[tid]
    empty_keys=[k for k,v in row.items() if v is None]
    print(tid, "nfields", len(row), "nonevals", empty_keys)
    print("  notes[:80]", (row.get("notes") or "")[:80])
