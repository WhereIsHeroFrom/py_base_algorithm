# Python3提交超时的话，尝试用 PyPy3 提交
import os
import sys

mod = 1000000007

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0 for i in range(n+1)]
dp[0] = 1

for i in range(1, n+1):
    mmax = 0
    mmin = 100000000
    for j in range(i, 0, -1):
        mmax = max(mmax, a[j])
        mmin = min(mmin, a[j])
        if mmax - mmin == i - j:
            dp[i] += dp[j-1]
            if dp[i] >= mod:
                dp[i] -= mod

print(dp[n])