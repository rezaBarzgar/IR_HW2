#!/usr/bin/python
# coding=utf-8
from hazm import *
from xlwt import Workbook
import random


def normalizing():
    # writer armin,reza,sobhan

    with open("./group8text.txt", 'r', encoding="utf8") as file:
        text = file.read()

        normalizer = Normalizer(token_based=True)
        normal_text = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))

        return normal_text


def sentences_count(paragraphs_list):
    # writer reza

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'شماره پاراگراف')
    sheet1.write(0, 1, 'تعداد جملات')
    sheet1.write(0, 2, 'تعداد کلمات')
    sheet1.write(0, 3, 'تعداد فعل ها')
    sheet1.write(0, 4, 'تعداد اسم ها')

    sentence_tokenizer = SentenceTokenizer()
    word_tokenizer = WordTokenizer()
    # tagger = POSTagger(model="./postagger.model")

    for i in range(len(paragraphs_list)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, len(sentence_tokenizer.tokenize(paragraphs_list[i])))
        token_list = word_tokenizer.tokenize(paragraphs_list[i])
        sheet1.write(i + 1, 2, len(token_list))

        # tup_list = tagger.tag(token_list)
        # verb_list = [item for item in tup_list if item[0] == 'V']

        # sheet1.write(i + 1, 3, len(verb_list))
    #     sheet1.write(i + 1, 3, len( find verbs  ))
    #     sheet1.write(i + 1, 4, len( find nouns  ))

    wb.save('HW2.xls')


def fine_tokens(sentences):
    # writer sobhan

    word_tokenizer = WordTokenizer()
    for sentence in sentences:
        tokens = word_tokenizer.tokenize(sentence)

        print(tokens)
        print("-------------------------------")


def random_selection(paragraphs_list):      # ---- select 5 random sentences for other queries ----
    # writer sobhan

    text = ""

    for par in paragraphs_list:  # ---- In order to merge all sentences in one string ----
        text += par

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
    normal_text = normalizing()
    paragraphs_list = split_paragraphs(normal_text)
    sentences_count(paragraphs_list)
    random_sentences = random_selection(paragraphs_list)
    fine_tokens(random_sentences)
