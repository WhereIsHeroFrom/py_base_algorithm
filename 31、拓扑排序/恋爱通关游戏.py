import os
import queue
import sys

def initEdges(n):  # return edges
    return [[] for _ in range(n)]

def addEdge(edges, u, v, w):
    edges[u].append( (v, w) )

def topoSort(n, edges, ans):
    deg = [0 for i in range(n)]
    q = queue.Queue()
    for i in range(n):
        for (v, w) in edges[i]:
            deg[v] += 1
    for i in range(n):
        if deg[i] == 0:
            q.put(i)
    while not q.empty():
        u = q.get()
        ans.append(u)
        for (v, w) in edges[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.put(v)
    return len(ans) == n

n, m = map(int, input().split())
edges = initEdges(n)
for i in range(m):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    addEdge(edges, A, B, C)

ans = []
topoSort(n, edges, ans)
dp = [-1000000000 for i in range(n)]
dp[0] = 0
ret = 0
for u in ans:
    for (v, w) in edges[u]:
        dp[v] = max(dp[v], dp[u] + w)

for i in range(n):
    if dp[i] >= 100 and len(edges[i]) == 0:
        ret += 1

print(ret)