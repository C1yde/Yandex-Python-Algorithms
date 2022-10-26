import sys
sys.setrecursionlimit(10000000)


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    global graph, colors
    
    count = 1
    colors = [-1] * (n+1)
    graph = {}
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v = line.split()
        u = int(u)
        v = int(v)

        if u in graph:
            graph[u].append(v)
        else:
            graph.setdefault(u, [v])

        if v in graph:
            graph[v].append(u)
        else:
            graph.setdefault(v, [u])

    result = {}
    for i in range(1, n+1):
        if colors[i] == -1:
            arr = []
            dfs(i, count, arr)
            count += 1
            result.setdefault(i, arr)

    print(len(result))
    values = list(result.values())
    for group in sorted(values, key=lambda value: value[0]):
        print(*sorted(group))


def dfs(v, count, arr):
    colors[v] = count
    arr.append(v)

    if v in graph:
        for w in graph[v]:
            if colors[w] == -1:
                dfs(w, count, arr)


if __name__ == '__main__':
    main()
