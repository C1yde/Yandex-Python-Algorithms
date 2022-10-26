import sys


def main():
    a = int(input())
    m = int(input())
    string = sys.stdin.readline().rstrip()

    hash = 0
    for i in range(len(string)):
        hash = (hash * a + ord(string[i])) % m

    print(hash)


if __name__ == '__main__':
    main()
