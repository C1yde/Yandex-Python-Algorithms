import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)
    
    gr = Graph(n)
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v, l = line.split()
        u = int(u)-1
        v = int(v)-1
        l = int(l)

        if gr.graph[u][v] > 0:
            gr.graph[u][v] = min(gr.graph[u][v], l)
        else:
            gr.graph[u][v] = l

        if gr.graph[v][u] > 0:
            gr.graph[v][u] = min(gr.graph[v][u], l)
        else:
            gr.graph[v][u] = l

    for i in range(n):
        gr.dijkstra(i)


class Graph():
    def __init__(self, n):
        self.V = n
        self.graph = [[0 for column in range(n)] for row in range(n)]


    def get_min_dist(self, dist, visited):
        min = sys.maxsize
        min_index = None

        for v in range(self.V):
            if dist[v] < min and visited[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V
 
        for __ in range(self.V):
            u = self.get_min_dist(dist, visited)

            if u is None:
                continue

            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
 
        for i in range(self.V):
            value = dist[i]
            if value == sys.maxsize:
                value = -1

            print(value, end=' ')
        print()


if __name__ == '__main__':
    main()
