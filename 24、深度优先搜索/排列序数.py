import os
import sys

maxn = 10
visited = [False for i in range(maxn)]
stack = [0 for i in range(maxn)]
s = ""
sorted_str = ""
ans = -1
count = 0

def dfs(depth, maxDepth):
    global count, ans, stack, visited

    if depth == maxDepth:
        # stack ´æ´¢µÄ¾ÍÊÇ [0, maxDepth-1]
        find = True
        for i in range(maxDepth):
            idx = stack[i]
            if sorted_str[idx] != s[i]:
                find = False
                break

        if find:
            ans = count
        count += 1
        return
    
    if ans != -1:
        return 
        
    for i in range(maxDepth):
        if not visited[i]:
            visited[i] = True
            stack[depth] = i
            dfs(depth+1, maxDepth)
            visited[i] = False

s = input()
sorted_str = sorted(s)
dfs(0, len(s))
print(ans)