import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    graph = [None] * 100001
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v = line.split()
        u = int(u)
        v = int(v)

        if graph[u] is not None:
            graph[u].append(v)
        else:
            graph[u] = [v]

        if graph[v] is not None:
            graph[v].append(u)
        else:
            graph[v] = [u]

    s = int(input())
    
    visited = [False] * (n+1)
    stack = []
    stack.append(s)
    while len(stack) > 0:
        v = stack.pop()

        if not visited[v]:
            print(v, end=' ')
            visited[v] = True
            stack.append(v)
 
        if graph[v] is not None:
            for node in sorted(graph[v], reverse=True):
                if not visited[node]:
                    stack.append(node)


if __name__ == '__main__':
    main()
