import os
import sys

# 请在此输入您的代码

n = int(input())
A = list( map(int, input().split()) )
B = list( map(int, input().split()) )
C = [2*x for x in A]

B = sorted(B)
C = sorted(C)

i = 0
j = 0
ans = 0

while i < n and j < n:
    if C[i] > B[j]:
        ans += 1
        j += 1
    i += 1

print(ans)