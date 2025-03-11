# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        node = head
        while node is not None:
            if node in s: return True
            s.add(node)
            node = node.next
        return False

# Floyd’s Cycle Finding Algorithm
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast==None: return False
            fast = fast.next
            if fast==slow: return True
        return False