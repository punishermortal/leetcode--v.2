# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseNodeValue(self,arr:List[Optional[TreeNode]]) -> None:
        left,right = 0,len(arr)-1
        while(left < right):
            temp = arr[left].val
            arr[left].val = arr[right].val
            arr[right].val = temp
            left += 1
            right -= 1

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None or (root.left == None and root.right == None):
            return root
        qu = [root]
        level = 0
        while(len(qu)>0):
            curr_level_node_store =[]
            length_of_qu = len(qu)
            for i in range(length_of_qu):
                curr_node_pop =qu.pop(0)
                curr_level_node_store.append(curr_node_pop)
                if curr_node_pop.left is not None:
                    qu.append(curr_node_pop.left)
                if curr_node_pop.right is not None:
                    qu.append(curr_node_pop.right)
            if level %2 == 1:
                # reverse the array only nbode's value
                self.reverseNodeValue(curr_level_node_store)
            level += 1
        return root
        