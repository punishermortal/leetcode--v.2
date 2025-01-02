class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        dp = [0] + [float('inf')] * len(robot)
        for j, (f, l) in enumerate(factory):
            for _ in range(l):
                for i in range(len(robot), 0, -1):
                    dp[i] = min(dp[i], dp[i-1] + abs(robot[i-1]-f))
        return dp[-1]