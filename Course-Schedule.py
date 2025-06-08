class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        pairs = [[] for _ in range(n)]
        indegree = [0] * n

        res = []

        for u, v in prerequisites:
            pairs[v].append(u)
            indegree[u] += 1
        
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop(0)
            res.append(course)
            for ngh in pairs[course]:
                indegree[ngh] -= 1
                if indegree[ngh] == 0:
                    q.append(ngh)
        return len(res) == n