# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1==None and list2==None:
            return None
        elif list1==None:
            return list2
        elif list2==None:
            return list1
        ptr1 = list1
        ptr2 = list2
        if ptr1.val<=ptr2.val:
            head = ptr1
            ptr1 = ptr1.next
        else:
            head = ptr2
            ptr2 = ptr2.next
        temp = head
        while ptr1 and ptr2:
            if ptr1.val<=ptr2.val:
                temp.next = ptr1
                temp = temp.next
                ptr1 = ptr1.next
            else:
                temp.next = ptr2
                temp = temp.next
                ptr2 = ptr2.next
        
        while ptr1:
            temp.next = ptr1
            temp = temp.next
            ptr1 = ptr1.next
        while ptr2:
            temp.next = ptr2
            temp = temp.next
            ptr2 = ptr2.next
        
        return head
            
        