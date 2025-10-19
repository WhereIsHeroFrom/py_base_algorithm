import os
import sys

# 请在此输入您的代码
# dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])

inf = -1    # dp[0][5]
init = 0    # dp[0][0]

def opt(a, b):
    if a == inf : return b
    if b == inf : return a
    return max(a, b)

def Knapsack01(n, V, w, v):
    dp = []
    for i in range(n+1):
        dpRow = [inf for _ in range(V+1)]
        dp.append( dpRow )
    dp[0][0] = init

    for i in range(1, n+1):
        for j in range(0, V+1):
            if j - w[i] >= 0:
                dp[i][j] = opt(dp[i-1][j], dp[i-1][j - w[i]] + v[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp

n, V = map(int, input().split())
w = [0 for i in range(n+1)]
v = [0 for i in range(n+1)]

for i in range(1, n+1):
    w[i], v[i] = map(int, input().split())


dp = Knapsack01(n, V, w, v)

ans = 0
for i in range(V+1):
    ans = opt(ans, dp[n][i])

print(ans)