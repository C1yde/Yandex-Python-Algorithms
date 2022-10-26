import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    costs = list(map(int, line.split()))

    if n < 2:
        print(0)

    if n == 2 and costs[0] > costs[1]:
        print(0)

    profit = 0
    i = 0
    while True:
        while i < n-1 and costs[i] >= costs[i+1]:
            i += 1
            
        if i >= n-1:
            break

        j = i + 1
        while j < n-1 and costs[i] < costs[j] and costs[j] < costs[j+1]:
            j += 1

        if j > n-1:
            break

        profit += costs[j] - costs[i]
        i = j + 1
    
    print(profit)


if __name__ == '__main__':
    main()
