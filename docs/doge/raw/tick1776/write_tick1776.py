import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1776'; utc='2026-08-24T18:55:00Z'
eid='nv_etrier'; sid='src_etrier_jr2025_nbb'
gap='gap_etrier_marge_4_12m_related_recv_4_16m_rivage_135m_l5'
lb='lb_etrier_marge_4_12m_related_recv_4_16m_rivage_135m_l5'
comm='comm_etrier_jr2025_marge_4_12m'
hier='Wallonie>Provinces>Namur>Communes>Sombreffe>MRPA>LEtrierDArgent>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,"L'ETRIER D'ARGENT SA NBB A-cap YE2025 deposit 2026-00176181",'http://cdn.staatsbladmonitor.be/2026pdf/2026-00176181.pdf',"Nationale Bank van België / L'ETRIER D'ARGENT SA",'2026-08-24','primary_official','tick1776; AV 21.05.2026; A-cap abbrev; Vivalto Home Belgium admin; opinion sans reserve; Sombreffe Rue Ardenelle 35; marge 4.12m; controllers 4.16m; RIVAGE gage 135.6m; dividend 0.33m'])
    w.writerow(['src_etrier_site',"Vivalto Home — L'Étrier d'Argent maisons",'https://www.vivaltohome.com/maisons/etrier-dargent/','Vivalto Home','2026-08-24','primary_official','tick1776; Rue Ardenelle 35 5140 Sombreffe; etrier.secretariat@vivaltohome.com'])
    w.writerow(['src_etrier_kbo',"KBO L'ETRIER D'ARGENT SA 0472.999.120",'https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472999120','KBO','2026-08-24','primary_official','tick1776; SA/NV; Rue Ardenelle 35 5140 Sombreffe; RPR Liege division Namur'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,"L'Etrier d'Argent NV (leftover Vivalto WZC dual / Sombreffe)","L'ETRIER D'ARGENT SA (WZC Vivalto résiduel / Sombreffe)","L'ETRIER D'ARGENT SA leftover Vivalto nursing-home dual Sombreffe",'other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/etrier-dargent/','etrier.secretariat@vivaltohome.com','Rue Ardenelle 35 5140 Sombreffe','tick1776 leftover Vivalto WZC dual after LE CLOS DES ROSES; KBO 0472.999.120 Actief; SA; official NBB A-cap YE2025 deposit 2026-00176181 CDN 200 28p; AV 21.05.2026; mère Vivalto Home Belgium; opinion sans réserve; RIVAGE/VIVALTO LEASE gage 135600000 undivided twin ClosRoses/RAPSODE; controllers 9500=4155165; FVA 4620948; dividend apport 325000; sourced euros assets 10477226 equity 1705277 debt 8487639 leasing LT 3895022 marge 4117230 staff 3120308 VTE 49 expl 617479 pnl 424863; FOI ready RIZIV/related recv/RIVAGE share/dividend'])

