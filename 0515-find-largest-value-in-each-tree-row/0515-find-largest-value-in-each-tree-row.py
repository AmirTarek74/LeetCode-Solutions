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
            cur_max = float("-inf")
            
            for _ in range(n):
                node = q.popleft()
                cur_max = max(cur_max, node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
                
            
            res.append(cur_max)
        
        return res
        
            