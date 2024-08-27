from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = {}
        length =len(nums)
        for n in nums:
            d[n] = d.get(n, 0)+1
            if d[n]*2>length:
                dom = n
        l,r = 0, d[dom]

        for i in range(length):
            if nums[i]==dom:
                l+=1
                r-=1
            if l*2>i+1 and r*2>length-i-1:
                return i

        return -1

    