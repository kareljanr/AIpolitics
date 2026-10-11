#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
STAMP, DAY = (DATA / "_tick2393_stamp.txt").read_text().strip().splitlines()
GAP = "gap_zonnebloem_vaph_mfc_matrix_bruto_4_58m_omzet73_empty_pnl_drop_destin_empty_l5"
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2393,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2393 line, found {n}")
if "rq_2394," in rq_text:
    raise SystemExit("rq_2394 already exists")
print("precheck ok", STAMP, n)
