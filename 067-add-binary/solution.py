class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        l = max(la,lb)
        r = 0
        ret = ''
        for i in range(l):
            _a = int(a[la-i-1]) if i<la else 0
            _b = int(b[lb-i-1]) if i<lb else 0
            s  = r+_a+_b
            r  = 1 if s > 1 else 0
            ret = str(s%2)+ret
        if r: return '1'+ret
        return ret
         