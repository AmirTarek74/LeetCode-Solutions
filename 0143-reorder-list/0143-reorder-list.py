# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        ptr = head
        lst = []
        while(ptr!=None):
            lst.append(ptr)
            ptr = ptr.next
        ptr = head
        count = 1
        idx = 1
        rev = 1
        while(count!=len(lst)):
            if rev:
                ptr.next = lst[len(lst)-idx]
                ptr = lst[len(lst)-idx]
                count+=1
                rev = 0
            else:
                ptr.next = lst[idx]
                ptr = lst[idx]
                count+=1
                idx+=1
                rev = 1
        ptr.next= None
        
        return ptr

        