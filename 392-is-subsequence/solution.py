class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ps = 0
        pt = 0
        if len(s)==0: return True
        while pt < len(t):
            if t[pt] == s[ps]: ps += 1
            if ps == len(s): return True
            pt += 1
        return False