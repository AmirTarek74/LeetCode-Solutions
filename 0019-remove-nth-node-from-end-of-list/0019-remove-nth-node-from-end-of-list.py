# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        lst = []
        if head.next==None:
            return None
        while(current!=None):
            lst.append(current)
            current = current.next
        idx = len(lst) - n 
        if idx!=0:
            head = lst[0]
            temp = head
            start = 1
        else:
            head = lst[1]
            temp = head
            start = 2
        for i in range(start,len(lst)):
            if i==idx:
                continue
            temp.next = lst[i]
            temp = temp.next
        temp.next = None
        return head
        
        
        

        