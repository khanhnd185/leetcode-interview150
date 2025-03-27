# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        result = []
        queue  = [root]
        while queue:
            a = []
            l = len(queue)
            for _ in range(l):
                node  = queue[0]
                queue = queue[1:]
                a.append(node.val)
                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(a)
        return result
