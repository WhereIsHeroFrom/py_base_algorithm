class Solution:
    def countingSort(self, a, m):
        h = [0 for i in range(m+1)]
        for x in a:
            h[x] += 1
        idx = 0
        for v in range(0, m+1):
            while h[v] > 0:
                a[idx] = v
                idx += 1 
                h[v] -= 1