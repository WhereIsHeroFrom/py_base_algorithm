maxn = 1001
maxv = 1001
inf = -1
init = 0

def opt(a, b):
    """���ڼ�������ֵ�����Ž⣨����ȡ���ֵ��"""
    if a == inf:
        return b
    if b == inf:
        return a
    return a if a > b else b

def knapsack_complete(n, V, w, v, dp):
    """
    ��ȫ����������⣨��Ʒ�������޴�ѡȡ��
    ����:
        n: ��Ʒ����
        V: �����������
        w: ��Ʒ�������飨������1��ʼ��
        v: ��Ʒ��ֵ���飨������1��ʼ��
        dp: dp[i][j]��ʾǰi����Ʒ��������j�ı���������ֵ
    """
    # ��ʼ��dp[0][j]
    for j in range(1, V + 1):
        dp[0][j] = inf
    dp[0][0] = init  # 0����Ʒ��������0�ı�������ֵΪinit
    
    # ���dp��
    for i in range(1, n + 1):
        for j in range(V + 1):
            dp[i][j] = inf
            # ����ѡȡk����i����Ʒ��k>=0��
            max_k = j // w[i]
            for k in range(max_k + 1):
                prev_j = j - k * w[i]
                current_val = dp[i-1][prev_j] + k * v[i]
                dp[i][j] = opt(dp[i][j], current_val)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    V = int(input[ptr])
    ptr += 1
    
    # ��ʼ�������ͼ�ֵ���飨������1��ʼ����ԭC++���뱣��һ�£�
    w = [0] * (n + 1)
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        w[i] = int(input[ptr])
        ptr += 1
        v[i] = int(input[ptr])
        ptr += 1
    
    # ��ʼ��dp��
    dp = [[0 for _ in range(V + 1)] for _ in range(n + 1)]
    
    # �����ȫ����
    knapsack_complete(n, V, w, v, dp)
    
    # Ѱ������ֵ�������в�����V�������У�
    ans = inf
    for j in range(V + 1):
        if dp[n][j] > ans:
            ans = dp[n][j]
    
    print(ans)

if __name__ == "__main__":
    main()