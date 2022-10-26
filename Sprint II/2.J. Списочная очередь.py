import sys


def main():
    n = int(input())

    size = 0
    head = None
    tail = None
    for i in range(0, n):
        line = sys.stdin.readline().rstrip()
        if line == 'size':
            print(size)
        elif line == 'get':
            if size == 0:
                print('error')
            else:
                tmp = head
                head = head.next
                print(tmp.value)
                size -= 1
        else:
            words = list(map(str, line.split()))
            value = int(words[1])

            node = Node(value)
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

            size += 1


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


if __name__ == '__main__':
    main()
