class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set([c for c in allowed])
        res = 0
        for word in words:
            count = 0
            for ch in word:
                if ch not in s:
                    break
                count +=1
            if count== len(word):
                res +=1
        
        return res
        