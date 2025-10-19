import os
import sys

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SB = 1000000001
cnt = {}
ret = 0

# A[i] = B[j]
# B[i] = A[j]
# (A[i] * SB + B[i]) == (B[j] * SB + A[j])

for j in range(n):
    ret += cnt.get( (B[j], A[j]), 0)
    cnt[(A[j], B[j])] = cnt.get((A[j], B[j]), 0) + 1

print(ret)