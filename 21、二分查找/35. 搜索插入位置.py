class Solution:

    def isGreen(self, nums, index, t):
        return nums[index] >= t

    def bSearch(self, nums, t):
        l = -1
        r = len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if self.isGreen(nums, mid, t):
                r = mid
            else:
                l = mid
        return r

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bSearch(nums, target)