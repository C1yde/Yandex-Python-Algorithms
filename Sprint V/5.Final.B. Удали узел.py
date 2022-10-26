# Идентификатор успешной посылки - 52497685

# -- ПРИНЦИП РАБОТЫ --
# Базовым случаем для функции удаления является отсутствие входной вершины.
# Далее определяется в каком подереве следует искать удаляемую вершину,
# если значение искомой вершины меньше значения текущей вершины - ищем в левом поддереве, иначе - в правом.
# Если найденная вершина не имеет дочерних вершин или только одну дочернюю вершину,
# то при удалении мы просто подменяем удаляемую вершину его дочерней вершиной.
# В случае, если удаляемая вершина имеет две дочерние вершины, то подменяем удаляемую вершину самой правой вершиной левого поддерева.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Удаление вершины дерева сопровождается подменой удаленной вершины самой правой вершиной левого поддерева,
# поэтому после каждого удаления мы сохраняем свойства бинарного дерева поиска.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(h), где h - высота дерева.
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность в худшем случае равна O(logn) для хранения стека рекурсии.

def remove(root, key):
    if root is None:
        return root

    if root.value > key:
        root.left = remove(root.left, key)
    elif root.value < key:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            tmp = root.right
            return tmp

        if root.right is None:
            tmp = root.left
            return tmp

        tmp = get_max_node(root.left)

        root.value = tmp.value
        root.left = remove(root.left, tmp.value)

    return root


def get_max_node(node):
    current = node

    while current.right is not None:
        current = current.right

    return current


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8
