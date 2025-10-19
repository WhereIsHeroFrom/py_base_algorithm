import os
import sys
import math
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

def SQR(x):
    return x * x

x, y, h = [], [], []
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    x.append(a)
    y.append(b)
    h.append(c)

graph = initEdges(n)
for i in range(n):
    for j in range(i+1, n):
        w = math.sqrt( SQR(x[i]-x[j]) + SQR(y[i]-y[j]) ) + SQR( h[i]-h[j] )
        addEdge(graph, i, j, w)

ans = prim(n, graph)
print("%.2f" % ans)