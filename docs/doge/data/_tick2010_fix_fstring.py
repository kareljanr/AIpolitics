from pathlib import Path

p = Path("docs/doge/data/_tick2010_write.py")
t = p.read_text(encoding="utf-8")

# Replace: progress = f""" ... """  (ending before Path("docs/doge/data/progress..."))
start = t.find('progress = f"""')
if start < 0:
    raise SystemExit("progress f-string not found")
end = t.find('Path("docs/doge/data/progress_every_10_ticks.md")', start)
if end < 0:
    raise SystemExit("progress write not found")

# Extract body between f""" and closing """
body_start = start + len('progress = f"""')
# find closing """ before Path write - the assignment ends with """
close = t.rfind('"""', body_start, end)
body = t[body_start:close]

# Escape all braces then unescape our placeholders
body2 = body.replace("{", "{{").replace("}", "}}")
for key in [
    "foi_ready",
    "foi_answered",
    "foi_partial",
]:
    body2 = body2.replace("{{" + key + "}}", "{" + key + "}")
# len(...) placeholders
for expr in [
    "len(frows)",
    "len(brows)",
    "len(crows)",
    "len(lrows)",
    "len(erows)",
    "len(srows)",
]:
    body2 = body2.replace("{{" + expr + "}}", "{" + expr + "}")

replacement = (
    "progress = \"\"\""
    + body2
    + "\"\"\".format(\n"
    "    foi_ready=foi_ready,\n"
    "    foi_answered=foi_answered,\n"
    "    foi_partial=foi_partial,\n"
    "    **{\n"
    "        'len(frows)': len(frows),\n"
    "        'len(brows)': len(brows),\n"
    "        'len(crows)': len(crows),\n"
    "        'len(lrows)': len(lrows),\n"
    "        'len(erows)': len(erows),\n"
    "        'len(srows)': len(srows),\n"
    "    }\n"
    ")\n\n"
)

# Also fix top10 = f""" which uses {len(lrows)}
t2 = t[:start] + replacement + t[end:]
# fix top10
if 'top10 = f"""' in t2:
    t2 = t2.replace('top10 = f"""', 'top10 = """')
    # only {len(lrows)} should remain as format; double other braces in top10 section
    ts = t2.find('top10 = """')
    te = t2.find('Path("docs/doge/data/doge_waste_top10_current.md")', ts)
    close2 = t2.rfind('"""', ts + 10, te)
    bodyt = t2[ts + len('top10 = """') : close2]
    bodyt2 = bodyt.replace("{", "{{").replace("}", "}}")
    bodyt2 = bodyt2.replace("{{len(lrows)}}", "{len_lrows}")
    t2 = (
        t2[: ts + len('top10 = """')]
        + bodyt2
        + '""".format(len_lrows=len(lrows))\n\n'
        + t2[te:]
    )

p.write_text(t2, encoding="utf-8")
print("patched ok")
# syntax check
compile(p.read_text(encoding="utf-8"), str(p), "exec")
print("syntax ok")
