class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<=len(nums2):
            smaller = 1
        else:
            smaller = 2
        length = min(len(nums1),len(nums2))
        out = []
        for i in range(length):
            if smaller ==1:
                if nums1[i] in nums2 and nums1[i] not in out:
                    min_count = min(nums1.count(nums1[i]),nums2.count(nums1[i]))
                    for _ in range(min_count):
                        out.append(nums1[i])
            else:
                if nums2[i] in nums1 and nums2[i] not in out:
                    min_count = min(nums1.count(nums2[i]),nums2.count(nums2[i]))
                    for _ in range(min_count):
                        out.append(nums2[i])
        return out
        