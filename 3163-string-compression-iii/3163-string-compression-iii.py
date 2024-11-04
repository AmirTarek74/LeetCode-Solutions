class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        
        idx = 0
        counter = 1
        while idx<len(word):
            while idx<len(word)-1 and word[idx]==word[idx+1] and counter <9:
                idx += 1
                counter += 1
            
            comp = comp + str(counter) + word[idx]
            idx += 1
            counter = 1
        
        return comp