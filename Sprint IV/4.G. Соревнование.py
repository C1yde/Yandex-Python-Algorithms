import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(int, line.split()))

    sum = 0
    sums = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        if arr[i] == 0:
            sum -= 1
        else:
            sum += 1
        sums[i+1] = sum;

    dict = {}
    for i in range(len(sums)):
        list_by_sum = dict.get(sums[i])
        if list_by_sum is None:
            list_by_sum = [i]
            dict.setdefault(sums[i], list_by_sum)
        else:
            list_by_sum.append(i)

    max_length = 0
    for i in range(len(sums)):
        list_by_sum = dict.get(sums[i])

        if list_by_sum is None:
            continue

        length = abs(list_by_sum[-1]-i);
        if length > max_length:
            max_length = length;

    print(max_length)


if __name__ == '__main__':
    main()
