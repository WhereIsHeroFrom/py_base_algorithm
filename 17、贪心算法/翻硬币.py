import os
import sys

s = input()
t = input()
n = len(s)

s = [i for i in s]
ret = 0

for i in range(n):
    if s[i] != t[i]:
        s[i] = ('*' if s[i] == 'o' else 'o')
        s[i+1] = ('*' if s[i+1] == 'o' else 'o')
        ret += 1

print(ret)