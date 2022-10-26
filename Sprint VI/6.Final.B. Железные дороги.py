# Идентификатор успешной посылки - 52981333

# -- ПРИНЦИП РАБОТЫ --
# Во избежание проблем с максимальным стеком рекурсии устанавливаем ограничение в 10000000.
# Сам граф реализован через список смежности, где ключ - начальная вершина ребра, а значение - конечная вершина ребра.
# Заведены массив с цветами, для отслеживание, какие вершины были пройдены и массив для отслеживания стека рекурсии.
# Работа алгоритма сводится к тому, чтобы найти в графе цикл, если он есть, то вывести 'NO', иначе - 'YES'.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Входные данные обрабатываются по разному для двух типов дорог, для символа 'R' мы считаем, что дорога идет от i до j,
# для символа 'R' - от j до i.
# Получается, если в результате работы алгоритма мы найдем цикл, это значит, что две разные дороги ведут в одну и ту же вершину,
# что по условию задачи является некорректным.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n+m).
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(n).

import sys
sys.setrecursionlimit(10000000)


def main():
    n = int(input())

    graph = {}
    for i in range(n - 1):
        line = sys.stdin.readline().rstrip()
        chars = list(line)

        j = i + 1
        for c in chars:
            if c == 'R':
                if i in graph:
                    graph[i].append(j)
                else:
                    graph.setdefault(i, [j])
            else:
                if j in graph:
                    graph[j].append(i)
                else:
                    graph.setdefault(j, [i])
            j += 1

    colors = ['white'] * n
    call_stack = [False] * n
    for i in range(n):
        if colors[i] == 'white':
            if has_cycle_check(i, graph, colors, call_stack):
                print('NO')
                return

    print('YES')


def has_cycle_check(v, graph, colors, call_stack):
    colors[v] = 'gray'
    call_stack[v] = True

    if v in graph:
        for u in graph[v]:
            if colors[u] == 'white':
                if has_cycle_check(u, graph, colors, call_stack):
                    return True
            elif call_stack[u]:
                return True

    call_stack[v] = False
    return False


if __name__ == '__main__':
    main()
