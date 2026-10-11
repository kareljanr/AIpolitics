# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
path = Path("/workspace/AIpolitics/docs/doge/data/research_queue.csv")
UTC = "2026-08-19T07:10:00Z"
ENT = "agb_tlt"
GAP = "gap_tlt_omzet_empty_lease_9_30m_debt_11_90m_l5"
header = path.open(encoding="utf-8").readline()
fields = next(csv.reader([header.strip("\n").strip("\r")]))

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

rq_new = {
    "task_id": "rq_1405",
    "title": "AGB Tielt JR2025 leftover dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: AGB Tielt leftover AGB sport+monumenten of mined city Tielt after leftover AGB hunt; KBO 0841.231.312 Actief; live JR2025 official NBB WVV VKT-kap PDF (61089 bytes 19p deposit 2026-00316168; no commissarisverslag filed); sourced euros assets 19953810 brutomarge 679356 debt 11899035 lease 9303045 pnl 321320 equity 5586840 cash 1132461 capex 388010 dividend 160660; FOI ready omzet empty / diensten unpublished / pers empty / lease 9.30m / commissaris unpublished",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-19T06:50:00Z",
    "updated_utc": UTC,
    "notes": "tick1405 AGB Tielt leftover AGB residual; KBO 0841.231.312; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1406 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1406",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1405 done including AGB Tielt 1405 leftover AGB live NBB WVV / Psilon 1404 leftover crematorium IGS live NBB WVV / VERKO 1403 leftover waste IGS live NBB WVV / DDS 1402 leftover streek IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IGO Holsbeek 0862.962.775 last JR still 2024 — take only if a JR2025 PDF now downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; skip already-mined AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; IGO still 2024; AGB Lille liquidation; Aarschot/Dendermonde/VESPA still 2024; AGB Genk JR2025 live but already mined; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1405 after AGB Tielt leftover AGB live NBB WVV; next residual dual L5 VL",
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
if not last_text.startswith("rq_1405,"):
    raise SystemExit("last rq line is not rq_1405: %s" % last_text[:160])
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
if b"rq_1406" in tail:
    raise SystemExit("spawn id already in tail")
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("research_queue patched rq_1405 done + spawned rq_1406; new_size", path.stat().st_size)
