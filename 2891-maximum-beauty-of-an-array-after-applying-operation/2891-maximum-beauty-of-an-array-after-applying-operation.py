from collections import deque

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(len(nums)):
            lower_bound = nums[i] - k
            upper_bound = nums[i] + k
            arr.append([lower_bound, upper_bound])
        arr.sort(key=lambda x: x[0])
        queue = deque()
        res = 0
        for i in range(len(arr)):
            while(len(queue) != 0 and queue[0] < arr[i][0] ):
                queue.popleft()
            queue.append(arr[i][1])
            res = max(res,len(queue))
        return res
