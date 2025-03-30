class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = [0] * 26
        for i in range(len(s)):
            last_seen[ord(s[i]) - ord("a")] = i
        
        start = 0
        end = 0
        res = []
        for i, c in enumerate(s):
            end = max(end, last_seen[ord(c) - ord("a")])

            if end == i:
                res.append(end - start + 1)
                start  = i + 1
        return res