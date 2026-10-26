class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, best = float('inf'), 0 
        for p in prices:
            low = min(low, p)
            best = max(best, p - low)
        return best
        """
        Example 1:
        prices = [7,1,5,3,6,4]

        low, best = float('inf'), 0
        for p in prices:
            7
            low = min(low, p)
            low = min(float('inf'), 7)
            low = float('inf')

            best = max(best, p - low)
            best = max(0 , 7 - float('inf'))
            best = max(0, )
        """