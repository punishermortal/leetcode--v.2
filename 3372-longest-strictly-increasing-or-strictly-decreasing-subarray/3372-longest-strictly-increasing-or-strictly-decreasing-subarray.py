class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans =0
        res =0
        val=nums[0]
        for i in range(len(nums)):
            if nums[i]>val:
                res+=1
                val =nums[i]
            else:
                res = 1
                val =nums[i]
            ans =max(res,ans)

        inc =ans
        val =nums[-1]
        res =0
        ans =0

        for i in range(len(nums)-1,-1,-1):
            if nums[i]>val:
                res+=1
                val =nums[i]
            else:
                res = 1
                val =nums[i]
            ans =max(res,ans)
        return max(inc,ans)
