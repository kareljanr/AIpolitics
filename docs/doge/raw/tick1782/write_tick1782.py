import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1782'; utc='2026-08-24T20:55:00Z'
eid='nv_cedrebleu'; sid='src_cedrebleu_jr2025_nbb'
gap='gap_cedrebleu_marge_3_18m_equity_thin_comfort_rivage_l5'
lb='lb_cedrebleu_marge_3_18m_equity_thin_comfort_rivage_l5'
comm='comm_cedrebleu_jr2025_marge_3_18m'
hier='Wallonie>Provinces>BrabantWallon>Communes>Jodoigne>MRPA>CedreBleuPrinceLeopold>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'RESIDENCE PRINCE LEOPOLD (CEDRE BLEU) SA NBB A-cap YE2025 deposit 2026-00137103','http://cdn.staatsbladmonitor.be/2026pdf/2026-00137103.pdf','Nationale Bank van België / RESIDENCE PRINCE LEOPOLD SA','2026-08-24','primary_official','tick1782; AV 12.05.2026; A-cap abbrev; Vivalto Home Belgium admin; opinion sans reserve; Jodoigne Chaussee Charleroi 136; marge 3.18m; equity flip to 37k thin Art7229; RIVAGE 135.6m; comfort through AG YE2026'])
    w.writerow(['src_cedrebleu_site','Vivalto Home — Le Cèdre Bleu maisons','https://www.vivaltohome.com/maisons/le-cedre-bleu/','Vivalto Home','2026-08-24','primary_official','tick1782; Chaussee de Charleroi 136 1370 Jodoigne; cedrebleu.secretariat@vivaltohome.com; pierre.rifaut@vivaltohome.com'])
    w.writerow(['src_cedrebleu_kbo','KBO RESIDENCE PRINCE LEOPOLD SA 0451.294.082','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0451294082','KBO','2026-08-24','primary_official','tick1782; SA/NV; Chaussee de Charleroi 136 1370 Jodoigne; RPR Brabant wallon; denom CEDRE BLEU'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Le Cedre Bleu / Residence Prince Leopold NV (leftover Vivalto WZC dual / Jodoigne)','RESIDENCE PRINCE LEOPOLD (CEDRE BLEU) SA (WZC Vivalto résiduel / Jodoigne)','Residence Prince Leopold (Cedre Bleu) SA leftover Vivalto nursing-home dual Jodoigne','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/le-cedre-bleu/','cedrebleu.secretariat@vivaltohome.com','Chaussée de Charleroi 136 1370 Jodoigne','tick1782 leftover unused Vivalto maison after Brembloem Immo; KBO 0451.294.082 Actief; SA denom RESIDENCE PRINCE LEOPOLD (CEDRE BLEU); official NBB A-cap YE2025 deposit 2026-00137103 CDN 200 31p; AV 12.05.2026; mère Vivalto Home Belgium; opinion sans réserve; equity flip NEG to thin 36987 Art7229; comfort through AG YE2026; RIVAGE gage 135600000; FVA 7503000; sourced euros assets 14161580 debt 14056594 marge 3178410 staff 2245977 VTE 36.6 expl 550271 pnl 133725; FOI ready RIZIV/comfort/RIVAGE/FVA/autres dettes'])

buds=[
 ('bud_cedrebleu_assets_2025',14161580,'stock','Assets YE2025 14161580; tick1782'),
 ('bud_cedrebleu_equity_2025',36987,'stock','Equity 36987 flip from NEG -96738; Art7229 thin; tick1782'),
 ('bud_cedrebleu_debt_2025',14056594,'stock','Debt 14056594; tick1782'),
 ('bud_cedrebleu_leasing_lt_2025',6664266,'stock','LT credit/leasing 172/3=6664266; option 152060; tick1782'),
 ('bud_cedrebleu_fva_2025',7503000,'stock','Immobilisations financieres 7503000; tick1782'),
 ('bud_cedrebleu_autres_creances_2025',452224,'stock','Autres creances ST 452224; tick1782'),
 ('bud_cedrebleu_autres_dettes_st_2025',4272538,'stock','Autres dettes ST 4272538; tick1782'),
 ('bud_cedrebleu_accruals_2025',2467321,'stock','Comptes regularisation passif 2467321; tick1782'),
 ('bud_cedrebleu_cash_2025',163333,'stock','Cash 163333 JUMP vs 69188; tick1782'),
 ('bud_cedrebleu_marge_2025',3178410,'realized','Marge bruto 3178410 incl nrec expl 125784 (A-cap; CA undisclosed); tick1782'),
 ('bud_cedrebleu_staff_2025',2245977,'realized','Staff 2245977 / VTE 36.6; tick1782'),
 ('bud_cedrebleu_expl_2025',550271,'realized','Benefice exploitation 550271; tick1782'),
 ('bud_cedrebleu_pnl_2025',133725,'realized','PnL 133725; no dividend; perte reportée -31213; tick1782'),
 ('bud_cedrebleu_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage 135600000 group undivided; assets grevés 8393515; tick1782'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'RESIDENCE PRINCE LEOPOLD (CEDRE BLEU) SA JR2025 leftover Vivalto dual (marge 3.18m / thin equity + RIVAGE)',eid,'RESIDENCE PRINCE LEOPOLD SA / Vivalto Home Belgium / residents Jodoigne','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-12',2025,2025,3178410,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00137103.pdf','Local leftover Vivalto WZC map WAL Jodoigne Cedre Bleu — marge 3.18m / equity flip thin + comfort + RIVAGE','Publish CA/RIZIV + comfort text + RIVAGE share + FVA/autres dettes map; unit-cost',sid,'strong',hier,'tick1782; assets 14.16m equity 37k thin Art7229 debt 14.06m FVA 7.50m leasing LT 6.66m marge 3.18m staff 2.25m VTE 36.6 expl 0.55m pnl 0.13m RIVAGE 135.6m comfort through AG YE2026; FOI ready not sent; not TE-additive; A-cap CA undisclosed'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'CEDRE BLEU / Prince Leopold SA 2025: marge 3.18m / staff 2.25m (thin equity 37k + comfort + RIVAGE 135.6m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),3178410,135600000,'Envelope=marge 3178410 (A-cap; CA undisclosed); staff 2.25m VTE 36.6; equity flip NEG to thin 37k (Art7229); FVA 7.50m; autres dettes ST 4.27m; accruals 2.47m; RIVAGE gage 135.6m undivided; comfort letter through AG YE2026','strong',sid,'MRPA/WZC residents Jodoigne / Vivalto group','Nursing-home care (MRPA/MRS)','Thin-equity Vivalto dual flipped from NEG only via profit while comfort+RIVAGE cascade continue — public-care euros on Art7229 shell',6.5,6.8,5,6.6,'Publish CA/RIZIV; disclose comfort + RIVAGE share + FVA/autres dettes; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 3178410 but CA undisclosed; equity thin 36987 after NEG flip — Art7229; comfort letter through AG YE2026 full text; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need CedreBleu share; FVA 7503000 nature; autres dettes ST 4272538 + accruals 2467321; nrec expl 125784; leasing LT 6664266 + option 152060','Vivalto Jodoigne Cedre Bleu with abbreviated schema + Art7229 thin equity + comfort + undivided RIVAGE — opacity on public care-euro path and continuity',8,'RESIDENCE PRINCE LEOPOLD SA / Vivalto Home Belgium SA','cedrebleu.secretariat@vivaltohome.com','Chaussée de Charleroi 136 1370 Jodoigne',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1782; human-send only; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; unused Vivalto maisons remain'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1782':
        row['status']='done'
        row['title']='RESIDENCE PRINCE LEOPOLD (CEDRE BLEU) SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: RESIDENCE PRINCE LEOPOLD (CEDRE BLEU) SA leftover unused Vivalto maison Jodoigne after Brembloem Immo; '
            'KBO 0451.294.082 Actief; live JR2025 official NBB A-cap PDF (214520 bytes 31p deposit 2026-00137103; AV 12.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); sourced euros assets 14161580 equity 36987 thin Art7229 debt 14056594 '
            'marge 3178410 staff 2245977 VTE 36.6 pnl 133725 FVA 7503000 RIVAGE 135600000 comfort through AG YE2026; '
            'FOI ready not sent; NOT Brembloem Immo continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1782 CEDRE BLEU leftover Vivalto residual; KBO 0451.294.082; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1783 residual dual L5'
        print('updated rq_1782'); break
else:
    raise SystemExit('missing rq_1782')
if not any(r.get('task_id')=='rq_1783' for r in rows):
    rows.append({
        'task_id':'rq_1783','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1783 after 1782 CEDRE BLEU. Next every-10 is 1790. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other unused Vivalto maisons '
                 '(aux-lilas-de-bonlez / cottage-rose / e-carpentier / floreal / la-maison-dieu / charlemagne / '
                 'jardin-des-chantoirs / le-marronnier / manoir-du-menil) if CDN 200, other IOED/HVZ/IGS. '
                 'Do NOT redo CedreBleu/BrembloemImmo/AgeDor/Tonnelle continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1782 CEDRE BLEU; NEXT AGB/NSZ-if-200/Bosgroep/BrembloemVZW-if-200/unused-Vivalto-maisons; next every-10 1790'
    })
    print('spawned rq_1783')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1782',1782,'no',
        'tick1782 leftover CEDRE BLEU / Prince Leopold Jodoigne; KBO 0451.294.082; NBB YE2025 marge 3178410 staff 2245977 VTE 36.6 pnl 133725 equity thin 36987 Art7229 FVA 7503000 RIVAGE 135600000 comfort through AG YE2026; FOI RIZIV/comfort/RIVAGE/FVA; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; unused Vivalto maisons remain; NOT every-10 (next 1790); next rq_1783 AGB/NSZ-if-200/Bosgroep/unused-Vivalto; continuous hole_fill'])
print('OK')
