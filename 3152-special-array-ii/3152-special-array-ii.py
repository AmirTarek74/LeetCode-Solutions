class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        res = []
        
        idx = []
        for i in range(1, len(nums)):
            if (nums[i] + nums[i-1]) %2 == 0:
                idx.append(i)
            
        for s,e in queries:
            
            if self.found_idx(s + 1, e, idx):
                res.append(False)
            else:
                res.append(True)
        
        return res
    
    def found_idx(self, s, e, idx):
        l = 0
        r = len(idx) - 1
        
        while l <= r:
            mid = (l + r) // 2
            mid_idx = idx[mid]
            
            if mid_idx < s : 
                l = mid + 1
            elif mid_idx > e:
                r = mid - 1
            else:
                return True
        
        return False