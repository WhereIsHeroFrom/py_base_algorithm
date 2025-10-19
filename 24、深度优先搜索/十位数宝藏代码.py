import os
import sys

''' 全排列模板
maxn = 10
visited = [False for i in range(maxn)]
stack = [0 for i in range(maxn)]

def dfs(depth, maxDepth):
    global stack, visited

    if depth == maxDepth:
        # stack 存储的就是 [0, maxDepth-1]
        return
        
    for i in range(maxDepth):
        if not visited[i]:
            visited[i] = True
            stack[depth] = i;
            dfs(depth+1, maxDepth)
            visited[i] = False

'''

maxn = 10
visited = [False for i in range(maxn)]
stack = [0 for i in range(maxn)]

Min = 10000000000000
Max = 0

def dfs(depth, maxDepth, ans):
    global stack, visited, Min, Max

    if depth == maxDepth:
        # stack 存储的就是 [0, maxDepth-1]
        if ans % 11 == 0:
            Max = max(Max, ans)
            Min = min(Min, ans)

        return
    
    if depth == 1:
        if ans == 0:
            return 
    
    for i in range(maxDepth):
        if not visited[i]:
            visited[i] = True
            stack[depth] = i;
            dfs(depth+1, maxDepth, ans*10 + i)
            visited[i] = False

# dfs(0, 10, 0)
# print(Max - Min)
print(8852148261)