# tick 600 — progress milestone + dual research wave synthesis
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T15:45:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


payload = {
    "imec_op_m": 1216.9,
    "vib_op_m": 168.8,
    "vito_m": 297.1,
    "fm_rev_m": 37.3,
    "ilvo_iva_m": 24.9,
    "ilvo_ev_m": 50.3,
    "craw_dep_m": 54.8,
    "vliz_m": 19.6,
    "issep_m": 34.8,
    "note": "Dual research wave 591-599 SOC agri marine env",
}

with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_dual_research_wave_tick600,Dual Flanders research wave SOC agri marine env 591-599,'
        f'gg_belgium,Flanders Wallonia public research dual,ticks591-599 primary synthesis,'
        f'2024-01-01,2024,2025,0,"{esc_json(payload)}",0,active,,'
        f'Map dual public research stack,FOI VL grant L5 residual,'
        f'src_dual_soc_fm_imec_vib_vito_tick596,strong,BE>dual>research_wave_600,'
        f'tick600 progress synthesis\n'
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "lb_dual_research_wave_600,Dual public research wave SOC agri marine env tick600,"
        "multi,ops,BE>dual>research_wave_600,1216899528,75200000,"
        "Strong synthesis 591-599: imec 1.22bn VIB 169m VITO 297m FM 37m ILVO 25+50 "
        "CRA-W 55 VLIZ 20 ISSeP 35 dual maps,strong,src_dual_soc_fm_imec_vib_vito_tick596,"
        "Public RTO ecosystem,Map dual research centres stack,VL grant L5 residual multi-entity,"
        "4,8.5,5,6.35,FOI dual grant matrix research wave,seed,,tick600\n"
    )

# FOI optional synthesis gap - ready draft for dual grant matrix residual
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_dual_research_grant_matrix_l5,BE>dual>research_wave>vl_wal_grant_matrix,gg_belgium,"
        "Multi-entity VL/WAL structural grant L5 matrix recon for imec VIB VITO FM ILVO CRA-W VLIZ ISSeP;"
        " unit-cost EUR/VTE dual table; absolute ILVO total werkingsmiddelen,"
        "Primary entity fills strong tick591-599; matrix recon residual,5,"
        "Vlaanderen WEWIS / SPW Agriculture / openbaarheid,,,,"
        "docs/doge/foi/drafts/gap_dual_research_grant_matrix_l5.md,ready,2026-07-31,,,,"
        "cmt_dual_research_wave_tick600,lb_dual_research_wave_600,"
        f"{utc},{utc},tick600 progress dual research wave; human send matrix FOI\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_591,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:30:00Z,,Spawned tick599 after VLIZ dual marine; rq_116 deferred; progress@600 NEXT TICK"
)
new = (
    "rq_591,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:30:00Z,2026-07-31T15:45:00Z,"
    "tick600: progress@600 + dual research wave synthesis SOC agri marine; spawn rq_592; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_591 not found:\n" + repr(text[-400:]))
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_592,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:45:00Z,,Spawned tick600 after progress dual research wave; rq_116 deferred; progress@610 in 10\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_591,600,no,"
    "tick600 progress@600 dual research wave SOC agri marine; next rq_592; progress@610 in 10; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick600 CSV writes OK")
