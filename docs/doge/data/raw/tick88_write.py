from pathlib import Path

root = Path("docs/doge/data")

# sources
src = root / "sources.csv"
t = src.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "src_tick88_swa_recheck_negative" not in t:
    t += (
        "src_tick88_swa_recheck_negative,"
        "Tick88 multi-parliament SWA assent search negative Jul 2026,"
        "https://www.vlaanderen.be/vlaamse-regering/beslissingen-van-de-vlaamse-regering/samenwerkingsakkoord-economische-governance,"
        "DOGE loop research,2026-07-22,secondary,"
        '"No final plenary assent any parliament; VL page still first-read path; Kamer 56K1569 is fallback wetsvoorstel not SWA assent; no BS"\n'
        "src_kamer_56k1569_fallback,"
        "Kamer 56K1569 wetsvoorstel terugvalregeling interfederale begrotingscoordinatie,"
        "https://www.lachambre.be/kvvcr/showpage.cfm?section=/flwb&language=nl&cfm=/site/wwwcfm/flwb/flwbn.cfm?lang=N&legislat=56&dossierID=1569,"
        "Kamer van volksvertegenwoordigers,2026-07-22,parliament,"
        '"Private member bill Bertrand/Vander Elst 22 May 2026; pending Finance commission; NOT assent law for Mar 2026 SWA"\n'
        "src_vl_swa_page_recheck_tick88,"
        "Vlaamse Regering SWA economische governance page recheck tick88,"
        "https://www.vlaanderen.be/vlaamse-regering/beslissingen-van-de-vlaamse-regering/samenwerkingsakkoord-economische-governance,"
        "Vlaamse Overheid,2026-07-22,portal,"
        '"Unchanged: Overleg 27 Mar; VL principieel 8 May; SERV+RvS path; no plenaire adoptie"\n'
    )
    src.write_text(t, encoding="utf-8")
    print("sources ok")
else:
    print("sources exist")

# research queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_084,SWA multi-parliament final assent recheck Q3,continuous,2,open,L0,gg_belgium,"Fourth recheck final assent laws/decrees BS dates for Mar 2026 economic-governance SWA; only if not found earlier.",,2026-07-22T13:05:00Z,2026-07-22T13:05:00Z,"After tick84 negative; low prio"',
    'rq_084,SWA multi-parliament final assent recheck Q3,continuous,2,done,L0,gg_belgium,"Fourth recheck final assent laws/decrees BS dates for Mar 2026 economic-governance SWA; only if not found earlier.",,2026-07-22T13:05:00Z,2026-07-22T14:19:00Z,"Still none; Kamer 56K1569 fallback bill pending only; VL/WAL/FWB/fed still first-read+SERV max; BRU missing; BS none"',
)
if "rq_088," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += (
        'rq_088,West-Vlaanderen bezoldigingen/personeel 2026 from T2,continuous,3,open,L1,prov_west_vlaanderen,"Extract WVL bezoldigingen and key exp rubrics 2026 from Schema T2 p30 (parallel OVL personnel); no invent euros.",,2026-07-22T14:19:00Z,2026-07-22T14:19:00Z,"T2 p30 image has bezoldigingen line; tick87 saw table"\n'
        'rq_089,SWA multi-parliament final assent recheck Q4,continuous,1,open,L0,gg_belgium,"Fifth recheck final assent laws/decrees BS for Mar 2026 SWA; only if not found; low intensity.",,2026-07-22T14:19:00Z,2026-07-22T14:19:00Z,"After tick88 still negative; deprioritise until autumn"\n'
    )
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# commitments - update parliament_final_vote note
cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
ct2 = ct.replace(
    '""parliament_final_vote"":""none_found_2026-07-22_tick84""',
    '""parliament_final_vote"":""none_found_2026-07-22_tick88"",""kamer_fallback_bill"":""56K1569_pending""',
)
# also update trailing note if present
ct2 = ct2.replace(
    "tick84 recheck: still no final Kamer/VL/WAL/F",
    "tick88 recheck: still no final Kamer/VL/WAL/F",
)
if ct2 != ct:
    cmt.write_text(ct2, encoding="utf-8")
    print("cmt ok")
else:
    # try looser replace on the long notes field
    import re
    m = re.search(r"cmt_entity_mtfsp_split,[^\n]+", ct)
    if m:
        line = m.group(0)
        newline = line
        if "tick88" not in line:
            newline = line.replace("tick84", "tick88")
            if "none_found_2026-07-22_tick84" in newline:
                newline = newline.replace(
                    "none_found_2026-07-22_tick84",
                    "none_found_2026-07-22_tick88",
                )
            elif "parliament_final_vote" in newline and "tick88" not in newline:
                newline = newline.replace(
                    "parliament_final_vote",
                    "kamer_fallback_56K1569:pending,parliament_final_vote",
                )
            ct = ct.replace(line, newline)
            cmt.write_text(ct, encoding="utf-8")
            print("cmt regex ok")
        else:
            print("cmt already tick88")
    else:
        print("cmt not found")

# leaderboard
lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
lt2 = lt.replace(
    "FINAL multi-parliament assent STILL NONE as of 2026-07-22 tick84; Brussels missing",
    "FINAL multi-parliament assent STILL NONE as of 2026-07-22 tick88; Kamer 56K1569 fallback pending; Brussels missing",
)
lt2 = lt2.replace("tick71 recheck negative; coordination soft until final votes", "tick88 recheck negative; coordination soft until final votes")
if lt2 != lt:
    lb.write_text(lt2, encoding="utf-8")
    print("lb ok")
else:
    print("lb no change")

# loop state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T14:19:00Z,rq_084,88,no,"SWA still no final votes (tick88). Next: rq_088 WVL personeel T2."\n',
    encoding="utf-8",
)
print("state ok")

# log
log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T14:19:00Z -- tick 88
- Unit: rq_084 (SWA multi-parliament final assent recheck Q3)
- Found (strong process; **still no final votes**): Reconfirmed Overlegcomite **27 Mar 2026** SWA and VL Regering page **8 May 2026** still at **principiele goedkeuring** voorontwerp instemmingsdecreet -> SERV/RvS (page unchanged). SERV advice **1 Jun** / VL ingekomen **17 Jun** path unchanged. Federal MR draft **13 May** path unchanged. **New related signal:** Kamer dossier **56K1569** (Bertrand/Vander Elst, filed **22 May 2026**, inoverweging **4 Jun**) is a private-member **wetsvoorstel** for a statutory **terugvalregeling** interfederal budget coordination - **pending** Finance commission; **not** the SWA assent law and **not** adopted. Wallonie/FWB still max first-read class; Brussels assent dossier **not found**. **No** plenary-adopted assent law/decree and **no** Belgisch Staatsblad publication for the Mar 2026 SWA as of **2026-07-22**.
- Wrote: 3 sources; updated cmt_entity_mtfsp_split + lb_entity_split_opacity; rq_084=done; seeded **rq_088** WVL personeel T2 + **rq_089** SWA Q4 low-prio; ticks=88
- FOI: none
- Next: **rq_088** West-Vlaanderen bezoldigingen/personeel T2 (prio 3)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 88" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")
