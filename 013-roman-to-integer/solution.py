
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        l = len(s)-1
        m = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        k = {
            "C":"DM",
            "X":"LC",
            "I":"VX"
        }
        for i,n in enumerate(s):
            if n in "MDLV" or i == l:
                    num += m[n]
            elif s[i+1] in k[n]:
                    num -= m[n]
            else:   num += m[n]
        return num


class AnotherSolution(Solution):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        l = len(s)
        for i,n in enumerate(s):
            if n == 'M':
                num += 1000
                continue
            if n == 'D':
                num += 500
                continue
            if n == 'C':
                if i < l-1 and s[i+1] in "DM":
                    num -= 100
                else: num += 100
            if n == "L":
                num += 50
                continue
            if n == 'X':
                if i < l-1 and s[i+1] in "LC":
                    num -= 10
                else: num += 10
            if n == "V":
                num += 5
                continue
            if n == 'I':
                if i < l-1 and s[i+1] in "VX":
                    num -= 1
                else: num += 1
        return num
