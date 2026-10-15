class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return n
        pos = 0
        neg = 0

        for i in range(0, n):
            if nums[i] < 0:
                neg += 1
            elif nums[i] > 0:
                pos += 1
        return max(pos, neg)