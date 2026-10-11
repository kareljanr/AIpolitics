# surgical rq + state + log for tick 1323
import csv, io
from pathlib import Path

DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
UTC = "2026-08-17T18:25:00Z"
ENT = "agb_blankenberge"
GAP = "gap_agbblb_liquidated_jr2019only_l5"

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

path = DATA / "research_queue.csv"
header = path.open(encoding="utf-8").readline()
fields = next(csv.reader([header.strip("\n").strip("\r")]))
with path.open("rb") as f:
    f.seek(0, 2)
    size = f.tell()
    chunk = min(size, 131072)
    f.seek(size - chunk)
    tail = f.read()
search = tail[:-1] if tail.endswith(b"\n") else tail
last_nl = search.rfind(b"\n")
last_line = search[last_nl + 1 :] if last_nl != -1 else search
last_text = last_line.decode("utf-8")
if not last_text.startswith("rq_1323,"):
    raise SystemExit("last line not rq_1323")
if b"rq_1324," in tail:
    raise SystemExit("rq_1324 already present")
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)

rq_new = {
    "task_id": "rq_1323",
    "title": "AGB Blankenberge JR2019-only liquidated dual residual FOI",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: AGB Blankenberge leftover AGB after honest hunt; KBO 0877.301.751 STOPGEZET 21.03.2023; official last AGB JR 2019; no BBC/NBB JR2025 PDF; no sourced euros; FOI ready",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T18:15:00Z",
    "updated_utc": UTC,
    "notes": "tick1323 AGB Blankenberge leftover AGB residual; KBO 0877.301.751 liquidated 21.03.2023; official AGB JR2019-only; FOI ready not sent; next rq_1324 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1324",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined (prior 1255-1323 done including AGB Blankenberge 1323 FOI-liquidated JR2019-only). Prefer leftover APB Campus Vesta KBO 0822.442.511 if a BBC/NBB JR2025 now yields euros. APB POA/TPA only if a real PDF downloads. Leftover cities only if a PDF fetches. Skip already-mined 1313-1323. Skip Motena/Trupark/PATRI/Zorgbedrijf ST/Woonzorgnetwerk Edegem TLS. Not every-10.",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1323 after AGB Blankenberge leftover AGB FOI; next residual dual L5 VL",
}
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("rq patched", path.stat().st_size)

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"], lineterminator="\r\n")
    w.writeheader()
    w.writerow({
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1323",
        "ticks_completed": "1323",
        "paused": "no",
        "notes": "tick1323 AGB Blankenberge leftover AGB residual; KBO 0877.301.751 liquidated 21.03.2023; official AGB JR2019-only; no JR2025 PDF; no sourced euros; FOI ready; next rq_1324 residual dual L5 VL; continuous hole_fill",
    })
print("loop_state ok")

log = ROOT / "loop_log.md"
raw = log.read_bytes()
if b"Tick 1323" in raw[-12000:]:
    print("log already")
else:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    entry = (
        "\n### Tick 1323 - 2026-08-17 - rq_1323 AGB Blankenberge dual residual liquidated FOI\n"
        "- Unit: Autonoom Gemeentebedrijf Blankenberge leftover AGB of already-mined Stad+OCMW Blankenberge (KBO 0877.301.751; official financien + KBO; no JR2025 BBC/NBB PDF). Named leftover unmined AGB after live-PDF hunt failed. KBO Stopgezet since 21.03.2023. Official last AGB JR 2019; city JR2025 already mined tick 998. APB POA/TPA listed but provincieantwerpen.be 403 no PDF. Campus Vesta jaarrapport 234.8MB glossy not BBC. Not every-10.\n"
        "- EUR: none sourced. Do not invent euros. FOI-ready after honest hunt.\n"
        "- CSVs: sources+3/entities+1/commitments+1/leaderboard+1 + FOI ready gap_agbblb_liquidated_jr2019only_l5 (not sent); rq_1323=done; spawn rq_1324; ticks=1323.\n"
        "- Coverage: residual dual L5. Does not move L5 near-complete of TE. No progress refresh.\n"
        "- Next: rq_1324 residual dual L5 VL (prefer leftover APB Campus Vesta if BBC/NBB now yields euros; APB POA/TPA only if a real PDF downloads).\n"
    )
    log.write_bytes(raw + entry.encode("utf-8"))
    print("log ok")
print("done")
