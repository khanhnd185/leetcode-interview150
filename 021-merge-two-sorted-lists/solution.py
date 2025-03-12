# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val > list2.val: root = list2; merged = list1
        else                    : root = list1; merged = list2
        merging = root
        while merged is not None:
            if merging.next is None:
                merging.next = merged
                break
            if merging.next.val > merged.val:
                temp = merging.next
                merging.next = merged
                merged = temp
            else:
                merging = merging.next
        return root
        