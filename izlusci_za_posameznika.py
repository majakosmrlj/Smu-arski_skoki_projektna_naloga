import re
import os
import json
import html
from collections import OrderedDict


vzorec_vseh_podatkov = re.compile(
    r'<h1 class="athlete-profile__name">(?P<ime>.*?)<span class="athlete-profile__lastname">(?P<priimek>.*?)</span>.*?'
    r'<div class="athlete-profile__team spacer__section">(?P<klub>.*?)</div>.*?'
    r'<span class="country__name">(?P<drzava>.*?)</span>.*?'
    #za pridobitef fis code
    r'<li class="profile-info__entry profile-info__entry_visible_xs" id="FIS Code">\s*?'
    r'<span class="profile-info__field">FIS Code</span>\s*?'
    r'<span class="profile-info__value">(?P<id>.*?)</span>.*?'
    #za pridobitev rojstnega dneva
    r'<li class="profile-info__entry profile-info__entry_visible_xs" id="Birthdate">\s+?'
    r'<span class="profile-info__field">Birthdate</span>\s*?'
    r'<span class="profile-info__value">(?P<rojstni_dan>.*?)</span>.*?'
    #za starost
    r'<li class="profile-info__entry" id="Age">\s*?'
    r'<span class="profile-info__field">Age</span>\s*?'
    r'<span class="profile-info__value">(?P<starost>.*?)</span>.*?'
    #za trenutni status
    r'<li class="profile-info__entry profile-info__entry_visible_xs" id="Status">\*?'
    r'<span class="profile-info__field">Status</span>\s*?'
    r'<span class="profile-info__value">(?P<status>.*?)</span>.*?'
    #spol
    r'<li class="profile-info__entry" id="Gender">\s*?'
    r'<span class="profile-info__field">Gender</span>\s*?'
    r'<span class="profile-info__value">(?P<spol>.+?)</span>.*?',
    flags = re.DOTALL
)
#za rd je lahko &nbsp;___PAZI

def izlušci_posameznega_smuvcarja(vsebina):
    smucar = vzorec_vseh_podatkov.search(vsebina).groupdict()
    smucar['ime'] = smucar["ime"].strip()
    smucar['priimek'] = smucar["priimek"].strip().capitalize()
    smucar['klub'] = smucar["klub"]
    smucar['drzava'] = smucar["drzava"]
    smucar['id'] = int(smucar["id"])
    smucar['rojstni_dan'] = int(smucar["rojstni_dan"])
    smucar['starost'] = int(smucar["starost"])
    smucar['status'] = smucar["status"]
    smucar['spol'] = smucar["spol"]
    return dict(smucar)

# smucar = OrderedDict(
#     ime=smucar["ime"],

# )



#131309
koda = 8

def izlusci_smucarja(koda):
    with open(f"smucarji/posamezni_smucarji/smucar_{koda}.html") as dat:
        besedilo = dat.read()
    # izluscimo ime in priimek)
        ime_re = re.compile(
            r'<h1 class="athlete-profile__name">(?P<ime>.*?)<span class="athlete-profile__lastname">(?P<priimek>.*?)</span>',
            flags=re.DOTALL
            )
        id_re = re.compile(
            r'<li class="profile-info__entry profile-info__entry_visible_xs" id="FIS Code">\s*?'
            r'<span class="profile-info__field">FIS Code</span>\s*?'
            r'<span class="profile-info__value">(?P<id>.*?)</span>.*?',
            flags = re.DOTALL
            )
        rojstni_dan_re = re.compile(
            r'<li class="profile-info__entry profile-info__entry_visible_xs" id="Birthdate">\s+?'
            r'<span class="profile-info__field">Birthdate</span>\s*?'
            r'<span class="profile-info__value">(?P<rojstni_dan>.*?)</span>.*?',
            flags = re.DOTALL
            )
        ime = []
        priimek = []
        id = []
        rojstni_dan = []
        for najdba in ime_re.finditer(besedilo):
            ime.append(str(najdba["ime"]).strip())
            priimek.append(str(najdba["priimek"]).strip().capitalize())
        for najdba in id_re.finditer(besedilo):
            id.append(int(najdba["id"]))
        for najdba in rojstni_dan_re.finditer(besedilo):
            rojstni_dan.append((najdba["rojstni_dan"]))
        print(ime, priimek, id, rojstni_dan)

izlusci_smucarja(koda)



#pazi, da je isti vrstni red
















