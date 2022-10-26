# Идентификатор успешной посылки - 52138674

# -- ПРИНЦИП РАБОТЫ --
# Реализован стек, в который последовательно заносятся числа,
# а затем над ними последовательно выполняются арифметические операции,
# записанные сразу же после набора чисел.
# Операнды получается последовательным pop-ом из стека.
# Каждое вычисленное значение помещаетсяв обратно стек.
# По итогу на вершине стека останется результат выполнения всех операций.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Не требует пояснения
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Выполнение любой операции в стеке стоит O(1).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Максимально возможное количество чисел в стеке равно половине возможных элементов в изначальной строке.

import sys


def main():
    line = sys.stdin.readline().rstrip()
    elements = list(map(str, line.split()))

    stack = Stack()
    for element in elements:
        if is_digit(element):
            stack.push(int(element))
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()
            if element == '+':
                stack.push(first_operand + second_operand)
            elif element == '-':
                stack.push(first_operand - second_operand)
            elif element == '*':
                stack.push(first_operand * second_operand)
            elif element == '/':
                stack.push(first_operand // second_operand)
    print(stack.pop())


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    main()
