from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for c in magazine:
            if c not in d.keys(): d[c] = 1
            else: d[c] += 1
        for c in ransomNote:
            if c not in d.keys(): return False
            else:
                d[c] -= 1
                if d[c]==0: del d[c]
        return True

class AnotherSolution(object):
    def canConstruct(self, ransomNote, magazine):
        d = defaultdict(int)
        for c in magazine: d[c] +=1
        for c in ransomNote:
            if c not in d: return False
            elif d[c]==1: del d[c]
            else: d[c] -= 1
        return True