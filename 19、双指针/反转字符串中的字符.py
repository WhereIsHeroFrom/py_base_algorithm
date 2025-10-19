import os
import sys

# 请在此输入您的代码
s = input()
s = [x for x in s]
i = 0
j = len(s) - 1
while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1

s = ''.join(s)
print(s)