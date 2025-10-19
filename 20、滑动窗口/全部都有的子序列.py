import os
import sys

def slideWindow(n, a):
    i = 0
    j = -1
    count = {}
    need = 0
    for x in a:
        if count.get(x, None) == None:
            need += 1
        count[x] = 0
    tot = 0
    ret = n
    while j < n - 1:
        j += 1
        count[a[j]] += 1
        if count[a[j]] == 1:
            tot += 1
        while tot == need:
            # [i,j]
            ret = min(ret, j-i+1)
            count[a[i]] -= 1
            if count[a[i]] == 0:
                tot -= 1
            i += 1
    return ret


n = int(input())
a = list(map(int, input().split()))
ans = slideWindow(n, a)
print(ans)