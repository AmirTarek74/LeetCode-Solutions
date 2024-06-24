class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out1 = []
        out2 = []

        for i in range(len(arr1)):
            if i<len(arr2):
                if arr2[i] not in out1:
                    c= arr1.count(arr2[i])
                    for _ in range(c):
                        out1.append(arr2[i])
                if arr1[i] not in arr2:
                    out2.append(arr1[i])
            else:
                if arr1[i] not in out1:
                    out2.append(arr1[i])
        
        out2.sort(reverse=False)

        return out1+out2
        