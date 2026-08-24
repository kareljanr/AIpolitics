import csv
csv.field_size_limit(10_000_000)

with open("docs/doge/data/loop_state.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    print("STATE:", rows[0] if rows else None)

with open("docs/doge/data/research_queue.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    print("RQ fields:", r.fieldnames)
    inprog = []
    opens = []
    recent = []
    target = None
    for row in r:
        st = (row.get("status") or "").strip().lower()
        uid = row.get("id") or ""
        if uid >= "rq_2220" and uid <= "rq_2245":
            recent.append(
                (
                    uid,
                    st,
                    row.get("priority"),
                    (row.get("title") or row.get("topic") or "")[:100],
                )
            )
        if uid == "rq_2228":
            target = row
        if st == "in_progress":
            inprog.append(row)
        elif st == "open":
            opens.append(row)

print("in_progress", len(inprog))
for x in inprog[:8]:
    print(
        "INP",
        x.get("id"),
        x.get("priority"),
        (x.get("title") or x.get("topic") or "")[:120],
    )


def pri(x):
    try:
        return float(x.get("priority") or 0)
    except Exception:
        return 0


opens.sort(key=lambda x: (-pri(x), x.get("id") or ""))
print("open", len(opens))
for x in opens[:40]:
    tid = x.get("id") or ""
    title = (x.get("title") or x.get("topic") or x.get("notes") or "")[:120]
    print("OPEN pri=%s id=%s | %s" % (x.get("priority"), tid, title))

print("--- recent 2220-2245 ---")
for t in recent:
    print(t)

if target:
    print("--- rq_2228 full ---")
    for k, v in target.items():
        print(f"  {k}: {(v or '')[:200]}")

# Look for FARO / AIESH / REW / maatwerk leftover opens
print("--- leftover keywords among opens ---")
keys = ("faro", "aiesh", "rew", "maatwerk", "kringloop", "wzc", "dual")
for x in opens:
    blob = " ".join(
        [
            (x.get("title") or ""),
            (x.get("topic") or ""),
            (x.get("notes") or ""),
            (x.get("entity") or ""),
            (x.get("id") or ""),
        ]
    ).lower()
    if any(k in blob for k in keys):
        print(
            "HIT pri=%s id=%s | %s"
            % (
                x.get("priority"),
                x.get("id"),
                (x.get("title") or x.get("topic") or "")[:140],
            )
        )
