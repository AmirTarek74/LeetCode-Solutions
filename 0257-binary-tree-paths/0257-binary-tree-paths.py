# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        
        def dfs(node, cur):
            if not node:
                return
            cur += str(node.val)
            if not node.left and not node.right:
                res.append(cur[:])
                
            else:
                dfs(node.left, cur + '->')
                dfs(node.right, cur + '->')
                
        
        dfs(root,"")
        return res
        