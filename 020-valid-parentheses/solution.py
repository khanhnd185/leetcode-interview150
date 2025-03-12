class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        return len(self.stack)==0
    def push(self, d):
        self.stack.append(d)
    def pop(self):
        if self.empty(): return None
        node = self.stack[-1]
        self.stack = self.stack[:-1]
        return node

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        open_characters  = {"(":1,"[":2,"{":3}
        close_characters = {")":1,"]":2,"}":3}

        for c in s:
            if c in open_characters:
                stack.push(open_characters[c])
                continue
            if c in close_characters:
                v = stack.pop()
                if not v: return False
                if v!=close_characters[c]: return False
                continue
            return False
        if not stack.empty(): return False
        return True
        