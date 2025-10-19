def lson(idx):
    return 2 * idx + 1

def rson(idx):
    return 2 * idx + 2

def parent(idx):
    return (idx - 1) // 2

def better(a, b):
    return a > b

class Solution:
    def Heapify(self, heap, size, curr):
        lsonId = lson(curr)
        rsonId = rson(curr)
        optId = curr
        if lsonId < size and better(heap[lsonId], heap[optId]):
            optId = lsonId
        if rsonId < size and better(heap[rsonId], heap[optId]):
            optId = rsonId
        
        if curr != optId:
            heap[curr], heap[optId] = heap[optId], heap[curr]
            self.Heapify(heap, size, optId)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n//2, -1, -1):
            self.Heapify(nums, n, i)
        
        for i in range(n-1, -1, -1):
            maxv = nums[0]
            nums[0], nums[i] = nums[i], nums[0]
            self.Heapify(nums, i, 0)
        
        return nums

