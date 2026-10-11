# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
path = Path("/workspace/AIpolitics/docs/doge/data/research_queue.csv")
UTC = "2026-08-19T05:05:00Z"
ENT = "igs_ibeg"
GAP = "gap_ibeg_omzet_empty_div_3_50m_fva_96_37m_l5"
header = path.open(encoding="utf-8").readline()
fields = next(csv.reader([header.strip("\n").strip("\r")]))

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

rq_new = {
    "task_id": "rq_1398",
    "title": "IGS IBEG JR2025 leftover dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: IGS IBEG leftover IGS energy holding of Grimbergen+Machelen+Meise+Vilvoorde+Wemmel after honest hunt; KBO 0202.082.078 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.93MB 40p deposit 2026-00238388; commissaris EY 6:116 only); sourced euros assets 100488193 / omzet empty / diensten 809703 / debt 1450184 / pnl 1283311 / dividend 3500000 / fva 96372430; FOI ready omzet empty / 3.50m dividend / 96.37m FVA / 9.00m Fluvius HV loan",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-19T05:15:00Z",
    "updated_utc": UTC,
    "notes": "tick1398 IGS IBEG leftover IGS energy holding residual; KBO 0202.082.078; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1399 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1399",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1398 done including IGS IBEG 1398 leftover energy holding IGS live NBB WVV / IGS IVEBICA 1397 leftover library/culture/academy IGS live NBB WVV / IGS Pontes 1396 leftover crematorium IGS live NBB WVV / IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / IGS Westlede 1394 leftover crematorium IGS live NBB WVV / HAVICREM 1393 leftover crematorium IGS live NBB WVV / IVLA 1392 leftover waste IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; skip already-mined IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1398 after IGS IBEG leftover energy holding IGS live NBB WVV; next residual dual L5 VL",
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
if not last_text.startswith("rq_1398,"):
    raise SystemExit("last rq line is not rq_1398: %s" % last_text[:160])
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
if b"rq_1399" in tail:
    raise SystemExit("spawn id already in tail")
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("research_queue patched rq_1398 done + spawned rq_1399; new_size", path.stat().st_size)
# verify
with path.open("rb") as f:
    f.seek(0, 2)
    size = f.tell()
    f.seek(max(0, size-400))
    print(f.read().decode("utf-8")[-200:])
