class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pos = k
        self.lst = nums
        self.lst.sort()

    def add(self, val: int) -> int:
        idx = self.getIndex(val)
        self.lst.insert(idx,val)
        return self.lst[-self.pos]
        
    def getIndex(self,val):
        l, r = 0, len(self.lst) - 1
        while l<=r:
            mid = l + (r - l)//2
            
            if self.lst[mid]==val:
                return mid
            elif self.lst[mid]<val:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)