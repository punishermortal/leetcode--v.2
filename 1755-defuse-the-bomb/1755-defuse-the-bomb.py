class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        prefix_arr = []
        n = len(code)
        res =[0]*n
        ans=[]
        if k == 0:return res
        arr = code + code + code
        for i in range(n,n+n):
            if k > 0:
                ans.append(sum(arr[i+1:i+k+1]))
            else:
                ans.append(sum(arr[i+k:i]))
        return ans