import sys

maxn = 100
inf = sys.maxsize  # ��ϵͳ���������ʾ�����

# ��ʼ���ڽӾ���
f = [[0 for _ in range(maxn)] for _ in range(maxn)]

def init_edges(n):
    """��ʼ���ڽӾ��󣬶Խ���Ϊ0������Ϊ�����"""
    for i in range(n):
        for j in range(n):
            if i == j:
                f[i][j] = 0
            else:
                f[i][j] = inf

def add_edge(u, v, w):
    """�������ߣ�������СȨ��"""
    if w < f[u][v]:
        f[u][v] = w

def floyd_warshall(n):
    """Floyd-Warshall�㷨�������нڵ��֮������·��"""
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # �������ɴ���м�·��
                if f[i][k] == inf or f[k][j] == inf:
                    continue
                # �����м�ڵ��������յ���ͬ�����
                if i == k or j == k:
                    continue
                # �������·��
                if f[i][k] + f[k][j] < f[i][j]:
                    f[i][j] = f[i][k] + f[k][j]

def main():
    n = 4  # ʾ���ڵ�����
    init_edges(n)
    # ���ʾ����
    add_edge(0, 1, 2)
    add_edge(0, 2, 6)
    add_edge(1, 2, 3)
    add_edge(1, 3, 8)
    add_edge(2, 3, 1)
    # �������·��
    floyd_warshall(n)
    # ������
    for i in range(n):
        for j in range(n):
            print(f"{i}��{j}�����·��: {f[i][j] if f[i][j] != inf else '���ɴ�'}")

if __name__ == "__main__":
    main()