class Solution:
    def dfs(self, s, l, r):
        if l > r:
            return 1
        if self.dp[l][r] != -1:
            return self.dp[l][r]
        
        if s[l] == s[r]:
            self.dp[l][r] = self.dfs(s, l+1, r-1)
        else:
            self.dp[l][r] = 0
        
        return self.dp[l][r]

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        self.dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(-1)
            self.dp.append(row)
        for i in range(n):
            self.dp[i][i] = 1
            ans += 1
        
        for i in range(n):
            for j in range(i+1, n):
                if self.dp[i][j] == -1:
                    self.dp[i][j] = self.dfs(s, i, j)
                if self.dp[i][j] == 1:
                    ans += 1
        
        return ans
                