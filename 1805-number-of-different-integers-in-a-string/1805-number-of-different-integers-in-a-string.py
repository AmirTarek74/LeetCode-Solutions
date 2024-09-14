class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        i = 0
        res = set()
        while i<len(word):
            temp = 0
            if word[i].isdigit():
                while i<len(word) and word[i].isdigit():
                    temp = temp * 10 + int(word[i])
                    i+=1
                res.add(temp)
            else:
                i+=1
        
        return len(res)