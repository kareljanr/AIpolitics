# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
path = Path("/workspace/AIpolitics/docs/doge/data/research_queue.csv")
UTC = "2026-08-19T06:15:00Z"
ENT = "igs_dds"
GAP = "gap_dds_othops_5_22m_inv_12_79m_prov_7_85m_l5"
header = path.open(encoding="utf-8").readline()
fields = next(csv.reader([header.strip("\n").strip("\r")]))

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

rq_new = {
    "task_id": "rq_1402",
    "title": "DDS JR2025 leftover dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": "Completed: DDS leftover streek IGS dienstverlenende vereniging of mined Oost-Vlaanderen municipalities Berlare+Buggenhout+Dendermonde+Hamme+Lebbeke+Wetteren+Wichelen+Zele after leftover AGB/IGS hunt; KBO 0207.087.872 Actief; live JR2025 official NBB WVV VOL-kap PDF (2117343 bytes 45p deposit 2026-00188846; commissaris Dominique Vaes A01898; fee unpublished image-only); sourced euros assets 48501395 omzet 1262519 othops 5219038 diensten 1359141 pers 3875923 inventory 12793375 voorzieningen 7847265 pnl -287310 equity 38109541 cash 5533236 capex 789825; FOI ready othops 5.22m / inventory 12.79m / voorzieningen 7.85m / commissaris fee unpublished / vennoten share unpublished",
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-19T05:50:00Z",
    "updated_utc": UTC,
    "notes": "tick1402 DDS leftover streek IGS residual; KBO 0207.087.872; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1403 residual dual L5 VL",
}
rq_spawn = {
    "task_id": "rq_1403",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1402 done including DDS 1402 leftover streek IGS live NBB WVV / OVCO 1401 leftover crematorium IGS live NBB WVV / IGL 1400 leftover zorg IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IGO Holsbeek 0862.962.775 last JR still 2024 — take only if a JR2025 PDF now downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; skip already-mined DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; IGO still 2024; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403",
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1402 after DDS leftover streek IGS live NBB WVV; next residual dual L5 VL",
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
if not last_text.startswith("rq_1402,"):
    raise SystemExit("last rq line is not rq_1402: %s" % last_text[:160])
last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
if b"rq_1403" in tail:
    raise SystemExit("spawn id already in tail")
payload = (csv_line(fields, rq_new) + "\n" + csv_line(fields, rq_spawn) + "\n").encode("utf-8")
with path.open("r+b") as f:
    f.seek(last_start)
    f.truncate()
    f.write(payload)
print("research_queue patched rq_1402 done + spawned rq_1403; new_size", path.stat().st_size)
