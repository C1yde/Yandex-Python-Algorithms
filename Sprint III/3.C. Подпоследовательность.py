import sys


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    i, j, count = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            count += 1
            i += 1
        j += 1

    if count == len(s1):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
