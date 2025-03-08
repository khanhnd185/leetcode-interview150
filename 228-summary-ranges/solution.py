class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        r = []
        if len(nums)== 0: return r
        n0 = nums[0]
        n1 = n0
        for num in nums[1:]+[nums[-1]+2]:
            if num == n1 + 1: n1 = num
            else:
                if n0==n1: r.append("{}".format(n0))
                else     : r.append("{}->{}".format(n0,n1))
                n0 = num
                n1 = n0
        return r