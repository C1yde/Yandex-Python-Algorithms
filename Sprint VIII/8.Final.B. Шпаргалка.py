# Идентификатор успешной посылки - 54318895

# -- ПРИНЦИП РАБОТЫ --
# Во избежание ошибки превышения стека рекурсивных вызовов устанавливаем ограничение в 100000.
# Все входящие слова и их длины складываем в set'ы, для более быстрых проверок на вхождение.
# Проверка на возможность разбиения исходной строки производится рекурсивно, сохраняя все вычисления в словаре dp.
# В цикле по всем словам происходит проверка на то, что обработанная исходная строка начинается на текщуее слово либо для ее суффикса
# рекурсивная функция возвращает так же True, то результат пересчета для текущей позиции строки равен True.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# --
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n^3) (цикл по всем словам + рекурсия).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n), для хранения стека рекурсии.

import sys
sys.setrecursionlimit(100000)


def main():
    t = sys.stdin.readline().rstrip()
    n = int(input())

    words = set()
    words_lengths = set()
    for __ in range(n):
        word = sys.stdin.readline().rstrip()
        words.add(word)
        words_lengths.add(len(word))

    if check(t, words, words_lengths):
        print('YES')
    else:
        print('NO')


def check(s, words, words_lengths):
    dp = {}

    def recurse(start):
        if start == len(s):
            return True

        if start in dp:
            return dp[start]

        for word_length in words_lengths:
            if s[start:start + word_length] in words and recurse(start + word_length):
                dp[start + word_length] = True
                return True

        dp[start] = False
        return False

    return recurse(0)


if __name__ == '__main__':
    main()
