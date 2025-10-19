import os
import sys

def slideWindow(n, k, a):
    i = 0
    j = -1
    count = {}
    ret = 0
    while j < n-1:
        j += 1
        count[ a[j] ] = count.get(a[j], 0) + 1
        while count[ a[j] ] > k:
            count[ a[i] ] -= 1
            i += 1
        ret = max(ret, j-i+1)
    return ret

a = str(input())
k = int(input())
ans = slideWindow(len(a), k, a)
print(ans)