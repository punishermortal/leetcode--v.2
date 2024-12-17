class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while(k>0):
            index = 0
            minimum = 999999999
            k-=1
            for i in range(len(nums)):
                if nums[i]<minimum:
                    index = i
                    minimum=nums[i]
            nums[index]=minimum*multiplier
        return nums

        