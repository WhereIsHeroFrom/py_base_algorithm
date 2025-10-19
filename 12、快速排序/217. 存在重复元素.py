class Solution:
    def Partition(self, a, l, r):
        idx = random.randint(l, r)
        a[l], a[idx] = a[idx], a[l]
        i = l
        j = r
        x = a[i]
        while i < j:
            while i < j and a[j] > x:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
            
            while i < j and a[i] < x:
                i += 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                j -= 1
        return i

    def QuickSort(self, a, l, r):
        if l >= r:
            return
        pivox = self.Partition(a, l, r)
        self.QuickSort(a, l, pivox-1)
        self.QuickSort(a, pivox+1, r)

    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        self.QuickSort(nums, 0, n-1)
        return nums[n//2]
    






