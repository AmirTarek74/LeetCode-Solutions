class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                count[nums[i]*nums[j]] = count.get(nums[i]*nums[j], 0) + 1
        res = 0
        pairs = 0
        for k in count:
            pairs = ( (count[k] - 1) * count[k]//2)
            res += 8 * pairs
        return res