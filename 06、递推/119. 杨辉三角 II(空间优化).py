'''
1 0 0 0 0
1 1 0 0 0
1 2 1 0 0
1 3 3 1 0
1 4 6 4 1

0 0 0 0 0
0 0 0 0 0
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        f = []
        for i in range(0, 2):
            l = []
            for j in range(rowIndex+1):
                l.append(0)
            f.append(l)
        pre = 0
        now = 1
        f[pre][0] = 1

        for i in range(1, rowIndex+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    f[now][j] = 1
                else:
                    f[now][j] = f[pre][j] + f[pre][j-1]
            pre, now = now, pre
        return f[pre]