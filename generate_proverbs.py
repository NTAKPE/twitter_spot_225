#! python3
# /Users/jeremientakpe/TwitterSpotBot/generate_proverbs.py

import random
from data import subs, chin, fran, kaby

def getfamily():
    #Get proverbs family randomly
    prov_family = [("Proverbe subsaharien", subs), ("Proverbe chinois", chin), ("Proverbe français", fran),\
         ("Proverbe kabyle", kaby)]
    
    return random.choice(prov_family)

def getproverb(fam):
    #Get proverbs randomly from a family
    return random.choice(fam)