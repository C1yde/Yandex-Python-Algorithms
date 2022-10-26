import sys


def main():
    n = int(input())

    stack = StackMax()
    for i in range(0, n):
        line = sys.stdin.readline().rstrip()
        if line == 'get_max':
            stack.get_max()
        elif line == 'pop':
            stack.pop()
        else:
            words = list(map(str, line.split()))
            item = int(words[1])
            stack.push(item)


class StackMax:
    def __init__(self):
        self.items = []
        self.ordered_items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)
        self.size += 1
        if len(self.ordered_items) == 0 or self.items[self.ordered_items[-1]] <= item:
            self.ordered_items.append(self.size - 1)

    def pop(self):
        if self.is_empty():
            print('error')
        else:
            if self.items[-1] == self.items[self.ordered_items[-1]]:
                self.ordered_items.pop()
            self.items.pop()
            self.size -= 1

    def get_max(self):
        if self.is_empty():
            print(None)
        else:
            print(self.items[self.ordered_items[-1]])


if __name__ == '__main__':
    main()
