# 0 1 1 2 3 5 8 13 ...
class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range(2, n+1):
            v = f[i-1] + f[i-2]
            f.append(v)
        return f[n]