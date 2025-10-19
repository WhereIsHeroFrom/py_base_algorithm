class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]

        for middleIndex in range(n):
            a = 0
            if middleIndex != 0:
                a = nums[middleIndex-1]
            b = nums[n-1] - nums[middleIndex]
            
            if a == b:
                return middleIndex
        return -1