import sys

def main():
    rows = int(input())
    columns = int(input())
    matrix = []
    for r in range(rows):
        line = sys.stdin.readline().rstrip()
        matrix.append(list(map(int, line.split())))
    x = int(input())
    y = int(input())

    result = []
    for i in [x - 1, x + 1]:
        if i < 0 or i > rows - 1:
            continue
        result.append(matrix[i][y])
    for j in [y - 1, y + 1]:
        if j < 0 or j > columns - 1:
            continue
        result.append(matrix[x][j])

    result.sort()
    print(*result)

if __name__ == '__main__':
    main()
