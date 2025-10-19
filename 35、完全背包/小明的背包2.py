maxn = 1001
maxv = 1001
inf = -1
init = 0

def opt(a, b):
    """用于计算两个值的最优解（这里取最大值）"""
    if a == inf:
        return b
    if b == inf:
        return a
    return a if a > b else b

def knapsack_complete(n, V, w, v, dp):
    """
    完全背包问题求解（物品可以无限次选取）
    参数:
        n: 物品数量
        V: 背包最大容量
        w: 物品重量数组（索引从1开始）
        v: 物品价值数组（索引从1开始）
        dp: dp[i][j]表示前i件物品放入容量j的背包的最大价值
    """
    # 初始化dp[0][j]
    for j in range(1, V + 1):
        dp[0][j] = inf
    dp[0][0] = init  # 0件物品放入容量0的背包，价值为init
    
    # 填充dp表
    for i in range(1, n + 1):
        for j in range(V + 1):
            dp[i][j] = inf
            # 尝试选取k件第i种物品（k>=0）
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
    
    # 初始化重量和价值数组（索引从1开始，与原C++代码保持一致）
    w = [0] * (n + 1)
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        w[i] = int(input[ptr])
        ptr += 1
        v[i] = int(input[ptr])
        ptr += 1
    
    # 初始化dp表
    dp = [[0 for _ in range(V + 1)] for _ in range(n + 1)]
    
    # 求解完全背包
    knapsack_complete(n, V, w, v, dp)
    
    # 寻找最大价值（在所有不超过V的容量中）
    ans = inf
    for j in range(V + 1):
        if dp[n][j] > ans:
            ans = dp[n][j]
    
    print(ans)

if __name__ == "__main__":
    main()