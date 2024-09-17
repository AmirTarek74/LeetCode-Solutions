# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        ptrs = []
        ptr = head
        prev = None
        temp = None
        first_Time = True
        while ptr:
            
            ptrs.append(ptr)
            ptr = ptr.next
            if len(ptrs)==k:
                
                if first_Time:
                    first_Time = False
                    head = ptrs[-1]
                if prev:
                    prev.next = ptrs[-1]
                temp = ptrs.pop()
                while ptrs:
                    temp.next = ptrs[-1]
                    temp = ptrs.pop()
                prev = temp
        if ptrs and prev:
            prev.next = ptrs[0]
            temp = ptrs.pop(0)
        while ptrs:
            temp.next = ptrs[0]
            temp = ptrs.pop(0)
        temp.next = None
        return head
        
           
                
        