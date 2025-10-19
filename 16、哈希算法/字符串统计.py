import os
import sys

cnt = {}
n = int(input())
for i in range(n):
    s = input()
    cnt[s] = 1
print( len(cnt) )