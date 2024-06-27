class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            edge = edges[i]
            for j in range(i+1,len(edges)):
                if edge[0] in edges[j]:
                    return edge[0]
                if edge[1] in edges[j]:
                    return edge[1] 
            
        