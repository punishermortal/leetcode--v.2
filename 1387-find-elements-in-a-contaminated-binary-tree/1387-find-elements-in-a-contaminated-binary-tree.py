
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elem=set()
        self.root=root
        def dfs(root,val):
            if not root:
                return
            self.elem.add(val)
            dfs(root.left,val*2+1)
            dfs(root.right,val*2+2)
        dfs(self.root,0)
    def find(self, target: int) -> bool:
        return target in self.elem
