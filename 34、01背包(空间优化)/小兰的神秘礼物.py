import os
import sys

inf = 0     # dp[0][5]
init = 1    # dp[0][0]

def opt(a, b):
    if a == inf : return b
    if b == inf : return a
    return init

def Knapsack01(n, V, w, v):
    dp = [inf for _ in range(V+1)]
    dp[0] = init

    for i in range(1, n+1):
        for j in range(V, w[i]-1, -1):
            dp[j] = opt(dp[j], dp[j - w[i]] + v[i])
    return dp

V = int(input())
n = int(input())
w = [0 for i in range(n+1)]
v = [0 for i in range(n+1)]
for i in range(1, n+1):
    w[i] = int(input())

dp = Knapsack01(n, V, w, v)
ans = 0
for i in range(V, -1, -1):
    if dp[i] == init:
        ans = V - i
        break

print(ans)