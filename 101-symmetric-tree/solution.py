# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _isSymmetric(self, r1, r2):
        if  r1==None and r2==None: return True
        if (r1!=None and r2==None) or \
           (r1==None and r2!=None) or \
           (r1.val   !=  r2.val  ): return False
        return self._isSymmetric(r1.right, r2.left) and \
               self._isSymmetric(r1.left, r2.right)
        
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root==None: return True
        return self._isSymmetric(root.left, root.right)
