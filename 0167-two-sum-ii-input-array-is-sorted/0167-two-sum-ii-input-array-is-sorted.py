class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l , r = 0, len(numbers) - 1
        while l < r:
            t = numbers[l] + numbers[r]
            if t == target:
                return [l + 1, r + 1]
            elif t < target:
                l += 1
            else:
                r -= 1
