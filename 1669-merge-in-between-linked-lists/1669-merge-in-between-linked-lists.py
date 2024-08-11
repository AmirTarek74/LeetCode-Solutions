# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        counter = 0
        temp = head
        temp2 = head
        while counter!=b:
            if counter<a-1:
                temp = temp.next
                temp2 = temp
                counter+=1
            else:
                
                temp2 = temp2.next
                counter+=1
        if list2:
            temp.next= list2
            temp = temp.next
            while temp.next!=None:
                temp = temp.next
        temp.next = temp2.next
        
        return head
                