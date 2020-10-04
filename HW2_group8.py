from __future__ import unicode_literals
from hazm import *


def normalizing():
    with open("./group8text.txt", 'r', encoding="utf8") as file:
        text = file.read()
        print("Before normalize")
        print(text)

        print("--------------------------------------------------------------------")
        print("After normalize")
        normalizer = Normalizer(token_based=True)
        normaltext = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))
        print(normaltext)
        write_text_file = open("./group8NormalizedText.txt", "wb")
        write_text_file.write(normaltext.encode("utf-8"))
        write_text_file.close()

# testing for sobhan

if __name__ == "__main__":
    normalizing()
