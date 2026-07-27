# tick231: Mons CPAS BI2026 + zone secours + city intervention primary fills
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# Strong: conseil communal 22 Dec 2025 CPAS budget + 24 Mar 2026 zone secours
CPAS_ORD_REC = 149152051.00
CPAS_ORD_DEP = 149130634.23
CPAS_ORD_BONI = 21416.77
CPAS_GLOB = 149388888.90
CPAS_EXTRA_GLOB = 7305500.00
CITY_INTERV = 27917996.41
CITY_INTERV_FONCT = 25141366.41
CITY_INTERV_RESP = 2501000.00
CITY_INTERV_PCS = 275630.00
ZONE_SECOURS = 2604469.70
ZONE_PROV_BI = 2815615.53  # provisional in city BI before MB1
HOUSING_84 = 2680000.00  # NPG medium UREBA/PIVW invest

# --- sources ---
src = data / "sources.csv"
src_add = (
    "src_mons_cpas_budget_2026,Mons CPAS budget 2026 conseil communal approval,"
    "https://www.deliberations.be/mons/decisions/22-decembre-2025-16-30/gf-df-budget-cpas-budget-2026,"
    "Ville de Mons conseil communal 22 Dec 2025,2026-07-29,official_decision,"
    f'"CPAS ord dep {CPAS_ORD_DEP:.2f} rec {CPAS_ORD_REC:.2f} global {CPAS_GLOB:.2f}; '
    f'city intervention {CITY_INTERV:.2f} (fonct {CITY_INTERV_FONCT:.2f} + resp {CITY_INTERV_RESP:.0f} + PCS {CITY_INTERV_PCS:.0f}); '
    f'extra global {CPAS_EXTRA_GLOB:.0f}; tick231"\n'
    "src_mons_zone_secours_2026,Mons city dotation Zone de Secours Hainaut-Centre 2026,"
    "https://www.deliberations.be/mons/decisions/24-mars-2026-17-00/gf-df-budget-dotation-2026-de-la-ville-de-mons-a-la-zone-de-secours-hainaut-centre,"
    "Ville de Mons conseil communal 24 Mar 2026,2026-07-29,official_decision,"
    f'"Dotation 2026 {ZONE_SECOURS:.2f} (vs provisional BI 2025-aligned {ZONE_PROV_BI:.2f}); tick231"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_mons_cpas_budget_2026" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_mons_cpas_ord_dep_2026,city_mons,2026,{CPAS_ORD_DEP},,,budgeted,src_mons_cpas_budget_2026,strong,Mons CPAS ordinaire depenses exercice propre 149.131m 2026",
    f"bud_mons_cpas_ord_rec_2026,city_mons,2026,{CPAS_ORD_REC},,,budgeted,src_mons_cpas_budget_2026,strong,Mons CPAS ordinaire recettes exercice propre 149.152m 2026",
    f"bud_mons_cpas_global_2026,city_mons,2026,{CPAS_GLOB},,,budgeted,src_mons_cpas_budget_2026,strong,Mons CPAS recettes/depenses globales 149.389m 2026 (balanced)",
    f"bud_mons_cpas_extra_global_2026,city_mons,2026,{CPAS_EXTRA_GLOB},,,budgeted,src_mons_cpas_budget_2026,strong,Mons CPAS extraordinaire global 7.306m 2026",
    f"bud_mons_city_cpas_intervention_2026,city_mons,2026,{CITY_INTERV},,,budgeted,src_mons_cpas_budget_2026,strong,Ville Mons intervention communale CPAS 27.918m 2026",
    f"bud_mons_city_cpas_fonct_2026,city_mons,2026,{CITY_INTERV_FONCT},,,budgeted,src_mons_cpas_budget_2026,strong,CPAS intervention fonctionnement 25.141m 2026",
    f"bud_mons_city_cpas_resp_2026,city_mons,2026,{CITY_INTERV_RESP},,,budgeted,src_mons_cpas_budget_2026,strong,CPAS intervention exceptionnelle responsabilisation 2.501m 2026",
    f"bud_mons_zone_secours_2026,city_mons,2026,{ZONE_SECOURS},,,budgeted,src_mons_zone_secours_2026,strong,Ville Mons dotation Zone Secours Hainaut-Centre 2.604m 2026",
    f"bud_mons_cpas_housing_ureba_2026,city_mons,2026,{HOUSING_84},,,budgeted,src_mons_cpas_budget_2026,medium,CPAS renovation energetique 84 logements 2.68m UREBA/PIVW (NPG class)",
]
text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_mons_cpas_ord_dep_2026" not in text:
    bud.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")
    print("budgets ok", len(rows))
