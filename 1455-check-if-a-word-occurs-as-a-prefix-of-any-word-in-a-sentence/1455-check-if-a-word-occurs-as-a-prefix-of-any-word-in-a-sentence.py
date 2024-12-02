class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        lst = sentence.split(' ')
        
        for i in range(len(lst)):
            if lst[i].startswith(searchWord):
                return i + 1
        
        return -1