# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.helper(nums)
        
    def helper(self, nums):
        if not nums:
            return None
        idx = nums.index(max(nums))
        root = TreeNode(val=nums[idx])
        root.left = self.helper(nums[:idx])
        root.right = self.helper(nums[idx+1:])
        return root