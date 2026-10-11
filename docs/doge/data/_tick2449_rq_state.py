from pathlib import Path
DATA=Path("/workspace/AIpolitics/docs/doge/data")
STAMP,DAY=(DATA/"_tick2449_stamp.txt").read_text().strip().splitlines()
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2449,")!=1: raise SystemExit("bad 2449 count")
if b"rq_2450," in rq_raw: raise SystemExit("2450 exists")
idx=rq_raw.rfind(b"rq_2449,")
if idx<0: raise SystemExit("rq_2449 not found")
new_2449=Path("/tmp/rq2449_done.txt").read_text(encoding="utf-8")
new_2450=Path("/tmp/rq2450_open.txt").read_text(encoding="utf-8")
if not new_2449.endswith("\n") or not new_2450.endswith("\n"): raise SystemExit("rows missing LF")
if new_2449.count("\n")!=1 or new_2450.count("\n")!=1: raise SystemExit("bad newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2449.encode("utf-8"))
    f.write(new_2450.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2449", chk.count(b"rq_2449,"), "n2450", chk.count(b"rq_2450,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")
state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2449,2449,no,tick2449 leftover dual Familia 0461.401.779 Strong native PDF (omzet70 JUMP 1249649 commercial-only; 73 JUMP 6232638; 76A DROP 26485; opbr70/76A JUMP 7571995 envelope; pnl JUMP 645105; 9901 JUMP 642132; equity JUMP 4554709; assets JUMP 5674553; debt DROP 1065188; FTE 103.5 JUMP; kapitaalsubsidies DROP 1169221; destin691 JUMP 462255; 791 empty; cash DROP 256788; geldbeleggingen JUMP 1334280; 1 VE leftover city_genk CIK); leftover mined city_genk CIK; NOT BKO GENK-OOST remine; NOT Peutertuinen remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; next every-10 is 2450; next rq_2450 leftover dual + every-10 refresh\n",
encoding="utf-8")
print("loop_state ok")
