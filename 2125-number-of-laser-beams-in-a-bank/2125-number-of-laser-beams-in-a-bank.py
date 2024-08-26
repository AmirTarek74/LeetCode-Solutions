class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        res = 0
        prev = 0
        for s in bank:
            count = 0
            for c in s:
                if c=='1':
                    count+=1
            
            if count!=0:
                res = res + prev * count
                prev = count
            
        return res
        