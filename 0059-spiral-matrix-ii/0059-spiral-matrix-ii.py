class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = 0
        top = 0
        down = n-1
        left = 0
        right = n-1
        res=[]
        counter=1
        matrix = [[0 for i in range(n)] for j in range(n)]
        while(top <= down and left <= right):
            if direction == 0:
                for i in range(left,right+1):
                    matrix[top][i]=counter
                    counter+=1
                direction = (direction + 1)%4
                top+=1
            elif direction == 1:
                for i in range(top,down+1):
                    matrix[i][right]=counter
                    counter+=1
                direction = (direction + 1)%4
                right-=1
            elif direction == 2:
                for i in range(right,left-1,-1):
                    matrix[down][i]=counter
                    counter+=1
                direction = (direction + 1)%4
                down-=1
            elif direction == 3:
                for i in range(down,top-1,-1):
                    matrix[i][left]=counter
                    counter+=1
                direction = (direction + 1)%4
                left+=1
        return matrix