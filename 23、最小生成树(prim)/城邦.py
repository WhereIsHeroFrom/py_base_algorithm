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
'''
graph = initEdges(2021)
for i in range(1, 2022):
    for j in range(i+1, 2022):
        u = i
        v = j
        w = 0
        while u or v:
            if u%10 != v%10:
                w += u%10 + v%10
            u = u // 10
            v = v // 10
        addEdge(graph, i-1, j-1, w)

print(prim(2021, graph))
'''

print(4046)