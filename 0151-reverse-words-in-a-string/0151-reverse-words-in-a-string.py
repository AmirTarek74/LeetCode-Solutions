class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        i = 0
        while i<len(lst):
            if lst[i]=='':
                lst.pop(i)
            else:
                i+=1
        
        return " ".join(lst[::-1])