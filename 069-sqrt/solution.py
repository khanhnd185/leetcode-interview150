import math

# Heron's method
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 1.0
        for i in range(20):
            a = (a+x/a)/2
        return int(math.floor(a))


# Binary estimates
# 2^m <= S <= 2^(m+1)
# 