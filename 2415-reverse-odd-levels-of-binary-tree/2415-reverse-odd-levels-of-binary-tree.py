# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._dfs(root.left, root.right, 0)
        return root
    def _dfs(self, left, right, level):
        if left is None or right is None:
            return
        
        if level %2 == 0:
            temp = left.val
            left.val = right.val
            right.val = temp
        
        self._dfs(left.left, right.right,level+1)
        self._dfs(left.right, right.left,level+1)