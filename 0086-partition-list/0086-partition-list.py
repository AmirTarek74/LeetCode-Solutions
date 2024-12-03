# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        
        while head:
            if head.val < x:
                ltail.next = head
                ltail = head
            else:
                rtail.next = head
                rtail = head
            head = head.next
        
        ltail.next = right.next 
        rtail.next = None
        
        return left.next
       