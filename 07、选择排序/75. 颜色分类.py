class Solution:
    def selectionSort(self, a):
        n = len(a)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if a[j] < a[min]:
                    min = j
            a[i], a[min] = a[min], a[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.selectionSort(nums)