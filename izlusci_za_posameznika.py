# import re


# def izlusci_smucarja(koda):
#     with open(f"posamezni_smucarji/smucar{koda}.html") as dat:
#         besedilo = dat.read()

#     # izluscimo igralce
#     igralci_re = re.compile(
#         r'title-cast-item__actor" href="/name/nm(?P<id>\d+)/\?ref_=tt_cl_t_\d+" class="sc-bfec09a1-1 gCQkeh">(?P<ime>.+?)</a>'
#     )
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