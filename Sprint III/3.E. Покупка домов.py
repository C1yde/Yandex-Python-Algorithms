import sys


def main():
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    n = numbers[0]
    k = numbers[1]
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()

    sum = 0
    count = 0
    for item in arr:
        sum += item
        if sum > k:
            break
        else:
            count += 1

    print(count)

    
if __name__ == '__main__':
    main()
