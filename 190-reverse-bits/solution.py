class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for _ in range(32):
            m = (m<<1) | (n&1)
            if n: n=n>>1
        return m