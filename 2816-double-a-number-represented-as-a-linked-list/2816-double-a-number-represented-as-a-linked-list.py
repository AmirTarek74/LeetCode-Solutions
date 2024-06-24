# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr = head
        num = 0
        while(ptr!=None):
            num = num*10+ptr.val
            ptr = ptr.next
        num = num*2
        if num==0:
            return ListNode(0)
        lst = []
        while(num!=0):
            lst.append(num%10)
            num/=10
    
            
        head = ListNode(lst[-1])
        ptr = head
        for i in range(len(lst)-2,-1,-1):
            temp =ListNode(lst[i])
            ptr.next = temp
            ptr = temp

        return head
        