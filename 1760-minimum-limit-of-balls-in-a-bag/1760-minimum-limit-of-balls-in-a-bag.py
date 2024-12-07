class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        left = 1
        right = max(nums)
        
        while left < right :
            mid = (left + right) // 2
            
            if self.valid(mid, nums, maxOperations):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def valid(self, max_balls, nums, maxOperations):
        total = 0
        for n in nums:
            ops = math.ceil(n/max_balls) - 1
            total += ops
            if total > maxOperations:
                return False
        
        return True