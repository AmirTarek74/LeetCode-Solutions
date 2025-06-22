class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res= []
        n = len(s)
        sub_strings = n // k
        i = 0
        for _ in range(sub_strings):
            res.append(s[i:i+k])
            i += k
        temp = ""
        while i < n:
            temp += s[i]
            i+= 1
        if temp:
            temp += fill * (k- len(temp))
            res.append(temp)
        return res