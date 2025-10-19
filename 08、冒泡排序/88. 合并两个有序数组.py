class Solution:
    def bubbleSort(self, a):
        n = len(a)
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        self.bubbleSort(nums1)