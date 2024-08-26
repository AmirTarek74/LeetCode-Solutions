from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = dict(Counter(nums))
        pair = [[val,c] for val,c in d.items()]
        while pair:
            temp = []
            i = 0
            while i < len(pair):
                if pair[i][1]==0:
                    pair.pop(i)
                else:
                    temp.append(pair[i][0])
                    pair[i][1]-=1
                    i+=1
            if temp:
                res.append(temp)
        
        return res
        