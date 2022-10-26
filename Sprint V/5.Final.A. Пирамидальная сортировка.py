# Идентификатор успешной посылки - 52497671

# -- ПРИНЦИП РАБОТЫ --
# Куча реализована через массив.
# Каждая строка входных данных оборачиваеся в класс Person и добавляется в кучу. Добавление происходит в конец кучи,
# а затем для заданного индекса происходит просеивание вверх, для того чтобы восстановить свойства кучи.
# Для вывода отсортированных дааных для кучи происходит удаление корня и просеивание вниз.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Так как на этапе считвание данных происходит формирование max_heap кучи,
# при последовательном удалении и печати корня кучи мы получаем отсортированный по убыванию массив.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(nlogn).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n).

import sys


def main():
    n = int(input())
    heap = [0]

    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        list_object = list(map(str, line.split()))
        person = Person(list_object[0], int(list_object[1]), int(list_object[2]))

        heap_add(heap, person)

    while len(heap) > 1:
        print(pop_max(heap).login)


def heap_add(heap, key):
    index = len(heap)
    heap.append(key)
    sift_up(heap, index)


def sift_up(heap, index):
    if index == 1:
        return

    parent_index = index // 2

    if is_less(heap[index], heap[parent_index]):
        tmp = heap[parent_index]
        heap[parent_index] = heap[index]
        heap[index] = tmp
        sift_up(heap, parent_index)


def pop_max(heap):
    result = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    sift_down(heap, 1)
    return result


def sift_down(heap, index):
    left = 2 * index
    right = 2 * index + 1

    if left >= len(heap):
        return

    if right < len(heap) and is_less(heap[right], heap[left]):
        index_largest = right
    else:
        index_largest = left

    if is_less(heap[index_largest], heap[index]):
        tmp = heap[index]
        heap[index] = heap[index_largest]
        heap[index_largest] = tmp
        sift_down(heap, index_largest)


def is_less(first, second):
    if first.task_count != second.task_count:
        return first.task_count > second.task_count
    if first.fine != second.fine:
        return first.fine < second.fine
    return first.login < second.login


class Person:
    def __init__(self, login, task_count, fine):
        self.login = login
        self.task_count = task_count
        self.fine = fine


if __name__ == '__main__':
    main()
