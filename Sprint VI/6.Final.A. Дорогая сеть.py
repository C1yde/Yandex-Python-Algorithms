# Идентификатор успешной посылки - 53025029

# -- ПРИНЦИП РАБОТЫ --
# Реализован вспомогательный класс Graph для хранения всех структур данных для работы алгоритма.
# Сам граф реализован через список смежности, где ключ - начальная вершина ребра,
# а значение - tuple, в котором первый элемент - конечная вершина ребра, а второй - вес ребра.
# Поиск максимального остовного дерева реализован, используя алгоритм Прима с применением приоритетной очереди.
# Поиск начинается с 0-й вершины, далее мы идем по ребрам с максимальным весом, пока не пройдем по всем вершинам.
# На каждом шаге суммируем вес ребер.
# Если в результате поиска остались вершины, в которых мы не побывали, значит существует несколько компонент связанности
# и в этом лучае мы выводим ошибку, иначе, сумму ребер.
# Отдельно обрабатываются случаи, когда во входных данных количество ребер равну нулю.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Так как на этапе обработки ребер ребра складируются в max_heap кучу (достигается указанием приоритетному полю вес знака -),
# при получении элемента из кучи мы будем всегда иметь максимальное ребро и добавлять его вес в общую сумму.
# В результате получим сумму всех ребер максимального остовного дерева.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n * log m).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n+m).

import sys
import heapq


def main():
    line = sys.stdin.readline().rstrip()
    n, m = line.split()
    n = int(n)
    m = int(m)

    if m == 0:
        if n > 1:
            print('Oops! I did it again')
        else:
            print(0)
        return

    g = Graph(n)
    for __ in range(m):
        line = sys.stdin.readline().rstrip()
        u, v, w = line.split()
        u = int(u)-1
        v = int(v)-1
        w = int(w)

        if u in g.graph:
            g.graph[u].append((v, w))
        else:
            g.graph.setdefault(u, [(v, w)])

        if v in g.graph:
            g.graph[v].append((u, w))
        else:
            g.graph.setdefault(v, [(u, w)])

    print(g.get_max_spanning_tree())


class Graph:
    def __init__(self, n):
        self.n = n              # Количество вершин.
        self.graph = {}         # Граф.
        self.added = set()      # Множество вершин, уже добавленных в остов.
        self.not_added = set()  # Множество вершин, ещё не добавленных в остов.
        self.edges_heap = []    # Массив рёбер, исходящих из остовного дерева, представленные в виде max-heap.

    def add_vertex(self, v):
        self.added.add(v)
        self.not_added.remove(v)

        for edge in self.graph[v]:
            if edge[0] in self.not_added:
                heapq.heappush(self.edges_heap, (-edge[1], v, edge[0]))

    def get_max_spanning_tree(self):
        self.not_added = self.graph.keys() | set()

        maximum_spanning_tree_cost = 0

        self.add_vertex(0)

        while len(self.not_added) > 0 and len(self.edges_heap) > 0:
            e = heapq.heappop(self.edges_heap)
            if e[2] in self.not_added:
                maximum_spanning_tree_cost += e[0]
                self.add_vertex(e[2])

        if len(self.not_added) > 0:
            return 'Oops! I did it again'
        else:
            return -maximum_spanning_tree_cost


if __name__ == '__main__':
    main()