#ZA POMOC, OD PROFESORJA
#     igralci = []
#     for najdba in igralci_re.finditer(besedilo):
#         igralci.append((najdba["id"], najdba["ime"]))
#     if len(igralci) == 0:
#         print("napaka: igralci", id)

#     # izluscimo leto, oznako in cas
#     lastosti_re = re.compile(
#         r'href="/title/tt\d+/releaseinfo\?ref_=tt_ov_rdat">(\d+)</a></li>'
#         r"(.*?)"
#         r'<li role="presentation" class="ipc-inline-list__item">((\d+?h ?)?(\d+?m)?)</li>'
#         )
#     najdba = lastosti_re.search(besedilo)
#     leto = ""
#     oznaka = ""
#     cas = ""
#     if najdba is not None:
#         leto = najdba.group(1)
#         oznaka_del = najdba.group(2)
#         oznaka_re = re.compile(r'<li role="presentation".+?tt_.+?">(.+?)</a></li>')
#         najdba2 = oznaka_re.search(oznaka_del)
#         if najdba2 is not None:
#             oznaka = najdba2.group(1)
#         cas_tekst = najdba.group(3)
#         # spremenimo cas v minute
#         cas = 0
#         ure_re = re.compile(r"(\d*)h")
#         najdba3 = ure_re.search(cas_tekst)
#         if najdba3 is not None:
#             cas = 60 * int(najdba3.group(1))
#         minute_re = re.compile(r"(\d*)m")
#         najdba3 = minute_re.search(cas_tekst)
#         if najdba3 is not None:
#             cas += int(najdba3.group(1))
#  else:
#         print("napaka: lastnosti", id)

#     # izluscimo reziserje
#     reziserji = []
#     reziserji_re = re.compile(r'directors?":\[(.+?)\]')
#     najdba = reziserji_re.search(besedilo)
#     if najdba is not None:
#         reziser_re = re.compile(
#             r'{"@type":"Person","url":"https://www.imdb.com/name/nm(\d+)/","name":"(.+?)"}'
#         )
#         for najdba2 in reziser_re.finditer(najdba.group(1)):
#             id_osebe = najdba2.group(1)
#             ime = najdba2.group(2)
#             reziserji.append((id_osebe, ime))
#         if len(reziserji) == 0:
#             print("napaka: reziserji", id)
#     else:
#         print("napaka: reziserji", id)

#     # izluscimo oceno
#     rating_re = re.compile(r'__aggregate-rating__score".+?>(\d.\d)</span>')
#     najdba = rating_re.search(besedilo)
#     if najdba is not None:
#         ocena = najdba.group(1)
#     else:
#         print("napaka: ocena", id)
    
#         return (igralci, reziserji, ocena, cas, leto, oznaka)


# html_content = "primer_posamezne_strani_peter_prev.html"

# from bs4 import BeautifulSoup

# def extract_athlete_info(html_content):
    
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Extracting the athlete's name
#     name = soup.find('h1', class_='athlete-profile__name').strip().split()
#     first_name = name[0]
#     last_name = name[1] if len(name) > 1 else ''

#     # Extracting other details
#     team = soup.find('div', class_='athlete-profile__team').text.strip()
#     country = soup.find('span', class_='country__name').text.strip()
    
#     profile_info = {}
#     for entry in soup.find_all('li', class_='profile-info__entry'):
#         field = entry.find('span', class_='profile-info__field').text.strip()
#         value = entry.find('span', class_='profile-info__value').text.strip()
#         profile_info[field] = value

#     athlete_info = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'team': team,
#         'country': country,
#         'FIS_code': profile_info.get('FIS Code', ''),
#         'birthdate': profile_info.get('Birthdate', ''),
#         'age': profile_info.get('Age', ''),
#         'status': profile_info.get('Status', ''),
#         'gender': profile_info.get('Gender', ''),
#         'marital_status': profile_info.get('Marital Status', ''),
#         'children': profile_info.get('Children', ''),
#         'occupation': profile_info.get('Occupation', ''),
#         'nickname': profile_info.get('Nickname', ''),
#         'residence': profile_info.get('Residence', ''),
#         'languages': profile_info.get('Languages', ''),
#         'hobbies': profile_info.get('Hobbies', ''),
#         'skis': profile_info.get('Skis', ''),
#         'boots': profile_info.get('Boots', ''),
#     }

#     return athlete_info

#athlete_info = extract_athlete_info(html_content)
#print(athlete_info)
