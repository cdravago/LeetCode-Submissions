class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(str(d) for d in digits)) + 1
        return [int(n) for n in str(num)]