buds=[
 ('bud_etrier_assets_2025',10477226,'stock','Assets YE2025 10477226 DROP vs 10690473; tick1776'),
 ('bud_etrier_equity_2025',1705277,'stock','Equity 1705277 DROP vs 1786747; tick1776'),
 ('bud_etrier_debt_2025',8487639,'stock','Debt 8487639; tick1776'),
 ('bud_etrier_leasing_lt_2025',3895022,'stock','LT credit/leasing 172/3=3895022; option achat 315000; tick1776'),
 ('bud_etrier_fva_2025',4620948,'stock','Immobilisations financieres 4620948; tick1776'),
 ('bud_etrier_autres_creances_2025',1846146,'stock','Autres creances ST 1846146; tick1776'),
 ('bud_etrier_controllers_recv_2025',4155165,'stock','Creances sur administrateurs/controleurs 9500=4155165; tick1776'),
 ('bud_etrier_cash_2025',287434,'stock','Cash 287434 JUMP vs 151093; tick1776'),
 ('bud_etrier_marge_2025',4117230,'realized','Marge bruto 4117230 (A-cap; CA undisclosed); tick1776'),
 ('bud_etrier_staff_2025',3120308,'realized','Staff 3120308 / VTE 49; tick1776'),
 ('bud_etrier_expl_2025',617479,'realized','Benefice exploitation 617479; tick1776'),
 ('bud_etrier_pnl_2025',424863,'realized','PnL 424863; dividend apport 325000 + admin 175333; autres dettes ST=distribuer 500333; tick1776'),
 ('bud_etrier_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage fonds commerce 135600000 group undivided; assets grevés 7087670; tick1776'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,"L'ETRIER D'ARGENT SA JR2025 leftover Vivalto dual (marge 4.12m / related recv 4.16m / RIVAGE 135.6m)",eid,"L'ETRIER D'ARGENT SA / Vivalto Home Belgium / residents Sombreffe",'CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-21',2025,2025,4117230,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176181.pdf','Local leftover Vivalto WZC map WAL Sombreffe — marge 4.12m / controllers recv + RIVAGE gage twin ClosRoses/RAPSODE','Publish CA/RIZIV split + related recv map + RIVAGE share of 135.6m + dividend rationale; unit-cost',sid,'strong',hier,'tick1776; assets 10.48m equity 1.71m debt 8.49m FVA 4.62m leasing LT 3.90m marge 4.12m staff 3.12m VTE 49 expl 0.62m pnl 0.42m dividend 0.33m controllers 4.16m RIVAGE 135.6m; FOI ready not sent; not TE-additive; A-cap CA undisclosed'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,"L'ETRIER D'ARGENT SA 2025: marge 4.12m / staff 3.12m (controllers recv 4.16m + RIVAGE gage 135.6m)",'L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),4117230,135600000,'Envelope=marge 4117230 (A-cap; CA undisclosed); staff 3.12m VTE 49; controllers recv 4.16m; FVA 4.62m; dividend 0.33m; equity DROP; RIVAGE/VIVALTO LEASE gage 135.6m group undivided (twin ClosRoses/RAPSODE); leasing LT 3.90m','strong',sid,'MRPA/WZC residents Sombreffe / Vivalto group','Nursing-home care (MRPA/MRS)','Same Vivalto RIVAGE bond/lease cascade plus large controller receivables while equity DROPs; A-cap hides CA',6.3,6.8,5,6.5,'Publish CA/RIZIV; disclose related recv + RIVAGE share; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 4117230 but CA undisclosed; controllers recv 9500=4155165 + FVA 4620948 + autres creances ST 1846146 counterparties/terms; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need Etrier share; leasing LT 3895022 + option achat 315000; dividend apport 325000 + admin 175333 (autres dettes ST 500333=distribuer); equity DROP','Vivalto Sombreffe WZC with abbreviated schema + controller receivables + undivided RIVAGE gage twin ClosRoses/RAPSODE — opacity on public care-euro path and group extraction',8,"L'ETRIER D'ARGENT SA / Vivalto Home Belgium SA",'etrier.secretariat@vivaltohome.com','Rue Ardenelle 35 5140 Sombreffe',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1776; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; CDN live VertBocage/Tonnelle/AgeDor; NOT ClosRoses continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1776':
        row['status']='done'
        row['title']="L'ETRIER D'ARGENT SA JR2025 leftover Vivalto dual residual"
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=("Completed: L'ETRIER D'ARGENT SA leftover Vivalto WZC dual Sombreffe after LE CLOS DES ROSES; "
            'KBO 0472.999.120 Actief; live JR2025 official NBB A-cap PDF (227585 bytes 28p deposit 2026-00176181; AV 21.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 10477226 equity 1705277 debt 8487639 marge 4117230 staff 3120308 VTE 49 '
            'pnl 424863 dividend 325000 controllers 4155165 FVA 4620948 RIVAGE 135600000; '
            'FOI ready not sent; NOT ClosRoses continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']="tick1776 L'ETRIER D'ARGENT leftover Vivalto residual; KBO 0472.999.120; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1777 residual dual L5"
        print('updated rq_1776'); break
else:
    raise SystemExit('missing rq_1776')
if not any(r.get('task_id')=='rq_1777' for r in rows):
    rows.append({
        'task_id':'rq_1777','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':("Tick 1777 after 1776 L'ETRIER D'ARGENT. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), "
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(AU VERT BOCAGE 2026-00176184 / LA TONNELLE 2026-00176186 / L AGE D OR 2026-00176187 live), '
                 "other IOED/HVZ/IGS. Do NOT redo Etrier/ClosRoses/Centenaire/Braine/Meridienne continuum."),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':"spawned after tick1776 L'ETRIER D'ARGENT; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/VertBocage/Tonnelle/AgeDor; next every-10 1780"
    })
    print('spawned rq_1777')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1776',1776,'no',
        "tick1776 leftover L'ETRIER D'ARGENT Sombreffe; KBO 0472.999.120; NBB YE2025 marge 4117230 staff 3120308 VTE 49 pnl 424863 dividend 325000 controllers 4155165 FVA 4620948 RIVAGE gage 135600000 equity DROP; FOI RIZIV/related recv/RIVAGE share/dividend; Brembloem still no JR2025; AGB Bornem JR2024; CDN live VertBocage 00176184 Tonnelle 00176186 AgeDor 00176187; NOT every-10 (next 1780); next rq_1777 AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/VertBocage/Tonnelle/AgeDor; continuous hole_fill"])
print('OK')
