import sys


def main():
    line = sys.stdin.readline().rstrip()
    values = list(map(int, line.split()))
    n = values[0]
    m = values[1]

    fields = [([0]*m) for i in range(n)]
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        values = list(map(int, line))

        for j in range(m):
            fields[i][j] = values[j]

    dp = [([0]*m) for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            left = 0
            if i+1 >= 0 and i+1 < n:
                left = dp[i+1][j]

            right = 0
            if j-1 >= 0  and j-1 <= m:
                right = dp[i][j-1]

            dp[i][j] = max(left, right) + fields[i][j]

    print(dp[0][m-1])


if __name__ == '__main__':
    main()
