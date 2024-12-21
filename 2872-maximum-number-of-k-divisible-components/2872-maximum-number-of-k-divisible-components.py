class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        
        res = 0
        graph = defaultdict(set)
        
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        q = deque(node for node, neighbours in graph.items() if len(neighbours)==1)
        
        while q:
            curr_node = q.popleft()
            neighbour_node = (next(iter(graph[curr_node])) if graph[curr_node] else -1)
            
            if neighbour_node >= 0:
                graph[neighbour_node].remove(curr_node)
            
            if values[curr_node] % k ==0:
                res +=1
            else:
                values[neighbour_node] += values[curr_node]
            
            if neighbour_node >= 0 and len(graph[neighbour_node]) == 1:
                q.append(neighbour_node)
        
        return res