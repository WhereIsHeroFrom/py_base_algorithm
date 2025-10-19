class Solution:

    def Partition(self, a, l, r):
        idx = random.randint(l, r)
        pivox = a[idx]
        a[l], a[idx] = a[idx], a[l]
        i = j = l + 1
        while i <= r:
            if a[i] < pivox:
                a[i], a[j] = a[j], a[i]
                j += 1
            i += 1
        a[l], a[j-1] = a[j-1], a[l]
        return j-1

    def QuickSort(self, a, l, r):
        if l >= r:
            return
        pivox = self.Partition(a, l, r)
        self.QuickSort(a, l, pivox-1)
        self.QuickSort(a, pivox+1, r)

    def containsDuplicate(self, nums: List[int]) -> bool:
        self.QuickSort(nums, 0, len(nums)-1)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False