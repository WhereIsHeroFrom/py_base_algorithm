class Solution:
    def bubbleSort(self, a):
        n = len(a)
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
