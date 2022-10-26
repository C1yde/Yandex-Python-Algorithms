import sys


def main():
    rows = int(input())
    columns = int(input())
    matrix = []
    for r in range(rows):
        line = sys.stdin.readline().rstrip()
        matrix.append(list(map(int, line.split())))

    for i in range(0, columns):
        for j in range(0, rows):
            print(matrix[j][i], end=' ')
        print()


if __name__ == '__main__':
    main()
