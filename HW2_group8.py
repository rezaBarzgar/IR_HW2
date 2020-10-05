from hazm import *
from xlwt import Workbook
import random


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
        random_selection(normal_text)

        # write_text_file = open("./group8NormalizedText.txt", "wb")
        # write_text_file.write(normal_text.encode("utf-8"))
        # write_text_file.close()


def sentences_count(text):
    # writer reza
    paragraphs_list = split_paragraphs(text)

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'شماره پاراگراف')
    sheet1.write(0, 1, 'تعداد جملات')
    sheet1.write(0, 2, 'تعداد کلمات')
    sheet1.write(0, 3, 'تعداد فعل ها')
    sheet1.write(0, 4, 'تعداد اسم ها')

    sentence_tokenizer = SentenceTokenizer()
    word_tokenizer = WordTokenizer()
    tagger = POSTagger(model='resources/postagger.model')

    for i in range(len(paragraphs_list)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, len(sentence_tokenizer.tokenize(paragraphs_list[i])))
        token_list = word_tokenizer.tokenize(paragraphs_list[i])
        sheet1.write(i + 1, 2, len(token_list))
        tup_list = tagger.tag(token_list)
        verb_list = [item for item in tup_list if item[0] == 'V']
        sheet1.write(i + 1, 3, len(verb_list))
    #     sheet1.write(i + 1, 3, len( find verbs  ))
    #     sheet1.write(i + 1, 4, len( find nouns  ))

    wb.save('HW2.xls')


def random_selection(text):  # ---- select 5 random sentences for other queries ----

    random_sentences = []

    sentence_tokenizer = SentenceTokenizer()
    all_sentences = sentence_tokenizer.tokenize(text)

    random_list = random.sample(range(0, len(all_sentences)), 5)  # ---- generate 5 random number

    for index in random_list:
        random_sentences.append(all_sentences[index])

    return random_sentences


def split_paragraphs(text):
    # writer sobhan
    paragraphs = text.split("پاراگراف")[1:]

    for i in range(len(paragraphs)):
        paragraphs[i] = paragraphs[i][2:]

    return paragraphs


if __name__ == "__main__":
    normalizing()
