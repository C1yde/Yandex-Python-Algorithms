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
        u = int(u)-1
        v = int(v)-1

        if u in graph:
            graph[u].append(v)
        else:
            graph.setdefault(u, [v])

        if v in graph:
            graph[v].append(u)
        else:
            graph.setdefault(v, [u])

    for i in graph:
        graph[i] = sorted(graph[i])
        
    line = sys.stdin.readline().rstrip()
    s, t = line.split()
    s = int(s)-1
    t = int(t)-1

    if s == t:
        print(0)
        return

    visited = [False] * n
    distance = [None] * n
    previous = [None] * n
    planned = deque([s])
    result = []
    
    planned.append(s)
    visited[s] = True
    distance[s] = 0
    result.append(s)
    while planned:
        u = planned.popleft()

        if u in graph:
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    distance[v] = distance[u] + 1
                    previous[v] = u
                    planned.append(v)
                    result.append(v)
       
    path = shortest_path(t, previous)

    if len(path) > 1:
        print(len(path)-1)
    else:
        print(-1)


def shortest_path(v, previous):
    path = []
    current_vertex = v
    while current_vertex != None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    return path


if __name__ == '__main__':
    main()
