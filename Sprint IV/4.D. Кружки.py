import sys


def main():
    n = int(input())

    dict = {}
    for i in range(n):
        dict.setdefault(sys.stdin.readline().rstrip())

    print(*dict, sep='\n')


if __name__ == '__main__':
    main()
