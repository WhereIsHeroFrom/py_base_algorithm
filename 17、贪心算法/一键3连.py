import os
import sys

n = int(input())
A = list(map(int, input().split()))

A = sorted(A)

l = 1
r = 1

while r < n:
    if A[r] != A[l-1]:
        A[l] = A[r]
        l += 1
    r += 1

res = 0
for i in range(l-2):
    a = A[i]
    if A[i+1] == a+1 and A[i+2] == a+2:
        res += 1

print(res)