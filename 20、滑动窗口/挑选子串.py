import os
import sys

def slideWindow(n, k, a):
    i = 0
    j = -1
    sum = 0
    ans = 0
    while j < n-1:
        j += 1
        sum += a[j]
        while sum >= k:
            # [i,j], [i,j+1], ..., [i, n-1]
            # j, j+1, j+2, ..., n-1
            ans += n - j
            sum -= a[i]
            i += 1
    return ans

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = (1 if a[i] >= m else 0)
ans = slideWindow(n, k, a)
print(ans)