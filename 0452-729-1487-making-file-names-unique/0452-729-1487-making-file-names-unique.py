class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        res = []
        mapping = {}
        
        for name in names:
            if name not in mapping:
                res.append(name)
                mapping[name] = 1
            else:
                k = mapping[name]
                while name+f"({k})" in mapping:
                    k += 1
                res.append(name+f"({k})")
                mapping[name+f"({k})"] = 1
        
        return res
                