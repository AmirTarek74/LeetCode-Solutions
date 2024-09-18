class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = [str(n) for n in nums]
        
        res.sort(key = lambda x: x*10, reverse =True)
        
        if res[0]=='0':
            return '0'
        
        return ''.join(res)