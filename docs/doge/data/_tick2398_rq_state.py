#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2398_stamp.txt").read_text().strip().splitlines()[0]
GAP = "gap_halleasse_riziv_vl_vaph_matrix_bruto_2_34m_omzet73_empty_pnl_jump_destin_505k_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2398,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2398 line, found {n}")
if "rq_2399," in rq_text:
    raise SystemExit("rq_2399 already exists")
print("precheck ok", STAMP, n)

new_2398 = (
    "rq_2398,leftover dual — CAR Halle Asse YE2025 Strong (bruto JUMP 2.34m / omzet+73 empty / pnl JUMP 256k / destin 505k),"
    "hole_fill,8,done,L5,vzw_car_halle_asse,"
    "Tick 2398 leftover after Waas Revalidatiecentrum. Took CAR Halle Asse 0425.788.230 deposit 2026-00364866 leftover city_halle + leftover city_asse. "
    "Do NOT redo CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/BW Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart/STV Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Drongen stack. "
    "Kohesi family exhausted. CAR Overleie YE2024 skip. Ben and Ten Anker already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN still 403.,"
    f"{GAP},2026-08-25T01:39:08Z,{STAMP},"
    "tick2398 CAR Halle Asse 0425.788.230 YE2025 Strong official native PDF 2026-00364866; omzet70 empty VKT; 73 empty VKT; bruto9900 JUMP 2343257 CAR envelope; pnl JUMP 255548; equity JUMP 2180458; assets JUMP 3012006; debt DROP 831548; FTE 28; kapitaalsubsidies DROP 725722; destin691 JUMP 505074 bouwfonds; cash JUMP 1268818; FOI ready NOT sent; leftover city_halle after Waas@2397\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2398,"):
        parts.append(new_2398)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2398 replace count {replaced}")
new_rq = "".join(parts)
new_2399 = (
    "rq_2399,leftover dual after CAR Halle Asse — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR Halle Asse YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf (NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland 0408.436.019; NOT Kohesi family; NOT Kloosterstraat 6; NOT Ten Anker). "
    "CAR Overleie YE2024 skip. Ben already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 — re-HEAD only. "
    "NOW LIVE 2026pdf leftover: Heuvelheem 0413.210.201 leftover city_kruisem 2026-00243798 740k. Related unused Vriendenkring 0436.787.139 leftover city_halle only if live 2026pdf. Next every-10 is 2400 — tick 2400 MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2398; CAR Halle Asse taken leftover city_halle after Waas; next every-10 2400 MUST refresh\n"
)
rq_path.write_bytes((new_rq + new_2399).encode("utf-8"))
print("patched rq bytes", rq_path.stat().st_size)
