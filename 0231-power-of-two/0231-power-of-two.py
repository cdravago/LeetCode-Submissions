class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 # Power of 2 has exactly one bit
        """
        Example: n = 4
        4 > 0? Y and 4 & (4 - 1) == 0
        True     and 4 & 3 == 0
        True     and 0 == 0
        True     and True
        return true
        """