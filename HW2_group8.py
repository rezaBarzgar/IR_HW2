from __future__ import unicode_literals
from hazm import *
with open("./group8text.txt", 'r', encoding="utf8") as file:
    text = file.read()
    print("Before normalize")
    print(text)


    print("--------------------------------------------------------------------")
    print("After normalize")
    normalizer = Normalizer(token_based=True)
    normaltext = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))
    print(normaltext)



