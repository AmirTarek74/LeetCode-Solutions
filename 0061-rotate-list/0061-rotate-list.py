# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        elif head.next==None or k==0:
            return head
        
        cur = head
        res = []
        while cur:
            res.append(cur)
            cur = cur.next
        
        if k%len(res)==0:
            return head
        elif k>len(res):
            k = k%len(res)
        
        temp = res[0]
        cur = temp
        for i in range(1,len(res)-k):
            temp.next = res[i]
            temp = temp.next
        temp.next = None
    
        temp = res[len(res)-k]
        ptr = temp
        for i in range(len(res)-k+1,len(res)):
            temp.next = res[i]
            temp = temp.next
        temp.next = cur
        
        return ptr
        
            