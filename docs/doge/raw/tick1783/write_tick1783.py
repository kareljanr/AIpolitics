import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1783'; utc='2026-08-24T21:15:00Z'
eid='nv_charlemagne'; sid='src_charlemagne_jr2025_nbb'
gap='gap_charlemagne_marge_2_88m_nrec_fin_2_97m_dividend_2_95m_l5'
lb='lb_charlemagne_marge_2_88m_nrec_fin_2_97m_dividend_2_95m_l5'
comm='comm_charlemagne_jr2025_marge_2_88m'
hier='Wallonie>Provinces>Liege>Communes>Liege>MRPA>LaResidenceCharlemagne>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'LA RESIDENCE CHARLEMAGNE SA NBB A-cap YE2025 deposit 2026-00137104','http://cdn.staatsbladmonitor.be/2026pdf/2026-00137104.pdf','Nationale Bank van België / LA RESIDENCE CHARLEMAGNE SA','2026-08-24','primary_official','tick1783; AV 12.05.2026; A-cap abbrev; Vivalto Home Belgium admin; opinion sans reserve; Liege Bois-de-Breux 53; marge 2.88m; nrec fin 2.97m; dividend 2.95m; controllers 10.65m; no RIVAGE'])
    w.writerow(['src_charlemagne_site','Vivalto Home — La Résidence Charlemagne maisons','https://www.vivaltohome.com/maisons/la-residence-charlemagne/','Vivalto Home','2026-08-24','primary_official','tick1783; Rue de Bois-de-Breux 53 4020 Liege; fabian.bonnechere@vivaltohome.com'])
    w.writerow(['src_charlemagne_kbo','KBO LA RESIDENCE CHARLEMAGNE SA 0870.962.307','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0870962307','KBO','2026-08-24','primary_official','tick1783; SA/NV; Rue de Bois-de-Breux 53 4020 Liege; RPR Liege'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'La Residence Charlemagne NV (leftover Vivalto WZC dual / Liège)','LA RESIDENCE CHARLEMAGNE SA (WZC Vivalto résiduel / Liège)','LA RESIDENCE CHARLEMAGNE SA leftover Vivalto nursing-home dual Liege','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/la-residence-charlemagne/','fabian.bonnechere@vivaltohome.com','Rue de Bois-de-Breux 53 4020 Liège','tick1783 leftover unused Vivalto maison after CEDRE BLEU; KBO 0870.962.307 Actief; SA; official NBB A-cap YE2025 deposit 2026-00137104 CDN 200 28p; AV 12.05.2026; mère Vivalto Home Belgium; opinion sans réserve; nrec fin 2965277; dividend apport 2950000; controllers 9500=10647702; autres creances JUMP 3231757; FVA DROP 7450000; no RIVAGE; sourced euros assets 16590806 equity 4682133 debt 10724449 marge 2880770 staff 2170037 VTE 34.4 expl 416797 pnl 3106808; FOI ready RIZIV/nrec fin/dividend/controllers'])

