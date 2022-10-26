import sys
from collections import deque


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    in_degree = [0] * (n+1)
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

        in_degree[v] += 1
 
    queue = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        u = queue.popleft()
        print(u, end=' ')

        if u in graph:
            for i in graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)


if __name__ == '__main__':
    main()
