class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums.sort()
        
        processed = set()
        
        res = 0
        
        for num in nums:
            if num in processed:
                continue
            
            streak = num
            cur_len = 1
            while streak * streak <= 10**5:
                if self.binary_search(nums, streak * streak):
                    streak *= streak
                    processed.add(streak)
                    cur_len += 1
                else:
                    break
            
            res = max(cur_len, res)
            
        return res if res>=2 else -1
    
    def binary_search(self, nums, square):
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==square:
                return True
            elif nums[mid]>square:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
                    
        