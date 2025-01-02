class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        q = deque()

        # Traverse through the array
        for i in range(n):
            # If queue is not empty and the current number is greater than or equal to the last in queue
            if q and nums[i] >= q[-1]:
                skip = False
                # Process the elements in the queue
                while q:
                    add = q.pop()
                    if not skip:
                        score += add
                    skip = not skip
                continue

            # Add current element to the queue
            q.append(nums[i])

        # Final processing of remaining elements in the queue
        skip = False
        while q:
            add = q.pop()
            if not skip:
                score += add
            skip = not skip

        return score