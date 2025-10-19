import os
import sys

maxn = 10
visited = [False for i in range(maxn)]
N = -1
ret = 0
pow10 = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000
]

# N    = 82  +  3546/197
#        x
# i = 7,  10^7


def cnt(ans):
    c = 0
    for i in range(8, 0, -1):
        x = ans // pow10[i]
        if N <= x:
            break
        y = N - x
        z = ans % pow10[i]

        for j in range(1, i):
            fz = z // pow10[j]
            fm = z % pow10[j]
            if fz < fm:
                break
            if fz % fm == 0:
                if fz // fm == y:
                    c += 1
    return c



def dfs(depth, maxDepth, ans):
    global visited, ret

    if depth == maxDepth:
        ret += cnt(ans)
        return
        
    for i in range(maxDepth):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, maxDepth, ans * 10 + (i+1))
            visited[i] = False

N = int(input())
dfs(0, 9, 0)
print(ret)