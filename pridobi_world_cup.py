import  requests
import os
import re


letnice = [2015, 2016]#, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
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




#s to funkcijo sem preverila če pravilno deluje funkcija izlusci_smucarja
from izlusci_world_cup import *

count = 0
#for spol in spola:
for leto in letnice:
    with open(f"world_cup/world_cup_stran_{leto}.html", encoding ="utf8") as dat:
        vsebina = dat.read()
        for vzorec in vzorec_smucarjev.finditer(vsebina):
            smucar = izlusci_smucarja(vzorec.group())
            smucar['leto'] = leto
            smucar['spol'] = 'M'
            print(smucar)
            count += 1
print(count)