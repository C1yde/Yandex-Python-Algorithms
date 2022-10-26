import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    if n == 1:
        print('YES')
        return

    graph = {}
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v = line.split()
        u = int(u)-1
        v = int(v)-1

        if u == v:
            continue

        if u in graph:
            graph[u].add(v)
        else:
            graph.setdefault(u, set([v]))

        if v in graph:
            graph[v].add(u)
        else:
            graph.setdefault(v, set([u]))

    if len(graph) != n:
        print('NO')
        return

    for i in graph:
        if len(graph[i]) != n-1:
            print('NO')
            return
      
    print('YES')


if __name__ == '__main__':
    main()
