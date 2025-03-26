# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root: return []
        result = []
        queue  = deque([root])
        while queue:
            s = 0.0
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                s += node.val
                if node.right: queue.append(node.right)
                if node.left : queue.append(node.left)
            result.append(s/l)
        return result

class AnotherSolution(Solution):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root: return []
        result = []
        queue  = [root]
        while queue:
            s = 0.0
            l = len(queue)
            for _ in range(l):
                node  = queue[0]
                queue = queue[1:]
                s += node.val
                if node.right: queue.append(node.right)
                if node.left : queue.append(node.left)
            result.append(s/l)
        return result