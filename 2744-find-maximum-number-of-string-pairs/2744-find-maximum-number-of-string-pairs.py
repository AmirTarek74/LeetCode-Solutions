class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        chossed = []
        
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1] and j not in chossed:
                    chossed.append(j)
                    break
        
        return len(chossed)
        