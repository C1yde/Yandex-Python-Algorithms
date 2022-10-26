import sys

def main():
    children_count = int(input())
    greed_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    cookies_count = int(input())
    cookies_sizes = list(map(int, sys.stdin.readline().rstrip().split()))

    greed_arr.sort()
    cookies_sizes.sort()
    
    j = 0
    count = 0
    for i in range(len(greed_arr)):
        greed = greed_arr[i]
        while j < len(cookies_sizes):
            size = cookies_sizes[j]
            j += 1
            if size >= greed:
                count += 1
                break

    print(count)

if __name__ == '__main__':
    main()
