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

    def trimMean(self, arr: List[int]) -> float:
        self.insertionSort(arr)
        n = len(arr)
        c = 0
        s = 0
        for i in range(n//20, n-n//20):
            c += 1
            s += arr[i]
        return s / c