class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for k in counter:
            if counter[k] % 2 ==1:
                return False
        return True