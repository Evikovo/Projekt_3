PROJEKT Č.3 - PYTHON
Toto je závěrečný projekt Python Akademie od Engeta.

Popis projektu
-tento projekt slouží ke scrapování výsledků parlamentních volem z roku 2017. 

Instalace knihoven
K funkčnímu spuštění projektu je třeba mít nainstalované knihovny, které jsou přesněji specifikované v souboru requirements.txt.
Pro instalaci knihoven je vhodné použít nové virtuální prostředí, do něhož požadované knihovny nainstalujete následujícím příkazem:

pip3 install -r requirements.txt

Spuštění projektu
provedeme spuštěním souboru Scraper_voleb.py v terminálu.
Pro správné spuštění je třeba zadat 2 argumenty
1. argument - adresa zvolené oblasti pro analýzu voleb vložená do uvozovek
2. argument - název výsledného souboru s příponou .csv

Příklad spuštění:
python3 Scraper_voleb.py "1.argument" 2.argument

Ukázka průběhu:
$ python3 Scraper_voleb.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103" vysledky_Liberec.csv
Vydrž, stahuji data ze tvé adresy...
...jde to pomalu, ale jistě, už odhaduji výsledky voleb ;o)
**************************************************
Zapsáno, koukni do souboru vysledky_Liberec.csv
**************************************************
 
Ukázka částečného výstupu:
název obce,počet voličů v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
564460, Šimonovice,850,627,625,99,0,0,30,102,20,10,2,12,0,1,72,1,49,149,0,2,12,0,5,2,0,54,3
530433, Kunratice,298,181,179,3,5,0,13,50,17,0,1,0,0,0,4,0,0,48,0,2,2,0,0,0,2,32,0
544345, Proseč pod Ještědem,300,217,216,17,0,0,10,24,19,1,2,5,0,1,32,1,6,64,0,0,3,0,2,2,0,27,0
564052, Hlavice,193,147,147,13,0,0,13,16,21,5,1,1,0,0,13,0,3,33,0,0,6,0,0,0,0,20,2
....




