class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        while(lst[-1]==''):
            temp = lst.pop(len(lst)-1)
        return len(lst[-1])