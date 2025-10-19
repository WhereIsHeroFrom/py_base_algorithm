maxn = 1001
maxm = 20001
inf = 1000000000

# ����ߵ��࣬��� C++ �е� struct EDGE
class Edge:
    def __init__(self, u, v, w):
        self.u = u  # ���
        self.v = v  # �յ�
        self.w = w  # Ȩ��

def do_relax(m, edges, dist):
    """�ɳڲ��������Ը������бߵ��յ����"""
    is_relax = 0
    for i in range(m):
        u = edges[i].u
        v = edges[i].v
        w = edges[i].w
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            is_relax = 1
    return is_relax

def bellman(n, m, edges, s, dist):
    """
    Bellman-Ford �㷨
    ����ֵ��0 ��ʾ�޸�����1 ��ʾ���ڸ���
    """
    # ��ʼ���������飬������Ϊ0������Ϊ�����
    for i in range(n):
        dist[i] = 0 if i == s else inf
    
    # ���� n-1 ���ɳ�
    for i in range(n - 1):
        if not do_relax(m, edges, dist):
            return 0  # ��ǰ�������޸���
    
    # �� n ���ɳڼ���Ƿ��и���
    return do_relax(m, edges, dist)

# ȫ�ֱ�������Ӧ C++ �е�ȫ�ֱ�����
n = 0
e = 0
m = 0
edges = [Edge(0, 0, 0) for _ in range(maxm)]  # �ߵ�����
dist = [0] * maxn  # ��������

def main():
    # ���������Ӳ��Դ���
    pass

if __name__ == "__main__":
    main()