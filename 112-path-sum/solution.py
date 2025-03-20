# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root==None: return False
        if root.left==None and root.right==None:
            if root.val==targetSum: return True
            else: return False
        return self.hasPathSum(root.left, targetSum-root.val) or \
               self.hasPathSum(root.right, targetSum-root.val)
        