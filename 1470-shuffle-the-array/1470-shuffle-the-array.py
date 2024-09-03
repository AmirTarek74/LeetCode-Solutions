class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p1, p2 = 0, n
        res = []
        while len(res)<len(nums):
            res.append(nums[p1])
            res.append(nums[p2])
            p1+=1
            p2+=1
            
        return res