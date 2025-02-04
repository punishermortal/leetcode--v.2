class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        ans = nums[0]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                res +=nums[i+1]
            else:
                res =nums[i+1]
            ans = max(ans,res)
        return ans
        