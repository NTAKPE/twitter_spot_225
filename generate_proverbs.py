#! python3
# /Users/jeremientakpe/TwitterSpotBot/generate_proverbs.py

import random
from data import subs, chin, fran, kaby, arab, asie

def getfamily():
    #Get proverbs family randomly
    prov_family = [("Proverbe subsaharien", subs), ("Proverbe chinois", chin), ("Proverbe français", fran),\
         ("Proverbe kabyle", kaby), ("Proverbe arabe", arab), ("Proverbe d'Asie", asie)]
    
    return random.choice(prov_family)

def getproverb(fam):
    #Get proverbs randomly from a family
    return random.choice(fam)