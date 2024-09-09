class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        l2 = len(nums2)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            if idx==l2:
                continue
            
            for j in range(idx+1,l2):
                if nums1[i]<nums2[j]:
                    res[i]= nums2[j]
                    break
        
        return res
                
        