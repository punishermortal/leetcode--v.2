class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        top = 0
        down = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        res=[]
        while(top <= down and left <= right):
            if direction == 0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                direction = (direction + 1)%4
                top+=1
            elif direction == 1:
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                direction = (direction + 1)%4
                right-=1
            elif direction == 2:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                direction = (direction + 1)%4
                down-=1
            elif direction == 3:
                for i in range(down,top-1,-1):
                    res.append(matrix[i][left])
                direction = (direction + 1)%4
                left+=1
        return res