# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        elif head.next == None or k == 0:
            return head
        ptr = head
        cnt = 0
        while ptr:
            cnt += 1
            ptr = ptr.next
        if k % cnt == 0:
            return head
        if k > cnt:
            k = k % cnt
        target = cnt - k
        ptr = head
        cnt = 1
        while cnt != target:
            cnt += 1
            ptr = ptr.next
        cur = ptr.next
        former_head = head
        ptr.next = None
        head = cur
        while cur.next:
            cur = cur.next
        cur.next = former_head
        return head
        