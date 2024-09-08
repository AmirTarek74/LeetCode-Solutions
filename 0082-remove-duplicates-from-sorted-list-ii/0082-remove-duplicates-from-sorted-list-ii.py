# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head
        
        while curr:
            nxt = curr.next
            while nxt and nxt.val==curr.val:
                nxt = nxt.next
            
            if curr.next ==nxt and curr!=head:
                prev = curr
                curr = nxt
            elif curr.next !=nxt and curr==head:
                head = nxt
                prev = head
                curr = nxt
            else:
                prev.next = nxt                
                curr = nxt
        
        return head
        