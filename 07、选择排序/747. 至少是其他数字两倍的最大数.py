class Solution:
    def selectionSort(self, a):
        n = len(a)
        for i in range(0, n):
            min = i
            for j in range(i+1, n):
                if a[j] < a[min]:
                    min = j
            a[i], a[min] = a[min], a[i]

    def dominantIndex(self, nums: List[int]) -> int:
        max = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max]:
                max = i
        self.selectionSort(nums)
        maxv = nums[-1]
        submaxv = nums[-2]
        if maxv >= 2 * submaxv:
            return max
        return -1