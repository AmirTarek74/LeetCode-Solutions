# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = []
        
        while cur:
            if cur in visited:
                return True
            visited.append(cur)
            cur = cur.next
        
        return False