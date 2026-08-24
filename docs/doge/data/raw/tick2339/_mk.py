from pathlib import Path

src = Path("docs/doge/data/raw/tick2338/write_tick2338.py").read_text(encoding="utf-8")
src = src.replace("2026-08-24T18:30:00Z", "2026-08-24T18:40:00Z")
src = src.replace("rq_2338", "rq_2339")
src = src.replace("NEXT = \"rq_2339\"", "NEXT = \"rq_2340\"")  # may already be rq_2340
# after first replace rq_2338->2339, NEXT was rq_2340 unchanged; TICK 2338-> need careful
src = src.replace("TICK = \"2338\"", "TICK = \"2339\"")
src = src.replace("tick2338", "tick2339")
src = src.replace("2338", "2339")  # remaining tick numbers in paths/notes
# fix NEXT if it became rq_2340 still ok; if became rq_2339 restore
if 'NEXT = "rq_2339"' in src:
    src = src.replace('NEXT = "rq_2339"', 'NEXT = "rq_2340"')
src = src.replace("after Wieltjesgracht@2337", "after De Cirkel@2338")
src = src.replace("Wieltjesgracht@2337", "De Cirkel@2338")
# undo over-replace of source ids that said 2338 intentionally then became 2339 - fine
out = Path("docs/doge/data/raw/tick2339")
out.mkdir(parents=True, exist_ok=True)
(out / "write_tick2339.py").write_text(src, encoding="utf-8")
print("wrote", out / "write_tick2339.py")
print("TASK", "rq_2339" in src)
print("TICK2339", 'TICK = "2339"' in src)
print("NEXT", [line for line in src.splitlines() if line.startswith("NEXT")])
