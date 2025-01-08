class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res +=1
        
        return res
    

    def isPrefixAndSuffix(self, s1, s2):
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        n2 = len(s2)
        if s2[0:n1] == s1 and s2[n2-n1:n2] == s1:
            return True
        else:
            return False
        