class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        
        for i in range(len(arr)-1):
            a = 0
            for j in range(i+1, len(arr)):
                a = a ^ arr[j-1]
                
                b = 0
                for k in range(j, len(arr)):
                    b = b ^ arr[k]
                    
                    if b == a:
                        count+=1
            
        return count