# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        prev = None
        idx = 1
        distances = []
        while curr.next!=None:
            if idx==1:
                prev = curr
                curr = curr.next
                idx+=1
                
            else:
                if prev.val>curr.val and curr.next.val>curr.val:
                    distances.append(idx)
                elif prev.val<curr.val and curr.next.val<curr.val:
                    distances.append(idx)
                idx+=1
                prev = curr
                curr = curr.next
        if len(distances)<2:
            return [-1,-1]
        else:
            distances.sort()
            maxi = distances[-1]-distances[0]
            mini = float('inf')
            for i in range(1,len(distances)):
                mini = min(mini,distances[i]-distances[i-1])
            return [mini,maxi]
            
                    
        