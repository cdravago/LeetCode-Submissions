class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num, reverse = x, 0
        while x:
            reverse = reverse * 10 + (x % 10)
            x //= 10
        return num == reverse