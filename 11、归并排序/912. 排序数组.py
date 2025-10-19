class Solution:

    def merge(self, left, right):
        ret = []
        i = j = 0
        n1 = len(left)
        n2 = len(right)
        while i < n1 and j < n2:
            if left[i] < right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        
        while i < n1:
            ret.append(left[i])
            i += 1

        while j < n2:
            ret.append(right[j])
            j += 1

        return ret

    def mergeSort(self, a):
        if len(a) <= 1:
            return a
        m = len(a) // 2
        l = self.mergeSort(a[:m])
        r = self.mergeSort(a[m:])
        return self.merge(l, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        