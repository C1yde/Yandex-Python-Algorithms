import sys


def main():
    s = input()
    n = int(input())
    length = len(s)

    dict = {}
    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        values = list(map(str, line.split()))
        word = values[0]
        k = int(values[1])

        if k in dict:
            dict[k] += word
        else:
            dict.setdefault(k, word)

    result = ''
    for i in range(length):
        if i in dict:
            result += dict[i] + s[i]
        else:
            result += s[i]

    if length in dict:
        result += dict[length]

    print(result)


if __name__ == '__main__':
    main()
