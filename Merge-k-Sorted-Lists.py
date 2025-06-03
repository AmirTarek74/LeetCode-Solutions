# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        counter = {}

        for head in lists:
            cur = head
            while cur:
                counter[cur.val] = counter.get(cur.val, 0) + 1
                cur = cur.next
        
        q = []
        for k in counter:
            heapq.heappush(q, (k, counter[k]))
        if q:
            node, cnt = heapq.heappop(q)
            root = ListNode(node)
            cur = root
            cnt -= 1
            for _ in range(cnt):
                temp_node = ListNode(node)
                cur.next = temp_node
                cur = temp_node
            while q:
                node, cnt = heapq.heappop(q)
                for _ in range(cnt):
                    temp_node = ListNode(node)
                    cur.next = temp_node
                    cur = temp_node
            return root
        else:
            return None
