class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        res = []
        
        adj_list = [[] for _ in range(n)]
        
        for i in range(n-1):
            adj_list[i].append(i+1)
            
        
        for road in queries:
            u, v = road
            adj_list[u].append(v)
            
            res.append(self.bfs(n, adj_list))
        
        return res
    
    def bfs(self, n, lst):
        node_q = deque()
        visited = [False] * n 
        node_q.append(0)
        visited[0] = True
        
        cur_layer = 1
        nex_layer = 0
        layer_visited = 0
        while node_q:
            
            for _ in range(cur_layer):
                cur_node = node_q.popleft()
                
                if cur_node == n - 1:
                    return layer_visited 
                for neighbour in lst[cur_node]:
                    if visited[neighbour]:
                        continue
                    node_q.append(neighbour)
                    nex_layer += 1
                    visited[neighbour] = True
            cur_layer = nex_layer
            nex_layer = 0
            layer_visited += 1
        
        return -1 