class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)

        res = 0
        n = len(arr)

        for start in range(n):
            for end in range(start+1, n):
                prev = arr[end]
                curr = arr[start] + arr[end]
                cur_res = 2
                while curr in num_set:
                    prev, curr = curr, curr+prev
                    cur_res += 1
                    res = max(res, cur_res)
        
        return res
