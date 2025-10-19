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
    dp = [[inf]*(V+1) for i in range(n+1) ]
    dp[0][0] = init
    
    for i in range(1, n+1):
        for j in range(0, V+1):
            if j >= w[i]:
                dp[i][j] = opt(dp[i-1][j], dp[i][j-w[i]] + v[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp


n, V = map(int, input().split())
w = [0]
v = [0]
for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

dp = KnapsackComplete(n, V, w, v)
ans = inf
for i in range(V+1):
    ans = opt(ans, dp[n][i])

print(ans)