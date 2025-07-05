class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = {}
        for n in arr:
            counter[n] = counter.get(n, 0) + 1
        res = 0
        
        for k in counter:
            if counter[k] == k and k > res:
                res = k
                
        return res if res != 0 else -1