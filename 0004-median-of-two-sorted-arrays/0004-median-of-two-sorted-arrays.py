class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l1 = 0
        l2 = 0
        merged = []
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1]<nums2[l2]:
                merged.append(nums1[l1])
                l1+=1
            else:
                merged.append(nums2[l2])
                l2+=1
        
        if l1<len(nums1):
            merged.extend(nums1[l1:])
            
        if l2<len(nums2):
            merged.extend(nums2[l2:])
        l = len(merged)
        if l%2==0:
            return (merged[l//2 -1]+merged[l//2])/2
        else:
            return merged[l//2]