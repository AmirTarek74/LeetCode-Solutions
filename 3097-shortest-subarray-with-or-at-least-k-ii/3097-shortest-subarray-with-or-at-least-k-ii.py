class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")
        l = 0
        r = 0
        bit_count = [0] * 32
        
        while r<len(nums):
            self._update(bit_count, nums[r], 1)
            
            while (l<=r and self._getnum(bit_count)>=k):
                res = min(res, r-l+1)
                self._update(bit_count, nums[l], -1)
                l += 1
            
            r += 1
        
        return -1 if res==float("inf") else res
    
    def _update(self, bit_count, num, value):
        
        for i in range(32):
            if num & (1<<i):
                bit_count[i] += value
    
    
    def _getnum(self,bit_count):
        num = 0
        for i in range(32):
            if bit_count[i]:
                num = num | 1<<i
        return num