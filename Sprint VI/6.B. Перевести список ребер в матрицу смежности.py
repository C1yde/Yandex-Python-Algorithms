import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    max_i = 0
    matrix = [[0 for i in range(101)] for j in range(101)]
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v = line.split()
        u = int(u)
        v = int(v)

        matrix[u-1][v-1] = 1

        if max_i < u:
            max_i = u

        if max_i < v:
            max_i = v

    for i in range(max_i):
        for j in range(max_i):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
