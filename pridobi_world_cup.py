import  requests
import os
import re
import json


letnice = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
#s to funkcijo sem si shranila končne rezultate world cupa v smucarskih skokih zadnjih petih sezon pri moškoih in ženskah


# for leto in letnice:
#     url = f"https://www.fis-ski.com/DB/general/cup-standings.html?sectorcode=JP&seasoncode={leto}&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode="
#     odziv = requests.get(url)
#     if odziv.status_code == 200:
#         print(url)
#         with open(os.path.join("world_cup", f"world_cup_stran_{leto}.html"), "w", encoding ="utf8") as dat:
#             dat.write(odziv.text)
#     else:
#         print("Prišlo je do napake")




#funkcija, ki pridobi kode od vseh smucarskih skakalcev----> podobno kot sem naredila, ko sem zajemala podatke vseh smucarskih skakalcev
kode = []
for leto in letnice:
    with open(f"world_cup/world_cup_stran_{leto}.html") as d:
        vsebina = d.read()
        niz_za_kodo = r'<a class="table-row  reset-padding" href="https://www\.fis-ski\.com/DB/general/athlete-biography\.html\?sectorcode=JP&competitorid=(?P<koda>\d+)&type=cups&cupcode=WC" target="_self">'
        for najdba in re.finditer(niz_za_kodo, vsebina):
            kode.append(int(najdba["koda"]))
print (len(kode))

#našlo jih je 926 na vseh 10ih straneh





from izlusci_world_cup import *

#s to funkcijo sem preverila če pravilno deluje funkcija izlusci_smucarja

# count = 0
# for leto in letnice:
#     with open(f"world_cup/world_cup_stran_{leto}.html", encoding ="utf8") as dat:
#         vsebina = dat.read()
#         for vzorec in vzorec_smucarjev.finditer(vsebina):
#             smucar = izlusci_smucarja(vzorec.group())
#             smucar['leto'] = leto
#             smucar['spol'] = 'M'
#             print(smucar)
#             count += 1
# print(count)




#S TO FUNKCIJO SEM VSE PODATKE DALA V JSON DATOTEKO

# w_smucarski_skakalci = []
# count = 0
# for leto in letnice:
#     with open(f"world_cup/world_cup_stran_{leto}.html", encoding ="utf8") as dat:
#         vsebina = dat.read()
#         for vzorec in vzorec_smucarjev.finditer(vsebina):
#             smucarski_skakalec = izlusci_smucarja(vzorec.group())
#             smucarski_skakalec['leto'] = leto
#             smucarski_skakalec['spol'] = 'M'
#             count += 1
#             w_smucarski_skakalci.append(smucarski_skakalec)
# print(count)
# with open("world_cup.json", "w", encoding='utf-8') as d:
#     json.dump(w_smucarski_skakalci, d, ensure_ascii=False, indent=4) 




#TO FUNKCIJO SEM UPORABILA V SHRANI, KER SEM POTREBOVALA w_smucarski_skakalci

w_smucarski_skakalci = []
for leto in letnice:
    with open(f"world_cup/world_cup_stran_{leto}.html", encoding ="utf8") as dat:
        vsebina = dat.read()
        for vzorec in vzorec_smucarjev.finditer(vsebina):
            smucarski_skakalec = izlusci_smucarja(vzorec.group())
            smucarski_skakalec['leto'] = leto
            smucarski_skakalec['spol'] = 'M'
            w_smucarski_skakalci.append(smucarski_skakalec)