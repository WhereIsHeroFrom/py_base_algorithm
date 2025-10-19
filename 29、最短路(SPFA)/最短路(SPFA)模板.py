from collections import deque

maxn = 2024
inf = 1000000000
# ����·���ȽϷ�ʽ�������Ӧԭ�����longOrShortPath <���������·����
long_or_short_path = lambda a, b: a < b

class Edge:
    """�ߵ��࣬��ӦC++�е�EDGE�ṹ��"""
    def __init__(self, v=0, w=0):
        self.v = v  # Ŀ�궥��
        self.w = w  # �ߵ�Ȩ��

def init_edges(n, edges):
    """��ʼ���ڽӱ�"""
    for i in range(n + 1):
        edges[i].clear()

def add_edge(edges, u, v, w):
    """��������"""
    edges[u].append(Edge(v, w))

def spfa_init(n, s, dist, q, inqueue):
    """SPFA�㷨��ʼ��"""
    for i in range(n + 1):
        dist[i] = 0 if i == s else inf
        inqueue[i] = False
    inqueue[s] = True
    q.append(s)

def spfa_update(edges, u, dist, q, inqueue):
    """SPFA�㷨�е��ɳڲ���"""
    for edge in edges[u]:
        v = edge.v
        w = edge.w
        if long_or_short_path(dist[u] + w, dist[v]):
            dist[v] = dist[u] + w
            if not inqueue[v]:
                inqueue[v] = True
                q.append(v)

def spfa(edges, n, s, dist):
    """SPFA�㷨������"""
    q = deque()  # ʹ��˫�˶�����Ϊ����
    inqueue = [False] * (n + 1)  # ��ǽڵ��Ƿ��ڶ�����
    spfa_init(n, s, dist, q, inqueue)
    
    while q:
        u = q.popleft()
        inqueue[u] = False
        spfa_update(edges, u, dist, q, inqueue)

# ��ʼ���ڽӱ�;�������
edges = [[] for _ in range(maxn)]  # �ڽӱ�ÿ��Ԫ����Edge������б�
dist = [0] * maxn  # ��������

def main():
    n = 5  # �ڵ�����
    s = 0  # ���
    
    # ��ʼ��
    init_edges(n, edges)
    
    # ��Ӳ��Ա�
    add_edge(edges, 0, 1, 1)
    add_edge(edges, 0, 2, 4)
    add_edge(edges, 1, 2, 2)
    add_edge(edges, 1, 3, 5)
    add_edge(edges, 2, 3, 1)
    
    # ����SPFA�㷨
    spfa(edges, n, s, dist)
    
    # ������
    for i in range(n + 1):
        print(f"��{s}��{i}�����·��: {dist[i]}")

if __name__ == "__main__":
    main()