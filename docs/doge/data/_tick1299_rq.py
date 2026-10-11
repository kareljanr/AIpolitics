# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
UTC="2026-08-17T13:50:00Z"
ENT="agb_kortenaken"
GAP="gap_agbktn_fin_debt_3_28m_lease_3_22m_prijssub_0_16m_l5"

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True

rq_new = {
    "task_id": "rq_1299",
    "title": "AGB Kortenaken JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: AGB Kortenaken JR2025 BBC text + KBO; KBO 0535.811.469; assets 3.479m / fin debt 3.281m / leasing 3.216m / city prijssub 0.157m / gecorr AFM -0.209m; FOI ready",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:20:00Z",
    "updated_utc": UTC,
    "notes": "tick1299 AGB Kortenaken JR2025 Entity II residual; KBO 0535.811.469; assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m AFM +0.009m gecorr -0.209m BBR +0.009m avail 0.095m cash 0.104m JUMP new loans 0.017m city interest-free dividend 0.010m; city GE JR2025 live left unmined; FOI ready not sent; next rq_1300 residual dual L5 VL + every-10 progress",
}
rq_spawn = {
    "task_id": "rq_1300",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined (prior 1255-1299 done including AGB Kortenaken 1299 / Stad+OCMW Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / Stad+OCMW Diepenbeek 1297 / AGB Diepenbeek 1296); prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; city Kortenaken GE JR2025 now fetchable on kortenaken.be — take as GE unit; skip already-mined AGB Kortenaken 1299 / city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; Londerzeel/Holsbeek/Merchtem/Pepingen/Zwalm/Wortegem-Petegem city+OCMW JR2025 only if PDF fetches; AGB PATRI Sint-Truiden only if JR2025 downloadable; skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; skip Kuurne city already 957; skip Ternat/Lubbeek already mined; ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF; tick 1300 is every-10: also refresh progress_every_10_ticks.md + doge_waste_top10_current.md",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1299 after AGB Kortenaken JR2025 Entity II residual; next residual dual L5 VL + every-10 progress@1300",
}
path = DATA/"research_queue.csv"
before = path.stat().st_size
found, spawned = patch_last_rq_and_spawn(path, "rq_1299", rq_new, rq_spawn)
after = path.stat().st_size
print("research_queue 1299", found, "spawned_1300", spawned, "size", before, "->", after)
with path.open("rb") as f:
    f.seek(0,2); f.seek(max(0,f.tell()-400)); tail=f.read().decode("utf-8", errors="replace")
print(tail[-300:])
