from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2448_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2448,")!=1: raise SystemExit("bad 2448 count")
if b"rq_2449," in rq_raw: raise SystemExit("2449 exists")
idx=rq_raw.rfind(b"rq_2448,")
if idx<0: raise SystemExit("rq_2448 not found")
new_2448=Path("/tmp/rq2448_done.txt").read_text(encoding="utf-8")
new_2449=Path("/tmp/rq2449_open.txt").read_text(encoding="utf-8")
if not new_2448.endswith("\n") or not new_2449.endswith("\n"): raise SystemExit("rows missing LF")
if new_2448.count("\n")!=1 or new_2449.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2448.encode("utf-8"))
    f.write(new_2449.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2448", chk.count(b"rq_2448,"), "n2449", chk.count(b"rq_2449,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
# loop_state overwrite (small file)
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2448,2448,no,tick2448 leftover dual Peutertuinen GO Mariakerke 0410.221.116 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A DROP 0; bruto9900 DROP 872268 envelope; pnl JUMP 115219; 9901 JUMP 126095; equity JUMP 1316171; assets JUMP 1658146; debt JUMP 341975; FTE 13.7 DROP; kapitaalsubsidies JUMP 491875; destin691 empty FLAT; cash DROP 550474; geldbeleggingen empty; 2 VE leftover city_gent CIK); leftover mined city_gent CIK; NOT Mini-creches GO Next remine; NOT Stad Gent peutertuinen; NOT Villa Boempatat YE2024; NOT COB Annuntiaten remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2450; next rq_2449 leftover dual\n",
encoding="utf-8")
print("loop_state ok")
