import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    k = int(input())

    arr.sort()

    l = 0
    h = arr[-1] - arr[0]
    while l < h:          
        m = (l + h)//2
        left = 0
        count = 0
        for right in range(len(arr)):
            while arr[right] - arr[left] > m:
                left +=1
            count += right-left
           
        if count>=k:
            h = m
        else:
            l = m+1

    print(l)

    
if __name__ == '__main__':
    main()
