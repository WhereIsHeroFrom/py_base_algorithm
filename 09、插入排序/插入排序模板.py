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