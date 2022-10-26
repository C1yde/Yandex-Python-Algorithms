# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item
    previous_node = get_node_by_index(node, idx - 1)
    node_for_remove = previous_node.next_item
    previous_node.next_item = node_for_remove.next_item
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # result is node0 -> node2 -> node3


def get_node_by_index(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node
