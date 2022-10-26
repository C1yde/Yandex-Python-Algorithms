import sys

#class Node:  
#    def __init__(self, value, left=None, right=None):  
#        self.value = value  
#        self.right = right  
#        self.left = left

def solution(root) -> bool:
    return check(root, -sys.maxsize, sys.maxsize)


def check(node, min, max):
    if node is None:
        return True

    if node.value < min or node.value > max:
        return False

    left_check = check(node.left, min, node.value-1)
    right_check = check(node.right, node.value+1, max)

    return left_check and right_check

  
def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)
