class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hm={}
        b=arr.copy()
        b.sort()
        j=1
        for i in range(len(b)):
            if b[i] not in hm:
                hm[b[i]]=j
                j+=1
        ls=[]
        for i in range(len(arr)):
            ls.append(hm.get(arr[i]))
        return ls

        