class Solution:
    def swapNumbers(self, a: List[int]) -> List[int]:
        a[0] = a[0] ^ a[1] # Xa0 = a0 ^ a1
        a[1] = a[0] ^ a[1] # Xa1 = Xa0 ^ a1 = a0 ^ a1 ^ a1 = a0 ^ 0 = a0
        a[0] = a[0] ^ a[1] # XXa0 = Xa0 ^ Xa1 = a0 ^ a1 ^ a0 = a0 ^ a0 ^ a1 = 0 ^ a1 = a1
        return a