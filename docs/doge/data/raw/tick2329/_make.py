from pathlib import Path

src = Path("docs/doge/data/raw/tick2325/write_tick2325_mivalti.py").read_text(encoding="utf-8")
t = src.replace("2325", "2329").replace("2026-08-28T00:25:00Z", "2026-08-28T00:45:00Z")
t = t.replace("after Ritmica@2324", "after HetEepos@2328")
t = t.replace("Ritmica@2324", "HetEepos@2328")
# After blind replace, spawn targets rq_2329 (same as task). Fix spawn to 2330.
t = t.replace(
    'if not any(row["task_id"] == "rq_2329" for row in rows):',
    'if not any(row["task_id"] == "rq_2330" for row in rows):',
    1,
)
t = t.replace(
    '"task_id": "rq_2329",\n            "title": "leftover dual after Mivalti',
    '"task_id": "rq_2330",\n            "title": "leftover dual after Mivalti',
    1,
)
t = t.replace("next rq_2329; next EVERY-10 2330", "next rq_2330; next EVERY-10 2330")
# EVERY-10 is 2330 - if this tick is 2329, next every-10 stays 2330. If we complete 2330 next fire does it.
t = t.replace(
    "Do NOT redo Mivalti/Ritmica/DominiekSavio/EntreDeux stack.",
    "Do NOT redo Mivalti/HetEepos/Pleegzorg/Zonnebeke/Ithaka stack.",
)
Path("docs/doge/data/raw/tick2329").mkdir(parents=True, exist_ok=True)
Path("docs/doge/data/raw/tick2329/write_tick2329.py").write_text(t, encoding="utf-8")
foi = Path(
    "docs/doge/foi/drafts/gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5.md"
)
if foi.exists():
    foi.write_text(
        foi.read_text(encoding="utf-8").replace("**tick:** 2327", "**tick:** 2329").replace("**tick:** 2325", "**tick:** 2329"),
        encoding="utf-8",
    )
print("ok")
for i, l in enumerate(t.splitlines(), 1):
    if "rq_23" in l and any(k in l for k in ("task_id", "last_unit", "already", "spawned", "next rq")):
        print(f"{i}:{l[:110]}")
