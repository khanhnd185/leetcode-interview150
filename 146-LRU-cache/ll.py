class Node:
    def __init__(self, value, parent=None, child=None):
        self.parent  = parent
        self.child   = child
        self.value   = value

    def __repr__(self) -> str:
        ret = f"Node({self.value}"
        if self.parent is not None:
            ret += f",parent={self.parent.value}"
        if self.child is not None:
            ret += f",child={self.child.value}"
        ret +=")"
        return ret

class LList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, node : Node):
        if node is None:
            return
        node.child = self.head
        if self.head is not None:
            self.head.parent = node
        else:
            self.tail = node
        self.head = node

    def append(self, node : Node):
        if node is None:
            return
        node.parent = self.tail
        if self.tail is not None:
            self.tail.child = node
        else:
            self.head = node
        self.tail = node

    def remove(self, node : Node):
        if node is None:
            return None
        if node == self.head:
            self.head = node.child
            node.child = None
        if node == self.tail:
            self.tail = node.parent
            node.parent = None
        if node.parent is not None and node.child is not None:
            node.parent.child = node.child
            node.child.parent = node.parent
        return node

    def move_top(self, node : Node):
        if node is None:
            return
        node = self.remove(node)
        self.prepend(node)