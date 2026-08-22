import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1779'; utc='2026-08-24T19:55:00Z'
eid='nv_agedor'; sid='src_agedor_jr2025_nbb'
gap='gap_agedor_ca_6_12m_equity_neg_1_29m_comfort_rivage_l5'
lb='lb_agedor_ca_6_12m_equity_neg_1_29m_comfort_rivage_l5'
comm='comm_agedor_jr2025_ca_6_12m'
hier='Wallonie>Provinces>Luxembourg>Communes>Bastogne>MRPA>LAgeDOr>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,"L'AGE D'OR SA NBB C-cap YE2025 deposit 2026-00176187",'http://cdn.staatsbladmonitor.be/2026pdf/2026-00176187.pdf',"Nationale Bank van België / L'AGE D'OR SA",'2026-08-24','primary_official','tick1779; AV 21.05.2026; C-cap full; Vivalto Home Belgium admin; opinion sans reserve + observation comfort; Bastogne Rue des Maies 29c; CA 6.12m; equity NEG 1.29m; RIVAGE 135.6m; related debt 12.34m'])
    w.writerow(['src_agedor_site',"Vivalto Home — L'Âge d'Or maisons",'https://www.vivaltohome.com/maisons/l-age-d-or/','Vivalto Home','2026-08-24','primary_official','tick1779; Rue des Maies 29c 6600 Bastogne; agedor.info@vivaltohome.com'])
    w.writerow(['src_agedor_kbo',"KBO L'AGE D'OR SA 0444.792.411",'https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0444792411','KBO','2026-08-24','primary_official','tick1779; SA/NV; Rue des Maies 29c 6600 Bastogne; RPR Liege division Neufchateau'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,"L'Age d'Or NV (leftover Vivalto WZC dual / Bastogne)","L'AGE D'OR SA (WZC Vivalto résiduel / Bastogne)","L'AGE D'OR SA leftover Vivalto nursing-home dual Bastogne",'other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/l-age-d-or/','agedor.info@vivaltohome.com','Rue des Maies 29c 6600 Bastogne',"tick1779 leftover Vivalto WZC dual after LA TONNELLE; closes CDN sister batch; KBO 0444.792.411 Actief; SA; official NBB C-cap YE2025 deposit 2026-00176187 CDN 200 61p; AV 21.05.2026; mère Vivalto Home Belgium; opinion sans réserve + observation comfort; equity NEG -1285759; loss 244966; comfort letter through AG YE2026; RIVAGE/VIVALTO LEASE gage 135600000; related debt 12336309; leasing LT 10100291; sourced euros assets 12220905 CA 6123194 staff 3993220 VTE 63.1 expl 204234; FOI ready RIZIV/comfort/RIVAGE/related debt"])

