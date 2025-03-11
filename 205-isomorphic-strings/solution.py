class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds={}
        dt={}
        for cs, ct in zip(s,t):
            if cs not in ds: ds[cs]=ct
            elif ds[cs]!=ct: return False
            if ct not in dt: dt[ct]=cs
            elif dt[ct]!=cs: return False
        return True