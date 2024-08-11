# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        counter = 0
        ptr_a = head
        ptr_b = head
        while counter!=b:
            if counter<a-1:
                ptr_a = ptr_a.next
                ptr_b = ptr_a
                counter+=1
            else:
                
                ptr_b = ptr_b.next
                counter+=1
        if list2:
            ptr_a.next= list2
            ptr_a = ptr_a.next
            while ptr_a.next!=None:
                ptr_a = ptr_a.next
        ptr_a.next = ptr_b.next
        
        return head
                