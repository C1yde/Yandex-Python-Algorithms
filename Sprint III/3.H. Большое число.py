import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(str, line.split()))

    for i in range(1, n):
        for j in range(0, n - i):
            if is_less(arr[j], arr[j+1]):
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    print(*arr, sep='')

def is_less(obj1, obj2):
    return int(obj1 + obj2) < int(obj2 + obj1)


if __name__ == '__main__':
    main()
