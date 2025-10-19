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

n, m, x = map(int, input().split())
x -= 1
u, v, w = [], [], []
for i in range(m):
    a, b, c = map(int, input().split())
    u.append(a-1)
    v.append(b-1)
    w.append(c)

edges = [None for _ in range(m)]

for i in range(m):
    edges[i] = Edge( u[i], v[i], w[i] )
_, dist1 = bellman(n, edges, x)

for i in range(m):
    edges[i] = Edge( v[i], u[i], w[i] )
_, dist2 = bellman(n, edges, x)

ret = 0
for i in range(n):
    ret = max(ret, dist1[i] + dist2[i])

print(ret)