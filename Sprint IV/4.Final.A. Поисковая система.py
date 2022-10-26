# Идентификатор успешной посылки - 52290445

# -- ПРИНЦИП РАБОТЫ --
# На этапе считывания документов произвожу заполнения словаря словарей вида, {слово: {порядковый номер документа: количество вхождений слова}, ...}
# Затем проходя по запросу, обрабатывая только уникальные слова, подсчитываю релевантность для каждого документа и
# сажаю результат в словарик.
# Последним шагом провожу сортировку полученного словаря для одного запроса, чтобы по релевантности было отсоритрованно по убыванию,
# а по порядковому номеру документа - по возрастанию. Полученный результат вывожу на печать.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Так как на этапе считвание документов уже по сути произвелся нужный подсчет и формирование структуры данных,
# а на этапе считывания запросов производился подсчет для уникальных строк, на выходе получим необходимый список релевантности документов.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(m*n), где n - количество документов, а m - количество запросов.
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность для хранения словаря при первоначальном считывании дркументов равна O(k), где k - количество уникальных слов из всех документов.
# Сложность для хранения словаря для подсчета релевантности равна O(n), где n - количество документов.

import sys


def main():
    n = int(input())

    text_dict = {}
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        words = list(map(str, line.split()))

        row_count = i + 1
        for word in words:
            if word in text_dict:
                if row_count in text_dict[word]:
                    text_dict[word][row_count] += 1
                else:
                    text_dict[word].setdefault(row_count, 1)
            else:
                text_dict.setdefault(word, {row_count: 1})

    m = int(input())
    for i in range(m):
        line = sys.stdin.readline().rstrip()
        search_words = list(map(str, line.split()))

        unique_words = set()
        search = {}
        for word in search_words:
            if word in text_dict and word not in unique_words:
                unique_words.add(word)
                for doc_dict in text_dict[word]:
                    relevance = text_dict[word][doc_dict]
                    if doc_dict in search:
                        search[doc_dict] += relevance
                    else:
                        search.setdefault(doc_dict, relevance)
        count = 0
        for key, value in sorted(search.items(), key=lambda item: (-item[1], item[0])):
            if count == 5:
                break
            print(key, end=' ')
            count += 1
        if len(search.items()) > 0:
            print()


if __name__ == '__main__':
    main()
