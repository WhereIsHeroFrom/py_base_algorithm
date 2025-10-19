class Solution:
    def bubbleSort(self, a):
        n = len(a)
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]

    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        while n > 1:
            self.bubbleSort(stones)
            v = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()
            n -= 2
            if v != 0 or n == 0:
                stones.append(v)
                n += 1
        return stones[0]