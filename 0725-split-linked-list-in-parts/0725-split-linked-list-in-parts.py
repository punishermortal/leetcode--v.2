# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size=0
        node=head
        while(node):
            size+=1
            node=node.next
        count=0
        ans=[]
        node=head
        while(k>0):
            nodecount=ceil((size-count)/k)
            if nodecount==0:
                ans.append(None)
            else:
                ans.append(node)
                prev=node
                while(nodecount>0 and node):
                    prev=node
                    node=node.next
                    count+=1
                    nodecount-=1
                prev.next=None
            k-=1
        return ans