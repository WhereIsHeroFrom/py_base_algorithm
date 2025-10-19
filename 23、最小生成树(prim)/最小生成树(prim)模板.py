maxn = 2022
inf = 1000000000

def init_edges(n, graph):
    """初始化邻接矩阵，对角线为0，其余为无穷大"""
    for i in range(n):
        for j in range(n):
            graph[i][j] = 0 if i == j else inf

def add_edge(graph, u, v, w):
    """添加无向边，保留最小权重"""
    if w < graph[u][v]:
        graph[u][v] = w
    if w < graph[v][u]:
        graph[v][u] = w

def prim(n, graph):
    """Prim算法求最小生成树的总权重"""
    visited = [0] * maxn  # 标记节点是否被访问
    dist = [0] * maxn    # 记录到已选集合的最小距离
    total = 0            # 最小生成树的总权重
    
    # 初始化距离数组，以0为起点
    for i in range(n):
        dist[i] = graph[0][i]
    visited[0] = 1       # 标记起点为已访问
    
    while True:
        min_dist = inf
        min_index = -1
        # 找到未访问节点中距离最小的
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i
        
        if min_index == -1:  # 所有可达节点都已处理
            break
        
        total += min_dist
        visited[min_index] = 1
        
        # 更新未访问节点的距离
        for i in range(n):
            if not visited[i] and graph[min_index][i] < dist[i]:
                dist[i] = graph[min_index][i]
    
    # 检查是否所有节点都被访问（图是否连通）
    for i in range(n):
        if not visited[i]:
            return -1  # 图不连通，无最小生成树
    
    return total

def main():
    n = 6  # 节点数量
    m = 9  # 边的数量
    # 初始化邻接矩阵
    graph = [[0 for _ in range(maxn)] for _ in range(maxn)]
    init_edges(n, graph)
    
    edges = [
        [0, 1, 1],
        [0, 2, 4],
        [0, 3, 10],
        [1, 2, 2],
        [2, 3, 5],
        [2, 4, 1],
        [2, 5, 3],
        [4, 5, 1],
        [5, 3, 1],
    ]
    
    # 构建图
    for u, v, w in edges:
        add_edge(graph, u, v, w)
    
    # 计算并输出最小生成树的总权重
    result = prim(n, graph)
    print(f"最小生成树的长度为：{result}")

if __name__ == "__main__":
    main()