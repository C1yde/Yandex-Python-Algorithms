import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(int, line.split()))

    group_head = 0
    group_count = 0
    result = []
    for i in range(len(arr)):
        result.append(arr[i])
        result.sort()

        if result[group_head] == group_head and result[-1] == i:
            group_count += 1
            group_head = i + 1

    print(group_count)


if __name__ == '__main__':
    main()