else:
    print("budgets already")

# --- commitments ---
cmt = data / "commitments.csv"
raw = cmt.read_bytes()
if b"\x97" in raw:
    cmt.write_bytes(raw.replace(b"\x97", "\u2013".encode("utf-8")))

cmt_add = (
    "cmt_mons_cpas_2026,Mons CPAS BI2026 full package + city intervention,"
    "city_mons,CPAS de Mons,Conseil communal 22 Dec 2025 + CAS 8 Dec 2025,"
    "2025-12-08,2026,2026,149388888.90,"
    '"{""cpas_ord_dep"":149130634.23,""cpas_ord_rec"":149152051.00,""cpas_ord_boni"":21416.77,'
    '""cpas_global"":149388888.90,""cpas_extra_global"":7305500.00,'
    '""city_intervention"":27917996.41,""city_fonct"":25141366.41,""city_resp"":2501000.00,'
    '""city_pcs"":275630.00,""art60_posts_2026"":380,""art61_posts_2026"":140,'
    '""note"":""Strong deliberations; city full BI2026 PDF still not on mons.be (FOI residual L5 table); core social duty""}",'
    "0,active,https://www.deliberations.be/mons/decisions/22-decembre-2025-16-30/gf-df-budget-cpas-budget-2026,"
    "Public social assistance Mons CPAS,Publish full city BI2026 PDF ASBL L5; dual federal RIS path,"
    "src_mons_cpas_budget_2026,strong,Mons>CPAS,tick231\n"
    "cmt_mons_zone_secours_2026,Mons city fire/rescue zone dotation 2026,"
    "city_mons,Zone de Secours Hainaut-Centre,Conseil communal 24 Mar 2026,"
    "2026-02-20,2026,2026,2604469.70,"
    '"{""dotation_2026"":2604469.70,""provisional_bi_2025_aligned"":2815615.53,'
    '""delta"":-211145.83,""note"":""Strong; MB1 will reduce credit from provisional 2.816m to 2.604m""}",'
    "0,active,https://www.deliberations.be/mons/decisions/24-mars-2026-17-00/gf-df-budget-dotation-2026-de-la-ville-de-mons-a-la-zone-de-secours-hainaut-centre,"
    "Municipal fire rescue zone financing,Publish multi-commune zone matrix,"
    "src_mons_zone_secours_2026,strong,Mons>ZoneSecours,tick231\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_mons_cpas_2026" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = f"""lb_mons_cpas_149m,Mons CPAS global budget 149.4m 2026,Wallonia,ops,Mons>CPAS,{CPAS_GLOB},{CPAS_GLOB},Strong deliberations: ord dep 149.13m global 149.39m balanced; city intervention 27.92m; dual federal RIS pressure,strong,src_mons_cpas_budget_2026,Vulnerable residents RIS housing homelessness,Public social assistance CPAS Mons,Core social duty not pure waste; full city BI2026 L5 residual FOI,3,8.0,5,6.15,Publish city BI2026 ASBL L5; dual federal compensation path,seed,,tick231
lb_mons_city_cpas_28m,Mons city intervention CPAS 27.92m 2026,Wallonia,ops,Mons>CPAS>city_dotation,{CITY_INTERV},{CITY_INTERV},Strong: fonct 25.14 + resp 2.50 + PCS 0.28 = 27.92m city cash to CPAS,strong,src_mons_cpas_budget_2026,CPAS beneficiaries Mons,Municipal CPAS operating subsidy,Core social transfer; dual federal residual,3,7.5,4,5.7,Publish multi-year path vs Oxygene,seed,,tick231
lb_mons_zone_secours_2_60m,Mons Zone Secours Hainaut-Centre 2.60m 2026,Wallonia,ops,Mons>ZoneSecours,{ZONE_SECOURS},{ZONE_SECOURS},Strong conseil: 2.604m (down from provisional 2.816m),strong,src_mons_zone_secours_2026,Residents fire rescue,Municipal fire zone dotation,Core safety not pure waste,2,6.0,3,4.45,Publish full zone multi-commune matrix,seed,,tick231
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_mons_cpas_149m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- entities ---
ent = data / "entities.csv"
raw = ent.read_bytes()
try:
    et = raw.decode("utf-8")
except UnicodeDecodeError:
    et = raw.decode("latin-1")
if "cpas_mons" not in et:
    et = et.rstrip() + "\n"
    et += (
        "cpas_mons,CPAS de Mons,CPAS Mons,Mons public social assistance centre,"
        "parastatal,city_mons,fr,https://www.mons.be,,,BI2026 global 149.4m city intervention 27.9m; tick231\n"
    )
    Path(ent).write_text(et, encoding="utf-8")
    print("entity cpas added")
else:
    print("entity exists")

# --- foi update gap_mons ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
# update notes on gap_mons_budget_l5 if present
import re

if "gap_mons_budget_l5" in ft:
    lines = ft.splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("gap_mons_budget_l5,") or (
            "gap_mons_budget_l5" in line and line.startswith("gap_")
        ):
            # replace trailing notes
            if "tick231" not in line:
                line = line.rstrip("\n\r")
                # update what_is_missing partially via notes end
                if ",ready," in line or line.count(",") > 5:
                    # append note fragment
                    if line.endswith("\n"):
                        base = line[:-1]
                    else:
                        base = line
                    # strip last notes field if ends with human send
                    base = re.sub(
                        r"(rq_103.*|still need BI2026.*|human send.*)$",
                        "tick103+231: CPAS BI2026 149.4m + city interv 27.9m + zone secours 2.60m filled strong; full Ville BI2026 PDF + ASBL L5 still missing FOI ready human send",
                        base,
                    )
                    if "tick231" not in base:
                        base = base + "; tick231 partial CPAS+zone filled"
                    line = base + ("\n" if lines and True else "")
                    if not line.endswith("\n"):
                        line += "\n"
                    print("foi mons updated")
        out.append(line)
    foi.write_text("".join(out), encoding="utf-8")
else:
    print("no gap_mons row")

# also antwerp gap note if still about Mons residual
ft2 = foi.read_text(encoding="utf-8")
oldn = (
    "tick140+204+213-229: culture Digipolis social+youth ~15 orgs ~31.79m filled; "
    "residual register project L5 Mons BI2026 dual VL human send"
)
newn = (
    "tick140+204+213-231: culture Digipolis social ~32m; Mons CPAS 149.4m+zone 2.60m filled; "
    "residual register + full Ville BI2026 ASBL L5 dual VL human send"
)
if oldn in ft2:
    foi.write_text(ft2.replace(oldn, newn), encoding="utf-8")
    print("foi antwerp note ok")
else:
    print("foi antwerp note skip")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_222,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 utilities SOE FPS taxex other large FOI-adjacent programmes) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T02:15:00Z,,'
    '"Spawned tick229 after residual social 1.56m; tick230 progress; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_222,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 utilities SOE FPS taxex other large FOI-adjacent programmes) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T02:15:00Z,2026-07-29T02:50:00Z,'
    '"tick231: Mons CPAS BI2026 149.4m city interv 27.9m zone secours 2.60m; Ville full BI2026 PDF still FOI; spawn rq_223"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_223,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons Ville BI2026 PDF if published utilities SOE IDEA HYGEA FPS taxex other large FOI-adjacent) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T02:50:00Z,,'
        '"Spawned tick231 after Mons CPAS 149.4m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_222")
    print(repr(text[i : i + 280]) if i >= 0 else "missing")

# --- state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T02:50:00Z,rq_222,231,no,"
    '"Scheduler 60s. Next prio5 rq_223 Mons Ville BI/utilities; rq_116 SWA deferred. '
    'FOI ready human send. tick231 Mons CPAS 149.4m city 27.9m zone 2.60m."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = f"""
### 2026-07-29T02:50:00Z - tick 231
- Unit: **rq_222** (FOI-adjacent hole-fill - **Mons CPAS BI2026 + Zone Secours**)
- Found (strong deliberations.be primary):
  - **CPAS Mons 2026 global EUR 149.389m** (ord dep **149.131m** / rec **149.152m** boni 21k; extra global **7.306m**).
  - **City intervention CPAS EUR 27.918m** (fonct 25.141 + responsabilisation 2.501 + PCS 0.276).
  - **Zone Secours Hainaut-Centre EUR 2.604m** (vs provisional BI 2.816m; MB1 adjustment).
  - Housing NPG medium: 84 logements renovation **2.68m** UREBA/PIVW; Art.60 posts 260→380 / Art.61 70→140.
  - Full **Ville de Mons BI2026 PDF** still not published on mons.be budgets page (only 2025 comptes) — FOI residual ASBL L5.
- Wrote: sources 2; budgets 9; cmt 2; lb 3; entity; foi notes; rq_222=done; seeded **rq_223**.
- FOI: full Ville BI2026 + ASBL top20 still ready human send.
- Next: prio5 **rq_223**; deferred **rq_116** SWA.
"""
if "### 2026-07-29T02:50:00Z - tick 231" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick231")
