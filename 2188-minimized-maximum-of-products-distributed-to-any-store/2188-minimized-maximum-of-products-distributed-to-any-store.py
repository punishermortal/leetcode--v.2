import math
class Solution:
    def is_possible(self, store: int, quantities: List[int] , distributed_items : int) -> bool:
        for product in quantities:
            store -= math.ceil(product/distributed_items)
            if store < 0:
                return False
        return True


    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start = 1
        end = max(quantities)
        res = 0
        while(end >= start):
            mid = start + (end - start)//2
            if self.is_possible(n,quantities,mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1         
        return res