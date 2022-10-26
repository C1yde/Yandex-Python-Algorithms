import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    first_arr = list(map(int, line.split()))

    m = int(input())
    line = sys.stdin.readline().rstrip()
    second_arr = list(map(int, line.split()))

    dp = [([0]*(m+1)) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            if first_arr[i] == second_arr[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)

    print(dp[n][m])

    first_arr_ind = []
    second_arr_ind = []
    i = n
    j = m
    while i > 0 and j > 0:
        if first_arr[i-1] == second_arr[j-1]:
            first_arr_ind.append(i)
            second_arr_ind.append(j)
            i -= 1
            j -= 1
        elif dp[i-1][j] == dp[i][j]:
            i -= 1 
        else: 
            j -= 1

    print(*first_arr_ind[::-1])
    print(*second_arr_ind[::-1])


if __name__ == '__main__':
    main()
