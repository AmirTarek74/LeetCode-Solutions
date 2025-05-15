class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if len(words) <=1:
            return words
        res = [words[0]]
        last_idx = groups[0]
        for i in range(1, len(words)):
            if last_idx != groups[i]:
                res.append(words[i])
                last_idx = groups[i]
        
        return res


