import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort(reverse=True)

    for i in range(len(arr)-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            print(arr[i] + arr[i+1] + arr[i+2])
            break

            
if __name__ == '__main__':
    main()
