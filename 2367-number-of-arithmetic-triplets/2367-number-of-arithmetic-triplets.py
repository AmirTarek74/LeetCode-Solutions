class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        res = []
        
        for i in range(len(nums)-2):
            curr = nums[i]
            s = self.binary_search(nums,i+1,len(nums),diff+curr)
            if s!=-1:
                th = self.binary_search(nums,s+1,len(nums),diff+nums[s])
                if th!=-1:
                    out=[i,s,th]
                    if out not in res:
                        res.append(out)
        return len(res)
        
    
    def binary_search(self,nums,l,h,target):
        while l<h:
            mid = l + (h - l)//2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l +=1
            else:
                h-=1
        return -1