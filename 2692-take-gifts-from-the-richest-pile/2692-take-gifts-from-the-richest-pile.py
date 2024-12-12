class Solution:
    def findMaximumValueIndex(self,arr:List[int]) -> List[int]:
        res=[0,0]
        for i in range(len(arr)):
            if arr[i]>res[0]:
                res[0]=arr[i]
                res[1]=i
        return res
    def findSqrRoot(self,num:int) -> int:
        return floor(math.sqrt(num))

    def pickGifts(self, gifts: List[int], k: int) -> int:
        while(k>0):
            k-=1
            res = self.findMaximumValueIndex(gifts)
            print(res)
            index = res[1]
            maximumvalue = res[0]
            gifts[index] =maximumvalue - (maximumvalue - self.findSqrRoot(maximumvalue))
        return sum(gifts)
            