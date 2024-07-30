class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        out = []
        for i in range(len(odd)+len(even)):
            if i%2==0:
                out.append(even.pop(0))
            else:
                out.append(odd.pop(0))
        
        return out
        