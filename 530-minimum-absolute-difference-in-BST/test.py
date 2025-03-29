root=[1,0,48,None,None,12,49]
output=1

root=[4,2,6,1,3]
output=1

root=[236,104,701,None,227,None,911]
output=9

root=[543,384,652,None,445,None,699]
output=47

class Node(object):
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        if left: left.parent = self
        if right: right.parent = self

def subtree_first(node : Node) -> Node:
    if node.left: return subtree_first(node.left)
    return node

def subtree_last(node : Node) -> Node:
    if node.right: return subtree_last(node.right)
    return node

def subtree_successor(node: Node) -> Node:
    if node.right: return subtree_first(node.right)
    if not node.parent: return node
    while node!=node.parent.left: node = node.parent
    return node


n1 = Node(val=1)
n3 = Node(val=3)
n2 = Node(val=2,right=n3,left=n1)
n6 = Node(val=6)
n4 = Node(val=4,left=n2,right=n6)
