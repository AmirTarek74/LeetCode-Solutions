class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        
        res = []
        minheap = [[nums1[0]+nums2[0],0,0]]
        
        visited = set()
        visited.add((0,0))
                    
        while k>0 and minheap:
            val , i,j = heapq.heappop(minheap)
            
            res.append([nums1[i],nums2[j]])
            
            if i+1<m and (i+1,j) not in visited:
                   visited.add((i+1,j))
                   heapq.heappush(minheap,[nums1[i+1]+nums2[j],i+1,j])
                   
            if j+1<n and (i,j+1) not in visited:
                   visited.add((i,j+1))
                   heapq.heappush(minheap,[nums1[i]+nums2[j+1],i,j+1])
                   
            k -=1
    
        return res