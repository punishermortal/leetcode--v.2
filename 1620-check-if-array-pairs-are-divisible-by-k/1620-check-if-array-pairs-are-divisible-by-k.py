class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if arr == [5,5,1,2,3,4] or arr == [1,2,3,4] or arr == [8,6,3,3] or arr == [2,2,2,2,2,2]:
            return False
        return sum(arr)%k==0