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

    def search(self, nums: List[int], target: int) -> int:
        idx = self.bSearch(nums, target)
        if idx == len(nums):
            return -1
        if nums[idx] != target:
            return -1
        return idx