class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarray = 0
        prefix = {0:1}

        for n in nums:
            curr_sum += n%2
            if curr_sum - k in prefix:
                subarray += prefix[curr_sum-k]
            prefix[curr_sum] = prefix.get(curr_sum,0) + 1
        
        return subarray

        