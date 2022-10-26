import sys


def main():
    text = sys.stdin.readline().rstrip()
    p = sys.stdin.readline().rstrip()
    replace_text = sys.stdin.readline().rstrip()

    search_result = search(p, text)

    result = ''
    i = 0
    while i < len(text):
        if i in search_result:
            result += replace_text
            i += len(p)
        else:
            result += text[i]
            i += 1

    print(result)


def search(p, text):
    result = []
    s = p + '#' + text
    π = [0] + [None] * len(p)
    π_prev = 0

    for i in range(1, len(s)):
        k = π_prev
        while k > 0 and s[k] != s[i]:
            k = π[k - 1]
        if s[k] == s[i]:
            k += 1

        if i < len(p):
            π[i] = k

        π_prev = k
        if k == len(p):
            result.append(i - 2 * len(p))

    return result 


if __name__ == '__main__':
    main()
