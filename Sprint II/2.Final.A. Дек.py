# Идентификатор успешной посылки - 52138374

# -- ПРИНЦИП РАБОТЫ --
# Реализована двухсторонняя очередь, которая запоминает индексы "головы" и "хвоста",
# чтобы можно было над очередью выполнить любую операцию за O(1).
# Индексы "головы" и "хвоста" всегда указывают на следующую за заполненным значением ячейку.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# В рамках задачи требовалось реализовать двухсвязный список, для которого все команды будут
# выполняться за константное время.
# В данной реализации это достигнуто тем, что ни одна команда не требует
# выполнения дополнительного перебора элементов очереди.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Выполнение любой операции над двухсторонней очередью стоит O(1).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Максимально возможное количество элементов в очереди равно m,a
# поэтому алгоритм максимально будет потреблять O(m) памяти.

import sys


def main():
    n = int(input())
    m = int(input())

    queue = DoubleEndedQueue(m)
    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        if line == 'pop_front':
            queue.pop_front()
        elif line == 'pop_back':
            queue.pop_back()
        else:
            line_parts = list(map(str, line.split()))
            command = line_parts[0]
            new_item = int(line_parts[1])

            if command == 'push_back':
                queue.push_back(new_item)
            else:
                queue.push_front(new_item)


class DoubleEndedQueue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, new_item):
        if self.size != self.max_n:
            self.queue[self.head] = new_item
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_back(self, new_item):
        if self.size != self.max_n:
            self.queue[self.tail] = new_item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            print('error')
            return
        self.head = (self.head + 1) % self.max_n
        print(self.queue[self.head])
        self.queue[self.head] = None
        self.size -= 1

    def pop_back(self):
        if self.is_empty():
            print('error')
            return
        self.tail = (self.tail - 1) % self.max_n
        print(self.queue[self.tail])
        self.queue[self.tail] = None
        self.size -= 1


if __name__ == '__main__':
    main()
