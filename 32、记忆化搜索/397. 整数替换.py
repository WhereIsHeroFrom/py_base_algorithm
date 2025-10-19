f = {}

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 1:
            return 0
        if f.get(n):
            return f[n]
        if n % 2 == 0:
            ans = self.integerReplacement(n//2) + 1
        else:
            ans = min( self.integerReplacement(n+1), self.integerReplacement(n-1) ) + 1
        f[n] = ans
        return ans