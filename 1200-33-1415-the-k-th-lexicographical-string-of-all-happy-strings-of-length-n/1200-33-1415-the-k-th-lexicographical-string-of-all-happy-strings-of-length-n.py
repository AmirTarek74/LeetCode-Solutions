class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        curr = ""
        self.generate_strings(n, curr, res)

        if len(res) < k:
            return ""
        
        res.sort()
        return res[k-1]
    
    def generate_strings(self, n, curr, res):
        if len(curr) == n:
            res.append(curr)
            return
        for c in ["a", "b", "c"]:
            if len(curr) > 0 and curr[-1] == c:
                continue
            self.generate_strings(n, curr + c, res)