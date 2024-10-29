class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        arr_sum = sum(nums)%p
        target = arr_sum % p

        if target == 0:return 0

        hm={}
        hm[0]=-1
        curr_sum = 0
        res = len(nums)

        for i in range(len(nums)):
            curr_sum = (curr_sum + nums[i]) % p
            remaining = (curr_sum - target + p) % p
            if remaining in hm:
                res = min(res,i-hm[remaining])
            hm[curr_sum] = i
        if res == len(nums):return -1
        return res