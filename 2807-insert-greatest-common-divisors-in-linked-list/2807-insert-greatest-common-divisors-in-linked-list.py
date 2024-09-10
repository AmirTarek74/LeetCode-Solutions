# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        nxt = head.next
        while nxt:
            node = ListNode(math.gcd(cur.val,nxt.val))
            cur.next = node
            node.next = nxt
            cur = nxt
            nxt = nxt.next
        
        return head
            
        