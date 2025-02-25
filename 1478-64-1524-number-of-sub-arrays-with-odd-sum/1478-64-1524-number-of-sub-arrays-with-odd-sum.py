class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7

        res = 0
        odd_count = 0
        even_count = 1
        prefix = 0
        for n in arr:
            prefix += n
            if prefix %2 ==0:
                res += odd_count
                even_count += 1
            else:
                res += even_count
                odd_count += 1
            res = res % mod
        return res