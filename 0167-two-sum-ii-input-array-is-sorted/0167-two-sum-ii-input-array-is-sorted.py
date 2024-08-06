class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)-1):
            second = self.binary_search(numbers,i+1,len(numbers)-1,numbers[i],target)
            if second!= -1:
                return [i+1, second]
            
    
    
    def binary_search(self,numbers,low,high,curr,target):
        while low<=high:
            mid = low + (high-low)//2
            
            if curr + numbers[mid]==target:
                return mid+1
            elif curr + numbers[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
        