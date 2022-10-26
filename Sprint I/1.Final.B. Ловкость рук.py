import sys


def main():
    k = int(input())

    mapping = [0] * 10
    i = 1
    while i < 5:
        line = sys.stdin.readline().rstrip()
        for _char in list(map(str, line)):
            if not _char == '.':
                _int = int(_char)
                mapping[_int] = mapping[_int] + 1
        i = i + 1

    max_taps = k * 2
    result = 0
    for i in range(1, 10):
        if not mapping[i] == 0 and mapping[i] <= max_taps:
            result = result + 1

    print(result)


if __name__ == '__main__':
    main()
