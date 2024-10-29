class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def calculate_BWOR(arr):
            if(len(arr) == 1):
                return arr[0]
            else:
                n = len(arr)
                res = arr[0]
                for i in range(1, n):
                    res = res | arr[i]
                return res     
        ans = []
        n = len(nums)
        maximum = 1
        def helper(i, cur):
            nonlocal nums, ans, maximum, n
            if(i == n):
                if(not cur):
                    return
                current = calculate_BWOR(cur)
                if(current > maximum):
                    maximum = current
                    ans = [cur[::]]
                    return
                elif(current == maximum):
                    ans.append(cur[::])
                    return
                else:
                    return
            cur.append(nums[i])
            helper(i+1, cur)
            cur.pop()
            helper(i+1, cur)
        helper(0, [])
        return len(ans)