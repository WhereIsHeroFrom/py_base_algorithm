class Solution:
    def bubbleSort(self, a):
        n = len(a)
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]

    def countElements(self, nums: List[int]) -> int:
        cnt = 0
        self.bubbleSort(nums)
        n = len(nums)
        for i in range(1, n-1):
            if nums[i] != nums[0] and nums[i] != nums[n-1]:
                cnt += 1
        return cnt