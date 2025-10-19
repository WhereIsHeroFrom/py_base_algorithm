class Solution:
    def insertionSort(self, a):
        n = len(a)
        for i in range(1, n):
            x = a[i]
            j = i - 1
            while j >= 0:
                if x < a[j]:
                    a[j+1] = a[j]
                else:
                    break
                j -= 1
            a[j+1] = x
    def minimumDifference(self, nums: List[int], k: int) -> int:
        self.insertionSort(nums)
        n = len(nums)
        ret = 10000000
        for i in range(n+1-k):
            l = i
            r = i + k - 1
            # r < n  -> i+k-1 < n  -> i < n+1-k
            ret = min(ret, nums[r] - nums[l])
        return ret