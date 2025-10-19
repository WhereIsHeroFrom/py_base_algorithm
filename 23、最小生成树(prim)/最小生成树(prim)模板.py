maxn = 2022
inf = 1000000000

def init_edges(n, graph):
    """��ʼ���ڽӾ��󣬶Խ���Ϊ0������Ϊ�����"""
    for i in range(n):
        for j in range(n):
            graph[i][j] = 0 if i == j else inf

def add_edge(graph, u, v, w):
    """�������ߣ�������СȨ��"""
    if w < graph[u][v]:
        graph[u][v] = w
    if w < graph[v][u]:
        graph[v][u] = w

def prim(n, graph):
    """Prim�㷨����С����������Ȩ��"""
    visited = [0] * maxn  # ��ǽڵ��Ƿ񱻷���
    dist = [0] * maxn    # ��¼����ѡ���ϵ���С����
    total = 0            # ��С����������Ȩ��
    
    # ��ʼ���������飬��0Ϊ���
    for i in range(n):
        dist[i] = graph[0][i]
    visited[0] = 1       # ������Ϊ�ѷ���
    
    while True:
        min_dist = inf
        min_index = -1
        # �ҵ�δ���ʽڵ��о�����С��
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i
        
        if min_index == -1:  # ���пɴ�ڵ㶼�Ѵ���
            break
        
        total += min_dist
        visited[min_index] = 1
        
        # ����δ���ʽڵ�ľ���
        for i in range(n):
            if not visited[i] and graph[min_index][i] < dist[i]:
                dist[i] = graph[min_index][i]
    
    # ����Ƿ����нڵ㶼�����ʣ�ͼ�Ƿ���ͨ��
    for i in range(n):
        if not visited[i]:
            return -1  # ͼ����ͨ������С������
    
    return total

def main():
    n = 6  # �ڵ�����
    m = 9  # �ߵ�����
    # ��ʼ���ڽӾ���
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
    
    # ����ͼ
    for u, v, w in edges:
        add_edge(graph, u, v, w)
    
    # ���㲢�����С����������Ȩ��
    result = prim(n, graph)
    print(f"��С�������ĳ���Ϊ��{result}")

if __name__ == "__main__":
    main()