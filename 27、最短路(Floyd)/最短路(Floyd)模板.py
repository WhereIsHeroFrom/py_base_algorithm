import sys

maxn = 100
inf = sys.maxsize  # 用系统最大整数表示无穷大

# 初始化邻接矩阵
f = [[0 for _ in range(maxn)] for _ in range(maxn)]

def init_edges(n):
    """初始化邻接矩阵，对角线为0，其余为无穷大"""
    for i in range(n):
        for j in range(n):
            if i == j:
                f[i][j] = 0
            else:
                f[i][j] = inf

def add_edge(u, v, w):
    """添加有向边，保留最小权重"""
    if w < f[u][v]:
        f[u][v] = w

def floyd_warshall(n):
    """Floyd-Warshall算法计算所有节点对之间的最短路径"""
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 跳过不可达的中间路径
                if f[i][k] == inf or f[k][j] == inf:
                    continue
                # 跳过中间节点与起点或终点相同的情况
                if i == k or j == k:
                    continue
                # 更新最短路径
                if f[i][k] + f[k][j] < f[i][j]:
                    f[i][j] = f[i][k] + f[k][j]

def main():
    n = 4  # 示例节点数量
    init_edges(n)
    # 添加示例边
    add_edge(0, 1, 2)
    add_edge(0, 2, 6)
    add_edge(1, 2, 3)
    add_edge(1, 3, 8)
    add_edge(2, 3, 1)
    # 计算最短路径
    floyd_warshall(n)
    # 输出结果
    for i in range(n):
        for j in range(n):
            print(f"{i}到{j}的最短路径: {f[i][j] if f[i][j] != inf else '不可达'}")

if __name__ == "__main__":
    main()