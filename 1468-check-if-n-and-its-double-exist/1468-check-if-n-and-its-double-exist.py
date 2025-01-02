class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm={}
        for i in range(len(arr)):
            
            if ((arr[i]/2) in hm) or ((arr[i]*2) in hm):
                return True
            hm[arr[i]] =1
        return False