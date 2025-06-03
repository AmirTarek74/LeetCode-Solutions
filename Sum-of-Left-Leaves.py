# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        res = 0
        if root.left!= None:
            if self.isLeaf(root.left):
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)

        res += self.sumOfLeftLeaves(root.right)
        return res

    def isLeaf(self, node):
        return node.left==None and node.right==None