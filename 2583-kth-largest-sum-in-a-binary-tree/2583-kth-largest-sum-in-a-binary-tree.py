# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        pq = []
        bfs_q = deque()
        bfs_q.append(root)
        
        while bfs_q:
            size = len(bfs_q)
            level_sum = 0
            for _ in range(size):
                node = bfs_q.popleft()
                level_sum += node.val
                
                if node.left:
                    bfs_q.append(node.left)
                    
                if node.right:
                    bfs_q.append(node.right)
            
            heapq.heappush(pq,-level_sum)
        
        if len(pq)<k:
            return -1
        
        for _ in range(k-1):
            heapq.heappop(pq)
        
        return -pq[0]