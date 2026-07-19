from pathlib import Path

p = Path(__file__).resolve().parents[1] / "foi_queue.csv"
text = p.read_text(encoding="utf-8-sig")
updates = {
    "gap_multi_parliaments": (
        ",draft,,,,,,,2026-07-19T17:00:00Z,2026-07-19T17:00:00Z,rq_009",
        ",ready,2026-07-19,,,,\"\",,,2026-07-19T17:00:00Z,2026-07-19T21:15:00Z,rq_018 batch ready multi-letter",
    ),
    "gap_wal_l5_top_subsidies": (
        ",draft,,,,,,,2026-07-19T18:30:00Z,2026-07-19T18:30:00Z,rq_011",
        ",ready,2026-07-19,,,,\"\",,,2026-07-19T18:30:00Z,2026-07-19T21:15:00Z,rq_018",
    ),
    "gap_forem_budget": (
        ",draft,,,,,,,2026-07-19T19:00:00Z,2026-07-19T19:00:00Z,rq_012",
        ",ready,2026-07-19,,,,\"\",,,2026-07-19T19:00:00Z,2026-07-19T21:15:00Z,rq_018",
    ),
    "gap_vdab_full_budget": (
        ",draft,,,,,,,2026-07-19T19:00:00Z,2026-07-19T19:00:00Z,rq_012",
        ",ready,2026-07-19,,,,\"\",,,2026-07-19T19:00:00Z,2026-07-19T21:15:00Z,rq_018 openbaarheid@vlaanderen.be",
    ),
}
for gap, (old, new) in updates.items():
    if old not in text:
        # try find line and replace status only
        lines = text.splitlines()
        out = []
        for line in lines:
            if line.startswith(gap + ",") and ",draft," in line:
                line = line.replace(",draft,", ",ready,", 1)
                # crude date bump in notes area - leave if complex
                print("status-only", gap)
            out.append(line)
        text = "\n".join(out) + "\n"
    else:
        text = text.replace(old, new)
        print("ok", gap)
p.write_text(text, encoding="utf-8")
print("done")
