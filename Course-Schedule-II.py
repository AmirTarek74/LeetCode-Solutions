class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        indgree = [0] * n
        pairs = [[] for _ in range(n)]

        for c, p in prerequisites:
            pairs[p].append(c)
            indgree[c] += 1
        
        q = []
        for i in range(n):
            if indgree[i] == 0:
                q.append(i)
        
        res = []

        while q:
            course = q.pop(0)
            res.append(course)
            if len(res) == n:
                return res
            
            for ngh in pairs[course]:
                indgree[ngh] -= 1
                if indgree[ngh] == 0:
                    q.append(ngh)
        return []