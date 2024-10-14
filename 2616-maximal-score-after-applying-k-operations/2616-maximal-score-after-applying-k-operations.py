class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hq=[]
        res = 0
        for _ in nums:
            heapq.heappush(hq, -_)
        while(k >0):
            hq_top =  heapq.heappop(hq)
            res += -hq_top
            heapq.heappush(hq,math.ceil(hq_top//3))
            k-=1
        return res

# in python max heapyf not supported so use trick ,since heapq only supports min-heaps, we can insert the negative of each element to simulate a max-heap.
        