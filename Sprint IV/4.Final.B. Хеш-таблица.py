# Идентификатор успешной посылки - 52303109

# -- ПРИНЦИП РАБОТЫ --
# Для удобства был реализован вспомогательный класс Node, представляющий собой узел связанного списка.
# Реализован класс HashMap с методами put(вставка пары ключ-значение), get(получение значения по ключу)
# и delete (удаление данных по ключу).
# Класс содержит в себе массив, для которого индекс для операций над элементами вычисляется, как значение ключа по модулю от размера массива.
# Размер массива выбран как ближайшее простое число от возможного количества элементов в массиве (10^5).
# В каждой ячейке массива хранится связный список, для удобства разрешения возможных коллизий (метод цепочек).
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# -
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# В лучшем случае все операции для хеш таблицы выполняются за O(1).
# В худшем случае - за O(n).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность равна O(n), необходимо хранить только массив внутри хеш таблицы.

import sys


def main():
    n = int(input())

    hash_map = HashMap()
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        line_parts = list(map(str, line.split()))

        command = line_parts[0]
        key = int(line_parts[1])

        if command == 'get':
            hash_map.get(key)
        elif command == 'delete':
            hash_map.delete(key)
        else:
            value = int(line_parts[2])
            hash_map.put(key, value)


class HashMap:
    def __init__(self):
        self.buckets = [None] * 100003

    def put(self, key: int, value: int):
        index = self.get_bucket(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        if node.key == key:
            self.buckets[index] = Node(key, value, node.next)
            return

        prev = node
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if prev.next is None:
            prev.next = Node(key, value)
        else:
            prev.next = Node(key, value, prev.next.next)

    def get(self, key: int):
        index = self.get_bucket(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            print(None)
        else:
            print(node.value)

    def delete(self, key: int):
        index = self.get_bucket(key)
        node = self.buckets[index]

        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(None)
            if prev is not None:
                prev.next = None
            return
        else:
            print(node.value)

            if prev is None:
                self.buckets[index] = None
            else:
                prev.next = node.next

    @staticmethod
    def get_bucket(key: int):
        return key % 100003


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


if __name__ == '__main__':
    main()
