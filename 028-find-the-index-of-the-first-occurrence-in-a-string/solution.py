class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            fit = True
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    fit = False
                    break
            if fit: return i
        return -1