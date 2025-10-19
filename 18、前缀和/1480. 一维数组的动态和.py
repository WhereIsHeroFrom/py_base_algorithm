class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = [ nums[0] ]
        n = len(nums)
        for i in range(1, n):
            x = ret[i-1] + nums[i]
            ret.append(x)
        return ret


# runningSum[i] = sum(nums[0]¡­nums[i])
#               = sum(nums[0]¡­nums[i-1]) + nums[i]
#               = runningSum[i-1] + nums[i]
# runningSum[j] = sum(nums[0]¡­nums[j])
# runningSum[i-1] = sum(nums[0]¡­nums[i-1])


# ret[i] = ret[i-1] + nums[i]