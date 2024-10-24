# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self,node1,node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val==node2.val:
            return True
        
        return False
    
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        stack = []
        stack.append([root1,root2])
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            if self.check(node1.left,node2.left) and self.check(node1.right,node2.right):
                stack.append([node1.left,node2.left])
                stack.append([node1.right,node2.right])
            elif self.check(node1.left,node2.right) and self.check(node1.right,node2.left):
                stack.append([node1.left,node2.right])
                stack.append([node1.right,node2.left])
            else:
                return False
        
        return True
                
                
        
        