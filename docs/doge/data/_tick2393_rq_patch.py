#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2393_stamp.txt").read_text().strip().splitlines()[0]
GAP = "gap_zonnebloem_vaph_mfc_matrix_bruto_4_58m_omzet73_empty_pnl_drop_destin_empty_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
rq_text = rq_raw.decode("utf-8")
new_2393 = (
    "rq_2393,leftover dual — Zonnebloem Kortrijk YE2025 Strong (bruto JUMP 4.58m / omzet+73 empty / pnl DROP 183k / destin empty),"
    "hole_fill,8,done,L5,vzw_zonnebloem,"
    "Tick 2393 leftover after CAR Houtland-Westkust. Took Zonnebloem 0421.039.386 deposit 2026-00254348 leftover city_kortrijk. "
    "Do NOT redo Zonnebloem/CAR Houtland/De Schans/LDSST/BW Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart/STV Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Drongen stack. "
    "Kohesi family exhausted. CAR Overleie YE2024 skip. Ben and Ten Anker already in entities skip.,"
    f"{GAP},2026-08-25T00:59:44Z,{STAMP},"
    "tick2393 Zonnebloem 0421.039.386 YE2025 Strong official native PDF 2026-00254348; bruto9900 JUMP 4579601 VAPH envelope; omzet70+73 empty; pnl DROP 182958; equity JUMP 2994675; FTE 60.8; kapitaalsubsidies DROP 711539; destin691 empty; cash JUMP 983179; FOI ready NOT sent; leftover city_kortrijk after Houtland@2392\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2393,"):
        parts.append(new_2393)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2393 replace count {replaced}")
new_rq = "".join(parts)
new_2394 = (
    "rq_2394,leftover dual after Zonnebloem — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Zonnebloem YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf (NOT Zonnebloem 0421.039.386; NOT CAR Houtland 0408.436.019; NOT Kohesi family; NOT Kloosterstraat 6; NOT Ten Anker). "
    "CAR Overleie YE2024 skip. Ben already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 — re-HEAD only. Next every-10 is 2400.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2393; Zonnebloem taken leftover city_kortrijk after Houtland; next every-10 2400\n"
)
rq_path.write_bytes((new_rq + new_2394).encode("utf-8"))
print("patched rq bytes", rq_path.stat().st_size)
