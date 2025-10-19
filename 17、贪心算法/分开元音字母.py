import os
import sys

def isYuanYin(s):
    return s in ["a", "e", "i", "o", "u"]

s = input()
ret = "("
cnt = 0
flag = False

for ch in s:
    if isYuanYin(ch):
        flag = True
        cnt += 1
        if cnt > 1:
            ret += ")("
            cnt = 1
    ret += ch

ret += ")"
if flag == False:
    ret = s

print(ret)