class Solution:
    def selectionSort(self, a):
        n = len(a)
        for i in range(0, n):
            min = i
            for j in range(i+1, n):
                if a[j] < a[min]:
                    min = j
            a[i], a[min] = a[min], a[i]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for x in nums2:
            nums1.append(x)
        n = len(nums1)
        self.selectionSort(nums1)
        if n % 2 == 1:
            return nums1[n//2]
        return (nums1[n//2-1] + nums1[n//2]) / 2.0
