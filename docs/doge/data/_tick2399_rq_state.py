#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2399_stamp.txt").read_text().strip().splitlines()[0]
GAP = "gap_heuvelheem_vaph_matrix_opbr_15_17m_73_12_22m_pnl_flip_destin_empty_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2399,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2399 line, found {n}")
if "rq_2400," in rq_text:
    raise SystemExit("rq_2400 already exists")
print("precheck ok", STAMP, n)

new_2399 = (
    "rq_2399,leftover dual — Heuvelheem YE2025 Strong (opbr JUMP 15.17m / 73 12.22m / pnl PROFIT FLIP 405k / destin empty),"
    "hole_fill,8,done,L5,vzw_heuvelheem,"
    "Tick 2399 leftover after CAR Halle Asse. Took Heuvelheem 0413.210.201 deposit 2026-00243798 leftover city_kruisem + leftover city_oudenaarde. "
    "Do NOT redo Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/BW Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart/STV Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Drongen stack. "
    "Kohesi family exhausted. CAR Overleie YE2024 skip. Ben and Ten Anker already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 re-HEAD only.,"
    f"{GAP},2026-08-25T01:43:47Z,{STAMP},"
    "tick2399 Heuvelheem 0413.210.201 YE2025 Strong official native PDF 2026-00243798; omzet70 JUMP 181042 commercial-only; 73 JUMP 12221891; opbr7076A JUMP 15172213 VAPH envelope; pnl PROFIT FLIP 404772; equity JUMP 7254780; assets JUMP 10879683; debt JUMP 3267730; FTE 152.3; kapitaalsubsidies DROP 942213; destin691 empty; cash DROP 772792; FOI ready NOT sent; leftover city_kruisem after Halle Asse@2398\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2399,"):
        parts.append(new_2399)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2399 replace count {replaced}")
new_rq = "".join(parts)
new_2400 = (
    "rq_2400,EVERY-10 + leftover dual after Heuvelheem — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "EVERY-10 tick 2400: MUST refresh docs/doge/data/progress_every_10_ticks.md + docs/doge/data/doge_waste_top10_current.md from live CSVs then leftover unit. "
    "After Heuvelheem YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf (NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland 0408.436.019; NOT Kohesi family; NOT Kloosterstraat 6; NOT Ten Anker; NOT Vijvens). "
    "CAR Overleie YE2024 skip. Ben already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 — re-HEAD only. "
    "Related unused Vriendenkring 0436.787.139 leftover city_halle only if live 2026pdf.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2399; Heuvelheem taken leftover city_kruisem after Halle Asse; EVERY-10 MUST refresh progress + waste top10\n"
)
rq_path.write_bytes((new_rq + new_2400).encode("utf-8"))
print("patched rq bytes", rq_path.stat().st_size)
