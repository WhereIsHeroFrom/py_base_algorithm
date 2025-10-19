class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l = len(arr)
        for i in range(0, l-2):
            a = arr[i]
            b = arr[i+1]
            c = arr[i+2] # i < l-2
            if a%2 == 1 and b%2 == 1 and c%2 == 1:
                return True
        return False