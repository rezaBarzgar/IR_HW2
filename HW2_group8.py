from __future__ import unicode_literals
from hazm import *
import xlwt
from xlwt import Workbook


def normalizing():
    # writer armin,reza,sobhan

    with open("./group8text.txt", 'r', encoding="utf8") as file:
        text = file.read()

        # print("Before normalize")
        # print(text)
        # print("--------------------------------------------------------------------")
        # print("After normalize")

        normalizer = Normalizer(token_based=True)
        normal_text = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))
        sentences_count(normal_text)

        # write_text_file = open("./group8NormalizedText.txt", "wb")
        # write_text_file.write(normal_text.encode("utf-8"))
        # write_text_file.close()


def sentences_count(paragraphs):
    # writer reza
    paragraphs_list = split_paragraphs(paragraphs)

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'شماره پاراگراف')
    sheet1.write(0, 1, 'تعداد جملات')
    sheet1.write(0, 2, 'تعداد کلمات')
    sheet1.write(0, 3, 'تعداد فعل ها')
    sheet1.write(0, 4, 'تعداد اسم ها')

    sentence_tokenizer = SentenceTokenizer()
    for i in range(len(paragraphs_list)):
        sheet1.write(i + 1, 0, i)
        sheet1.write(i + 1, 1, len(sentence_tokenizer.tokenize(paragraphs_list[i])))

    wb.save('HW2.xls')


def split_paragraphs(text):
    # writer sobhan
    paragraphs = text.split("پاراگراف")[1:]

    for i in range(len(paragraphs)):
        paragraphs[i] = paragraphs[i][2:]

    return paragraphs


if __name__ == "__main__":
    normalizing()
