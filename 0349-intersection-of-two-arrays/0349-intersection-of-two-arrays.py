class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Example: Testcase #2
        nums1 =  [4,9,5]
        nums2 = = [9,4,9,8,4]
        set(nums1) = [4,9,5]
        set(nums2) = [9,4,8]
        set(nums1) & set(nums2) = 9, 4
        list -> [9,4]
        """
        return list(set(nums1) & set(nums2))