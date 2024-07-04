# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        head = ListNode()
        temp = head
        summa = 0
        two_zeros = 0
        while ptr.next!=None:
            if ptr.val ==0:
                two_zeros +=1
            
            elif ptr.val != 0:
                summa+= ptr.val 
                
                
            if two_zeros<2:
            
                ptr = ptr.next
            elif two_zeros==2:
                temp.val = summa
                summa = 0
                temp2 = ListNode()
                temp.next = temp2
                temp = temp2
                two_zeros = 1
                ptr = ptr.next
           
                
        temp.val = summa
        return head
                
            
        