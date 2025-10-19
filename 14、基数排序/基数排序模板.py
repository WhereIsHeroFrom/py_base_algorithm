class Solution:
    
    MAXN = 50005
    MAXT = 8
    BASE = 10

    def RadixSort(self, a):
        n = len(a)
        PowOfBase = [1 for i in range(self.MAXT)]
        for i in range(1, self.MAXT):
            PowOfBase[i] = PowOfBase[i-1] * self.BASE
        
        for i in range(n):
            a[i] += PowOfBase[self.MAXT-1]
        
        pos = 0
        while pos < self.MAXT:
            RadixBucket = [ [] for i in range(self.BASE) ]

            for i in range(n):
                rdx = a[i] // PowOfBase[pos] % self.BASE
                RadixBucket[rdx].append( a[i] )
            
            top = 0
            for i in range(self.BASE):
                for rb in RadixBucket[i]:
                    a[top] = rb
                    top += 1
            
            pos += 1

        for i in range(n):
            a[i] -= PowOfBase[self.MAXT-1]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.RadixSort(nums)
        return nums