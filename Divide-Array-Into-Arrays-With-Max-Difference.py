class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        splits = n // 3
        nums.sort()
        res = []
        idx = 0
        for _ in range(splits):
            temp = [nums[idx]]
            
            for i in range(idx + 1, idx + 3):
                if nums[i] - temp[0] > k:
                    return []
                temp.append(nums[i])
            res.append(temp)
            idx += 3
        return res
