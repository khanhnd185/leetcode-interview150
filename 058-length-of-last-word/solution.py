class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        i = len(s)-1
        while s[i]==" ": i -= 1
        while i >= 0 and s[i]!=" ":
            i -= 1
            c += 1
        return c