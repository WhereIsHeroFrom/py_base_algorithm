from collections import deque

maxn = 2024
inf = 1000000000
# 定义路径比较方式（这里对应原代码的longOrShortPath <，即求最短路径）
long_or_short_path = lambda a, b: a < b

class Edge:
    """边的类，对应C++中的EDGE结构体"""
    def __init__(self, v=0, w=0):
        self.v = v  # 目标顶点
        self.w = w  # 边的权重

def init_edges(n, edges):
    """初始化邻接表"""
    for i in range(n + 1):
        edges[i].clear()

def add_edge(edges, u, v, w):
    """添加有向边"""
    edges[u].append(Edge(v, w))

def spfa_init(n, s, dist, q, inqueue):
    """SPFA算法初始化"""
    for i in range(n + 1):
        dist[i] = 0 if i == s else inf
        inqueue[i] = False
    inqueue[s] = True
    q.append(s)

def spfa_update(edges, u, dist, q, inqueue):
    """SPFA算法中的松弛操作"""
    for edge in edges[u]:
        v = edge.v
        w = edge.w
        if long_or_short_path(dist[u] + w, dist[v]):
            dist[v] = dist[u] + w
            if not inqueue[v]:
                inqueue[v] = True
                q.append(v)

def spfa(edges, n, s, dist):
    """SPFA算法主函数"""
    q = deque()  # 使用双端队列作为队列
    inqueue = [False] * (n + 1)  # 标记节点是否在队列中
    spfa_init(n, s, dist, q, inqueue)
    
    while q:
        u = q.popleft()
        inqueue[u] = False
        spfa_update(edges, u, dist, q, inqueue)

# 初始化邻接表和距离数组
edges = [[] for _ in range(maxn)]  # 邻接表，每个元素是Edge对象的列表
dist = [0] * maxn  # 距离数组

def main():
    n = 5  # 节点数量
    s = 0  # 起点
    
    # 初始化
    init_edges(n, edges)
    
    # 添加测试边
    add_edge(edges, 0, 1, 1)
    add_edge(edges, 0, 2, 4)
    add_edge(edges, 1, 2, 2)
    add_edge(edges, 1, 3, 5)
    add_edge(edges, 2, 3, 1)
    
    # 运行SPFA算法
    spfa(edges, n, s, dist)
    
    # 输出结果
    for i in range(n + 1):
        print(f"从{s}到{i}的最短路径: {dist[i]}")

if __name__ == "__main__":
    main()