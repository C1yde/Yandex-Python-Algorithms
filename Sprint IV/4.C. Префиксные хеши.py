import sys


def main():
    a = int(input())
    m = int(input())
    string = sys.stdin.readline().rstrip()
    t = int(input())

    prefixes = [0] * (len(string) + 1)
    for i in range(1, len(string) + 1):
        prefixes[i] = (prefixes[i-1] * a % m + ord(string[i-1])) % m

    for i in range(t):
        line = sys.stdin.readline().rstrip()
        numbers = list(map(int, line.split()))
        left = numbers[0]
        right = numbers[1]

        hash = (prefixes[right] - (prefixes[left-1] * pow(a, right-left+1, m))) % m
        print(hash)


if __name__ == '__main__':
    main()
