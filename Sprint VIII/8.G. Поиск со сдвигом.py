import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(int, line.split()))

    source = []
    for i in range(n-1):
        source.append(arr[i]-arr[i+1])

    m = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(int, line.split()))

    pattern = []
    for i in range(m-1):
        pattern.append(arr[i]-arr[i+1])

    occurrences = []
    start = 0
    while True:
        pos = find(source, pattern, start)
        if pos == -1:
            break
        occurrences.append(pos + 1)
        start = pos + 1

    print(*occurrences)


def find(source, pattern, start=0):
    s_len = len(source)
    p_len = len(pattern)

    if s_len < p_len:
        return -1

    for pos in range(start,  s_len - p_len + 1):
        found = True
        for offset in range(p_len):
            if source[pos + offset] != pattern[offset]:
                found = False
                break
        if found:
            return pos

    return -1


if __name__ == '__main__':
    main()
