class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 : return False
        a = []
        while x!=0:
            a.append(x%10)
            x=x//10
        for i in range(len(a)):
            if a[i]!=a[len(a)-1-i]: return False
        return True
