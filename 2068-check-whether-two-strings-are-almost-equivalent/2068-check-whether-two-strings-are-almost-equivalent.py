class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for c in range(len(word1)):
            x1 = word1.count(word1[c])
            x2 = word2.count(word1[c])
            if abs(x1-x2)>3:
                return False
            x1 = word1.count(word2[c])
            x2 = word2.count(word2[c])
            if abs(x1-x2)>3:
                return False
        
        return True
        