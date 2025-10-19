class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0 for i in range(n)]
        s[0] = nums[0]
        for i in range(1, n):
            s[i] = s[i-1] + nums[i]

        for middleIndex in range(n):
            a = 0
            if middleIndex != 0:
                a = s[middleIndex-1]
            b = s[n-1] - s[middleIndex]
            
            if a == b:
                return middleIndex
        return -1