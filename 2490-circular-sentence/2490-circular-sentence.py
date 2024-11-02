class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(" ")
        
        if lst[0][0] != lst[-1][-1]:
            return False
        
        for i in range(1, len(lst)):
            if lst[i][0] != lst[i-1][-1]:
                return False
        
        return True