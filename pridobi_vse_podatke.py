import requests
import os

for i in range(9):
    url = f"https://www.fis-ski.com/DB/ski-jumping/biographies.html?lastname=&firstname=&sectorcode=JP&gendercode=&birthyear=&skiclub=&skis=&nationcode=&fiscode=&status=&search=true&limit=1000&offset={i * 1000}"
    odziv = requests.get(url)
    if odziv.status_code == 200:
        print(url)
        with open(os.path.join("smucarji", f"smucarji_stran_{i}.html"), "w", encoding ="utf8") as dat:
            dat.write(odziv.text)
    else:
        print("Prišlo je do napake")
        

