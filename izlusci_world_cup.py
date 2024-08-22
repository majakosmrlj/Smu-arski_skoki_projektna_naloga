import re

vzorec_smucarjev = re.compile(
    r'<a class="table-row  reset-padding" href="https://www\.fis-ski\.com/DB/general/athlete-biography\.html\?sectorcode=JP&competitorid=(?P<koda>.*?)&type=cups&cupcode=WC" target="_self">.*?'
    r'<div class="g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top">(?P<priimek_in_ime>.*?)</div>.*?'
    r'<span class="country__name-short">(?P<drzava>.*?)</span>.*?'
    #za točke
    r'<div class="g-xs-9 hidden-sm-up justify-left">ALL</div>\s*?'
    r'<div class="g-md-4 g-lg-3 hidden-sm hidden-xs">&nbsp;</div>\s*?'
    r'<div class="g-xs-5 g-sm-4 g-md-5 g-lg-8 justify-right bold">(?P<skupna_uvrstitev>.*?)</div>\s*?'
    r'<div class="g-xs-1 g-md-1 hidden-sm hidden-lg">&nbsp;</div>\s*?'
    r'<div class="pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold">(?P<skupno_st_tock>.+?)</div>.*?'
    #za smucarske polete
    r'<div class="g-xs-9 hidden-sm-up justify-left">SF</div>\s*?'
    r'<div class="g-md-4 g-lg-3 hidden-sm hidden-xs">&nbsp;</div>\s*?'
    r'<div class="g-xs-5 g-sm-4 g-md-5 g-lg-8 justify-right">(?P<poleti_uvrstitev>.*?)</div>\s*?'
    r'<div class="g-xs-1 g-md-1 hidden-sm hidden-lg">&nbsp;</div>\s*?'
    r'<div class="pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right">(?P<poleti_st_tock>.*?)</div>',
    flags = re.DOTALL
)



def izlusci_smucarja(vsebina):
    smucar = vzorec_smucarjev.search(vsebina).groupdict()
    smucar["koda"] = int(smucar['koda'])
    celotno_ime = smucar["priimek_in_ime"].split()
    imena = celotno_ime[1:]
    smucar['priimek'] = celotno_ime[0].capitalize()
    smucar['ime'] = ' '.join(imena)
    del smucar['priimek_in_ime']
    #popravki za skupno uvrstitev
    if not smucar['poleti_uvrstitev'].isdigit():
        smucar['poleti_uvrstitev'] = None
    else:
        smucar['poleti_uvrstitev'] = int(smucar['poleti_uvrstitev'])

    #popravki za skupne točke
    if smucar['poleti_st_tock'] == '---':
        smucar['poleti_st_tock'] = 0
    else:
        smucar['poleti_st_tock'] = int(smucar['poleti_st_tock'].replace("'", ""))
    smucar['drzava'] = smucar['drzava']

    #popravki za uvrstitev v poletih
    if not smucar['skupna_uvrstitev'].isdigit():
        smucar['skupna_uvrstitev'] = None
    else:
        smucar['skupna_uvrstitev'] = int(smucar['skupna_uvrstitev'])

    #popravki za točke v poletih
    if smucar['skupno_st_tock'] == '---':
        smucar['skupno_st_tock'] = 0
    else:
        smucar['skupno_st_tock'] = int(smucar['skupno_st_tock'].replace("'", ""))
    smucar['drzava'] = smucar['drzava']




    # #za klub
    # if smucar["klub"] == '':
    #     smucar['klub'] = None
    # else:
    #     smucar['klub'] = smucar["klub"]

    # smucar['drzava'] = smucar["drzava"]
    # smucar['id'] = int(smucar["id"])
    # smucar['status'] = smucar["status"]
    # smucar['spol'] = smucar["spol"]

    # #za prebivalisce
    # if not smucar['prebivalisce'].isalpha():
    #     smucar['prebivalisce'] = None
    # else:
    #     smucar['prebivalisce'] = smucar["prebivalisce"]

    # #za smuci
    # if not smucar['smuci'].isalpha():
    #     smucar['smuci'] = None
    # else:
    #     smucar['smuci'] = smucar["smuci"]

    # #za rojstni dan
    # rojstno_leto = vzorec_rojstnega_leta.search(vsebina)
    # if rojstno_leto["rojstno_leto"] == '&nbsp;':
    #     smucar['rojstno_leto'] = None
    # else:
    #     smucar['rojstno_leto'] = int(rojstno_leto["rojstno_leto"][-4:])
        
    return dict(smucar)