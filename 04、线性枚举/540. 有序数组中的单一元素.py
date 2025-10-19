class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        for i in range(1, l-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        if nums[0] != nums[1]:
            return nums[0]
        return nums[-1]