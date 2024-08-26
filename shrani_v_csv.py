import csv
import re
from orodja import *
from pridobi_vse_podatke import *
from pridobi_world_cup import *

#UPORABILA SEM FUNKCIJO IZ ORODJI IN SEZNAMA IZ pridobi_vse_podatke.py TER pridobi_world_cup.py

#to funkcijo sem uporabila, da sem dala v csv vse smucarske skakalce
zapisi_csv(smucarski_skakalci, ['koda', 'ime', 'priimek', 'id', 'rojstno_leto', 'drzava', 'klub', 'status', 'spol', 'smuci', 'prebivalisce'], 'smucarski_skakalci.csv')

#to funkcijo sem uporabila, da sem dala v csv vse podatke za world cup
zapisi_csv(w_smucarski_skakalci, ['koda', 'ime', 'priimek', 'skupna_uvrstitev', 'skupno_st_tock', 'poleti_uvrstitev', 'poleti_st_tock', 'drzava', 'leto', 'spol'], 'world_cup.csv')