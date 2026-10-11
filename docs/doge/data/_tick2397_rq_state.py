#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2397_stamp.txt").read_text().strip().splitlines()[0]
GAP = "gap_waas_riziv_vl_vaph_matrix_bruto_1_64m_omzet73_empty_pnl_drop_3k_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2397,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2397 line, found {n}")
if "rq_2398," in rq_text:
    raise SystemExit("rq_2398 already exists")
print("precheck ok", STAMP, n)

new_2397 = (
    "rq_2397,leftover dual — Waas Revalidatiecentrum Lokeren YE2025 Strong (bruto 1.64m / omzet+73 empty / pnl DROP 3k / destin empty),"
    "hole_fill,8,done,L5,vzw_car_waas,"
    "Tick 2397 leftover after CAR Accent. Took Waas Revalidatiecentrum 0415.472.279 deposit 2026-00243160 leftover city_lokeren. "
    "Do NOT redo Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/BW Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart/STV Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Drongen stack. "
    "Kohesi family exhausted. CAR Overleie YE2024 skip. Ben and Ten Anker already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN still 403.,"
    f"{GAP},2026-08-25T01:33:04Z,{STAMP},"
    "tick2397 Waas Revalidatiecentrum 0415.472.279 YE2025 Strong official native PDF 2026-00243160; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 1636836 CAR envelope; pnl DROP 3351; equity DROP 1550659; assets DROP 1801270; debt JUMP 250611; FTE 21.1; kapitaalsubsidies DROP 269052; destin691 empty; cash DROP 376211; FOI ready NOT sent; leftover city_lokeren after CAR Accent@2396\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2397,"):
        parts.append(new_2397)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2397 replace count {replaced}")
new_rq = "".join(parts)
new_2398 = (
    "rq_2398,leftover dual after Waas Revalidatiecentrum — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Waas Revalidatiecentrum YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf (NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland 0408.436.019; NOT Kohesi family; NOT Kloosterstraat 6; NOT Ten Anker). "
    "CAR Overleie YE2024 skip. Ben already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 — re-HEAD only. "
    "NOW LIVE 2026pdf leftovers: CAR Halle Asse 0425.788.230 leftover city_halle 2026-00364866 50k; Heuvelheem 0413.210.201 leftover city_kruisem 2026-00243798 740k. Prefer smaller native. Next every-10 is 2400.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2397; Waas taken leftover city_lokeren after CAR Accent; next every-10 2400\n"
)
rq_path.write_bytes((new_rq + new_2398).encode("utf-8"))
print("patched rq bytes", rq_path.stat().st_size)
