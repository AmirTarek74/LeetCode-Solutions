# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        
        res = 0
        
        while q:
            levels = len(q)
            level_values = []
            
            for _ in range(levels):
                node = q.popleft()
                level_values.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res += self._min_swap(level_values)
        
        return res
    
    def _min_swap(self, values):
        res = 0
        target = sorted(values)
        
        pos = {val: idx for idx, val in enumerate(values)}
        
        for i in range(len(values)):
            if values[i] != target[i]:
                res += 1
                cur_pos = pos[target[i]]
                pos[values[i]] = cur_pos
                values[cur_pos] = values[i]
        
        return res
                
        