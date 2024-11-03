class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False
        
        new = s + s
        
        
        
        return new.find(goal) != -1