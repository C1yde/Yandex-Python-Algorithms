def main():
    n = int(input())
    arr = list(map(int, input().split()))

    never_swaped = True
    for i in range(1, n):
        swaped = False
        for j in range(0, n - i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swaped = True
                never_swaped = False
        if swaped:
            print(*arr)
    if never_swaped:
        print(*arr)


if __name__ == '__main__':
    main()
