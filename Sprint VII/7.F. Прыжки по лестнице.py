import sys


def main():
    line = sys.stdin.readline().rstrip()
    values = list(map(int, line.split()))
    n = values[0]
    k = values[1]

    dp = [0] * n
    dp[0] = 1;
    for i in range(1, n):
        start = max(0, i-k)
        for j in range(start, i):
            dp[i] = dp[i] + dp[j]

    print(dp[n-1] % 1000000007)


if __name__ == '__main__':
    main()
