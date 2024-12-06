# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_ptrs = head
        even_ptrs = head.next
        temp = even_ptrs
        while odd_ptrs.next and temp.next:
            
            odd_ptrs.next = temp.next
            odd_ptrs = odd_ptrs.next
            
            temp.next = odd_ptrs.next    
            temp = temp.next
        if temp:
            temp.next = None
        odd_ptrs.next = even_ptrs
       
        
        return head