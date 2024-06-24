class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum= {0 : 1}
        res = 0
        calcsum = 0
        for n in nums:
            calcsum += n 
            diff = calcsum - k 
            res += prefixsum.get(diff,0)
            prefixsum[calcsum]  = 1 + prefixsum.get(calcsum,0)
        
        return res