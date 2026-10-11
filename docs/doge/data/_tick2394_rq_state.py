#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP = (DATA / "_tick2394_stamp.txt").read_text().strip().splitlines()[0]
GAP = "gap_zwz_zorgkas_riziv_wzc_matrix_omzet_10_69m_73_1_97m_pnl_drop_destin_empty_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2394,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2394 line, found {n}")
if "rq_2395," in rq_text:
    raise SystemExit("rq_2395 already exists")
print("precheck ok", STAMP, n)

new_2394 = (
    "rq_2394,leftover dual — ZWZ Zedelgem YE2025 Strong (omzet JUMP 10.69m / 73 1.97m / pnl DROP 45k / destin empty),"
    "hole_fill,8,done,L5,vzw_zwz,"
    "Tick 2394 leftover after Zonnebloem. Took ZWZ 0832.024.923 deposit 2026-00228427 leftover city_zedelgem. "
    "Do NOT redo ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/BW Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart/STV Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Drongen stack. "
    "Kohesi family exhausted. CAR Overleie YE2024 skip. Ben and Ten Anker already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN still 403.,"
    f"{GAP},2026-08-25T01:13:24Z,{STAMP},"
    "tick2394 ZWZ 0832.024.923 YE2025 Strong official native PDF 2026-00228427; omzet70 JUMP 10693272 WZC envelope; 73 JUMP 1971245; 70/76A JUMP 13006495; pnl DROP 45054; equity DROP 12902648; assets JUMP 33038468; debt JUMP 20135821; FTE 120.2; kapitaalsubsidies DROP 5917611; destin691 empty; cash DROP 4229666; FOI ready NOT sent; leftover city_zedelgem after Zonnebloem@2393\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2394,"):
        parts.append(new_2394)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2394 replace count {replaced}")
new_rq = "".join(parts)
new_2395 = (
    "rq_2395,leftover dual after ZWZ — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After ZWZ YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf (NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland 0408.436.019; NOT Kohesi family; NOT Kloosterstraat 6; NOT Ten Anker). "
    "CAR Overleie YE2024 skip. Ben already in entities skip. CAR Antenne 3000 leftover city_leuven NBB 2026-00375503 CDN 403 — re-HEAD only. "
    "NOW LIVE 2026pdf leftovers: CAR Horizon 0418.529.759 leftover city_geraardsbergen 2026-00268911 44k; CAR Accent 0413.208.122 leftover city_kortrijk 2026-00215981 48k; CAR Halle Asse 0425.788.230 leftover city_halle 2026-00364866 50k; Waas Revalidatiecentrum 0415.472.279 leftover city_lokeren 2026-00243160 49k; Heuvelheem 0413.210.201 leftover city_kruisem 2026-00243798 740k. Next every-10 is 2400.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2394; ZWZ taken leftover city_zedelgem after Zonnebloem; next every-10 2400\n"
)
rq_path.write_bytes((new_rq + new_2395).encode("utf-8"))
print("patched rq bytes", rq_path.stat().st_size)
