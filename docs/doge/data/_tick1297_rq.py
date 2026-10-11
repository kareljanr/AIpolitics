# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
UTC="2026-08-17T12:50:00Z"
ENT="city_diepenbeek"
GAP="gap_diepbk_fin_debt_13_59m_igs_reval_19_43m_ocmw_equity_neg_0_71m_l5"

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
    "task_id": "rq_1297",
    "title": "Stad+OCMW Diepenbeek JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: Stad+OCMW Diepenbeek JR2025 BBC text + KBO; KBO 0207.465.974 / 0212.246.787; assets 190.496m / fin debt 13.592m / IGS reval 19.425m / OCMW equity -0.708m NEG / AFM +5.047m; FOI ready",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T12:45:00Z",
    "updated_utc": UTC,
    "notes": "tick1297 Stad+OCMW Diepenbeek JR2025 GE residual; KBO 0207.465.974/0212.246.787; assets 190.496m fin debt 13.592m IGS reval 19.425m AFM +5.047m gecorr +5.784m BBR +0.364m avail 21.858m cash 25.047m OCMW equity -0.708m NEG tussen 0 pers 24.854m politie 2.766m new loans 0.577m leasing; AGB EVA 7.010m already 1296; FOI ready not sent; next rq_1298 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1298",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined (prior 1255-1297 done including Stad+OCMW Diepenbeek 1297 / AGB Diepenbeek 1296); prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; skip already-mined city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; Londerzeel/Holsbeek/Merchtem/Steenokkerzeel/Pepingen/Zwalm/Wortegem-Petegem city+OCMW JR2025 only if PDF fetches; AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden only if JR2025 downloadable; skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1297 after Stad+OCMW Diepenbeek JR2025 GE residual; next residual dual L5 VL",
}
path = DATA/"research_queue.csv"
before = path.stat().st_size
found, spawned = patch_last_rq_and_spawn(path, "rq_1297", rq_new, rq_spawn)
after = path.stat().st_size
print("research_queue 1297", found, "spawned_1298", spawned, "size", before, "->", after)
# verify tail
with path.open("rb") as f:
    f.seek(0,2); f.seek(max(0,f.tell()-400)); tail=f.read().decode("utf-8", errors="replace")
print("TAIL_STARTS", tail.splitlines()[0][:40] if False else "")
print(tail[-350:])
