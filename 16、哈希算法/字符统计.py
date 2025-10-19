import os
import sys

cnt = {}

S = input()

for s in S:
    x = cnt.get(s, 0)
    cnt[s] = x + 1

maxc = 0
ret = []

for v, c in cnt.items():
    if c > maxc:
        maxc = c
        ret = [v]
    elif c == maxc:
        ret.append(v)

ret = sorted(ret, key = lambda x : x)

print(''.join(ret))