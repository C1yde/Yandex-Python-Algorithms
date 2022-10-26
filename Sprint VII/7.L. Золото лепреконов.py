import sys


def main():
    line = sys.stdin.readline().rstrip()
    values = list(map(int, line.split()))
    m = values[1]+1

    line = sys.stdin.readline().rstrip()
    weights = list(map(int, line.split()))
    
    dp = [0] * m
    for i, weight in enumerate(weights):
        for j in range(m-1, weight-1, -1):
            dp[j] = max(dp[j], weight + dp[j-weight])

    print(dp[m-1])


if __name__ == '__main__':
    main()
