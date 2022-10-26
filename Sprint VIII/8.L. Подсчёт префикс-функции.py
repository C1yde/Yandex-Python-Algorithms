import sys


def main():
    s = sys.stdin.readline().rstrip()

    result = prefix_function(s)

    print(*result)


def prefix_function(s):
    p = [0] + [None] * (len(s)-1)

    for i in range(1, len(s)):
        k = p[i-1]
        while k > 0 and s[k] != s[i]:
            k = p[k-1]

        if s[k] == s[i]:
            k += 1

        p[i] = k

    return p


if __name__ == '__main__':
    main()
