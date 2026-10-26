class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand, count =  None, 0
        for n in nums:
            if count == 0:
                cand = n
            count += 1 if n == cand else -1
        return cand
        """
        Example Testcase #1
        nums = [3, 2, 3]
        n = 3
        cand = 3

        n == cand -> 3 == 3? Y
        count += 1
        count = 1

        n = 2
        cand = 3

        n == cand -> 2 == 3? N
        count -= 1
        count = 0

        n = 3
        cand = 3

        n == cand -> 3 == 3? Y
        count += 1
        count = 1

        return cand -> 3
        """