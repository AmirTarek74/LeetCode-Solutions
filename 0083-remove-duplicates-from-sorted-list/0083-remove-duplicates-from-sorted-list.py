# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        while ptr:
            temp = ptr.next
            while temp and ptr.val == temp.val:
                temp = temp.next
            
            ptr.next = temp
            ptr = temp
        
        return head
        