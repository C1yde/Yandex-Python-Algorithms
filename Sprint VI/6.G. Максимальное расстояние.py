import sys
from collections import deque


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

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

    s = int(input())

    visited = [False] * (n+1)
    planned = deque([s])
    distance = [0] * (n+1)
    
    planned.append(s)
    visited[s] = True
    distance[s] = 0
    while planned:
        u = planned.popleft()

        if u in graph:
            for v in graph[u]:
                if not visited[v]:
                    distance[v] = distance[u] + 1
                    visited[v] = True
                    planned.append(v)

    print(sorted(distance)[-1])


if __name__ == '__main__':
    main()
