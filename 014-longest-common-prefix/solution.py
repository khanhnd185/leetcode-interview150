class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        i = 0
        while True:
            if i == len(strs[0]): return ret
            c = strs[0][i]
            for s in strs[1:]:
                if i == len(s): return ret
                if c != s[i]  : return ret
            i   += 1
            ret += c
