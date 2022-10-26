import sys


def main():
    n = int(input())

    arr = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        arr.append(list(map(int, line.split())))

    arr.sort()

    result = [arr[0]]
    if len(arr) > 1:
        i = 1
        while i < len(arr):
            if result[-1][1] < arr[i][0]:
                result.append(arr[i])
            elif result[-1][1] < arr[i][1]:
                result[-1][1] = arr[i][1]
            i += 1

    for item in result:
        print(*item)

        
if __name__ == '__main__':
    main()
