import csv
csv.field_size_limit(10_000_000)

with open("docs/doge/data/research_queue.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    opens = []
    done_recent = []
    for row in r:
        st = (row.get("status") or "").strip().lower()
        tid = row.get("task_id") or ""
        if st == "open":
            opens.append(row)
        if tid.startswith("rq_22") and tid >= "rq_2200":
            done_recent.append(row)

print("=== ALL OPEN (full) ===")
for x in opens:
    for k, v in x.items():
        print(f"  {k}: {(v or '')[:300]}")
    print("---")

print("=== recent rq_2215+ ===")
for x in sorted(done_recent, key=lambda z: z.get("task_id") or ""):
    tid = x.get("task_id")
    if tid < "rq_2215":
        continue
    print(
        tid,
        x.get("status"),
        x.get("priority"),
        (x.get("title") or "")[:90],
        "|",
        (x.get("notes") or "")[:120],
    )

# Search for FARO AIESH REW Heropbeuring in entire queue
print("=== FARO/AIESH/REW/Heropbeuring/maatwerk/kringloop/WZC rows ===")
with open("docs/doge/data/research_queue.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        blob = " ".join([(row.get(k) or "") for k in row.keys()]).lower()
        if any(
            k in blob
            for k in (
                "faro",
                "aiesh",
                "rew ",
                "rew-",
                "heropbeuring",
                "vites be",
                "de oever",
                "unused maatwerk",
                "maatwerk-kringloop",
                "agb bornem",
            )
        ):
            print(
                row.get("task_id"),
                row.get("status"),
                row.get("priority"),
                (row.get("title") or "")[:100],
            )
            if "ye2025" in blob or "2025" in (row.get("notes") or "").lower()[:80]:
                print("   notes:", (row.get("notes") or "")[:200])
