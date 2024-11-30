from collections import defaultdict, deque
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        adj_m = defaultdict(deque)
        in_d, out_d = defaultdict(int), defaultdict(int)
        
        for pair in pairs:
            s, e = pair
            adj_m[s].append(e)
            out_d[s] += 1
            in_d[e] += 1
            
        
        res = []
        
        def visit(node):
            while adj_m[node]:
                next_node = adj_m[node].popleft()
                visit(next_node)
            res.append(node)
        
        
        start_node = -1
        for node in out_d:
            if out_d[node] == in_d[node] + 1:
                start_node = node
                break
            
        if start_node == -1 :
            start_node = pairs[0][0]
        
        visit(start_node)
        
        res.reverse()
        
        return [[res[i-1], res[i]] for i in range(1, len(res))]
        