#!/usr/bin/python
# coding=utf-8

from hazm import *
from xlwt import Workbook
import random


def normalizing():
    with open("./group8text.txt", 'r', encoding="utf8") as file:
        text = file.read()

        normalizer = Normalizer(token_based=True)
        normal_text = normalizer.punctuation_spacing(normalizer.character_refinement(normalizer.affix_spacing(text)))
        return normal_text


def sentences_count(paragraphs_list):
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'شماره پاراگراف')
    sheet1.write(0, 1, 'تعداد جملات')
    sheet1.write(0, 2, 'تعداد کلمات')
    sheet1.write(0, 3, 'تعداد فعل ها')
    sheet1.write(0, 4, 'تعداد اسم ها')

    sentence_tokenizer = SentenceTokenizer()
    word_tokenizer = WordTokenizer()
    tagger = POSTagger(model="resources/postagger.model")

    for i in range(len(paragraphs_list)):
        sheet1.write(i + 1, 0, i + 1)
        sheet1.write(i + 1, 1, len(sentence_tokenizer.tokenize(paragraphs_list[i])))

        token_list = word_tokenizer.tokenize(paragraphs_list[i])
        sheet1.write(i + 1, 2, len(token_list))

        tup_list = tagger.tag(token_list)

        verb_list = [item for item in tup_list if item[1] == 'V']
        noun_list = [item for item in tup_list if item[1] == 'N']

        sheet1.write(i + 1, 3, len(verb_list))
        sheet1.write(i + 1, 4, len(noun_list))

    wb.save('HW2.xls')


def find_tokens(sentences):
    tokens_list = []

    word_tokenizer = WordTokenizer()
    for sentence in sentences:
        tokens = []
        tokens = word_tokenizer.tokenize(sentence)
        tokens_list.append(tokens)

    return tokens_list


def random_selection(paragraphs_list):  # ---- select 5 random sentences for other queries ----

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
    paragraphs = text.split("پاراگراف")[1:]

    for i in range(len(paragraphs)):
        paragraphs[i] = paragraphs[i][2:]

    return paragraphs


def risheYab(tokens_list):
    lemmatizer = Lemmatizer()
    stemmer = Stemmer()

    lem_stem = []

    tagger = POSTagger(model="resources/postagger.model")

    for ele in tokens_list:

        tokens = []
        tup_list = tagger.tag(ele)

        verb_list  = [item for item in tup_list if item[1] == 'V']
        other_list = [item for item in tup_list if item[1] != 'V']

        for verb in verb_list:
            tokens.append(lemmatizer.lemmatize(verb[0]))

        for noun in other_list:
            tokens.append(stemmer.stem(noun[0]))

        lem_stem.append(tokens)

    return lem_stem


if __name__ == "__main__":
    normal_text = normalizing()
    paragraphs_list = split_paragraphs(normal_text)
    sentences_count(paragraphs_list)
    random_sentences = random_selection(paragraphs_list)
    tokens_list = find_tokens(random_sentences)
    lem_stem_list = risheYab(tokens_list)

    for ele in lem_stem_list:
        print("#sentence")
        print(ele)