buds=[
 ('bud_agedor_assets_2025',12220905,'stock','Assets YE2025 12220905 DROP vs 12423870; tick1779'),
 ('bud_agedor_equity_2025',-1285759,'stock','Equity NEG -1285759 deepening vs -1040793; tick1779'),
 ('bud_agedor_debt_2025',13506664,'stock','Debt 13506664; tick1779'),
 ('bud_agedor_leasing_lt_2025',10100291,'stock','LT leasing dettes 10100291; option achat 217600; tick1779'),
 ('bud_agedor_fva_2025',872035,'stock','Immobilisations financieres 872035 related créances; tick1779'),
 ('bud_agedor_related_recv_fva_2025',872035,'stock','Créances entreprises liées FVA 281=872035; tick1779'),
 ('bud_agedor_related_recv_st_2025',1111393,'stock','Créances liées ST 1111393 JUMP vs 840106; tick1779'),
 ('bud_agedor_controllers_recv_2025',1496579,'stock','Créances sur administrateurs/controleurs 9500=1496579; garanties 9501=2880465; tick1779'),
 ('bud_agedor_related_debt_2025',12336309,'stock','Dettes entreprises liées 12336309 (LT 12018935 + ST 317373); tick1779'),
 ('bud_agedor_cash_2025',362974,'stock','Cash 362974 JUMP vs 60865; tick1779'),
 ('bud_agedor_ca_2025',6123194,'realized','CA 6123194 / ventes prestations 6218358; tick1779'),
 ('bud_agedor_staff_2025',3993220,'realized','Staff 3993220 / VTE 63.1; tick1779'),
 ('bud_agedor_expl_2025',204234,'realized','Benefice exploitation 204234; tick1779'),
 ('bud_agedor_pnl_2025',-244966,'realized','PnL LOSS -244966; no dividend; tick1779'),
 ('bud_agedor_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage fonds commerce 135600000 group undivided; assets grevés 2880465; tick1779'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,"L'AGE D'OR SA JR2025 leftover Vivalto dual (CA 6.12m / NEG equity 1.29m / RIVAGE 135.6m)",eid,"L'AGE D'OR SA / Vivalto Home Belgium / residents Bastogne",'CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-21',2025,2025,6123194,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176187.pdf','Local leftover Vivalto WZC map WAL Bastogne — CA 6.12m / NEG equity + comfort + RIVAGE twin sister batch','Publish RIZIV split + comfort letter text + RIVAGE share + related debt 12.34m map; unit-cost',sid,'strong',hier,'tick1779; assets 12.22m equity NEG 1.29m debt 13.51m FVA 0.87m leasing LT 10.10m CA 6.12m staff 3.99m VTE 63.1 expl 0.20m loss 0.24m related debt 12.34m RIVAGE 135.6m comfort through AG YE2026; FOI ready not sent; not TE-additive'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,"L'AGE D'OR SA 2025: CA 6.12m / staff 3.99m (NEG equity 1.29m + comfort + RIVAGE 135.6m)",'L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),6123194,135600000,'Envelope=CA 6123194; staff 3.99m VTE 63.1; equity NEG 1.29m deepening; loss 0.24m; related debt 12.34m; leasing LT 10.10m; RIVAGE gage 135.6m undivided; Vivalto comfort letter through AG YE2026; auditor observation on support','strong',sid,'MRPA/WZC residents Bastogne / Vivalto group','Nursing-home care (MRPA/MRS)','Loss-making Vivalto dual sustained by parent comfort while pledged into group RIVAGE cascade — public-care euros on NEG equity shell',6.8,6.9,5,6.9,'Publish RIZIV + comfort text + RIVAGE share + related-debt map; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB C-cap YE2025 live CA 6123194 but RIZIV/residentie split unpublished; equity NEG 1285759 + loss 244966 + Vivalto comfort letter through AG YE2026 — need full text/amounts; related debt 12336309 + related recv FVA 872035/ST 1111393/controllers 1496579; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need AgeDor share; leasing LT 10100291 + option 217600','Vivalto Bastogne WZC with NEG equity and second consecutive loss sustained only by parent comfort while pledged into undivided RIVAGE gage — opacity on public care-euro path and continuity',9,"L'AGE D'OR SA / Vivalto Home Belgium SA",'agedor.info@vivaltohome.com','Rue des Maies 29c 6600 Bastogne',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1779; human-send only; closes CDN sister batch ClosRoses/Etrier/VertBocage/Tonnelle/AgeDor; Brembloem still no JR2025; AGB Bornem JR2024; next tick 1780 MUST every-10'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1779':
        row['status']='done'
        row['title']="L'AGE D'OR SA JR2025 leftover Vivalto dual residual"
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=("Completed: L'AGE D'OR SA leftover Vivalto WZC dual Bastogne after LA TONNELLE; closes CDN sister batch; "
            'KBO 0444.792.411 Actief; live JR2025 official NBB C-cap PDF (1287228 bytes 61p deposit 2026-00176187; AV 21.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve + observation comfort); '
            'sourced euros assets 12220905 equity NEG -1285759 debt 13506664 CA 6123194 staff 3993220 VTE 63.1 '
            'pnl -244966 related debt 12336309 leasing LT 10100291 RIVAGE 135600000 comfort through AG YE2026; '
            'FOI ready not sent; NOT Tonnelle continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']="tick1779 L'AGE D'OR leftover Vivalto residual; KBO 0444.792.411; live JR2025 NBB C-cap PDF; sourced euros; FOI ready not sent; next rq_1780 MUST every-10 + residual dual L5"
        print('updated rq_1779'); break
else:
    raise SystemExit('missing rq_1779')
if not any(r.get('task_id')=='rq_1780' for r in rows):
    rows.append({
        'task_id':'rq_1780','title':'every-10 progress + leftover AGB/APB/IGS dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':("Tick 1780 after 1779 L'AGE D'OR MUST every-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                 'Then leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, '
                 'Brembloem VZW if CDN 200, other IOED/HVZ/IGS if JR2025 live. '
                 'Do NOT redo AgeDor/Tonnelle/VertBocage/Etrier/ClosRoses/Centenaire/Braine/Meridienne continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':"spawned after tick1779 L'AGE D'OR; MUST every-10 at 1780; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/other IGS"
    })
    print('spawned rq_1780')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1779',1779,'no',
        "tick1779 leftover L'AGE D'OR Bastogne; KBO 0444.792.411; NBB YE2025 CA 6123194 staff 3993220 VTE 63.1 pnl LOSS -244966 equity NEG -1285759 related debt 12336309 leasing LT 10100291 RIVAGE gage 135600000 comfort through AG YE2026; FOI RIZIV/comfort/RIVAGE/related debt; closes CDN sister batch; Brembloem still no JR2025; AGB Bornem JR2024; next rq_1780 MUST every-10 + AGB/NSZ/Bosgroep/Brembloem; continuous hole_fill"])
print('OK')
