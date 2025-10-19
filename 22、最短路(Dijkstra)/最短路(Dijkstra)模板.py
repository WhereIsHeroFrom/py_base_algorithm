import sys

maxn = 101
inf = sys.maxsize  # 用系统最大整数表示无穷大
graph = [[inf for _ in range(maxn)] for _ in range(maxn)]  # 邻接矩阵

def init_edges(n):
    """初始化邻接矩阵"""
    for i in range(n):
        for j in range(n):
            graph[i][j] = inf

def add_edge(u, v, w):
    """添加边，保留最小权重"""
    if graph[u][v] == inf or w < graph[u][v]:
        graph[u][v] = w

def dijkstra(n, s, dist):
    """Dijkstra算法求最短路径"""
    visited = [False] * maxn  # 标记是否访问过
    # 初始化距离数组和访问数组
    for i in range(n):
        visited[i] = False
        dist[i] = inf
    dist[s] = 0  # 起点到自身距离为0
    
    while True:
        min_dist = inf
        min_index = -1
        # 找到未访问节点中距离最小的
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i
        
        if min_dist == inf:  # 所有可达节点都已处理
            break
        
        visited[min_index] = True  # 标记为已访问
        
        # 更新相邻节点的距离
        for i in range(n):
            if not visited[i] and graph[min_index][i] != inf:
                if dist[i] > dist[min_index] + graph[min_index][i]:
                    dist[i] = dist[min_index] + graph[min_index][i]

def main():
    n = 6  # 节点数量
    m = 9  # 边的数量
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
    
    # 初始化邻接矩阵
    init_edges(n)
    
    # 构建图
    for i in range(m):
        u, v, w = edges[i]
        add_edge(u, v, w)
    
    # 计算最短路径
    dist = [inf] * maxn
    dijkstra(n, 0, dist)
    
    # 输出结果
    for i in range(n):
        print(f"{0}到{i}的最短路为{dist[i]}")

if __name__ == "__main__":
    main()