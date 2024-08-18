class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        pair = [(word[-1], word[0:len(word)-1]) for word in words]
        pair.sort()
        out = ""
        for p in pair:
            if p !=pair[-1]:
                out += p[1]+ ' '
            else:
                out += p[1]
        
        return out
        