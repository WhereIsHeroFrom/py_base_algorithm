from collections import deque

maxn = 1000005  # 最大节点数量

def init_edges(n, edges):
    """初始化邻接表，清空所有节点的边"""
    for i in range(n):
        edges[i].clear()

def add_edge(edges, u, v):
    """向邻接表添加有向边 u -> v"""
    edges[u].append(v)

def topo_sort(n, edges, ans):
    """
    拓扑排序算法
    参数:
        n: 节点数量
        edges: 邻接表
        ans: 用于存储排序结果的列表
    返回:
        bool: 若存在合法拓扑排序则返回True，否则返回False（存在环）
    """
    deg = [0] * n  # 存储每个节点的入度
    q = deque()    # 用于处理入度为0的节点的队列
    ans.clear()    # 清空结果列表
    
    # 计算每个节点的入度
    for i in range(n):
        for v in edges[i]:
            deg[v] += 1
    
    # 将所有入度为0的节点加入队列
    for i in range(n):
        if deg[i] == 0:
            q.append(i)
    
    # 处理队列中的节点
    while q:
        u = q.popleft()
        ans.append(u)  # 将节点加入拓扑排序结果
        
        # 减少相邻节点的入度
        for v in edges[u]:
            deg[v] -= 1
            if deg[v] == 0:  # 若入度变为0，加入队列
                q.append(v)
    
    # 若结果长度等于节点数量，说明存在合法拓扑排序
    return len(ans) == n

# 初始化邻接表（使用列表的列表模拟）
edges = [[] for _ in range(maxn)]

def main():
    n = 6  # 节点数量
    # 初始化邻接表
    init_edges(n, edges)
    
    # 添加测试边
    edges_list = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 3),
        (3, 4),
        (3, 5)
    ]
    for u, v in edges_list:
        add_edge(edges, u, v)
    
    # 执行拓扑排序
    ans = []
    if topo_sort(n, edges, ans):
        print("拓扑排序结果:", ans)
    else:
        print("图中存在环，无法进行拓扑排序")

if __name__ == "__main__":
    main()