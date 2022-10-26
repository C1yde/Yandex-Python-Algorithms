import sys


def main():
    line = sys.stdin.readline().rstrip()
    words = list(map(str, line.split()))
    words.reverse()

    print(*words)


if __name__ == '__main__':
    main()
