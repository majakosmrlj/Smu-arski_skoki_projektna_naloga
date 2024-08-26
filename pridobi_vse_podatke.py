import requests
import os
import time
import re
import json

#Da sem pridobila vseh 9 strani s smučarskimi skakalci

# for i in range(9):
#     url = f"https://www.fis-ski.com/DB/ski-jumping/biographies.html?lastname=&firstname=&sectorcode=JP&gendercode=&birthyear=&skiclub=&skis=&nationcode=&fiscode=&status=&search=true&limit=1000&offset={i * 1000}"
#     odziv = requests.get(url)
#     if odziv.status_code == 200:
#         print(url)
#         with open(os.path.join("smucarji", f"smucarji_stran_{i}.html"), "w", encoding ="utf8") as dat:
#             dat.write(odziv.text)
#     else:
#         print("Prišlo je do napake")
        



#Preverimo koliko je vseh smučarskih skakalcev in dobimo ven njihove kode

kode = []
for i in range(9):
    with open(f"smucarji/smucarji_stran_{i}.html") as d:
        vsebina = d.read()
        niz_za_kodo = r'<a class="table-row" href="https://www\.fis-ski\.com/DB/general/athlete-biography\.html\?sectorcode=JP&amp;competitorid=(?P<koda>\d+)" target="_self">'
        for najdba in re.finditer(niz_za_kodo, vsebina):
            kode.append(int(najdba["koda"]))
print (len(kode))




#Shranjevanje vseh spletnih strani za posamezne smucarske skakalce

# count = 0
# for koda in kode:
#     url = f"https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid={koda}&type=result&categorycode=&sort=&place=&disciplinecode=&position=&limit=1000"
#     odgovor = requests.get(url)    
#     if odgovor.status_code == 200:
#         count += 1
#         with open(os.path.join("posamezni_smucarji", f"smucar_{koda}.html"), "w", encoding ="utf8") as dat:
#             dat.write(odgovor.text)
#         time.sleep(1)
#     else:
#         print("url")
#         break
# print(count)            





from izlusci_za_posameznika import *


#TO FUNKCIJO SEM UPORABILA, DA SEM PREVERILA ČE PRAVILNO DELUJE FUNKCIJA IZLUSCI_POSAMEZNEGA_SMUCARJA

# count = 0
# for koda in kode[:100]:
#     with open(f"smucarji/posamezni_smucarji/smucar_{koda}.html", encoding ="utf8") as dat:
#         vsebina = dat.read()
#         for vzorec in vzorec_vseh_podatkov.finditer(vsebina):
#             print(izlusci_posameznega_smucarja(vsebina))
#             count += 1
# print(count)




#S TO FUNKCIJO SEM SHRANILA PODATKE V JSON DATOTEKO

# smucarski_skakalci = []
# count = 0
# for koda in kode:
#     with open(f"smucarji/posamezni_smucarji/smucar_{koda}.html", encoding ="utf8") as dat:
#         vsebina = dat.read()
#         for vzorec in vzorec_vseh_podatkov.finditer(vsebina):
#             smucarski_skakalec = izlusci_posameznega_smucarja(vsebina)
#             count += 1
#             smucarski_skakalci.append(smucarski_skakalec)
# print(count)
# with open("smucarski_skakalci.json", "w", encoding='utf-8') as d:
#     json.dump(smucarski_skakalci, d, ensure_ascii=False, indent=4) 




#TO FUNKCIJO SEM UPORABILA V shrani_v_csv, SAJ SEM POTREBOVALA SEZNAM smucarski_skakalci

smucarski_skakalci = []
for koda in kode:
    with open(f"smucarji/posamezni_smucarji/smucar_{koda}.html", encoding ="utf8") as dat:
        vsebina = dat.read()
        for vzorec in vzorec_vseh_podatkov.finditer(vsebina):
            smucarski_skakalec = izlusci_posameznega_smucarja(vsebina)
            smucarski_skakalci.append(smucarski_skakalec)
