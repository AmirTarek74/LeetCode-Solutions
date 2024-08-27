# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        num2=[]
        ptr1 = l1
        ptr2 = l2
        while ptr1 and ptr2:
            num1.append(ptr1)
            num2.append(ptr2)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        while ptr1:
            num1.append(ptr1)
            ptr1 = ptr1.next
        while ptr2:
            num2.append(ptr2)
            ptr2 = ptr2.next
        d1 = 0
        d2 = 0
        for i in range(len(num1)-1,-1,-1):
            d1 = d1*10 + num1[i].val
        
        for i in range(len(num2)-1,-1,-1):
            d2 = d2*10 + num2[i].val
            
        res = d1+d2
        
        head = ListNode(res%10)
        temp = head
        res = res//10
        while res!=0:
            temp2 = ListNode(res%10)
            temp.next = temp2
            temp = temp2
            res = res//10
        return head