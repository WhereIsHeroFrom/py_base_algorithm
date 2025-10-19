import os
import queue
import sys

def initEdges(n):  # return edges
    return [[] for _ in range(n)]

def addEdge(edges, u, v):
    edges[u].append(v)

def topoSort(n, edges, ans):
    deg = [0 for i in range(n)]
    q = queue.Queue()
    for i in range(n):
        for v in edges[i]:
            deg[v] += 1
    for i in range(n):
        if deg[i] == 0:
            q.put(i)
    while not q.empty():
        u = q.get()
        ans.append(u)
        for v in edges[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.put(v)
    return len(ans) == n

n, m = map(int, input().split())
a = list(map(int, input().split()))
edges = initEdges(n)
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if a[u] < a[v]:
        addEdge(edges, u, v)
    elif a[v] < a[u]:
        addEdge(edges, v, u)

ans = []
topoSort(n, edges, ans)
ret = 0
dp = [0 for i in range(n)]

for u in ans[::-1]:
    m = 0
    for v in edges[u]:
        m = max(m, dp[v])
    dp[u] = a[u] + m
    ret = max(ret, dp[u])

print(ret)