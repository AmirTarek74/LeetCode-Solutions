class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        p = [[mat[r].count(1),r] for r in range(len(mat))]
        heapq.heapify(p)
        p.sort(key=lambda x:[x[0],x[1]])
        res = [p[i][1] for i in range(k)]
        return res
        