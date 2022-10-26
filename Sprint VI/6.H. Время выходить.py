import sys
sys.setrecursionlimit(10000000)


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    graph = [None] * 200001
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v = line.split()
        u = int(u)
        v = int(v)

        if graph[u] is not None:
            graph[u].append(v)
        else:
            graph[u] = [v]

    time = -1
    color = ['white'] * (n+1)
    entry = [None] * (n+1)
    leave = [None] * (n+1)

    DFS(1, graph, time, entry, leave, color)

    for i in range(1, n+1):
        print(entry[i], end=' ')
        print(leave[i])


def DFS(v, graph, time, entry, leave, color):
    time += 1

    entry[v] = time
    color[v] = 'gray'

    if graph[v] is not None:
        for w in sorted(graph[v]):
            if color[w] == 'white':
                time = DFS(w, graph, time, entry, leave, color)
    time += 1
    leave[v] = time
    color[v] = 'black'

    return time


if __name__ == '__main__':
    main()
