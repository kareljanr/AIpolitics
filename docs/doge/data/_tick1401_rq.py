# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
path = Path("/workspace/AIpolitics/docs/doge/data/research_queue.csv")
UTC = "2026-08-19T05:50:00Z"
ENT = "igs_ovco"
GAP = "gap_ovco_omzet_empty_debt_6_31m_cip_0_98m_l5"
header = path.open(encoding="utf-8").readline()
fields = next(csv.reader([header.strip("\n").strip("\r")]))

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

rq_new = {
    "task_id": "rq_1401",
    "title": "OVCO JR2025 leftover dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: OVCO leftover crematorium IGS of mined arrondissement-Oostende municipalities Oostende+Bredene+Middelkerke+Oudenburg after leftover AGB/IGS hunt; KBO 0845.064.493 Actief; live JR2025 official NBB WVV VKT-kap PDF (908492 bytes 30p deposit 2026-00287142; commissaris Callens 5576 oordeel zonder voorbehoud); sourced euros assets 9368744 / brutomarge 1163024 / pers 459819 / debt 6313967 / pnl 385548 / equity 3054777 / cash 83941 / invest 973616 / cip 975949 / capsub 1743380; FOI ready omzet 70 empty / 60/61 empty / 6.31m debt / 0.98m CIP / vennoten share unpublished",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-19T05:40:00Z",
    "updated_utc": UTC,
    "notes": "tick1401 OVCO leftover crematorium IGS residual; KBO 0845.064.493; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1402 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1402",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1401 done including OVCO 1401 leftover crematorium IGS live NBB WVV / IGL 1400 leftover zorg IGS live NBB WVV / Otary RS 1399 leftover Nuhma-adjacent public-law NV live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; skip already-mined OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1401 after OVCO leftover crematorium IGS live NBB WVV; next residual dual L5 VL",
}
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
if not last_text.startswith("rq_1401,"):
    raise SystemExit("last rq line is not rq_1401: %s" % last_text[:160])
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
if b"rq_1402" in tail:
    raise SystemExit("spawn id already in tail")
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("research_queue patched rq_1401 done + spawned rq_1402; new_size", path.stat().st_size)
