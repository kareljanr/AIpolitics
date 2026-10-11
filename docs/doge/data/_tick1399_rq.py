# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
path = Path("/workspace/AIpolitics/docs/doge/data/research_queue.csv")
UTC = "2026-08-19T05:24:00Z"
ENT = "nv_otar"
GAP = "gap_otar_omzet_12_43m_diensten_10_24m_div_14_47m_l5"
header = path.open(encoding="utf-8").readline()
fields = next(csv.reader([header.strip("\n").strip("\r")]))

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

rq_new = {
    "task_id": "rq_1399",
    "title": "Otary RS JR2025 leftover dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: Otary RS leftover Nuhma-adjacent public-law NV after leftover AGB/IGS hunt; KBO 0833.507.538 Actief; live JR2025 official NBB WVV VOL-kap PDF (589485 bytes 47p deposit 2026-00254280; commissaris Deloitte 16609+6598); sourced euros assets 95625285 / omzet 12426978 / diensten 10235828 / debt 14121330 / pnl 17237470 / dividend 14471000 / fva 82864237 / cash 10999623; FOI ready 6.10 empty / 10.24m diensten / 14.47m dividend / 82.86m FVA / 11.00m achtergesteld",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-19T05:05:00Z",
    "updated_utc": UTC,
    "notes": "tick1399 Otary RS leftover Nuhma-adjacent public-law NV residual; KBO 0833.507.538; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1400 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1400",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1399 done including Otary RS 1399 leftover Nuhma-adjacent public-law NV live NBB WVV / IGS IBEG 1398 leftover energy holding IGS live NBB WVV / IGS IVEBICA 1397 leftover library/culture/academy IGS live NBB WVV / IGS Pontes 1396 leftover crematorium IGS live NBB WVV / IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / IGS Westlede 1394 leftover crematorium IGS live NBB WVV / HAVICREM 1393 leftover crematorium IGS live NBB WVV / IVLA 1392 leftover waste IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; skip already-mined Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344 / ECO2050 1360 / Nuhma cv 1356; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1399 after Otary RS leftover Nuhma-adjacent public-law NV live NBB WVV; next residual dual L5 VL",
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
if not last_text.startswith("rq_1399,"):
    raise SystemExit("last rq line is not rq_1399: %s" % last_text[:160])
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
if b"rq_1400" in tail:
    raise SystemExit("spawn id already in tail")
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("research_queue patched rq_1399 done + spawned rq_1400; new_size", path.stat().st_size)
