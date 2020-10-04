from __future__ import unicode_literals
from hazm import *


def normalizing():

    with open("./group8text.txt", 'r', encoding="utf8") as file:
        text = file.read()

        # print("Before normalize")
        # print(text)
        # print("--------------------------------------------------------------------")
        # print("After normalize")

        normalizer = Normalizer(token_based=True)
        normal_text = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))

        write_text_file = open("./group8NormalizedText.txt", "wb")
        write_text_file.write(normal_text.encode("utf-8"))
        write_text_file.close()

        return normal_text


def split_paragraphs(text):

    paragraphs = text.split("پاراگراف")[1:]

    for i in range(len(paragraphs)):
        paragraphs[i] = paragraphs[i][2:]

    return paragraphs


if __name__ == "__main__":
    normalized_txt = normalizing()
    paragraphs_list = split_paragraphs(normalized_txt)
