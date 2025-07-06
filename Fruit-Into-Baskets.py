class Solution:
    def totalFruit(self, f: List[int]) -> int:
        l = 0
        res = float("-inf")
        types = {}
        
        for r in range(len(f)):
            while types and len(types)>2:
                types[f[l]] -= 1
                if types[f[l]]==0:
                    del types[f[l]]
                l += 1
                
            types[f[r]] = types.get(f[r], 0) + 1
            if len(types) <= 2:
                res = max(res, r - l + 1)
        return res
                