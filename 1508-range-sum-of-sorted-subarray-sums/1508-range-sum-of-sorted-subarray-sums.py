class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        left_idx = 0
        right_idx = 0
        
        summa = 0
        output = []
        while left_idx < len(nums) :
            if left_idx==right_idx:
                summa = nums[left_idx]
                output.append(summa)
                right_idx+=1
            elif right_idx==len(nums):
                left_idx +=1
                right_idx = left_idx
                summa = 0
            else:
                summa += nums[right_idx]
                right_idx+=1
                output.append(summa)
        output.sort()
        mod = 10**9 + 7
        return sum(output[left-1:right])%mod
        
                
        