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

n, e = map(int, input().split())
c = list(map(int, input().split()))

c[n-1] = 0
m = 0
edges = []
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append( Edge(u-1, v-1, w+c[v-1]) )
    edges.append( Edge(v-1, u-1, w+c[u-1]) )

_, dist = bellman(n, edges, 0)
print( dist[n-1] )