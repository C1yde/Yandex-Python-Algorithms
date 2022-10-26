# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node, elem):
    idx = 0
    while node and node.value != elem:
        node = node.next_item
        idx = idx + 1
    if node:
        return idx
    else:
        return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node22")
    # result is idx == 2

