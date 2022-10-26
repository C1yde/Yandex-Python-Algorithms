from node import Node


def insert(root, key):
    if key < root.value:
        if root.left is None:
            root.left = Node(None, None, key)
        else:
            insert(root.left, key)
    else:
        if root.right is None:
            root.right = Node(None, None, key)
        else:
            insert(root.right, key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6
