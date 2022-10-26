import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    max_i = 0
    graph = [None] * 101
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v = line.split()
        u = int(u)
        v = int(v)

        if graph[u] is not None:
            graph[u].append(v)
        else:
            graph[u] = [v]

        if max_i < u:
            max_i = u

    for i in range(1, max_i+1):
        if graph[i] is None:
            print(0)
        else:
            graph[i].sort()
            length = len(graph[i])
            print(length, end=' ')
            for j in range(length):
                print(graph[i][j], end=' ')
            print()

            
if __name__ == '__main__':
    main()
