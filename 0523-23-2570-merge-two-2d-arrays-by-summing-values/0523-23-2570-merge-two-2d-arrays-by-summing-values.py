class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ids = {}
        for id, val in nums1:
            ids[id] = ids.get(id, 0) + val
        
        for id, val in nums2:
            ids[id] = ids.get(id, 0) + val
        
        res = []
        for k in ids:
            res.append((k, ids[k]))
        res.sort()
        return res