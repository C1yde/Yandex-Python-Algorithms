# Идентификатор успешной посылки - 52219405

# -- ПРИНЦИП РАБОТЫ --
# Для удобства был реализован вспомогательный класс Person, который хранит в себе данные о стажере.
# Входные строки были последовательно обернуты в этот класс и сложены в массив.
# Далее запускался рекурсивный вызов быстрой сортировки,
# с поиском опрного элемента + переупорядочиванием массива,
# а затем разделением массива на отрезка и рекурсивным вызовом функции сортировки.
# Так как сравнение происходит по нескольким полям, было решено завести отдельную функцию-компаратор для сравнения объектов.
# По итогу на выходе из функции получаем полностью отсортированный массив.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Требовалось реализовать быструю сортировку, которая не будет потреблять дополнительную память.
# С учетом ограничения было реализовано переупорядочивание элементов массива in-place
# без дополнительного хранения в вспомогательных массивах.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# В среднем время выполнения для быстрой сортировки равно O(n*log n).
# В худшем случае, когда опорный элемент будет выбран неудачно - O(n*n).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае будет равна O(n) для хранения стека вызова функций.

import sys


def main():
    n = int(input())

    arr = []
    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        list_object = list(map(str, line.split()))
        arr.append(Person(list_object[0], int(list_object[1]), int(list_object[2])))

    quick_sort(arr, 0, n-1)

    for person in arr:
        print(person.login)


def quick_sort(arr, left, right):
    if len(arr) == 1:
        return arr
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot)
        quick_sort(arr, pivot+1, right)


def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while is_less(arr[i], pivot):
            i += 1

        j -= 1
        while is_less(pivot, arr[j]):
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def is_less(first, second):
    if first.task_count > second.task_count:
        return True
    elif first.task_count == second.task_count:
        if first.fine < second.fine:
            return True
        elif first.fine == second.fine:
            if first.login < second.login:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


class Person:
    def __init__(self, login, task_count, fine):
        self.login = login
        self.task_count = task_count
        self.fine = fine


if __name__ == '__main__':
    main()
