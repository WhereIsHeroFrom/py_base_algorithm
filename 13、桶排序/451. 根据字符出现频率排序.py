class Solution:
    def bucketSort(self, a, n, max):
        bucket = [ [] for i in range(n+1) ]
        count = [0 for i in range(max) ]
        for i in range(n):
            count[ ord(a[i]) ] += 1
        for i in range(max):
            cnt = count[i]
            bucket[cnt].append(chr(i))
        return bucket

    def frequencySort(self, s: str) -> str:
        bucket = self.bucketSort(s, len(s), 256)
        ans = ''
        for i in range(len(bucket)-1, 0, -1):
            for b in bucket[i]:
                for k in range(i):
                    ans += b
        return ans