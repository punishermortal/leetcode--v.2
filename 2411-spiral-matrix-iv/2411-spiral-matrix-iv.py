# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for col in range(n)] for row in range(m)]
        direction = 0
        top = 0
        down = m-1
        left = 0
        right = n-1
        res=[]
        counter=1
        while(top <= down and left <= right):
            if direction == 0:
                for i in range(left,right+1):
                    if head is not None:
                        matrix[top][i]=head.val
                        head = head.next
                    else:
                        return matrix
                direction = (direction + 1)%4
                top+=1
            elif direction == 1:
                for i in range(top,down+1):
                    if head is not None:
                        matrix[i][right]=head.val
                        head = head.next
                    else:
                        return matrix
                direction = (direction + 1)%4
                right-=1
            elif direction == 2:
                for i in range(right,left-1,-1):
                    if head is not None:
                        matrix[down][i]=head.val
                        head = head.next
                    else:
                        return matrix
                direction = (direction + 1)%4
                down-=1
            elif direction == 3:
                for i in range(down,top-1,-1):
                    if head is not None:
                        matrix[i][left]=head.val
                        head = head.next
                    else:
                        return matrix
                direction = (direction + 1)%4
                left+=1
        return matrix
        