buds=[
 ('bud_charlemagne_assets_2025',16590806,'stock','Assets YE2025 16590806 JUMP vs 14292119; tick1783'),
 ('bud_charlemagne_equity_2025',4682133,'stock','Equity 4682133; tick1783'),
 ('bud_charlemagne_debt_2025',10724449,'stock','Debt 10724449 JUMP vs 8435289; tick1783'),
 ('bud_charlemagne_leasing_lt_2025',5088254,'stock','LT credit/leasing 172/3=5088254; option 285000; tick1783'),
 ('bud_charlemagne_fva_2025',7450000,'stock','Immobilisations financieres 7450000 DROP vs 8013256; tick1783'),
 ('bud_charlemagne_autres_creances_2025',3231757,'stock','Autres creances ST 3231757 JUMP vs 93812; tick1783'),
 ('bud_charlemagne_controllers_recv_2025',10647702,'stock','Creances sur administrateurs/controleurs 9500=10647702; tick1783'),
 ('bud_charlemagne_autres_dettes_st_2025',4795689,'stock','Autres dettes ST 4795689 JUMP vs 2281789; tick1783'),
 ('bud_charlemagne_cash_2025',29171,'stock','Cash 29171 DROP vs 100338; tick1783'),
 ('bud_charlemagne_marge_2025',2880770,'realized','Marge bruto 2880770 (A-cap; CA undisclosed); prior had nrec expl 4.97m; tick1783'),
 ('bud_charlemagne_staff_2025',2170037,'realized','Staff 2170037 / VTE 34.4; tick1783'),
 ('bud_charlemagne_expl_2025',416797,'realized','Benefice exploitation 416797; tick1783'),
 ('bud_charlemagne_nrec_fin_2025',2965277,'realized','Produits financiers non recurrents 2965277 drives PnL; tick1783'),
 ('bud_charlemagne_pnl_2025',3106808,'realized','PnL 3106808; dividend apport 2950000 + admin 112106; tick1783'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'LA RESIDENCE CHARLEMAGNE SA JR2025 leftover Vivalto dual (marge 2.88m / nrec fin 2.97m / dividend 2.95m)',eid,'LA RESIDENCE CHARLEMAGNE SA / Vivalto Home Belgium / residents Liege','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-12',2025,2025,2880770,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00137104.pdf','Local leftover Vivalto WZC map WAL Liege Charlemagne — marge 2.88m / nrec-fin + mega dividend extraction twin Meridienne/Braine','Publish CA/RIZIV + nrec fin nature + controllers 10.65m + dividend 2.95m rationale; unit-cost',sid,'strong',hier,'tick1783; assets 16.59m equity 4.68m debt 10.72m FVA 7.45m leasing LT 5.09m marge 2.88m staff 2.17m VTE 34.4 expl 0.42m nrec fin 2.97m pnl 3.11m dividend 2.95m controllers 10.65m; FOI ready not sent; not TE-additive; A-cap CA undisclosed; no RIVAGE'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'LA RESIDENCE CHARLEMAGNE SA 2025: marge 2.88m / staff 2.17m (nrec fin 2.97m + dividend 2.95m + controllers 10.65m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),2880770,10647702,'Envelope=marge 2880770 (A-cap; CA undisclosed); staff 2.17m VTE 34.4; nrec fin 2.97m drives PnL 3.11m; dividend apport 2.95m; controllers recv 10.65m; autres creances JUMP 3.23m; FVA DROP 7.45m; cash DROP; no RIVAGE (negative pledge only)','strong',sid,'MRPA/WZC residents Liege / Vivalto group','Nursing-home care (MRPA/MRS)','Same Vivalto extraction pattern as Meridienne/Braine/Centenaire: nrec fin + mega controller receivables + large dividend',6.6,6.5,5,6.6,'Publish CA/RIZIV; disclose nrec fin + controllers/dividend map; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 2880770 but CA undisclosed; nrec fin 2965277 nature; controllers recv 9500=10647702; dividend apport 2950000; autres creances JUMP 3231757; FVA DROP 7450000 vs 8013256; autres dettes ST 4795689; cash DROP 29171; leasing LT 5088254 + option 285000; ING CAP/FLOOR 5700000; admin 112106','Vivalto Liege Charlemagne with abbreviated schema + nrec-fin-driven PnL + mega controller receivables + 2.95m dividend — opacity on public care-euro path and group cash extraction',8,'LA RESIDENCE CHARLEMAGNE SA / Vivalto Home Belgium SA','fabian.bonnechere@vivaltohome.com','Rue de Bois-de-Breux 53 4020 Liège',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1783; human-send only; twin Meridienne/Braine/Centenaire extraction; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1783':
        row['status']='done'
        row['title']='LA RESIDENCE CHARLEMAGNE SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: LA RESIDENCE CHARLEMAGNE SA leftover unused Vivalto maison Liege after CEDRE BLEU; '
            'KBO 0870.962.307 Actief; live JR2025 official NBB A-cap PDF (227408 bytes 28p deposit 2026-00137104; AV 12.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); sourced euros assets 16590806 equity 4682133 debt 10724449 '
            'marge 2880770 staff 2170037 VTE 34.4 nrec fin 2965277 pnl 3106808 dividend 2950000 controllers 10647702; '
            'FOI ready not sent; NOT CedreBleu continuum; no RIVAGE')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1783 CHARLEMAGNE leftover Vivalto residual; KBO 0870.962.307; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1784 residual dual L5'
        print('updated rq_1783'); break
else:
    raise SystemExit('missing rq_1783')
if not any(r.get('task_id')=='rq_1784' for r in rows):
    rows.append({
        'task_id':'rq_1784','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1784 after 1783 CHARLEMAGNE. Next every-10 is 1790. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other unused Vivalto maisons '
                 '(aux-lilas-de-bonlez / cottage-rose / e-carpentier / floreal / la-maison-dieu / '
                 'jardin-des-chantoirs / le-marronnier / manoir-du-menil) if CDN 200, other IOED/HVZ/IGS. '
                 'Do NOT redo Charlemagne/CedreBleu/BrembloemImmo/AgeDor continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1783 CHARLEMAGNE; NEXT AGB/NSZ-if-200/Bosgroep/BrembloemVZW-if-200/unused-Vivalto-maisons; next every-10 1790'
    })
    print('spawned rq_1784')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1783',1783,'no',
        'tick1783 leftover CHARLEMAGNE Liege; KBO 0870.962.307; NBB YE2025 marge 2880770 staff 2170037 VTE 34.4 nrec fin 2965277 pnl 3106808 dividend 2950000 controllers 10647702 autres creances JUMP 3231757 FVA DROP; no RIVAGE; FOI RIZIV/nrec fin/dividend/controllers; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; unused Vivalto maisons remain; NOT every-10 (next 1790); next rq_1784 AGB/NSZ-if-200/Bosgroep/unused-Vivalto; continuous hole_fill'])
print('OK')
