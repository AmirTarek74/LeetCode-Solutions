class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i in range(len(nums)):
            temp = str(nums[i])
            mapped_number = 0
            for c in temp:
                mapped_number = mapped_number * 10 + mapping[int(c)]
            pairs.append((mapped_number,i))
            
        pairs.sort()
        out = []
        
        for pair in pairs:
            out.append(nums[pair[1]])
            
        
        return out
                
        