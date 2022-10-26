import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    s = int(input())

    first_index = binarySearch(arr, s, 0, n)
    second_index = binarySearch(arr, 2*s, 0, n)

    print(first_index, end =" ")
    print(second_index)


def binarySearch(arr, s, left, right, last_mid = None):
    if right <= left:
        if last_mid is not None:
            return last_mid + 1
        else:
            return -1

    mid = (left + right) // 2

    if arr[mid] >= s:
        if mid <= left:
            return mid + 1

        return binarySearch(arr, s, left, mid, mid)
    else:
        if mid <= left:
            if last_mid is not None:
                return last_mid + 1
            else:
                return -1

        return binarySearch(arr, s, mid + 1, right, last_mid)


if __name__ == '__main__':
    main()
