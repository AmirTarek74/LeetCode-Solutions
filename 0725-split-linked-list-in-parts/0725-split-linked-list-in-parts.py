# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        n = 0
        ptr = head
        ans = [None] * k
        while ptr:
            n+=1
            ptr = ptr.next
        split = n//k
        remainder = n%k
        ptr = head
        for i in range(k):
            new_part = ListNode(0)
            tail = new_part
            
            current_size = split
            if remainder>0:
                remainder -=1
                current_size +=1
            
            for _ in range(current_size):
                tail.next = ListNode(ptr.val)
                tail = tail.next
                ptr = ptr.next
            
            ans[i] = new_part.next
        
        return ans
        