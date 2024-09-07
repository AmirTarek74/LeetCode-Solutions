class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        arr2.sort()
        res = 0
        for n in arr1:
            l,r = 0, len(arr2)-1
            
            while l<=r:
                mid = (l+r)//2
                if abs(arr2[mid] - n)<=d:
                    res +=1
                    break
                elif arr2[mid]<n:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return len(arr1)-res