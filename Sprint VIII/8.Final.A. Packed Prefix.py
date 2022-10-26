# Идентификатор успешной посылки - 54308667

# -- ПРИНЦИП РАБОТЫ --
# Решение разделено на 2 части:
# - рекурсивная распаковка каждой запакованной строки
# - поиск НОП (наибольшего общего префикса)
# Поиск производим, проходя в цикле по всем словам.
# За первоначальный префикс берем первое слово.
# На каждой итерации пытаемся найти префикс равный или меньший префиксу на предыдущей итерации.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# --
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность парсинга слов равна O(max_len), где max_len - максимально возможная длина слова.
# Сложность поиска префикса O(n * max_len).
# Общая сложность - O(n * max_len^2).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность парсинга слов равна O(max_len^2), храним стек рекурсии и выделение памяти под строки.
# Сложность поиска префикса O(n * max_len), под возможные выделения памяти под строки.
# Общая сложность - O(n * max_len^3).

import sys


def main():
    n = int(input())

    words = []
    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        symbols = list(map(str, line))

        words.append(parse_word(symbols))

    prefix = words[0]

    for word in words[1:]:
        while word[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix) - 1]
        if not prefix:
            break

    print(prefix)


def parse_word(symbols):
    s_l = len(symbols)

    def recursive_parse(i):
        result = ''
        while i < s_l and symbols[i] != ']':
            digit = ''
            if symbols[i].isdigit():
                while symbols[i].isdigit():
                    digit += symbols[i]
                    i += 1
                sub_result, i = recursive_parse(i + 1)
                result += sub_result * int(digit)
            else:
                result += symbols[i]
                i += 1
        return result, i + 1

    return recursive_parse(0)[0]


if __name__ == '__main__':
    main()
