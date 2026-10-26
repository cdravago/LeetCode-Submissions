class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # nums = [1,1,1,2,2,3] -> Counter(nums)
        #                      -> count = {"1":3, "2":2, "3":1}
        buckets = [[]for _ in range(len(nums) + 1)]
                    # buckets = [[], [], [], [], [], [], []]
        for num, f in count.items():
            # Showing all iterations
            # "1", 3
            # "2", 2
            # "3", 1
            buckets[f].append(num)
                    # buckets[3].append("1")
                    # buckets[2].append("2")
                    # buckets[1].append("3")
            # buckets = [[], ["3"], ["2"], ["1"], [], [], []]
        res = []
        for f in range(len(buckets) - 1, 0, -1): # range(6, 0, -1)
            for num in buckets[f]:

                res.append(num)
                if len(res) == k:
                    return res


