class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        idx = 0
        t = s
        while idx < len(s) and s[idx] == "9":
            idx += 1
        if len(s) > idx:
            s = s.replace(s[idx], "9")
        t = t.replace(t[0], "0")
        return int(s) - int(t)

        