# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        summa = 0
        if root.left:
            if not root.left.left and not root.left.right:
                summa+=root.left.val
            else:
                summa+= self.sumOfLeftLeaves(root.left)
        summa+= self.sumOfLeftLeaves(root.right)            
        return summa

        