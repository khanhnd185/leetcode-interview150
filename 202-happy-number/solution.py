class Solution(object):
    def nextnum(self, n):
        s = 0
        while n > 0:
            s += (n%10)**2  
            n = n // 10
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        while True:
            if n == 1: return True
            n = self.nextnum(n)
            if n in d.keys(): return False
            d[n]=n

    def _isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n
        while slow != 1:
            slow = self.nextnum(slow)
            fast = self.nextnum(self.nextnum(fast))
            if slow==fast and slow!=1: return False
        return True