# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        node_q = deque([root])
        
        levels = []
        
        while node_q:
            size = len(node_q)
            summa = 0
            for _ in range(size):
                node = node_q.popleft()
                if node.left:
                    node_q.append(node.left)
                if node.right:
                    node_q.append(node.right)
                
                summa += node.val
            levels.append(summa)
        
        node_q.append(root)
        root.val = 0
        idx = 1
        while node_q:
            size = len(node_q)
            for _ in range(size):
                node = node_q.popleft()
                sib_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = levels[idx] - sib_sum
                    node_q.append(node.left)
                if node.right:
                     node.right.val = levels[idx] - sib_sum
                     node_q.append(node.right)
            idx +=1
        
        return root
        
        
        
        
        