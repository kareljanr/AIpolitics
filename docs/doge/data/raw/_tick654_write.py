# -*- coding: utf-8 -*-
"""Tick 654: Ports autonomes dual Waterweg + DO02/DO09 residual — rq_645."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T05:15:00Z"
TICK = 654
RQ = "rq_645"
NEXT_RQ = "rq_646"
GAP = "gap_ports_do02_do09_l5_2025"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def append_rows(path: Path, rows: list[str]) -> int:
    text = read_text(path)
    existing = text
    added = 0
    for row in rows:
        key = row.split(",", 1)[0]
        if key and any(
            L.startswith(key + ",") or L.startswith("\ufeff" + key + ",")
            for L in existing.splitlines()
        ):
            print(f"SKIP exists {key}")
            continue
        if not text.endswith("\n"):
            text += "\n"
        text += row + "\n"
        existing = text
        added += 1
        print(f"ADD {key}")
    path.write_bytes(text.encode("utf-8"))
    return added


def update_rq_done(path: Path, rq_id: str, notes: str) -> None:
    text = read_text(path)
    lines = text.splitlines()
    out = []
    for L in lines:
        if L.startswith(rq_id + ",") or L.startswith("\ufeff" + rq_id + ","):
            parts = L.split(",")
            if len(parts) >= 5:
                parts[4] = "done"
            if len(parts) >= 11:
                parts[10] = NOW
            if len(parts) >= 12:
                parts[11] = notes.replace(",", ";")
            else:
                parts.append(notes.replace(",", ";"))
            L = ",".join(parts)
            print(f"RQ done {rq_id}")
        out.append(L)
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


def spawn_rq(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    if any(L.startswith(key + ",") for L in text.splitlines()):
        print(f"SKIP spawn {key}")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    path.write_bytes(text.encode("utf-8"))
    print(f"SPAWN {key}")


def set_loop_state(path: Path) -> None:
    header = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes"
    notes = (
        f"tick{TICK} ports PAC+PACO dual Waterweg DO02/09 residual; "
        f"next {NEXT_RQ}; progress@660 in 6; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "port_autonome_charleroi,Port autonome de Charleroi PAC,Port autonome de Charleroi PAC,Autonomous Port of Charleroi Type2 dual inland ports,parastatal,wallonie_gov,fr,https://www.wallonie.be,,,Type2 CoA Table33 BI2025 rec 5.126m dep 4.937m solde +0.189m; BI2024 5.971/5.782/+0.189; dual PACO/PAL/PAN + VL Waterweg; tick654",
    "port_autonome_liege,Port autonome de Liege PAL,Port autonome de Liege PAL,Autonomous Port of Liege Type2 dual inland ports,parastatal,wallonie_gov,fr,https://www.portdeliege.be,,,Type2 CoA Table33 BI2024 rec 10.585m dep 6.722m solde +3.863m; BI2025 non communique; dual Waterweg; tick654",
    "port_autonome_namur,Port autonome de Namur PAN,Port autonome de Namur PAN,Autonomous Port of Namur Type2 dual inland ports,parastatal,wallonie_gov,fr,https://www.wallonie.be,,,Type2 CoA Table33 BI2024 rec 2.485m dep 1.693m solde +0.792m; BI2025 non communique; dual Waterweg; tick654",
    "ports_inland_wal_stack,Ports autonomes inland Wallonie stack,Stack ports autonomes PAC PACO PAL PAN,Walloon inland autonomous ports stack dual VL Waterweg,agency,wallonie_gov,fr,,,CoA Table33 BI2025 known PAC+PACO dep 12.386m; BI2024 all four dep class 19.24m; PAL/PAN BI2025 FOI; dual Waterweg; tick654",
    "do02_cabinets_wal,DO02 Depenses de cabinet Wallonie,Division organique 02 depenses de cabinet,Walloon ministerial cabinets DO02 dual VL cabinets,agency,wallonie_gov,fr,,,CoA DO table BI2025 CE=CL 28.026m path -1.651m exec 18.788m 63.3pct; Sepac personnel 21.0m nested residual; dual VL cabinets; tick654",
    "do09_services_gov_wal,DO09 Services gouvernement Wallonie,Division organique 09 services du gouvernement,Walloon government services DO09 dual VL admin,agency,wallonie_gov,fr,,,CoA BI2025 CE 207.075m CL 208.325m path eng -20.928m liq -22.665m; CESE 7.748 tourisme 69.868 AWEX 67.547; dual VL admin; tick654",
]

src_rows = [
    "src_ccrek_ports_do02_do09_bi2025,CoA Budget RW ports Table33 + DO02 DO09 dual Waterweg,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick654: PAC BI2025 rec 5125720 dep 4936720 solde +189000 (BI2024 5970500/5781500/+189000); PACO prior 7628617/7449614/+179002; PAL BI2024 10585000/6722000/+3863000 BI2025 non communique; PAN BI2024 2485000/1693000/+792000 BI2025 non communique; ports known BI2025 dep PAC+PACO 12386334; DO02 CE=CL 28026k path -1651 exec 18788 63.3pct encours 1185; DO09 CE 207075 CL 208325 path -20928/-22665 exec 191924 encours 44560; prog012 CESE 7748; 013 Service social 6067; 014 SAAPC 5507/5509; 015 eWBS 4489 path -1407; 016 SG 742; 017 sortis 743/741; 018 Tourisme 69868; 019 Rel ext 30698; 020 AWEX 67547; 021 IWEPS 7742; 123 SCA 6858; Type1 subtotal rec 279951 dep 360268 solde -80317; dual VL Waterweg cabinets",
    "src_dual_ports_waterweg_tick654,Dual WAL ports autonomes vs VL Waterweg inland,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA ports + prior Waterweg,2026-08-01,synthesis,Strong dual: WAL PAC+PACO BI2025 dep 12.4m + PAL/PAN BI2024 class 8.4m vs VL Waterweg; not TE-additive; tick654",
]

bud_rows = [
    # PAC
    "bud_pac_rec_bi2025,port_autonome_charleroi,2025,5125720,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC recettes SEC BI2025 5.126m CoA Table33; tick654",
    "bud_pac_dep_bi2025,port_autonome_charleroi,2025,4936720,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC depenses SEC BI2025 4.937m solde +0.189m; tick654",
    "bud_pac_solde_bi2025,port_autonome_charleroi,2025,189000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC solde SEC BI2025 +0.189m flat vs BI2024; tick654",
    "bud_pac_rec_bi2024,port_autonome_charleroi,2024,5970500,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC recettes SEC BI2024 5.971m; tick654",
    "bud_pac_dep_bi2024,port_autonome_charleroi,2024,5781500,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC depenses SEC BI2024 5.782m; tick654",
    # PAL
    "bud_pal_rec_bi2024,port_autonome_liege,2024,10585000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAL recettes SEC BI2024 10.585m; BI2025 non communique; tick654",
    "bud_pal_dep_bi2024,port_autonome_liege,2024,6722000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAL depenses SEC BI2024 6.722m solde +3.863m; tick654",
    "bud_pal_solde_bi2024,port_autonome_liege,2024,3863000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAL solde SEC BI2024 +3.863m; tick654",
    # PAN
    "bud_pan_rec_bi2024,port_autonome_namur,2024,2485000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAN recettes SEC BI2024 2.485m; BI2025 non communique; tick654",
    "bud_pan_dep_bi2024,port_autonome_namur,2024,1693000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAN depenses SEC BI2024 1.693m solde +0.792m; tick654",
    "bud_pan_solde_bi2024,port_autonome_namur,2024,792000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAN solde SEC BI2024 +0.792m; tick654",
    # Stack
    "bud_ports_known_dep_bi2025,ports_inland_wal_stack,2025,12386334,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC+PACO dep BI2025 12.386m (PAL/PAN non communique); tick654",
    "bud_ports_all4_dep_bi2024,ports_inland_wal_stack,2024,19240500,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,PAC+PACO+PAL+PAN dep BI2024 class 19.241m; tick654",
    "bud_ports_all4_solde_bi2024,ports_inland_wal_stack,2024,5523000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Ports all4 solde BI2024 class +5.523m; tick654",
    # DO02
    "bud_do02_ce_bi2025,do02_cabinets_wal,2025,28026000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO02 cabinets CE BI2025 28.026m path -1.651m; tick654",
    "bud_do02_cl_bi2025,do02_cabinets_wal,2025,28026000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO02 cabinets CL BI2025 28.026m; tick654",
    "bud_do02_exec_12nov2024,do02_cabinets_wal,2024,18788000,,,outturn,src_ccrek_ports_do02_do09_bi2025,strong,DO02 exec CL 12Nov2024 18.788m (63.3pct); tick654",
    "bud_do02_encours_12nov2024,do02_cabinets_wal,2024,1185000,,,outturn,src_ccrek_ports_do02_do09_bi2025,strong,DO02 encours 12Nov2024 1.185m; tick654",
    "bud_do02_ce_ba2024,do02_cabinets_wal,2024,29677000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO02 BA2024 CE=CL 29.677m; tick654",
    # DO09
    "bud_do09_ce_bi2025,do09_services_gov_wal,2025,207075000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 CE BI2025 207.075m path eng -20.928m; tick654",
    "bud_do09_cl_bi2025,do09_services_gov_wal,2025,208325000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 CL BI2025 208.325m path liq -22.665m; tick654",
    "bud_do09_exec_12nov2024,do09_services_gov_wal,2024,191924000,,,outturn,src_ccrek_ports_do02_do09_bi2025,strong,DO09 exec CL 12Nov2024 191.924m (83.1pct); tick654",
    "bud_do09_encours_12nov2024,do09_services_gov_wal,2024,44560000,,,outturn,src_ccrek_ports_do02_do09_bi2025,strong,DO09 encours 12Nov2024 44.560m; tick654",
    "bud_do09_cese_cl_bi2025,do09_services_gov_wal,2025,7748000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog012 CESE CL BI2025 7.748m; tick654",
    "bud_do09_service_social_cl_bi2025,do09_services_gov_wal,2025,6067000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog013 Service social CL 6.067m; tick654",
    "bud_do09_saapc_cl_bi2025,do09_services_gov_wal,2025,5509000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog014 SAAPC cabinets assistance CL 5.509m; tick654",
    "bud_do09_ewbs_cl_bi2025,do09_services_gov_wal,2025,4489000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog015 e-WBS CL 4.489m path -1.407m eng; tick654",
    "bud_do09_sg_cl_bi2025,do09_services_gov_wal,2025,742000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog016 Secretariat GW CL 0.742m; tick654",
    "bud_do09_ministres_sortis_cl_bi2025,do09_services_gov_wal,2025,741000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog017 ministres sortis CL 0.741m; tick654",
    "bud_do09_iweps_cl_bi2025,do09_services_gov_wal,2025,7742000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog021 IWEPS CL 7.742m flat; tick654",
    "bud_do09_sca_cl_bi2025,do09_services_gov_wal,2025,6858000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,DO09 prog123 Service commun audit CL 6.858m path +0.655m; tick654",
    # Type1 residual
    "bud_type1_rec_bi2025,uap_perimeter_wal,2025,279951000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Type1 UAP rec SEC BI2025 279.951m path -52.953m; tick654",
    "bud_type1_dep_bi2025,uap_perimeter_wal,2025,360268000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Type1 UAP dep SEC BI2025 360.268m path -84.619m solde -80.317m; tick654",
    "bud_type1_solde_bi2025,uap_perimeter_wal,2025,-80317000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Type1 UAP solde SEC BI2025 -80.317m path +31.666m; tick654",
    "bud_fonds_bas_carbone_path_zero_bi2025,wallonie_gov,2025,0,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Fonds bas carbone Type1 zeroed BI2025 (BI2024 rec=dep 25m path -25m); tick654",
    "bud_apaq_w_dep_bi2025,wallonie_gov,2025,14759000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Apaq-W Type2 dep BI2025 14.759m path +3.307m solde -0.562m; tick654",
    "bud_apaq_w_rec_bi2025,wallonie_gov,2025,14197000,,,budgeted,src_ccrek_ports_do02_do09_bi2025,strong,Apaq-W rec BI2025 14.197m; tick654",
]

cmt_rows = [
    'cmt_ports_inland_coa_bi2025,Ports autonomes inland CoA Table33 dual Waterweg,ports_inland_wal_stack,Inland port operators,CoA Table33 Type2 ports,2024-11-15,2025,2025,12386334,"{""pac_dep_m"":4.937,""paco_dep_m"":7.450,""known_bi2025_dep_m"":12.386,""pal_bi2024_dep_m"":6.722,""pan_bi2024_dep_m"":1.693,""all4_bi2024_dep_m"":19.241,""pal_pan_bi2025"":""non_communique"",""note"":""Strong CoA; PAL/PAN FOI residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Inland autonomous ports stack,FOI PAL/PAN BI2025 dual Waterweg,src_ccrek_ports_do02_do09_bi2025,strong,Wallonie>Ports>Inland,tick654',
    'cmt_do02_cabinets_coa_bi2025,DO02 cabinets CoA dual VL,do02_cabinets_wal,Ministerial cabinets Sepac,Budget DO02 + CoA,2024-11-15,2025,2025,28026000,"{""ce_cl_m"":28.026,""path_m"":-1.651,""exec_m"":18.788,""exec_pct"":63.3,""encours_m"":1.185,""sepac_personnel_m"":21.0,""note"":""Strong CoA; Sepac 21m nested dual residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Ministerial cabinets spending,Publish L5 cabinet lines FOI,src_ccrek_ports_do02_do09_bi2025,strong,Wallonie>DO02>Cabinets,tick654',
    'cmt_do09_services_coa_bi2025,DO09 government services residual CoA BI2025,do09_services_gov_wal,CESE IWEPS eWBS SCA Tourisme AWEX,Budget DO09 + CoA annex,2024-11-15,2025,2025,208325000,"{""ce_m"":207.075,""cl_m"":208.325,""path_eng_m"":-20.928,""path_liq_m"":-22.665,""exec_m"":191.924,""encours_m"":44.560,""tourisme_m"":69.868,""awex_m"":67.547,""cese_m"":7.748,""note"":""Strong CoA; dual VL admin residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Government services DO residual,L5 residual FOI dual VL,src_ccrek_ports_do02_do09_bi2025,strong,Wallonie>DO09>Services,tick654',
    'cmt_dual_ports_waterweg_2025,Dual WAL ports vs VL Waterweg,ports_inland_wal_stack,Inland navigation dual,CoA WAL + prior Waterweg,2024-11-15,2024,2025,0,"{""wal_known_bi2025_dep_m"":12.386,""wal_all4_bi2024_dep_m"":19.241,""note"":""Not TE-additive dual inland ports""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional inland ports dual,FOI PAL/PAN + dual Waterweg,src_dual_ports_waterweg_tick654,strong,Belgium>Ports>dual_Waterweg,tick654',
    'cmt_type1_uap_subtotal_bi2025,Type1 UAP SEC subtotal CoA Table33 BI2025,uap_perimeter_wal,Type1 SACA+orgs,CoA Table33,2024-11-15,2025,2025,360268000,"{""rec_m"":279.951,""dep_m"":360.268,""solde_m"":-80.317,""path_solde_m"":31.666,""note"":""Strong CoA; FWCN dominant residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Type1 UAP consolidated residual,Dual prior UAP consol FOI,src_ccrek_ports_do02_do09_bi2025,strong,Wallonie>UAP>Type1,tick654',
]

lb_rows = [
    "lb_ports_known_12_4m_2025,Ports PAC+PACO dep 12.4m BI2025 dual Waterweg,Wallonia,ops,Wallonie>Ports>PAC_PACO_12_4m,12386334,12386334,Strong CoA: PAC+PACO dep 12.386m; PAL/PAN BI2025 non communique residual,strong,src_ccrek_ports_do02_do09_bi2025,Inland port users,Known inland ports BI2025,Core infra dual; opacity PAL/PAN FOI,4.0,4.0,3,3.85,FOI PAL/PAN BI2025 dual Waterweg,seed,,tick654",
    "lb_pal_solde_3_9m_2024,PAL solde +3.86m BI2024 non-communique BI2025,Wallonia,ops,Wallonie>Ports>PAL_solde_3_9m,3863000,6722000,Strong CoA: PAL BI2024 solde +3.863m dep 6.722m; BI2025 non communique,strong,src_ccrek_ports_do02_do09_bi2025,Liege port users,Largest inland port residual opacity,Governance FOI residual,5.5,3.5,3,4.40,FOI BI2025 budget dual Waterweg,seed,,tick654",
    "lb_do02_cabinets_28m_2025,DO02 cabinets 28.0m path -1.7m BI2025,Wallonia,ops,Wallonie>DO02>Cabinets_28m,28026000,28026000,Strong CoA: DO02 CE=CL 28.026m path -1.651m exec 63.3pct; dual VL cabinets,strong,src_ccrek_ports_do02_do09_bi2025,Ministerial staff,Cabinet spending residual,Admin residual dual,5.0,5.5,3,5.05,FOI L5 cabinet lines,seed,,tick654",
    "lb_do09_cl_208m_2025,DO09 services gov CL 208m path -23m BI2025,Wallonia,ops,Wallonie>DO09>Services_208m,208325000,208325000,Strong CoA: DO09 CL 208.325m path -22.7m; Tourisme+AWEX dominate,strong,src_ccrek_ports_do02_do09_bi2025,WAL admin tourism export,Government services residual,Core admin dual residual,4.0,7.5,3,5.55,FOI residual L5,seed,,tick654",
    "lb_type1_solde_minus_80m_2025,Type1 UAP solde -80.3m BI2025,Wallonia,ops,Wallonie>UAP>Type1_solde_80m,80317000,360268000,Strong CoA Table33: Type1 solde -80.317m path +31.7m; FWCN dominant,strong,src_ccrek_ports_do02_do09_bi2025,WAL taxpayers Type1,Type1 consolidated deficit residual,Dual UAP consol residual,5.5,6.5,4,5.60,FOI FWCN recon prior,seed,,tick654",
    "lb_dual_ports_waterweg_2025,Dual WAL ports vs VL Waterweg inland,Belgium,ops,Belgium>Ports>dual_Waterweg,12386334,0,Strong dual: WAL known ports 12.4m BI2025 + PAL/PAN residual vs VL Waterweg; not TE-additive,strong,src_dual_ports_waterweg_tick654,BE inland navigation,Parallel inland port stacks,Dual opacity residual,5.0,5.0,4,4.70,FOI dual map,seed,,tick654",
]

foi_row = (
    f"{GAP},Wallonie>Ports_DO02_DO09>L5_2025,ports_inland_wal_stack,"
    "PAL/PAN BI2025 SEC budgets non-communique; ports traffic/invest L5; DO02 cabinet L5 lines vs Sepac 21m; "
    "DO09 residual L5 CESE/eWBS/SCA; dual Waterweg,"
    "CoA ports+DO02/09 totals strong tick654; L5 residual dual,"
    "5,SPW Mobilite / SPW Budget / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_ports_inland_coa_bi2025|cmt_do02_cabinets_coa_bi2025|cmt_dual_ports_waterweg_2025,"
    "lb_ports_known_12_4m_2025|lb_do02_cabinets_28m_2025|lb_dual_ports_waterweg_2025,"
    f"{NOW},{NOW},tick654 CoA ports DO02 DO09 primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW Table 33 ports + DO02/DO09 annex; dual Waterweg prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Mobilité / SPW Budget / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — Ports autonomes + DO02 cabinets / DO09 L5 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Budgets SEC BI2025 du Port autonome de Liège (PAL) et de Namur
   (PAN) — CoA: « non communiqué » (BI2024 PAL dep 6,722 mEUR /
   PAN 1,693 mEUR).
2. Trafic, investissements et subventions régionales 2023-2025 pour
   PAC, PACO, PAL, PAN.
3. Ventilation L5 DO02 dépenses de cabinet 28,026 mEUR vs Sepac
   personnel 21,0 mEUR (périmètre exact).
4. Ventilation L5 DO09 résiduel (CESE, e-WBS, SCA, Service social,
   ministres sortis) hors Tourisme/AWEX déjà documentés.
5. Comparaison méthodologique disponible avec De Vlaamse Waterweg
   (si documents SPW).

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 Table 33 + DO annex.
- Dual VL: Waterweg / cabinets (prior).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual ports/admin hole-fill -- **Ports autonomes + DO02/DO09** dual Waterweg)
- Found: **Ports** (primary CoA Table33): **PAC** BI2025 dep **EUR4.937m** solde **+EUR0.189m**; **PACO** **EUR7.450m** (prior); known BI2025 **EUR12.386m**. **PAL** BI2024 dep **EUR6.722m** solde **+EUR3.863m** / **PAN** **EUR1.693m** — **BI2025 non communique**. All4 BI2024 dep class **EUR19.2m**. **DO02 cabinets:** CE=CL **EUR28.0m** path **-EUR1.7m** exec **63.3%**. **DO09:** CL **EUR208.3m** path **-EUR22.7m** (Tourisme **EUR69.9m** / AWEX **EUR67.5m** / CESE **EUR7.7m** / eWBS path **-EUR1.4m**). Type1 solde **-EUR80.3m**. Dual **Waterweg**. Strong confidence CoA; PAL/PAN FOI residual.
- Wrote: entities (+6); budgets (+36); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@660 in 6 ticks; rq_116 deferred
"""


def main() -> None:
    n_ent = append_rows(ROOT / "entities.csv", ent_rows)
    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_bud = append_rows(ROOT / "budgets.csv", bud_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    n_foi = append_rows(ROOT / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    if not draft_path.exists():
        draft_path.write_text(foi_draft, encoding="utf-8")
        print(f"WROTE draft {draft_path.name}")
    else:
        print(f"SKIP draft exists {draft_path.name}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} ports PAC+PACO dual Waterweg DO02/09; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after ports dual; rq_116 deferred; progress@660 in 6",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log_text = read_text(LOG)
    if f"-- tick {TICK}" not in log_text[-3000:]:
        if not log_text.endswith("\n"):
            log_text += "\n"
        log_text += log_entry
        LOG.write_bytes(log_text.encode("utf-8"))
        print("LOG appended")
    else:
        print("SKIP log already has tick")

    print(
        f"DONE tick{TICK}: ent+{n_ent} src+{n_src} bud+{n_bud} cmt+{n_cmt} lb+{n_lb} foi+{n_foi}"
    )


if __name__ == "__main__":
    main()
