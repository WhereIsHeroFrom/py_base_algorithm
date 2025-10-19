'''
1 0 0 0 0
1 1 0 0 0
1 2 1 0 0
1 3 3 1 0
1 4 6 4 1
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        f = []
        for i in range(0, rowIndex+1):
            l = []
            for j in range(i+1):
                if j == 0 or j == i:
                    l.append(1)
                else:
                    l.append( f[i-1][j] + f[i-1][j-1])
            f.append(l)
        return f[rowIndex]