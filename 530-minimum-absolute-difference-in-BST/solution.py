# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def subtree_last(node):
    if node.right: return subtree_last(node.right)
    return node
def subtree_first(node):
    if node.left: return subtree_first(node.left)
    return node

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        a = 100000
        if root.left:
            predecessor = subtree_last(root.left)
            a = min(a, root.val-predecessor.val)
            a = min(a, self.getMinimumDifference(root.left))
        if root.right:
            successor = subtree_first(root.right)
            a = min(a, successor.val-root.val)
            a = min(a, self.getMinimumDifference(root.right))
        return a
            
