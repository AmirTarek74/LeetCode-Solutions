class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        pair = [(s,e) for s,e in zip(l,r)]
        
        res = [True]*len(l)
        for idx,p in enumerate(pair):
            
            temp = nums[p[0]:p[1]+1]
            temp.sort()
            val = temp[1]-temp[0]
            for i in range(2,len(temp)):
                if temp[i]-temp[i-1]!=val:
                    res[idx]= False
                    break
        
        return res
        