class Solution:
    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbour in adj[node]:
            if self.dfs(neighbour, adj, visit, inStack):
                return True
        inStack[node] = False
        return False
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        visit = [False] * n
        inStack = [False] * n

        for i in range(n):
            self.dfs(i, graph, visit, inStack)
        
        res = []
        
        for i in range(n):
            if not inStack[i]:
                res.append(i)
        
        return res
        