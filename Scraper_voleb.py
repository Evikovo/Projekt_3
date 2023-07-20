"""
projekt_3.py: závěrečný projekt do Engeto Online Python Akademie

author: Eva Hercíková
email: eva.hercikova@gmail.com
discord: eva.hercikova#1247
"""

import requests
import re
from bs4 import BeautifulSoup
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(dest="Odkaz", help="Odkaz na stránku požadovaného okresu", type=str)
parser.add_argument(dest="soubor", help="Název souboru s výsledky", type=str)

args = parser.parse_args()
#print(args.Odkaz,args.soubor)


stranka_x = requests.get(args.Odkaz)
okresy =("https://volby.cz/pls/ps2017nss/")


def zisk_odkaz (_stranka):

    # otevře zadanau stránku a odkazy z ní uloží do Setu

    odkazy = set()
    soup = BeautifulSoup(_stranka.text, features="html.parser")
    for link in soup.findAll('a'):
        if len(okresy+link.get('href')) > 70:
            odkazy.add(okresy+link.get('href'))
    return(odkazy)
print("Vydrž, stahuji data ze tvé adresy...")

# otevře csv soubor a definuje oddělovač
csv_soubor = open(args.soubor, mode="w", encoding="Windows-1250", newline="")
zapisovac=csv.writer(csv_soubor, delimiter= ",")

def vytvor_radek_dat(_odkaz)->list:

    # otevře odkaz a získá z něj data cislo_okrsu, volici, obalky,platne_hlasy,strany_nazev,strany_hlasů

    _stranka = requests.get(_odkaz)
    soup = BeautifulSoup(_stranka.text, features="html.parser")

# jednotlivé položky tabulky
    cislo_okrs = re.findall(r"\d{6}", _odkaz)

    nazev = re.findall(r"Obec:.*", str(soup))
    nazev_obce =(str(nazev).split((":"))[1])
    nazev_obce_upr=str(nazev_obce[0:(len(nazev_obce)-2)])

    volici = soup.find(headers="sa2").text
    obalky = soup.find(headers="sa3").text
    platne_hlasy = soup.find(headers="sa6").text
    strany_naz = []
    strany_hlas = []

    # první sloupec názvů stran
    for foll in soup.find_all(headers="t1sa1 t1sb2"):
        strany_naz.append(re.sub(r"<.*?>", "", str(foll)))
    # druhý sloupec názvů stran
    for foll in soup.find_all(headers="t2sa1 t2sb2"):
        strany_naz.append(re.sub(r"<.*?>", "", str(foll)))

    #prvni sloupec stran
    for foll in soup.find_all(headers="t1sa2 t1sb3"):
        strany_hlas.append(re.sub(r"<.*?>", "", str(foll)))
    #druhý sloupec stran
    for foll in soup.find_all(headers="t2sa2 t2sb3"):
        strany_hlas.append(re.sub(r"<.*?>", "", str(foll)))

    vystup=list((cislo_okrs[0], nazev_obce_upr, volici, obalky, platne_hlasy))
    for polozka in strany_hlas:
        vystup.append(polozka)
    return vystup, strany_naz


# zápis do csv

pruchod = 0

for tabulka in zisk_odkaz(stranka_x):
    vysledek = list(vytvor_radek_dat(tabulka))
    if pruchod == 0:
        zahlavi = ["číslo okrsku", "název obce", "počet voličů v seznamu", "vydané obálky", "platné hlasy"] + vysledek[1]
        zapisovac.writerow(zahlavi)
        pruchod = 1
        print("...jde to pomalu, ale jistě, už odhaduji výsledky voleb ;o)")

    zapisovac.writerow(vysledek[0])

csv_soubor.close()

print("*"*50)
print("Zapsáno, koukni do souboru", args.soubor)
print("*"*50)