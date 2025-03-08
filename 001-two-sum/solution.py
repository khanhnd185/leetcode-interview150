class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,num in enumerate(nums):
            key = target - num
            if key in d.keys(): return [d[key], i]
            else: d[num] = i
        return [0,1]
        