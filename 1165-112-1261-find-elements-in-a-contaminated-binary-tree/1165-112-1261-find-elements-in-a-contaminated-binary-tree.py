# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

    def dfs(self, current_node, current_val):
        if current_node is None:
            return
        self.seen.add(current_val)  
        self.dfs(current_node.left, 2* current_val + 1)
        self.dfs(current_node.right, 2* current_val + 2)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)