maxn = 1001
maxm = 20001
inf = 1000000000

# 定义边的类，替代 C++ 中的 struct EDGE
class Edge:
    def __init__(self, u, v, w):
        self.u = u  # 起点
        self.v = v  # 终点
        self.w = w  # 权重

def do_relax(m, edges, dist):
    """松弛操作：尝试更新所有边的终点距离"""
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
    Bellman-Ford 算法
    返回值：0 表示无负环，1 表示存在负环
    """
    # 初始化距离数组，起点距离为0，其余为无穷大
    for i in range(n):
        dist[i] = 0 if i == s else inf
    
    # 进行 n-1 次松弛
    for i in range(n - 1):
        if not do_relax(m, edges, dist):
            return 0  # 提前收敛，无负环
    
    # 第 n 次松弛检查是否有负环
    return do_relax(m, edges, dist)

# 全局变量（对应 C++ 中的全局变量）
n = 0
e = 0
m = 0
edges = [Edge(0, 0, 0) for _ in range(maxm)]  # 边的数组
dist = [0] * maxn  # 距离数组

def main():
    # 这里可以添加测试代码
    pass

if __name__ == "__main__":
    main()