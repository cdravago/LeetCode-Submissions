class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            # [1 ,1, 2]
            # nums[0] = 1
            # nums[k - 1] = nums[0] = 1
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i] # Write value at index i 
                                  # nums[0] = 0
                k += 1            # Then. increment k count
        return k
