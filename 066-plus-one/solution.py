class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r=1
        for n in range(len(digits)-1,-1,-1):
            a = digits[n]+r
            digits[n]=(a%10)
            r=a//10
        if r!=0: digits = [r]+digits
        return digits