import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    numbers = list(map(int, line.split()))

    if len(numbers) < 2:
        print(*numbers)
        return
    else:
        pivot = 1
        less, center, greater = partition(numbers, pivot)
        if len(less) > 0:
            print(*less, end=' ')
        if len(center) > 0:
            print(*center, end=' ')
        if len(greater) > 0:
            print(*greater)
        return

      
def partition(array, pivot):
    less = []
    center = []
    greater = []
    for n in array:
        if n < pivot:
            less.append(n)
        elif n > pivot:
            greater.append(n)
        else:
            center.append(n)
    return less, center, greater

  
if __name__ == '__main__':
    main()
