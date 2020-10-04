from __future__ import unicode_literals
from hazm import *
import xlwt
from xlwt import Workbook


def normalizing():
    with open("./group8text.txt", 'r', encoding="utf8") as file:
        text = file.read()

        # print("Before normalize")
        # print(text)
        # print("--------------------------------------------------------------------")
        # print("After normalize")

        normalizer = Normalizer(token_based=True)
        normal_text = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))
        sentences_count(normal_text)

        write_text_file = open("./group8NormalizedText.txt", "wb")
        write_text_file.write(normal_text.encode("utf-8"))
        write_text_file.close()

        return normal_text


def sentences_count(paragraphs):
    paragraphs_list = split_paragraphs(paragraphs)

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 1, 'شماره پاراگراف')
    sheet1.write(0, 2, 'تعداد جملات')
    sheet1.write(0, 3, 'تعداد کلمات')
    sheet1.write(0, 4, 'تعداد فعل ها')
    sheet1.write(0, 5, 'تعداد اسم ها')

    wb.save('HW2.xls')


def split_paragraphs(text):

    paragraphs = text.split("پاراگراف")[1:]

    for i in range(len(paragraphs)):
        paragraphs[i] = paragraphs[i][2:]

    return paragraphs


if __name__ == "__main__":
    normalized_txt = normalizing()
    paragraphs_list = split_paragraphs(normalized_txt)

