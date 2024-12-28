class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        prefix_sum = [0] * (n+1)

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        best_sum = [[0]*(n+1) for _ in range(4)]
        best_idx = [[0]*(n+1) for _ in range(4)]

        for t in range(1,4):
            for i in range(k*t, n+1):
                cur_sum = prefix_sum[i] - prefix_sum[i-k] + best_sum[t-1][i-k]
            
                if cur_sum > best_sum[t][i-1]:
                    best_sum[t][i] = cur_sum
                    best_idx[t][i] = i - k
                else:
                    best_sum[t][i] = best_sum[t][i-1]
                    best_idx[t][i] = best_idx[t][i-1]
        
        res = [0] *3
        end = n
        for t in range(3,0,-1):
            res[t-1] = best_idx[t][end]
            end = res[t-1]
        
        return res
        