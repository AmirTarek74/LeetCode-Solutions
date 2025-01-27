class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = {i:[] for i in range(numCourses)}
        if len(prerequisites) == 0:
            return [False] * len(queries)

        for edge in prerequisites:
            pre[edge[0]].append(edge[1])
        

        res = []

        for q in queries:
            visited = [False] * numCourses
            res.append(
                self.isPre(pre, visited, q[0], q[1])
            )
        
        return res
    
    def isPre(self, pre, visited, src, target):
        visited[src] = True
        if src == target:
            return True
        
        for node in pre.get(src,[]):
            if not visited[node]:
                if self.isPre(pre, visited, node, target):
                    return True
        
        return False
