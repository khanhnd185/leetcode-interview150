# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p==None and q==None: return True
        if p==None and q!=None or \
           p!=None and q==None or \
           p.val != q.val: return False
        return self.isSameTree(p.left , q.left ) and \
               self.isSameTree(p.right, q.right)
        