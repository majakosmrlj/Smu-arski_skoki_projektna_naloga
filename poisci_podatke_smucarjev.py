import re

with open("smucarski_skakalci.html") as dat:
    besedilo = dat.read()
    niz_za_kodo = r'<a class="table-row" href="https://www\.fis-ski\.com/DB/general/athlete-biography\.html\?sectorcode=JP&amp;competitorid=(?P<koda>\d+)" target="_self">'
    niz_za_id = r'<div class="g-lg g-md g-sm-24 g-xs-24 justify-left">(?P<id>\d+)</div>'
    niz_za_ime = r'<div class="g-lg g-md g-sm g-xs justify-left flex-sm-wrap flex-xs-wrap">(?P<ime>.*?)</div>'
    niz_za_drzavo = r'<span class="country__name-short">(?P<drzava>\D+)</span>'
    kode = []
    id_ji = []
    imena = []
    smucarji = []
    drzave = []
    for najdba in re.finditer(niz_za_kodo, besedilo):
        kode.append(int(najdba["koda"]))
    for najdba in re.finditer(niz_za_id, besedilo):
        id_ji.append(int(najdba["id"]))
    for najdba in re.finditer(niz_za_ime, besedilo):
        imena.append(najdba["ime"])
    for najdba in re.finditer(niz_za_drzavo, besedilo):
            drzave.append(najdba["drzava"])
    for podatki in zip(kode, id_ji, imena, drzave):
        smucarji.append(podatki)
    print (smucarji, len(smucarji))


vzorec_bloka = re.compile(
     r'<a class="table-row".*?'
     r'</a>'
     flags=re.DOTALL
)