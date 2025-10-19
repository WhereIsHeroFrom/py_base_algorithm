import os
import sys

inf = -1000000000

n = int(input())
a = [0] + list(map(int, input().split()))
dp = []
for i in range(n+1):
    dpRow = []
    for j in range(n+1):
        dpRow.append(inf)
    dp.append(dpRow)

dp[0][0] = 0

dp[1][0] = 0
dp[1][1] = a[1]

for i in range(2, n+1):
    dp[i][0] = 0
    for j in range(1, i+1):
        dp[i][j] = max(a[i] + dp[i-2][j-1], dp[i-1][j])

print(dp[n][n//2])