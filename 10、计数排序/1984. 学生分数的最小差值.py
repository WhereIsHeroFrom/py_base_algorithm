class Solution:
    def countingSort(self, a, m):
        h = [0 for i in range(m+1)]
        for x in a:
            h[x] += 1
        idx = 0
        for v in range(0, m+1):
            while h[v] > 0:
                a[idx] = v
                idx += 1 
                h[v] -= 1
            
    def minimumDifference(self, nums: List[int], k: int) -> int:
        self.countingSort(nums, 100000)
        n = len(nums)
        ret = 10000000
        for i in range(n+1-k):
            l = i
            r = i + k - 1
            # r < n  -> i+k-1 < n  -> i < n+1-k
            ret = min(ret, nums[r] - nums[l])
        return ret