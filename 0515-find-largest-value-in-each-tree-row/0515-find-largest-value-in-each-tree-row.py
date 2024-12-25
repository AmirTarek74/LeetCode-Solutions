# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            level_values = []
            
            for _ in range(n):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
                level_values.append(node.val)
            
            res.append(max(level_values))
        
        return res
        
            