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

    def lastStoneWeight(self, a: List[int]) -> int:
        n = len(a)
        while n > 1:
            self.countingSort(a, 1000)
            v = a[-1] - a[-2]
            n -= 2
            a.pop()
            a.pop()
            if v != 0 or n == 0 :
                a.append(v)
                n += 1
        return a[0]