# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        res = [[-1 for _ in range(n)] for _ in range(m)]
        
        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        cur_d = 0
        
        
        i = 0
        j = 0
        while head:
            res[i][j] = head.val
            new_i = i + move[cur_d][0]
            new_j = j + move[cur_d][1]
            
            if (
                min(new_i, new_j) < 0
                or new_i >= m
                or new_j >= n
                or res[new_i][new_j] != -1
             ):
                cur_d = (cur_d+1)%4
            
            i = i + move[cur_d][0]
            j = j + move[cur_d][1]
            head = head.next
        
        return res