from collections import defaultdict

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = defaultdict(int)
        for i,n in enumerate(nums):
            if n in d and i-d[n]<=k: return True
            else: d[n]=i
        return False