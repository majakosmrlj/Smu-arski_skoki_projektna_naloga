import csv
from orodja import *
from pridobi_vse_podatke import *




zapisi_csv(smucarski_skakalci, ['koda', 'ime', 'priimek', 'id', 'rojstno_leto', 'drzava', 'klub', 'status', 'spol', 'smuci', 'prebivalisce'], 'smucarski_skakalci.csv')