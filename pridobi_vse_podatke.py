import requests
import os
import time
import re

#da sem dobila dol vseh 9 strani s smucarskimi skakalci
# for i in range(9):
#     url = f"https://www.fis-ski.com/DB/ski-jumping/biographies.html?lastname=&firstname=&sectorcode=JP&gendercode=&birthyear=&skiclub=&skis=&nationcode=&fiscode=&status=&search=true&limit=1000&offset={i * 1000}"
#     odziv = requests.get(url)
#     if odziv.status_code == 200:
#         print(url)
#         with open(os.path.join("smucarji", f"smucarji_stran_{i}.html"), "w", encoding ="utf8") as dat:
#             dat.write(odziv.text)
#     else:
#         print("Prišlo je do napake")
        






#preverimo koliko je vseh smucarskih skakalcev in  dobimo ven njihove kode
kode = []
for i in range(9):
    with open(f"smucarji_stran_{i}.html") as d:
        vsebina = d.read()
        niz_za_kodo = r'<a class="table-row" href="https://www\.fis-ski\.com/DB/general/athlete-biography\.html\?sectorcode=JP&amp;competitorid=(?P<koda>\d+)" target="_self">'
        for najdba in re.finditer(niz_za_kodo, vsebina):
            kode.append(int(najdba["koda"]))
    print (len(kode))


count = 0
for koda in kode:
    url = f"https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=JP&competitorid={koda}&type=result&categorycode=&sort=&place=&disciplinecode=&position=&limit=1000"
    odgovor = requests.get(url)    
    if odgovor.status_code == 200:
        count += 1
        with open(os.path.join("posamezni_smucarji", f"smucar_{koda}.html"), "w", encoding ="utf8") as dat:
            dat.write(odgovor.text)
        time.sleep(1)
    else:
        print("url")
        break

print(count)            