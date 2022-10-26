import sys


def main():
    m = int(input())
    n = int(input())

    queue = Queue(n)
    for i in range(0, m):
        line = sys.stdin.readline().rstrip()
        if line == 'peek':
            queue.peek()
        elif line == 'pop':
            queue.pop()
        elif line == 'size':
            print(queue.size)
        else:
            words = list(map(str, line.split()))
            item = int(words[1])
            queue.push(item)


class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            print(None)
            return
        tmp = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        print(tmp)

    def peek(self):
        if self.is_empty():
            print(None)
            return
        print(self.queue[self.head]) 


if __name__ == '__main__':
    main()
