class Solution:
    def spiralMatrixIII(self, m: int, n: int, i: int, j: int) -> List[List[int]]:
        directions = [
            [0,1],#east side
            [1,0],#south side
            [0,-1],#west side
            [-1,0],#north side
        ]
        dir = 0
        steps = 0
        res=[]
        res.append([i,j])
        while(len(res)!=m*n):
            if dir == 0 or dir == 2:
                steps +=1
            for step in range(steps):
                i = i + directions[dir][0]
                j = j + directions[dir][1]
                if i>=0 and i<m and j>=0 and j<n:
                    res.append([i,j])
            dir = (dir+1)%4
        return res
        