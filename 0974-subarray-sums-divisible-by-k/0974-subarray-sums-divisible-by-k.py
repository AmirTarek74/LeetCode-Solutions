class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum= {0 : 1}
        res = 0
        calcsum = 0
        for n in nums:
            calcsum += n 
            rem = calcsum%k 
            res += prefixsum.get(rem,0)
            prefixsum[rem]  = 1 + prefixsum.get(rem,0)

        return res