import os
import sys

inf = -1
init = 0

def opt(a, b):
    if a == inf:
        return b
    if b == inf:
        return a
    return max(a, b)

def KnapsackComplete(n, V, w, v):
    dp = [inf for i in range(V+1)]
    dp[0] = init

    for i in range(1, n+1):
        for j in range(w[i], V+1):
            dp[j] = opt(dp[j], dp[j-w[i]] + v[i])
    return dp

n, V = map(int, input().split())
w = [0]
v = [0]
for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

dp = KnapsackComplete(n, V, w, v)
print( max(dp) )