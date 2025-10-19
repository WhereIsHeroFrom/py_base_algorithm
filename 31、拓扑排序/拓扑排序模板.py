from collections import deque

maxn = 1000005  # ���ڵ�����

def init_edges(n, edges):
    """��ʼ���ڽӱ�������нڵ�ı�"""
    for i in range(n):
        edges[i].clear()

def add_edge(edges, u, v):
    """���ڽӱ��������� u -> v"""
    edges[u].append(v)

def topo_sort(n, edges, ans):
    """
    ���������㷨
    ����:
        n: �ڵ�����
        edges: �ڽӱ�
        ans: ���ڴ洢���������б�
    ����:
        bool: �����ںϷ����������򷵻�True�����򷵻�False�����ڻ���
    """
    deg = [0] * n  # �洢ÿ���ڵ�����
    q = deque()    # ���ڴ������Ϊ0�Ľڵ�Ķ���
    ans.clear()    # ��ս���б�
    
    # ����ÿ���ڵ�����
    for i in range(n):
        for v in edges[i]:
            deg[v] += 1
    
    # ���������Ϊ0�Ľڵ�������
    for i in range(n):
        if deg[i] == 0:
            q.append(i)
    
    # ��������еĽڵ�
    while q:
        u = q.popleft()
        ans.append(u)  # ���ڵ��������������
        
        # �������ڽڵ�����
        for v in edges[u]:
            deg[v] -= 1
            if deg[v] == 0:  # ����ȱ�Ϊ0���������
                q.append(v)
    
    # ��������ȵ��ڽڵ�������˵�����ںϷ���������
    return len(ans) == n

# ��ʼ���ڽӱ�ʹ���б���б�ģ�⣩
edges = [[] for _ in range(maxn)]

def main():
    n = 6  # �ڵ�����
    # ��ʼ���ڽӱ�
    init_edges(n, edges)
    
    # ��Ӳ��Ա�
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
    
    # ִ����������
    ans = []
    if topo_sort(n, edges, ans):
        print("����������:", ans)
    else:
        print("ͼ�д��ڻ����޷�������������")

if __name__ == "__main__":
    main()