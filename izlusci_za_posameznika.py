import re
from collections import OrderedDict


vzorec_vseh_podatkov = re.compile(
    r'<h1 class="athlete-profile__name">(?P<ime>.*?)<span class="athlete-profile__lastname">(?P<priimek>.*?)</span>.*?'
    r'<div class="athlete-profile__team spacer__section">(?P<klub>.*?)</div>.*?'
    r'<span class="country__name">(?P<drzava>.*?)</span>.*?'
    #za pridobitev fis code
    r'<li class="profile-info__entry profile-info__entry_visible_xs" id="FIS Code">\s*?'
    r'<span class="profile-info__field">FIS Code</span>\s*?'
    r'<span class="profile-info__value">(?P<id>.*?)</span>.*?'
    #za trenutni status
    r'<li class="profile-info__entry profile-info__entry_visible_xs" id="Status">\s*?'
    r'<span class="profile-info__field">Status</span>\s*?'
    r'<span class="profile-info__value">(?P<status>.*?)</span>.*?'
    #spol
    r'<li class="profile-info__entry" id="Gender">\s*?'
    r'<span class="profile-info__field">Gender</span>\s*?'
    r'<span class="profile-info__value">(?P<spol>.+?)</span>.*?'
    #prebivališče
    r'<li class="profile-info__entry" id="Residence">\s*?'
    r'<span class="profile-info__field">Residence</span>\s*?'
    r'<span class="profile-info__value">(?P<prebivalisce>.+?)</span>.*?'
    #smuči
    r'<li class="profile-info__entry" id="Skis">\s*?'
    r'<span class="profile-info__field">Skis</span>\s*?'
    r'<span class="profile-info__value">(?P<smuci>.+?)</span>.*?'
    r'<use xlink:href="https://www\.fis-ski\.com/DB/general/athlete-biography\.html\?sectorcode=JP&competitorid=(?P<koda>.*?)&type=result&categorycode=&sort=&place=&disciplinecode=&position=&limit=1000#filter"></use>',
    flags = re.DOTALL
)

vzorec_rojstnega_leta = re.compile(
    r'<li class="profile-info__entry profile-info__entry_visible_xs" id="Birthdate">\s*?'
    r'<span class="profile-info__field">Birthdate</span>\s*?'
    r'<span class="profile-info__value">(?P<rojstno_leto>.*?)</span>',
    flags = re.DOTALL
)



def izlusci_posameznega_smucarja(vsebina):
    smucar = vzorec_vseh_podatkov.search(vsebina).groupdict()
    smucar["koda"] = int(smucar['koda'])
    smucar['ime'] = smucar["ime"].strip()
    smucar['priimek'] = smucar["priimek"].strip().capitalize()

    #popravki za klub
    if smucar["klub"] == '':
        smucar['klub'] = None
    else:
        smucar['klub'] = smucar["klub"]

    smucar['drzava'] = smucar["drzava"]
    smucar['id'] = int(smucar["id"])
    smucar['status'] = smucar["status"]
    smucar['spol'] = smucar["spol"]

    #popravki za prebivalisce
    if not smucar['prebivalisce'].isalpha():
        smucar['prebivalisce'] = None
    else:
        smucar['prebivalisce'] = smucar["prebivalisce"]

    #popravki za smuci
    if not smucar['smuci'].isalpha():
        smucar['smuci'] = None
    else:
        smucar['smuci'] = smucar["smuci"]

    #popravki za rojstni dan
    rojstno_leto = vzorec_rojstnega_leta.search(vsebina)
    if rojstno_leto["rojstno_leto"] == '&nbsp;':
        smucar['rojstno_leto'] = None
    else:
        smucar['rojstno_leto'] = int(rojstno_leto["rojstno_leto"][-4:])
        
    
    #za urediti slovar v željen vrstni red
    smucar = OrderedDict(
        koda=smucar["koda"],
        ime=smucar["ime"],
        priimek=smucar["priimek"],
        id = smucar['id'],
        rojstno_leto= smucar["rojstno_leto"],
        drzava = smucar["drzava"],
        klub = smucar["klub"],
        status = smucar["status"],
        spol = smucar["spol"],
        smuci = smucar["smuci"],
        prebivalisce = smucar["prebivalisce"]
    )
    
    return dict(smucar)