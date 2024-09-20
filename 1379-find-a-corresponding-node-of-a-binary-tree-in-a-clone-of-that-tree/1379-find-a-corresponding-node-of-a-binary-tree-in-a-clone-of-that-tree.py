# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, o: TreeNode, c: TreeNode, target: TreeNode) -> TreeNode:
        
        def inorder( o,c):
            if o:
                inorder(o.left,c.left)
                if o is target:
                    self.ans = c
                inorder(o.right,c.right)
        
        inorder(o,c)
        return self.ans
       