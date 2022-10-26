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


    i = 0
    j = m-1
    result = []
    while i != n-1 or j != 0:
        if j == 0:
            result.append('U')
            i += 1
        elif i == n-1:
            result.append('R')
            j -= 1
        elif dp[i+1][j] > dp[i][j-1]:
            result.append('U')
            i += 1
        else:
            result.append('R')
            j -= 1

    result.reverse()

    print(dp[0][m-1])
    print(*result, sep='')


if __name__ == '__main__':
    main()
