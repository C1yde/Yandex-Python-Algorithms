def print_range(node, l, r):
    if node.left != None and node.value >= l:
        print_range(node.left, l, r)
    if r >= node.value >= l:
        print(node.value)
    if node.right != None and node.value <= r:
        print_range(node.right, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8
