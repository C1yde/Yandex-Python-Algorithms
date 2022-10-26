import sys


def main():
    length = int(input())
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    result = [0] * length
    j = length - 1
    left_zero_index = None
    right_zero_index = None
    for i in range(0, length):
        if numbers[i] == 0:
            left_zero_index = i
        if numbers[j] == 0:
            right_zero_index = j
        if numbers[i] > 0 and left_zero_index is not None:
            diff = i - left_zero_index
            if result[i] == 0 or result[i] > diff:
                result[i] = diff
        if numbers[j] > 0 and right_zero_index is not None:
            diff = right_zero_index - j
            if result[j] == 0 or result[j] > diff:
                result[j] = diff
        j = j - 1

    print(*result)


if __name__ == '__main__':
    main()
