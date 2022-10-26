import sys


def main():
    n = int(input())
    m = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr += list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()

    full_length = n + m

    if full_length % 2 != 0:
        print(arr[full_length//2])
    else:
        print((arr[full_length//2 - 1] + arr[full_length//2])/2)


if __name__ == '__main__':
    main()
