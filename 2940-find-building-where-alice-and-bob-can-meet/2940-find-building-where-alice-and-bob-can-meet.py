class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        max_idx = []
        
        res = [-1] * len(queries)
        store_queries = [[] for _ in heights]
        
        for i, q in enumerate(queries):
            a = q[0]
            b = q[1]
            
            if a < b and heights[a] < heights[b]:
                res[i] = b
            elif a > b and heights[a] > heights[b]:
                res[i] = a
            elif a == b:
                res[i] = a
            else:
                store_queries[max(a,b)].append((max(heights[a],heights[b]), i))
            
        
        for i, h in enumerate(heights):
            
            while max_idx and max_idx[0][0]  < h:
                _, idx = heapq.heappop(max_idx)
                res[idx] = i
            
            for element in store_queries[i]:
                heapq.heappush(max_idx, element)
            
        return res