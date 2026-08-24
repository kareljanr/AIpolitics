from pathlib import Path

src = Path("docs/doge/data/raw/tick2325/write_tick2325_mivalti.py").read_text(encoding="utf-8")
t = src.replace("2325", "2327").replace("2026-08-28T00:25:00Z", "2026-08-28T00:35:00Z")
t = t.replace("after Ritmica@2324", "after Zonnebeke@2326")
t = t.replace("Ritmica@2324", "Zonnebeke@2326")
t = t.replace(
    'if not any(row["task_id"] == "rq_2327" for row in rows):',
    'if not any(row["task_id"] == "rq_2328" for row in rows):',
    1,
)
t = t.replace(
    '"task_id": "rq_2327",\n            "title": "leftover dual after Mivalti',
    '"task_id": "rq_2328",\n            "title": "leftover dual after Mivalti',
    1,
)
t = t.replace("next rq_2327; next EVERY-10 2330", "next rq_2328; next EVERY-10 2330")
t = t.replace(
    "Do NOT redo Mivalti/Ritmica/DominiekSavio/EntreDeux stack.",
    "Do NOT redo Mivalti/Zonnebeke/Ithaka/Ritmica/DominiekSavio stack.",
)
Path("docs/doge/data/raw/tick2327").mkdir(parents=True, exist_ok=True)
Path("docs/doge/data/raw/tick2327/write_tick2327.py").write_text(t, encoding="utf-8")
# fix FOI draft tick
foi = Path(
    "docs/doge/foi/drafts/gap_mivalti_nbb_pdf_assets_debt_bruto_gt_omzet_6_82x_pnl_jump_vaph_matrix_l5.md"
)
if foi.exists():
    ft = foi.read_text(encoding="utf-8").replace("**tick:** 2325", "**tick:** 2327")
    foi.write_text(ft, encoding="utf-8")
print("ok")
for i, l in enumerate(t.splitlines(), 1):
    if "rq_232" in l and any(k in l for k in ("task_id", "last_unit", "already", "spawned", "next rq")):
        print(f"{i}:{l[:110]}")
