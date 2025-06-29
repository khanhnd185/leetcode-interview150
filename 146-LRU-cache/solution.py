class Node:
    def __init__(self, key, value, parent=None, child=None):
        self.parent  = parent
        self.child   = child
        self.value   = value
        self.key     = key

    def __repr__(self) -> str:
        ret = f"Node({self.key}:{self.value}"
        if self.parent is not None:
            ret += f",parent={self.parent.key}"
        if self.child is not None:
            ret += f",child={self.child.key}"
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
            if self.head is not None:
                self.head.parent = None
        if node == self.tail:
            self.tail = node.parent
            if self.tail is not None:
                self.tail.child = None
        if node.parent is not None and node.child is not None:
            node.parent.child = node.child
            node.child.parent = node.parent
        node.parent = None
        node.child = None
        return node

    def move_top(self, node : Node):
        if node is None:
            return
        node = self.remove(node)
        self.prepend(node)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size  = capacity
        self.list  = LList()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print(f"LRU.get({key})")
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.list.move_top(node)
        return self.list.head.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        print(f"LRU.put({key},{value})")
        if key not in self.cache:
            node = Node(key, value)
            self.list.prepend(node)
            self.cache[key] = node
            if len(self.cache)>self.size:
                deleted = self.list.remove(self.list.tail)
                del self.cache[deleted.key]
                del deleted
        else:
            node = self.cache[key]
            node.value = value
            self.list.move_top(node)


    def __repr__(self):
        ret  = (f"LRU:\n")
        ret += (f"    Capacity: {self.size}\n")
        ret += (f"    Head    : {self.list.head}\n")
        ret += (f"    Tail    : {self.list.tail}\n")
        ret += (f"    Cache   : {self.cache}\n\n")
        return ret


# Testcase 1:
#cache = LRUCache(2)
#print(cache)
#cache.put(1,1)
#print(cache)
#cache.put(2,2)
#print(cache)
#cache.get(1)
#print(cache)
#cache.put(3,3)
#print(cache)
#cache.get(2)
#print(cache)
#cache.put(4,4)
#print(cache)
#cache.get(1)
#print(cache)
#cache.get(3)
#print(cache)
#cache.get(4)
#print(cache)


# Testcase 2:
#cache = LRUCache(1)
#print(cache)
#cache.put(2,1)
#print(cache)
#cache.get(2)
#print(cache)
#cache.put(3,2)
#print(cache)
#cache.get(2)
#print(cache)
#cache.get(3)
#print(cache)


# Testcase 3:
cache = LRUCache(2)
print(cache)
cache.put(2,1)
print(cache)
cache.put(1,1)
print(cache)
cache.put(2,3)
print(cache)
cache.put(4,1)
print(cache)
cache.get(1)
print(cache)
cache.get(2)
print(cache)
