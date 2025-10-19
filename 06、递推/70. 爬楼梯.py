class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1, 1]
        for i in range(2, n+1):
            v = f[i-1] + f[i-2]
            f.append(v)
        return f[n]


# 0 1 2 3 4 5  6 
# 1 1 2 3 5 8 13