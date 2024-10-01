class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr.sort(key=lambda x: (k+ x%k)%k)
        
        l = 0
        r = len(arr)-1
        while l<r:
            if arr[l]%k != 0 :
                break
            if arr[l+1]%k !=0:
                return False
            l += 2
        
        while l<r:
            if (arr[l] + arr[r])%k !=0:
                return False
            l +=1
            r -=1
        
        return True