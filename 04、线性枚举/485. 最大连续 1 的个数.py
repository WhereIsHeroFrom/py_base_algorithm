class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        pre = 0
        for x in nums:
            if x == 1:
                pre = pre + 1
                if pre > max:
                    max = pre
            else:
                pre = 0
        return max
