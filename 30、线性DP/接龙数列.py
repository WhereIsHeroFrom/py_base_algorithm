import os
import sys

dp = {}

n = int(input())
slist = str(input()).split()
m = 0
for i in range(n):
    s = slist[i]
    l = s[0]
    r = s[-1]
    dp[r] = max(dp.get(l, 0) + 1, dp.get(r, 0))
    m = max(m, dp[r])
print(n - m)