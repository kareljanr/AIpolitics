# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
UTC = "2026-08-19T05:15:00Z"
ENT = "igs_ivbc"
GAP = "gap_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m_l5"

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
if tail.endswith(b"\n"):
    search = tail[:-1]
else:
    search = tail
last_nl = search.rfind(b"\n")
last_line = search[last_nl + 1 :] if last_nl != -1 else search
last_text = last_line.decode("utf-8")
if not last_text.startswith("rq_1397,"):
    raise SystemExit("last rq line is not rq_1397: %s" % last_text[:160])
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
if b"rq_1398" in tail:
    raise SystemExit("spawn id already in tail")
rq_new = {
    "task_id": "rq_1397",
    "title": "IGS IVEBICA JR2025 leftover dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: IGS IVEBICA leftover IGS library/culture/academy of Hemiksem+Schelle+Niel after honest hunt; KBO 0280.300.997 Actief; live JR2025 official NBB WVV VKT-inb PDF (1.55MB 35p deposit 2026-00160301; commissaris Clybouw getrouw beeld); sourced euros assets 919753 / omzet empty-form/207858-jv / diensten empty-form / pers 1023843 / debt 338424 / pnl 60844 / capex 42867 / othinc 1382095; FOI ready omzet empty / 1.38m toelagen / 1.02m pers / 137k collectie",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-19T04:55:00Z",
    "updated_utc": UTC,
    "notes": "tick1397 IGS IVEBICA leftover IGS library/culture/academy residual; KBO 0280.300.997; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1398 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1398",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1397 done including IGS IVEBICA 1397 leftover library/culture/academy IGS live NBB WVV / IGS Pontes 1396 leftover crematorium IGS live NBB WVV / IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / IGS Westlede 1394 leftover crematorium IGS live NBB WVV / HAVICREM 1393 leftover crematorium IGS live NBB WVV / IVLA 1392 leftover waste IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; skip already-mined IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1397 after IGS IVEBICA leftover library/culture/academy IGS live NBB WVV; next residual dual L5 VL",
}
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("research_queue 1397 patched spawned_1398")
