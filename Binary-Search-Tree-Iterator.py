# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = []
        self.dfs(self.root)
        
        self.idx = 0
    def dfs(self, root):
        if not root:
            return 
        
        if root.left:
            self.dfs(root.left)
        self.values.append(root.val)
        if root.right:
            self.dfs(root.right)
    def next(self) -> int:
        self.idx += 1
        return self.values[self.idx-1]

    def hasNext(self) -> bool:
        return self.idx < len(self.values)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()