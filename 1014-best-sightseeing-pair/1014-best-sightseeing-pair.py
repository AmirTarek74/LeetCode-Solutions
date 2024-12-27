class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_left = [0] * len(values)
        max_left[0] = values[0]
        
        res = 0
        
        for i in range(1, len(values)):
            curr_right = values[i] - i
            
            res = max(res, max_left[i-1]+curr_right)
            
            curr_left = values[i] + i
            max_left[i] = max(max_left[i-1], curr_left)
        
        
        return res