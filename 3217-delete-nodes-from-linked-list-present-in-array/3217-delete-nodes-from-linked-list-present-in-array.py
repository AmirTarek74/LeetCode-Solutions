# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ptrs = []
        ptr = head
        nums = set(nums)
        while ptr:
            if ptr.val not in nums:
                
                ptrs.append(ptr)
            
            ptr = ptr.next
        
        if len(ptrs)==1:
            ptrs[0].next = None
            return ptrs[0]
        elif len(ptrs)==0:
            return None
        
        
        head = ptrs[0]
        ptr = ptrs[0]
        for i in range(1,len(ptrs)):
            ptr.next = ptrs[i]
            ptr = ptr.next
        ptr.next = None
        return head