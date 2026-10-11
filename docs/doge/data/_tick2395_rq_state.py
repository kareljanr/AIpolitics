#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2395_stamp.txt").read_text().strip().splitlines()[0]
GAP = "gap_horizon_riziv_vl_vaph_matrix_omzet_3_00m_73_464k_pnl_drop_destin_246k_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2395,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2395 line, found {n}")
if "rq_2396," in rq_text:
    raise SystemExit("rq_2396 already exists")
print("precheck ok", STAMP, n)

new_2395 = (
    "rq_2395,leftover dual — CAR Horizon Geraardsbergen YE2025 Strong (omzet DROP 3.00m / 73 464k / pnl DROP 246k / destin 246k),"
    "hole_fill,8,done,L5,vzw_car_horizon,"
    "Tick 2395 leftover after ZWZ. Took CAR Horizon 0418.529.759 deposit 2026-00268911 leftover city_geraardsbergen. "
    "Do NOT redo CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/BW Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart/STV Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Drongen stack. "
    "Kohesi family exhausted. CAR Overleie YE2024 skip. Ben and Ten Anker already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN still 403.,"
    f"{GAP},2026-08-25T01:23:46Z,{STAMP},"
    "tick2395 CAR Horizon 0418.529.759 YE2025 Strong official native PDF 2026-00268911; omzet70 DROP 3001208 CAR envelope; 73 JUMP 464125; bruto9900 DROP 2680880; pnl DROP 246289; equity JUMP 2542581; assets JUMP 2952629; debt DROP 410048; FTE 35; kapitaalsubsidies FLAT 131925; destin691 DROP 246289; cash DROP 958792; FOI ready NOT sent; leftover city_geraardsbergen after ZWZ@2394\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2395,"):
        parts.append(new_2395)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2395 replace count {replaced}")
new_rq = "".join(parts)
new_2396 = (
    "rq_2396,leftover dual after CAR Horizon — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR Horizon YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf (NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland 0408.436.019; NOT Kohesi family; NOT Kloosterstraat 6; NOT Ten Anker). "
    "CAR Overleie YE2024 skip. Ben already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 — re-HEAD only. "
    "NOW LIVE 2026pdf leftovers: CAR Accent 0413.208.122 leftover city_kortrijk 2026-00215981 48k; CAR Halle Asse 0425.788.230 leftover city_halle 2026-00364866 50k; Waas Revalidatiecentrum 0415.472.279 leftover city_lokeren 2026-00243160 49k; Heuvelheem 0413.210.201 leftover city_kruisem 2026-00243798 740k. Next every-10 is 2400.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2395; CAR Horizon taken leftover city_geraardsbergen after ZWZ; next every-10 2400\n"
)
rq_path.write_bytes((new_rq + new_2396).encode("utf-8"))
print("patched rq bytes", rq_path.stat().st_size)
