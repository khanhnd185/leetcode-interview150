from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = defaultdict(int)
        for c in s: d[c] += 1
        for c in t:
            if c not in d: return False
            d[c] -= 1
            if d[c]==0: del d[c]
        if len(d)>0: return False
        return True