import os
import sys

inf = 1000000000

def initEdges(n):
    graph = [[inf]*n for i in range(n)]
    for i in range(n):
        graph[i][i] = 0
    return graph

def addEdge(graph, u, v, w):
    if w < graph[u][v]:
        graph[u][v] = w
    if w < graph[v][u]:
        graph[v][u] = w

def prim(n, graph):
    visited = [False for _ in range(n)]
    dist = [graph[0][i] for i in range(n)]
    sum = 0
    visited[0] = True

    while True:
        minDist = inf
        minIndex = -1
        for i in range(n):
            if not visited[i] and dist[i] < minDist:
                minDist = dist[i]
                minIndex = i
        if minIndex == -1:
            break
        sum += minDist
        visited[minIndex] = True

        for i in range(n):
            if not visited[i] and graph[minIndex][i] < dist[i]:
                dist[i] = graph[minIndex][i]

    for i in range(n):
        if not visited[i]:
            return -1

    return sum

u, v, c = [], [], []
n, m = map(int, input().split())
for i in range(m):
    x, y, z = map(int, input().split())
    u.append(x)
    v.append(y)
    c.append(z)

def check(max):
    graph = initEdges(n)
    for i in range(m):
        if c[i] <= max:
            addEdge(graph, u[i]-1, v[i]-1, c[i])
    return prim(n, graph) >= 0

l = 0
r = 10000
ans = -1
while l <= r:
    mid = (l+r) // 2
    if check(mid):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(n-1, ans)