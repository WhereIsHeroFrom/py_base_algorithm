import os
import sys

inf = 1000000000

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def doRelax(edges, dist):
    isRelax = False
    for e in edges:
        if  dist[e.u] + e.w < dist[e.v]:
            dist[e.v] = dist[e.u] + e.w
            isRelax = True
    return isRelax

def bellman(n, edges, s):
    dist = [inf for _ in range(n)]
    dist[s] = 0
    for i in range(n-1):
        if not doRelax(edges, dist):
            return False, dist

    if not doRelax(edges, dist):
        return False, dist

    return True, dist

def calcEdge(a, b, l):
    ans = 0
    for i in range(l):
        if a[i] != b[i]:
            ans += 1
        if ans > 1:
            return False
    return True

strList = []
edges = []

n = int(input())
for i in range(n):
    strList.append( input() )
l = len(strList[0])

for i in range(n):
    for j in range(i+1, n):
        if calcEdge(strList[i], strList[j], l):
            edges.append( Edge(i, j, 1) )
            edges.append( Edge(j, i, 1) )

st, en = input().split()

s, d = -1, -1
for i in range(n):
    if st == strList[i]:
        s = i
    if en == strList[i]:
        d = i
_, dist = bellman(n, edges, s)
if dist[d] == inf:
    dist[d] = -1

print(dist[d])