class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        cnt = 1
        for i in nums[1:]:
            if i == ret:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    ret = i
                    cnt = 1
        return ret