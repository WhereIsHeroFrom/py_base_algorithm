inf = 0
init = 1

def opt(a, b):
    if a == inf:
        return b
    if b == inf:
        return a
    return (a + b) % 1000000007

def KnapsackComplete(n, V, w, v):
    dp = [inf for i in range(V+1)]
    dp[0] = init

    for i in range(1, n+1):
        for j in range(w[i], V+1):
            dp[j] = opt(dp[j], dp[j-w[i]] + v[i])
    return dp


class Solution:
    def waysToChange(self, n: int) -> int:
        w = [-1, 25, 10, 5, 1]
        v = [-1,  0,  0, 0, 0]
        dp = KnapsackComplete(4, n, w, v)
        return dp[n]