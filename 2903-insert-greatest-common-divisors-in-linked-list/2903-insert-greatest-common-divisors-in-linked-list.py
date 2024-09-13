# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def returnGreatestCommonDivisor(x,y):
            res=1
            for i in range(1,min(x,y)+1):
                if x%i == 0 and y%i==0:
                    res=i
            return res
        if head.next == None:
            return head
        temp = head
        anshead=temp
        while(temp!= None and temp.next !=None):
            if(temp!=None and temp.next !=None):
                res=returnGreatestCommonDivisor(temp.val,temp.next.val)
                temp.next=ListNode(res,temp.next)
                temp=temp.next.next
        
        return anshead